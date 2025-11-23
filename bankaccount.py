# Welcome user to the app
print("Lets create a bank account for you!")
current_userName=""
# Define storage to store user data
userData = [
    {
        "name":"Davis",
        "password":"1235",
        "userName":"samorai",
        "startingBalance":4000
    }
]



# Create account for user and feed the starting data
def createAccount(Name,password,userName,startingAmount):
    # Check whether we have similar user 
    for user in userData:
        if user["userName"] == userName:
            print ("----------Failed to create account since similar user exists--------------")
            userEntryFunction()
    userData.append({
        "name":Name,
        "password":password,
        "userName":userName,
        "startingBalance":startingAmount
    })
    return

def userEntryFunction():
  choice1 = int(input("""What do you want to do today? enter(press 1 or 2)
1) Login into account
2) Open an account
choice: """))

  if choice1 == 1:
    print("please enter your username and password")
    userName = input ("userName: ")
    password = input ("password: ")
    login(userName,password)
  elif choice1 == 2:
      print("Lets create new account fot you")
      Name = input ("Enter your Name: ")
      password=input("Enter password to use: ")
      userName=input("enter a unique userName: ")
      startingAmount = int(input("Enter amount to start with: "))
      createAccount(Name,password,userName,startingAmount)
  else:
      print ("Invalid choice choose again")
  while choice1 != 1 or choice1 != 2:
   choice1 = int(input("""What do you want to do today? enter(press 1 or 2)
   1) Login into account
   2) Open an account
   choice: """))
   if choice1 == 1:
    print("please enter your username and password")
    userName = input ("userName: ")
    password = input ("password: ")
    login(userName,password)
    break;


    
   elif choice1 == 2:
      print("create new account")
      break;
   else:
      print ("Invalid choice choose again")

def login(userName, password):
    # Check for username match
    for user in userData:
        if user["userName"] == userName:
            print("-------------user found successfully--------------")
            if user["password"] == password:
                global current_userName
                current_userName = userName
                print("-----------Login successful----------")
                runme()
            else:
                print("---------------wrong password-----------")
            return   # ✅ exit only after handling this user
    # If loop finishes with no match:
    print("---------login failed------")
    userEntryFunction()


# Deposit function
def deposit(amount_to_deposit):
    for user in userData:
        if user["userName"] == current_userName:
            totalAmount = user["startingBalance"] + amount_to_deposit
            user["startingBalance"] = totalAmount
            print(f"------------Deposit of KES {amount_to_deposit} successful-------------")
        else:
            print("------------Deposit failed-------------")

# Widhdraw function
def withdraw(amount_to_withdraw):
    for user in userData:
        if user["userName"] == current_userName:
            if user["startingBalance"] >= amount_to_withdraw:
                totalAmount = user["startingBalance"] - amount_to_withdraw
                user["startingBalance"] = totalAmount
                print(f"------------Withdrawal of KES {amount_to_withdraw} successful-------------")
            else:
                print("------------Insufficient balance-------------")
        else:
            print("------------Withdrawal failed-------------")

# Check balance
def checkBalance():
    for user in userData:
        if user["userName"] == current_userName:
            balance = user["startingBalance"]
    print(f"----- confirmed your account balance is {balance}")

def combinedLoopingtransactions(choice):
    if choice == 1:
        depositAmount = int(input("Enter amount to deposit: "))
        deposit(depositAmount)
    elif(choice ==2):
        withdrawAmount = int(input("Enter amount to widtdraw"))
        withdraw(withdrawAmount)
    elif(choice == 3):
        checkBalance()
    elif(choice ==4):
        userEntryFunction()

def runme():
    choice = int(input("""
    1) Deposit
    2) Withdraw
    3) Check Balance
    4) Exit
    choice: """))
    combinedLoopingtransactions(choice)
    while(choice!=4):
        choice = int(input("""
        1) Deposit
        2) Withdraw
        3) Check Balance
        4) Exit
        choice: """))
        combinedLoopingtransactions(choice)
        

userEntryFunction()






# Flow logics
# Asks user to create or login




