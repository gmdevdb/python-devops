f1 = int(input("Enter 1st number:"))
f2 = int(input("Enter 2nd number:"))
f3 = int(input("Enter 3rd number:"))
for i in range(1,f1+1) :
    if (f1 % i == 0) :
       print("The factor of 6:", i)

for i in range(1,f2+1) :
    if (f2 % i == 0) :
        print("The factor of 2nd number:", i)

for i in range(1,f3+1) :
    if (f3 % i == 0) :
        print("The factor of 3rd number:", i)

  