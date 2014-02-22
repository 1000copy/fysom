from fysom import Fysom

fsm = Fysom({
  'initial': 'hungry',
  'events': [
    {'name': 'eat',  'src': 'hungry',    'dst': 'satisfied'},
    {'name': 'eat',  'src': 'satisfied', 'dst': 'full'},
    {'name': 'eat',  'src': 'full',      'dst': 'sick'},
    {'name': 'rest', 'src': ['hungry', 'satisfied', 'full', 'sick'],
                                         'dst': 'hungry'}
  ]
})
#
print(fsm.current)
fsm.eat()
print(fsm.current)
fsm.eat()
print(fsm.current)
fsm.eat()
print(fsm.current)
fsm.rest()
print(fsm.current)