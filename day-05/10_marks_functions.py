#LIST AND FUNCTION

def get_marks(marks):
    marks = []
    mark=int(input("Enter mark (or -1 to stop)"))

    while mark != -1:
        marks.append(mark)  #use append to put value inside the list
        mark=int(input("Enter mark (or -1 to stop)"))
    return marks

def print_list_size(marks):
    print(f"Our list has",len(marks))
    
def print_marks(marks):
    for i in range(len(marks)):
        print('Student', i + 1, '-', marks[i])
    
def getSum(marks):
    sum=0        
    for x in range(len(marks)):
        mark=marks[x]
        sum = sum + mark	
    return sum

def determine_highest(marks):
    highest=0
    for i in range(len(marks)):
        mark=marks[i]
        if(mark > highest):
            highest=mark
    print(f"The highestmark is {highest}")
    
menu="Press1: Capturing marks\n"
menu+="Press2: Check number of mark\n"
menu+="Press3: To calculate sum of marks\n"
menu+="Press4: To find the highest\n"
menu+="Press-1: To exit\n"
    
print(menu)
choice=int(input(":Make your choice"))
entered_marks= []
while choice != -1:
    #entered_marks =0
    if choice == 1:
       entered_marks = get_marks()
       print(entered_marks)
    elif choice == 2:
            print_list_size(entered_marks)
    elif choice == 3:
            calc_sum = get_sum_of_marks(entered_marks)
            print("Sum of all marks=", calc_sum)
        
    elif choice == 4:
        determine_highest(entered_marks)
        #print("Sum of all marks=", calc_sum)
    else: print("Not on the menu")
    print(menu)
    choice=int(input(":Make your choice"))
