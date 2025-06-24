#initiate a class
class employee:
    # special method/magic method/dunder method - constructor
    def __init__(self):
        print("Started executing attributes")
        self.id= 123
        self.salary= 50000
        self.designation = "Software Engineer"
        print("Attributes have been initialized")
    
    def travel(self,destination):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")

# creating an object/instance of the class

sam=employee()

#print(sam.id)
#print(sam.salary)
#print(sam.designation)

# Calling a mthod of the class
#sam.travel("New York")

print(type(sam))

