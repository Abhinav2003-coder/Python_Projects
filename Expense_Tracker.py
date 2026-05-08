# Expense Tracker Projects
#list of expense in form of dictionary
expenselist = []   
print(" welcome to Expense Tracker : Khrcha kam kiya kero ")

while True:
    print("===menu===")
    print("1. Add expense")
    print("2. View all expense")
    print("3. View total expense")
    print("4. Exit")

    choice = input("please enter your choice : ")

# Add expense    
    if(choice == "1"):
        date = input("IN Which Date you spend ?")
        category = input("What tpye of Expense did you make ? (food, travel, books, cloths): ")
        description = input("Tell more detail")
        Amount = float(input("Enter the amount:"))

        expense = {
            "Date" : date,
            "Category": category,
            "Description": description,
            "Amount": Amount

        }
        expenselist.append(expense)
        print("\n Done .Expense is added succesfully")
    
# 2. View all Expenses
    elif (choice == "2"):
        if( len(expenselist)== 0):
            print("No expenses Added. Go and spend some money")
        else:
            print("==== Total expense =====")
            count = 1
            for eachexpense in expenselist:
                print(f"Expense number {count} -> {eachexpense['Date']}, {eachexpense['Category']}, {eachexpense['Description']}, {eachexpense['Amount']}")
                count = count +1

# 3. View Total Spending
    elif(choice == "3"):
        total = 0
        for eachexpense in expenselist:
            total = total + eachexpense["Amount"]

        print("\n Total Khrcha = ",total)

# 4. Exit
    elif(choice == "4"):
        print("Thankyou for using our system")
        break
else:
     print("Invalid choce. TRY AGAIN ")

