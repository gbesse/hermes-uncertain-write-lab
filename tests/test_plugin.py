import importlib.util,json,sys,unittest
from pathlib import Path
class PluginContractTests(unittest.TestCase):
 def load(self):
  root=Path(__file__).resolve().parents[1];name='fixture_hermes_uncertain_write_lab';spec=importlib.util.spec_from_file_location(name,root/'__init__.py',submodule_search_locations=[str(root)]);module=importlib.util.module_from_spec(spec);sys.modules[name]=module;spec.loader.exec_module(module);return module,root
 def test_registration_and_localized_handler(self):
  module,root=self.load();calls=[]
  class Context:
   def register_tool(self,**kwargs):calls.append(kwargs)
  module.register(Context());self.assertEqual(len(calls),1);self.assertEqual(calls[0]['name'],'hermes_uncertain_write_lab');payload=json.loads((root/'examples/demo.json').read_text())
  for lang in ['fr','en','es']:
   result=json.loads(calls[0]['handler']({'payload':payload,'lang':lang},conversation_id='fixture'));self.assertEqual(result['language'],lang);self.assertIn('result',result)
 def test_errors_are_json_strings_in_three_languages(self):
  module,_=self.load();messages=[]
  for lang in ['fr','en','es']:
   x=json.loads(module.handle({'payload':{},'lang':lang}));self.assertEqual(x['code'],'invalid_input');messages.append(x['message'])
  self.assertEqual(len(set(messages)),3)
