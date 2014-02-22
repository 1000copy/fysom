# -*- coding: utf-8 -*-
from fysom import Fysom

def oneat(e):
  print("e:")
  print(e.src)
  print(e.dst)
  print(e.keyparameter)
fsm = Fysom({
  'initial': 'hungry',
  'events': [
    {'name': 'eat',  'src': 'hungry',    'dst': 'satisfied'},
    {'name': 'eat',  'src': 'satisfied', 'dst': 'full'},
    {'name': 'eat',  'src': 'full',      'dst': 'sick'},
    {'name': 'rest', 'src': ['hungry', 'satisfied', 'full', 'sick'],
                                         'dst': 'hungry'}
  ],
  'callbacks': {
    'oneat':  oneat
  }
})
#
# print(fsm.current)
fsm.eat(keyparameter=1)
print(fsm.current)
# fsm.eat()
# print(fsm.current)
# fsm.eat()
# print(fsm.current)
# fsm.rest()
# print(fsm.current)

# 交互状态下，用 fsm.__dict__() ,查看tmap可以帮助更好的了解fsm的工作机理。
# 代码的关键
# 1. 了解fsm.tmap 的构建—- event -> src -> dst ,通过简单的索引 tmap[event][src],就可以获得dst。
# 2. 了解 e = _e_obj() 的构建,目的是作为参数，传递context 给 onEVENThappen
# 3. def fn(**kwargs)的构造和返回 。返回一个函数。


# 终于，看着代码，反向写出了testcase。python也不简单。
