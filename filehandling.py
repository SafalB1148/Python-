# Writing to a file

file = open("example.txt", "w")  # 'w' means write mode
file.write("Hello, this is your first file handling program!")
file.close()

# Reading from the file
file = open("example.txt", "r")  # 'r' means read mode
content = file.read()
print(content)
file.close()
# Appending to a file
file = open("example.txt", "a")  # 'a' means append mode
file.write("\nThis is additional text added to the file.")
file.close()
# Reading multiple lines from a file
file = open("example.txt", "r")  # 'r' means read mode
lines = file.readlines()  # This reads all lines into a list

for line in lines:
    print(line.strip())  # strip() removes any leading/trailing whitespace
file.close()
try:
    file = open("non_existent_file.txt", "r")  # Attempt to open a file that doesn't exist
    content = file.read()
    print(content)
except FileNotFoundError:
    print("The file does not exist.")
finally:
    file.close()
