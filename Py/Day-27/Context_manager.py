with open("test.txt", "w") as file:
    file.write("Learning Python for Cloud and AI")

print("File operation completed")

with open("test.txt", "a") as file:
    file.write("\nAWS + Azire + AI")

print("File append completed")