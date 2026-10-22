mark = int(input("Please Enter Your mark"))

if mark >0 and mark <= 100:
    if mark <= 49:
        print("failed")
    elif mark >= 50 and mark <=74:
        print("Passed")
    elif mark >= 75:
        print("Distinction")
        
else:
    print("Invalid Number")