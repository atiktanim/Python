class Enemy:
    energy
    def __init__(self,x):
        self.energy=x
    def get_energy(self):
        print(self.energy)
Jason=Enemy(5)
Sandy=Enemy(15)
Jason.get_energy()
Sandy.get_energy()