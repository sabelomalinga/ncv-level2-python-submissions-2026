#def display_heading():
 #   print("Learner Mark Analyser")

#print("Program starts")
#display_heading()
#print("Program ends")


def place_Order(item):
     print(f"your order is placed:Your order is {item}")
     
def calc_Total(item):
    price=25.5
    VAT=0.15
    totalPrice=(price+ len(item))*1.15
    return totalPrice
    
        
        
        
     #place_order()
     
def get_Order():
    print("order ready")
    return "Collect order"


myFood=input("What would you like?")
place_Order(myFood)

print(get_Order())

order_Total=calc_Total(myFood)
print(f"Your order costs: R{order_Total}")
    
    #msg=get_Order()
    
    
    