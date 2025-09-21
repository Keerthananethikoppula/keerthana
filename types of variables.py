class sample:
    name="sri"
    age=20
    print("i am static variable",name)
    print("i am static variable",age)
    def __init__(self):
        a=10
        b=20
        print("i am instance variable",a)
        print("i am instance variable",b)
    def display(self):
         c=30
         d=40
         print("i am local variable",c)
         print("i am local variable",d)
obj=sample()
obj.display()
