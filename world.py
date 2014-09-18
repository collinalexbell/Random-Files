import random
from thing import thing

class world:
    def __init__(self, name):
        self.name = name
        self.life={}
        new_thing_name = ("Sophie")
        self.life[new_thing_name]  = thing(new_thing_name, thing("dalmation", thing("canus lupus familiaris")))
        new_thing_name = ("Jack")
        self.life[new_thing_name]  = thing(new_thing_name, thing("mut", thing("canus lupus familiaris")))



    def send_representative(self):
        rep = random.choice(list(self.life.keys()))
        print(rep)
        rep = self.life[rep]
        rep.comosellama()
