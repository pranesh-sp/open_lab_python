dir={}
n=input("enter number or entries you want to save: \n")
for i in range(int(n)):
    dir[input("\nenter contact: \n")]=input("\n enter name: \n")

s=input("enter number for searching:")
print(dir.get(s))