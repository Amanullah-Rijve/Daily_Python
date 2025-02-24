class Person:
    def __init__(self, name, occupation, age):
        self.name = name
        self.occupation = occupation
        self.age = age

    def info(self):
        print(f"{self.name} is a {self.occupation} and is {self.age} years old.")


a = Person("Rijve", "Developer", 23)
b = Person("Apon", "ML Developer", 24)
c = Person("Amanullah", "UI", 21)
d = Person("Tharim", "SEO", 26)

a.info()
b.info()
c.info()
d.info()
