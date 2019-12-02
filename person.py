class Person():
    def __init__(self, name, age, hair_color, occupation):
        self.name = name
        self.age = age
        self.hair_color = hair_color
        self.occupation = occupation

    def description(self):
        print(f"{self.name}, {self.age}, {self.hair_color}, {self.occupation}")
