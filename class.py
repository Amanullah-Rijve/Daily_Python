class person:
    name= 'Rijve'
    age = 23
    occupation = 'Developer'

a = person()

print(f"Name : {a.name}")
print(f"Age : {a.age}")
print(f"Occumation : {a.occupation}")

class Human:
    def __init__(self):

        self.name='Rijve'
        self.Gender = "Male"
        self.University ="Daffodil"

    def data(self):
        print(f"He is {self.name} is {self.Gender} studies in {self.University}")       

a = Human()
a.data()

! another example

class person :
    name='RIjve'
    occupation = 'Developer'

    def data(self):
        print(f"{self.name} is a  {self.occupation}")

a  = person()
b= person()
c = person()

b.name= 'Amanullah'
b.occupation='Ai Developer'

c.name = 'Sheikh'
c.occupation = 'Fullstack'

a.data()
b.data()
c.data()
