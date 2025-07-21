import os 
n = int(input("How many scripts do you want to create ? "))
for i in range(1,n+1) :
    os.system("python generator.py")