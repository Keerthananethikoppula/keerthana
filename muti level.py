#multi level inheritance
class Grandfather:
    def grandfather_func(self):
        print("This function is in grandfather class.")
class Father:
    def father_func(self):
        print("This function is in father class.")
class Child(Father,Grandfather):
    def child_func(self):
        print("This function is in child class.")
a=Child()
a.grandfather_func()    
a.father_func()
a.child_func()
b=Father()
b.father_func()
# b.grandfather_func() #this will give error
# b.child_func() #this will give error
c=Grandfather()
c.grandfather_func()
# c.father_func() #this will give error
# c.child_func() #this will give error