# Welcome user to the app
print("Lets create a bank account for you!")
# Define storage to store user data
userData = [
    # {
    #     "name":"Davis",
    #     "password":"As261",
    #     "userName":"samorai"
    # },
    #  {
    #     "name":"Danniel",
    #     "password":"1244",
    #     "userName":"samorai12"
    # }
]

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
      print("create new account")
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
                print("-----------Login successful----------")
            else:
                print("---------------wrong password-----------")
            return   # ✅ exit only after handling this user
    # If loop finishes with no match:
    print("---------login failed------")
    userEntryFunction()

# Create account for user and feed the starting data
def createAccount(Name,password,userName,startingAmount):
    # Check whether we have similar user 
    for user in userData:
        if user["userName"] == userName:
            print ("----------Failed to create account since similar user exists--------------")
    userData.append({
        "name":Name,
        "password":password,
        "userName":userName,
        "startingBalance":startingAmount
    })
    return






userEntryFunction()






# Flow logics
# Asks user to create or login




