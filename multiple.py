# multiple inheritance
class Mother:
    def mother_func(self):
        print("This function is in mother class.")
class Father(Mother):
    def father_func(self):
        print("This function is in father class.")  
class Child(Father):
    def child_func(self):
        print("This function is in child class.")
a=Child()
a.mother_func() 
a.father_func()
a.child_func()
b=Father()
b.mother_func()
b.father_func()
c=Mother()
c.mother_func()
# c.father_func() #this will give error
# c.child_func() #this will give error        