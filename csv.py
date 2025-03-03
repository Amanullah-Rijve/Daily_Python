import csv

boi_data = [["Name", "Age", "Occupation", "Gender"],
            ["Amanullah", 23, "Student", "Male"],
            ["Rijve", 37, "Developer", "Male"],
            ["Nil", 20, "Designer", "Female"]]

file_path = r"C:\Users\User\Desktop\output.csv"  

with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)  
    writer.writerows(boi_data)  
    print(f"CSV file '{file_path}' was created")
