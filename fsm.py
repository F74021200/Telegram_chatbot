from transitions import Machine
from transitions.extensions import GraphMachine as Machine

states = ['start', 'startcheck', 'frompart', 'topart', 'fromarea', 'toarea']

transition = [
	{'trigger': 'traintime', 'source': 'start', 'dest': 'startcheck'},
	{'trigger': 'part', 'source': 'startcheck', 'dest': 'frompart'},
	{'trigger': 'part', 'source': 'frompart', 'dest': 'topart'},
	{'trigger': 'area', 'source': 'topart', 'dest': 'fromarea'},
	{'trigger': 'area', 'source': 'fromarea', 'dest': 'toarea'},
	{'trigger': 'exit', 'source': 'startcheck', 'dest': 'start'},
	{'trigger': 'exit', 'source': 'frompart', 'dest': 'start'},
	{'trigger': 'exit', 'source': 'topart', 'dest': 'start'},
	{'trigger': 'exit', 'source': 'fromarea', 'dest': 'start'},
	{'trigger': 'exit', 'source': 'toarea', 'dest': 'start'},
]

class traintime(object):
	def hot(self):
		return True

m = traintime()
machine = Machine(model=m, states=states, transitions=transition, initial='toarea')

m.get_graph().draw('my_state_diagram.png', prog='dot')
