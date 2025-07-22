monthly_income = float(input("User's monthly income in THB : "))
rent_cost = float(input("Monthly rent/housing cost : "))
transportation_cost = float(input("Monthly transportation expenses : "))
entertainment_budget = int(input("Monthly entertainment budget : "))
emergency_fund_percent = float(input("Percentage to save for emergency : ")/    44)



number = 2                                                                                                                                                                                             
for number in range(2,10) :
    if number%2 == 0:
        print("the number "+str(number)+" is even")
    else :
        print("The number "+str(number)+" is odd")
    number = number+1


rows = int(input("Enter the rows:"))  
i=0
while i <= rows:  
    j=0
    while j < i:  
        print("*",end = '')  
        j+=1
    print()
    i+=1