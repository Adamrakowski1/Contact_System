import json

#Function to add a new person
def add_person(people):
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")

    #Check if trying to add a contact that already exists
    if name in people:
        print("This name already exists. Please use a unique name.")
    else:
    	#If name does not exist, add to people dictionary with key name and values age and email
        people[name] = {"age": age, "email": email}
        print(f"Added {name}")

#Function to display all contacts
def display_people(people):
	#If there are no contacts in people, print no contacts available
    if not people:
        print("No contacts available.")
    #Prints each contact in people
    for i, (name, details) in enumerate(people.items(), start=1):
        print(f"{i} - {name} | {details['age']} | {details['email']}")

#Function to delete a contact
def delete_contact(people):
    display_people(people)

    #Deletes the contact of person input by user
    while True:
        name = input("Enter the name to delete: ")
        if name in people:
            del people[name]
            print(f"{name} was deleted")
            break
        #Keeps asking user for a contact to delete if invalid name is input
        else:
            print("Contact not found. Please enter a valid name.")

#Function to search for a contact
def search(people):
    search_name = input("Search for a name: ").lower()

    #Looks for contacts that contains the name provided
    results = {name: details for name, details in people.items() if search_name in name.lower()}

    #If name found, display contact, else, show error
    if results:
        display_people(results)
    else:
        print("No contacts found matching the search criteria.")

#Function to sort contacts
def sort_contacts(people):
    while True:
    	#Keep asking for a criteria to sort by until one is found, prompt user again if criteria is not in people
        sort_by = input("Sort by 'name', 'age', or 'email': ").lower()
        if sort_by in {"name", "age", "email"}:
        	#Sorts items based on key provided by user
            sorted_people = dict(
                sorted(
                    people.items(),
                    key=lambda x: x[0].lower() if sort_by == "name" else x[1][sort_by].lower() if sort_by == "email" else int(x[1][sort_by])
                )
            )
            #Show the new dictionary
            display_people(sorted_people)
            #Exit loop
            return sorted_people
        else:
            print("Invalid sort option. Please choose 'name', 'age', or 'email'.")

#Main program
print("Hello, welcome to contact management system. \n")

#Loads a JSON file with the contact data and creates a dictionary from it. If it does not exist, makes empty dictionary
try:
    with open("contacts.json", "r") as f:
        data = json.load(f)
        people = {person["name"]: {"age": person["age"], "email": person["email"]} for person in data["contacts"]}
except (FileNotFoundError, json.JSONDecodeError):
    people = {}

while True:
    print("\nContact list size:", len(people))
    #Prompt user for action
    command = input("You can 'Add', 'Delete', 'Search', 'Sort', or 'Q' to quit: ").lower()

    if command == "add":
        add_person(people)
    elif command == "delete":
        delete_contact(people)
    elif command == "search":
        search(people)
    elif command == "sort":
        people = sort_contacts(people)  #Update the dictionary with the sorted version
    elif command == "q":
        break
    else:
        print("Invalid command")

#Save contacts to the file
with open("contacts.json", "w") as f:
    json.dump({"contacts": [{"name": name, **details} for name, details in people.items()]}, f)

print("Contacts saved. Goodbye!")

