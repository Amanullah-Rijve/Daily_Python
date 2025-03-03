
file_output = "Welcome To Bangladesh"

file_path = r"C:\Users\User\Desktop\output.txt"


with open (file_path, 'w') as file_name:
    file_name.write(file_output)

    print(f"the file was writen as {file_path}")




