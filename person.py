class Person:
    # name="Aahad-Ali"
    # age=22
    # height=5.9
    # weight=60

    def __init__(self,name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        print("constructor called")

    def info(self):
        print(f"{self.name} and {self.age} and {self.height} and {self.weight}")

a=Person("Aahad-Ali", 22, 5.9, 60)
a=Person("Aahad-Ali", 22, 5.9, 60)
# b=Person()
# c=Person()

a.name="Ali"

a.info()
# b.info()
# c.info()