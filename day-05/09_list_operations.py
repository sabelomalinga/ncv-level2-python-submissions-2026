marks = []

mark=int(input("Enter mark (or -1 to stop)"))
i=0
while mark!= -1:
    marks.append(mark)  #use append to put value inside the list
    marks[i]=mark
    i+=1
    mark=int(input("Enter mark (or -1 to stop)"))
    print(f"Our list has{len(marks)} elements")
total=0        
for x in range(len(marks)):
    mark=marks[x]
    total = total + mark

avg=total/len(marks)
print(f"The average of all marks= {avg}")