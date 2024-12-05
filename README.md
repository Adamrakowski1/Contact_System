# Contact Management System

This is a Python-based Contact Management System that allows users to manage their contact list efficiently. Users can add, display, delete, search, and sort contacts. All data is saved to a JSON file for persistence between sessions.

---

## Features

- **Add a Contact**: Add a new contact with a unique name, age, and email.
- **Display Contacts**: View all stored contacts in a formatted list.
- **Delete a Contact**: Remove a contact by name.
- **Search Contacts**: Search for contacts by name (case-insensitive).
- **Sort Contacts**: Sort contacts by name, age, or email.
- **Persistent Storage**: Contacts are saved to a JSON file (`contacts.json`) and reloaded upon restarting the program.

---

## How to Use

### Prerequisites

- Python 3.x must be installed on your system.

### Running the Program

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/contact-management-system.git
   cd contact-management-system

2. Run the program
   ```bash
   python contact_management.py
   
### Commands and Example Usage
Here are examples of the commands and their outputs when using the program:

## Adding a Contact
    You can 'Add', 'Delete', 'Search', 'Sort', or 'Q' to quit: add
    Name: Alice
    Age: 30
    Email: alice@example.com
    Added Alice
    
## Displaying Contacts 
    You can 'Add', 'Delete', 'Search', 'Sort', or 'Q' to quit: 
    Contact list size: 2
    1 - Alice | 30 | alice@example.com
    2 - Bob | 25 | bob@example.com

## Searching for a Contact
    You can 'Add', 'Delete', 'Search', 'Sort', or 'Q' to quit: search
    Search for a name: ali
    1 - Alice | 30 | alice@example.com

## Sorting Contacts
    You can 'Add', 'Delete', 'Search', 'Sort', or 'Q' to quit: sort
    Sort by 'name', 'age', or 'email': age
    1 - Bob | 25 | bob@example.com
    2 - Alice | 30 | alice@example.com

## Deleting a Contact
    You can 'Add', 'Delete', 'Search', 'Sort', or 'Q' to quit: delete
    Contact list size: 2
    1 - Alice | 30 | alice@example.com
    2 - Bob | 25 | bob@example.com
    Enter the name to delete: Bob
    Bob was deleted

## Exiting the Program
    You can 'Add', 'Delete', 'Search', 'Sort', or 'Q' to quit: q
    Contacts saved. Goodbye!


### File Structure

## contacts.json

The program uses a JSON file to store contact information persistently. The structure of the file is as follows:

      {
      "contacts": [
          {"name": "Alice", "age": "30", "email": "alice@example.com"},
          {"name": "Bob", "age": "25", "email": "bob@example.com"}
        ]
    }

### Known Limitations
- Age and email are stored as strings and are not validated.
- Sorting by age assumes that all ages are valid integers.

### Future Improvements
- Add input validation for age and email.
- Allow users to update contact details.
- Handle duplicate names more effectively.



