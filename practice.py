class  person:
    def __init__(self,  name,age,date):
        self.name = name
        self.age = age 
        self.date = date

    def __str__(self):
        return (f"My Name is {self.name} and  I am {self.age}  years old and my  brithdate is {self.date}")
    

Bio_data = person("Amanullah" , 23, 18)    
Bio_data1 = person("Rijve", 24, 18)
Bio_data2 = person("Apon",25,16)
print(Bio_data)
print(Bio_data1)
print(Bio_data2)
