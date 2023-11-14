class Doggy:
    #constructor ~ create defauls and builds the instance 
    def __init__(self):
        pass
        #? attributes
        self.name = "Snoop"
        self.age = 5
        self.breed = "malti poo"
        self.color = "Black"
    def bark(self):
        print("woof woof !!")
 


myDog=Doggy()

print(myDog.name)
myDog.bark()