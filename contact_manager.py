# Build a Contanct Management program with features outlined in README.

# This is a big one so lets start with pseudocode.

#1. Build the CLI (I can edit the main function after I write the functions)

#2. Write a function for printing the main menu

#3. Write out each of the reatures

#4. Write in error checking

#5. Considering building import contacts feature (possibly out of scope)

#import modules, setup regex patterns, and initialize dictionary

import re
import os
import datetime

# We will organize using a dict as the phone number for the Key, and a list for the values
# { Phone Number : [Name, Phone Number, Email Address, Notes]}

contacts = {} #Initialize Dict

# contacts = { "8585559778" : [ "Adam S", "8585559778", "adam@gmail.com", "whatever its 2009" ], 
# "8585559999" : [ "Bilbo Baggins" , "8585559999", "bilbo@gmail.com", "hobbit" ]}

# The above is a testing line, remove the comment if you want to test with info already loaded into the dict

#Setup Regex Patterns for later

name = ""
phone = ""
email = ""

namepatt = re.compile("[A-Za-z0-9._%+-]+\s+[A-Za-z0-9._%+-]+") #NOTE: Input accepts special characters. I used a positive lookahead to include results with a space in the last name. Like Mac Donald. If this dont work consider removing the lookahead
phonepatt = re.compile("[0-9]{3}[0-9]{3}[0-9]{4}")
emailpatt = re.compile("[A-Za-z0-9._%+-]+@[A-Za-z0-9._%+-]+\.[A-Z|a-z]{2,}")

print("Hello User! Welcome to the Contact Management System.")

def main():
    try:
        while True:
            print(f'''{"*"*7} Main Menu {"*"*7}
            1. Add a new contact
            2. Edit an existing contact
            3. Delete a contact
            4. Search for a contact
            5. Display all contacts
            6. Export to text file
            7. Import from text file
            8. Quit''')
            command = int(input("Input a number to make a selection:"))
            if command == 1:
                print(f"Adding contact.")
                addcontact()
            elif command == 2:
                print(f"Editing contact.")
                editcontact()
            elif command == 3:
                print(f"Deleting contact.")
                delcontact()
            elif command == 4:
                print(f"Searching for contact.")
                srchcontact()
            elif command == 5:
                print(f"Displaying all contacts: ")
                dispcontacts()
            elif command == 6:
                print(f"Exporting your contacts to a text file.")
                expcontacts()
            elif command == 7:
                print(f"Importing from text file. (Not Yet Implemented)")
                impcontacts()
            elif command == 8:
                print(f"Qutting the program. Goodbye!")
                break
    except Exception as e:
        print(f"An unexpected error occurred: {e}\n Please restart the program. :)")

def addcontact():
    try: #Take user input
        name = str(input("Please input the new contact's first and last name: "))
        phone = str(input("Please input the new contact's phone number: "))
        email = str(input("Please input the new contact's email address: "))
        notes = str(input("Please input any additional notes: "))
        #Apply Regex Patterns to verify inputs
        v_name = namepatt.match(name) #NOTE: Input accepts special characters. I used a positive lookahead to include results with a space in the last name. Like Mac Donald. If this dont work consider removing the lookahead
        v_phone = phonepatt.match(phone)
        v_email = emailpatt.match(email)
        print(f"Adding the entry: {v_name.group()}, {v_phone.group()}, {v_email.group()}, {notes} to your Contacts List.")
        contacts[v_phone.group()] = [v_name.group(),v_phone.group(),v_email.group(),notes] # Then we just add the new entry to the dict
    except Exception as e: #Make error checking more robust if needed
        print(f"Error Occurred: {e}")

def editcontact():
    try:
        contact = str(input("Please type the contact's first and last name: "))
        v_contact = namepatt.search(contact)
        for value in contacts.values:
            if value[0] == v_contact.group(): #Make sure to add an elif incase its not found
                print(f'''Contact {v_contact.group()} found!
    Which contact detail would you like to edit?
    1. Name
    2. Phone Number
    3. Email
    4. Notes''')
                editcommand = int(input("Input a number to make a selection: "))
                if editcommand == 1:
                    name = str(input("Input the new name: "))
                    v_name = namepatt.search(name)
                    oldname = contacts[v_name.group()[0]]
                    contacts[v_contact.group()][0] = v_name
                    print(f"The name {oldname} has been updated to {v_name.group()}.")
                elif editcommand == 2:
                    phone = str(input("Input the new phone number: "))
                    v_phone = phonepatt.search(phone)
                    oldphone = contacts[v_contact.group()[1]]
                    contacts[v_contact.group()][1] = v_phone
                    print(f"The phone number {oldphone} has been updated to {v_phone.group()}.")
                elif editcommand == 3:
                    email = str(input("Input the new email: "))
                    v_email = emailpatt.search(email)
                    oldemail = contacts[v_contact.group()[2]]
                    contacts[v_contact.group()]
                    print(f"The email {oldemail} has been updated to {v_email.group()}.")
                elif editcommand == 4:
                    notes = str(input("Input the new note: "))
                    contacts[v_contact.group()[3]] = notes
                    print(f"The note for contact {v_contact.group()} has been overwritten with the new note: {notes} ")
            else:
                print(f"{v_contact.group()} not found! Back to Main Menu. ")
    except Exception as e:
        print(f"Error Occurred: {e}")

def delcontact():
    try:
        contact = str(input("Please type the first and last name of the contact you'd like to delete: "))
        v_contact = namepatt.search(contact)
        for value in contacts.values:
            if value[0] == v_contact.group():
                del contacts[value]
                print(f"Deleted {v_contact.group()}'s contact information.")
    except Exception as e:
        print(f"Error Occurred: {e}")

def srchcontact():
    try:
        phone = str(input("Input the Contact's phone number: "))
        v_phone = phonepatt.search(phone)
        contact = v_phone.group()
        if v_phone.group() in contacts.keys():
            print(f"True")
            print(f'''{"*"*7} Found Contact for {v_phone.group()}
                Name: {contacts[contact][0]}
                Phone: {contacts[contact][1]}
                Email: {contacts[contact][2]}
                Notes: {contacts[contact][3]}\n''')
    except Exception as e:
        print(f"Error Occurred: {e}")

def dispcontacts():
    if not contacts: #Error fixing for a bug thrown when the contacts dict is empty
        print(f"Your Contact List is currently empty. Try adding a new contact, and then access this feature again.")

    for key, info in contacts.items():
        print(f'''{"*"*5}
    Name: {info[0]}
    Phone: {info[1]}
    Email: {info[2]}
    Notes: {info[3]}''')

def expcontacts():
    try:
        with open("contacts_export.txt", "w") as file:
            for key, info in contacts.items(): #consider a sort or enumerate here to number the list
                file.write(f'''{"*"*5}
    Name: {info[0]}
    Phone: {info[1]}
    Email: {info[2]}
    Notes: {info[3]}\n''')
        print("Contacts List exported as 'contacts_export.txt'!")
    except Exception as e:
        print(f"Error Occurred: {e}")

def impcontacts():
        print(f"Importing previously exported contacts...")
        print(f"Whoops, this feature is not completed! Sending you back to the Main Menu.")
#         try:
#             with open("contacts_export", "r") as file:
#                 next()
#                 for line in file:

main()