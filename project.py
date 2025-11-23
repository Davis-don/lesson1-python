import datetime
# Ask user for their name, age, and favourite subject
name,age,favourite_subject = input("Enter your name "),input("Enter your age "),input("Enter your favourite subject ")

# year born
def year_born(age):
    current_year = datetime.datetime.now().year
    return current_year - int(age)

# didplay message
def message(name,age,favourite_subject):
    birth_year = year_born(age)
    print(f"hello {name} you were born in  {birth_year} born and your favourite subject is {favourite_subject}")

message(name,age,favourite_subject)