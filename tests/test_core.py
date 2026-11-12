import unittest,copy,json
from hermes_uncertain_write_lab import run
DEMO={'operation_key': 'create-order-1', 'payload': {'item': 'synthetic', 'quantity': 1}, 'lookup_supported': True}
class DomainTests(unittest.TestCase):
 def test_lost_response_reconciles_existing_effect(self):
  x=run(DEMO);self.assertTrue(x['response_lost']);self.assertTrue(x['reconciled']);self.assertEqual(x['remote_effect_count'],1);self.assertEqual(x['resume_action'],'confirm_existing')
 def test_no_lookup_keeps_uncertainty(self):
  x=run(dict(DEMO,lookup_supported=False));self.assertFalse(x['reconciled']);self.assertEqual(x['resume_action'],'hold_uncertain');self.assertFalse(x['blind_retry_sent']);self.assertEqual(x['remote_effect_count'],1)
 def test_payload_not_production(self):
  self.assertFalse(run(DEMO)['production_provider_called'])
