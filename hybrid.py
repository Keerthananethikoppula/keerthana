#hybrid inheritance
class Grandfather:
    def grandfather_func(self):
        print("This function is in grandfather class.")
class Father:
    def father_func(self):
        print("This function is in father class.")  
class Child(Father,Grandfather): 
    def child_func(self):
        print("This function is in child class.")
class Daughter(Father,Grandfather):
    def daughter_func(self):
        print("This function is in daughter class.")
class Granddaughter(Father,Grandfather):
    def granddaughter_func(self):
        print("This function is in granddaughter class.")             