"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("Chamaiporn",19, "Chachoengsao", "TH")  # name, age, city, country
    hobbies = []
    while True:
        choice = input("what do you want to do?(1:Display 2:append hobbies 3:remove hobbies 4:edit age 5:exit):")
        # Your code here
        if choice =="1":
            #Display information
            print("Name: ",person[0])
            print(f"Age: {person[1]}")
            print("City: "+person[2])
            print("Country: ",person[3])
            print("Hobbies: ",hobbies)
        elif choice =="2":
            #append hobbies
            hobby = input("What is your new hobbies?: ")
            hobbies.append(hobby)
        elif choice =="3":
            #remove
            hobbies.pop()
        elif choice =="4":
            #edit age
            person_list = list(person)
            age = input("how old are you?: ")
            person_list[1] = age
            person  = tuple(person_list)
        elif choice =="5":
            break
        

if __name__ == "__main__":
    personal_info_manager()