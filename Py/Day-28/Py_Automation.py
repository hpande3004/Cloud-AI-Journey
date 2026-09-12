import os
print(os.getcwd())

print(os.listdir())

print("Current Dictionary")
print(os.getcwd())

print("\nFiles and Folders:")
print(os.listdir())

import os

os.mkdir("Test_Dicerctory")
print("Folder Created")

import os 
folder = "Test_Directory"

os.makedirs(folder, exist_ok=True)
file_path = os.path.join(folder, "config.txt")
with open(file_path, "w") as file:
    file.write("Environment = Development\n")
    file.write("Cloud = AWS\n")
    file.write("Project = Automation\n")

print("Project Completed!")