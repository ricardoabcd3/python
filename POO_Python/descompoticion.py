class Car:
    def __init__(self, model,branch,color):
        self.model= model
        self.branch=branch
        self.color=color
        self._state = 'rest'
        self._engine= engine(cylanders=4)
    def acceleration(self, type="slow"):
        if type=="fast":
            self._engine.gasoline_injection(10)
        else:
            self._engine.gasoline_injection(3)
class engine:
    def __init__(self, cylanders, type='gas'):
        self.cylanders = cylanders
        self.type = type
        self._temperature=0
        self._piston = 0
    def gasoline_injection(self,amount):
        if amount >10:
            piston = 10
            
        