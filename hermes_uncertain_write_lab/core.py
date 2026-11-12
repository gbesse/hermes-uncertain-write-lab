import sqlite3,tempfile,threading,socket,json,hashlib,urllib.request,urllib.error,http.client
from http.server import HTTPServer,BaseHTTPRequestHandler
from pathlib import Path
from .common import identifier
def run(data):
 key=identifier(data['operation_key']);payload=data['payload'];lookup=data.get('lookup_supported',True)
 if not isinstance(payload,dict)or not isinstance(lookup,bool):raise ValueError('input')
 canonical=json.dumps(payload,sort_keys=True,separators=(',',':'),allow_nan=False);expected=hashlib.sha256(canonical.encode()).hexdigest()
 if len(canonical)>10000:raise ValueError('payload_size')
 with tempfile.TemporaryDirectory(prefix='uncertain-write-')as tmp:
  path=Path(tmp)/'remote.sqlite'
  with sqlite3.connect(path)as db:db.execute('create table effects(id integer primary key,op text,digest text)')
  class Handler(BaseHTTPRequestHandler):
   def log_message(self,*args):pass
   def do_POST(self):
    body=self.rfile.read(int(self.headers['Content-Length']));obj=json.loads(body);digest=hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    with sqlite3.connect(path)as db:db.execute('insert into effects(op,digest)values(?,?)',(self.headers['Operation-Key'],digest))
    self.close_connection=True
    try:self.connection.shutdown(socket.SHUT_RDWR)
    except OSError:pass
    self.connection.close()
   def do_GET(self):
    if not lookup:self.send_response(404);self.end_headers();return
    with sqlite3.connect(path)as db:rows=db.execute('select id,digest from effects where op=?',(key,)).fetchall()
    raw=json.dumps({'receipts':[{'id':i,'digest':d}for i,d in rows]}).encode();self.send_response(200);self.send_header('Content-Length',str(len(raw)));self.end_headers();self.wfile.write(raw)
  server=HTTPServer(('127.0.0.1',0),Handler);thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start();base='http://127.0.0.1:'+str(server.server_port);opener=urllib.request.build_opener(urllib.request.ProxyHandler({}));lost=False
  try:
   req=urllib.request.Request(base+'/create',data=canonical.encode(),headers={'Content-Type':'application/json','Operation-Key':key},method='POST')
   try:
    with opener.open(req,timeout=5)as response:response.read()
   except(urllib.error.URLError,http.client.RemoteDisconnected,ConnectionError):lost=True
   try:
    with opener.open(base+'/receipts',timeout=5)as response:receipts=json.load(response)['receipts']
   except urllib.error.HTTPError:receipts=None
   verified=receipts is not None and len(receipts)==1 and receipts[0]['digest']==expected
   with sqlite3.connect(path)as db:count=db.execute('select count(*)from effects').fetchone()[0]
  finally:server.shutdown();server.server_close();thread.join(timeout=3)
 return {'response_lost':lost,'reconciled':verified,'resume_action':'confirm_existing'if verified else'hold_uncertain','remote_effect_count':count,'blind_retry_sent':False,'real_loopback_http':True,'production_provider_called':False}
