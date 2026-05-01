file = open("test.txt", "w")
file.write("Hello Sufiyan")
file.close()

file = open("test.txt", "r")
data = file.read()
print(data)
file.close()
 #always close file or use with open automatic colse
file = open("test.txt", "a")
file.write("\nNew line")
file.close()


# Requirements:
# user se input lo
# file me save karo
# phir file read karke print karo 

with open("studentIntro.txt", "a") as MYfile:
    Intro=input("Define your self:")
    MYfile.write(Intro + "\n")

file = open("studentIntro.txt", "r")
data = file.read()
print(data)
file.close()


     