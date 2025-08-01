class Mario:
    def __init__(self,speed,size,x,y):
        self.speed = speed
        self.size = size
        self.position = [x,y]
        self.create()
    def information(self):
        print(f"My speed as Mario is {self.speed}, my size is {self.size}, my x is {self.position[0]} and my y is {self.position[1]}")
    def create(self):
        
    @classmethod
    def gravity(self):
        pass

mario=Mario(30,10,20,25)
mario.information()