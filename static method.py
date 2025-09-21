#static method
class Person:
    @staticmethod
    def person_data(name,age):
        print("static method")
        print("name:",name)
        print("age:",age)
        return name, age
    def display(color):
        return f"static method",color
        print("color:",color)
print(Person.person_data("sri keerthana",22))
print(Person.display("blue"))
       
        
