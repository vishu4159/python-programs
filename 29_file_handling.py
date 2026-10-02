# Python program to demonstrate file handling

# Writing data to a file
file = open("student.txt", "w")

file.write("Name: Rahul\n")
file.write("Course: BCA\n")
file.write("Subject: Python")

file.close()


# Reading data from the file
file = open("student.txt", "r")

data = file.read()

print("File contents:")
print(data)

file.close()
