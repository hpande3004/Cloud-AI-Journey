# import shutil

# shutil.copy("Test_Directory/config.txt", "Test_Directory/ config_backup.txt")

# print("Backup Created!")

# import os

# os.mkdir("Test_Directory/Backup")

# import os
# print("Current folder:")
# print(os.getcwd())

# print("\nContent of Test Dir:")
# print(os.listdir("Test_Directory"))
# #------------------------------------
# import os
# import shutil

# source = os.path.abspath("Test_Directory/_config_backup.txt")
# destination = os.path.abspath("Test_Directory/Backup/_config_backup.txt")

# print("Source:", source)
# print("Source exists:", os.path.exists(source))

# print("Destination:", destination)
# print("Destination exists:", os.path.exists(destination))

# shutil.move(source, destination)
# print("File Moved")

#------------------------------------
# import os
# os.remove("Test_Directory/config.txt")
# print("File Deleted")
#------------------------------------
# import os 
# os.makedirs("Temporary")
# with open("Temporary/test.txt", "w") as file:
#     file.write("This file will be deleted")

# print("Temporary File Created")
#-------------------------------------
import os
# os.remove("Temporary/test.txt")
# print("File deleted")

os.rmdir("Temporary")
print("Folder Deleted")