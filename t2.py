# -*- coding: utf-8 -*-
class state_machine_error(Exception):
  pass
class state_machine:
  def __init__(self,cfg):
    self.initial = cfg['initial'] if 'initial' in cfg else None
    self.current_state = self.initial
    self.events = cfg['events'] if 'events' in cfg else []
  def get_next(self,event,events,current_state):
    for e in events:
      if e['name'] == event and (e['src'] == current_state or current_state in e['src']):
        return e['dst']
    return None
  def get_current_state(self):
    return self.current_state
  def fire(self,event):
    dst = self.get_next(event,self.events,self.current_state)
    if dst:
      self.current_state =dst 
      return dst
    else:
      #fire exception
      raise state_machine_error("event %s inappropriate in current state %s"
            % (event, self.current_state))

# run 

import unittest

class t1(unittest.TestCase):
  def setUp(self):
    cfg = {
      'initial': 'hungry',
      'events': [
        {'name': 'eat',  'src': 'hungry',    'dst': 'satisfied'},
        {'name': 'eat',  'src': 'satisfied', 'dst': 'full'},
        {'name': 'eat',  'src': 'full',      'dst': 'sick'},
        {'name': 'rest', 'src': ['hungry', 'satisfied', 'full', 'sick'],
                                             'dst': 'hungry'}
      ]
    }
    self.fsm = state_machine(cfg)
  def tearDown(self):
    pass
  def test_1(self):
    self.assertEqual(self.fsm.get_current_state(),"hungry")
    self.assertEqual(self.fsm.fire("eat"),"satisfied")
    self.assertEqual(self.fsm.get_current_state(),"satisfied")
    self.assertEqual(self.fsm.fire("eat"),"full")
    self.assertEqual(self.fsm.fire("eat"),"sick")
    # 函数调用，灵活的发指。http://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception
    self.assertRaises(state_machine_error, self.fsm.fire,"eat")
    self.assertEqual(self.fsm.fire("rest"),"hungry")
    self.assertEqual(self.fsm.fire("rest"),"hungry")

if __name__=="__main__":
  unittest.main()