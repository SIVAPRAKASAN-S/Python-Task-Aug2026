# file = open("student.txt", "w")

# file.write("Name: Siva\n")
# file.write("Course: B.E CSE\n")
# file.write("College: ABC College\n")

# file.close()


file = open("student.txt", "r")

data = file.read()

print(data)

file.close()


# file = open("student.txt", "a")

# file.write("Age: 22\n")

# file.close()


file = open("student.txt", "r")

data = file.read()

data = file.readline()

data = file.readlines()

file.write("Hello")

file.writelines(["Hello\n", "Welcome\n"])

file.close()