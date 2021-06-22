class Washing_machine:
    def __init__(self,):
        pass

    def wash(self,temperature="hot"):
        self._fill_shoap_bucket(temperature)
        self._add_shoap()
        self._wash()
        self._spin_dry()
    def _fill_shoap_bucket(self, temperature):
        print("filling bucket soap",temperature)
    def _add_shoap(self):
        print("Add shoap")
    
    def _wash(self):
        print("washing clothing")
    
    def _spin_dry(sefl):
        print("spin dry")

if __name__=="__main__":
    wa= Washing_machine()
    wa.wash()



