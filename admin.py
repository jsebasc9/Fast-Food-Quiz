# Name: Juan Sebastian Calderon Cordoba
# Student Number:  10551059

# This file is provided to you as a starting point for the "admin.py" program of Assignment 2
# of Programming Principles in Semester 2, 2021.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter file runs smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the json module to allow us to read and write data in JSON format.
import json
data=[]

# This function repeatedly prompts for input until an integer is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.
def input_int(prompt):
    while True:
        try:
            response = int(prompt)
            if response <= 0:
                prompt = input('Invalid input - Try again: ')
            else:
                return response
                break
        except ValueError:
            prompt = input('Invalid input - Try again: ')
            continue
    # pass



# This function repeatedly prompts for input until something other than whitespace is entered.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def input_something(prompt):  
    while True: 
        if not prompt.strip():
            prompt = input('Invalid input - Try again: ')
        else:
            return prompt
            break
    # pass



# This function opens "data.txt" in write mode and writes data_list to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
def save_data(data_list):
    with open('data.json', 'w') as file:
            json.dump(data_list, file, indent=4)
    file.close()
    # pass



# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.

try:
    with open('data.json', 'r') as file: # Opening JSON File on read mode
        data = json.load(file) 
    print(data)
except FileNotFoundError: # In case there is no file
    print('File not found, will create a new one.')
    with open('data.json', 'w') as file:  # Create a file using write/read mode
        json.dump(data, file) 

file.close()

# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Requirements of admin.py" section of the assignment brief.
# The rest is up to you.
print('Welcome to the Fast-Food Quiz Admin Program.')

while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ').lower() # Convert input to lowercase to make choice selection case-insensitive.
        
    if choice == 'a':
        # Add a new fast-food item.
        fast_food = {'name':'', 'energy':'', 'fat':'', 'protein':'', 'carbohydrates':'', 'sugars':'', 'sodium':''}
        
        # repeatedly re-prompt the user for valid input no whitespace
        fast_food['name'] = input('Enter name of fast-food item: ')
        fast_food['name'] = input_something(fast_food['name']) # repeatedly re-prompt the user for valid input no whitespace         
        fast_food['energy'] = input('Enter energy in kilojoules: ')
        input_int(fast_food['energy']) # repeatedly re-prompt the user for valid input integer
        fast_food['fat'] = input('Enter fat in grams: ')
        input_int(fast_food['fat']) # repeatedly re-prompt the user for valid input integer
        fast_food['protein'] = input('Enter protein in grams: ')
        input_int(fast_food['protein']) # repeatedly re-prompt the user for valid input integer
        fast_food['carbohydrates'] = input('Enter carbohydrates in grams: ')
        input_int(fast_food['carbohydrates']) # repeatedly re-prompt the user for valid input integer
        fast_food['sugars'] = input('Enter sugars in grams: ')
        input_int(fast_food['sugars']) # repeatedly re-prompt the user for valid input integer
        fast_food['sodium'] = input('Enter sodium in milligrams: ')
        input_int(fast_food['sodium']) # repeatedly re-prompt the user for valid input integer

        data.append(fast_food) # Appending fast_food dictionary to data list
        save_data(data) # Saving information of the list in JSON
        print('Fast-food item added.')
        # pass


    
    elif choice == 'l':
        # List the current fast-food items.
        dictionary = {}
        if data:
            for index, itemlist in enumerate(data, 1): # Iterating data dictionary using enumerate to start from 1
                temp_dictionary = itemlist # Setting item as a Dictionary to iterate
                for itemdictionary, detail in temp_dictionary.items(): # Iterating dictionary
                    if itemdictionary == 'name': # Lookinf for key 'name'
                        name_item = detail # Setting name to display depending of key
                print(index, ') ', name_item, sep='', end='\n')        
        else:
            print('No items saved') 
        # See Point 4 of the "Requirements of admin.py" section of the assignment brief.
        # pass



    elif choice == 's':
        # Search the current fast-food items.
        flag_search = False # Defining flag to confirm available results
        index = 1 # Initialization of index for search results
        term = input('Enter search term: ')
        term = input_something(term) # repeatedly re-prompt the user for valid input no whitespace
        print(term)
        print('Search results: ')
        if data:
            for itemlist in data: # Iterating data dictionary
                temp_dictionary = itemlist # Setting item as a Dictionary to iterate
                for itemdictionary, detail in temp_dictionary.items(): # Iterating dictionary
                    if itemdictionary == 'name': # Looking for key 'name' and the term input by user
                        if term.lower() in detail.lower():
                            flag_search = True # Setting flag to confirm results available
                            print(index, ') ', detail, sep='', end='\n')
                            index += 1
            if not flag_search:
                print('No results found')
        else:
            print('No items saved')
        # See Point 5 of the "Requirements of admin.py" section of the assignment brief.
        # pass



    elif choice == 'v':
        # View a fast-food item.
        number_item = input('Enter item number to view: ')
        number_item = input_int(number_item) # repeatedly re-prompt the user for valid input integer
        if data:
                for index, itemlist in enumerate(data, 1): # Iterating data dictionary using enumerate to start from 1
                    temp_dictionary = itemlist # Setting item as a Dictionary to iterate
                    if int(number_item) <= len(data): # checking if index number entered does not exist
                        if int(number_item) == index: # checking if index is equal to number_item to print information
                            for itemdictionary, detail in temp_dictionary.items(): # Iterating dictionary
                                if itemdictionary == 'name': # Looking for key 'name'
                                    print(detail, sep='', end='\n')
                                if itemdictionary == 'energy': # Looking for key 'name' 
                                    number_calories = int(detail) / 4.184
                                    print('  Energy: ', detail, ' kilojoules (', round(number_calories),')',sep='', end='\n')
                                if itemdictionary == 'fat': # Looking for key 'name'
                                    print('  Fat: ', detail, ' grams', sep='', end='\n')
                                if itemdictionary == 'protein': # Looking for key 'name'
                                    print('  Protein: ', detail, ' grams',sep='', end='\n')
                                if itemdictionary == 'carbohydrates': # Looking for key 'name'
                                    print('  Carbohydrates: ', detail, ' grams',sep='', end='\n')
                                if itemdictionary == 'sugars': # Looking for key 'name'
                                    print('  Sugars: ', detail, ' grams',sep='', end='\n')
                                if itemdictionary == 'sodium': # Looking for key 'name'
                                    print('  Sodium: ', detail, ' milligrams',sep='', end='\n')
                    else:
                        print('Invalid index number') 
                        break    
        else:
            print('No items saved') 
        # See Point 6 of the "Requirements of admin.py" section of the assignment brief.
        # pass

        

    elif choice == 'd':
        # Delete a fast-food item.
        number_item = input('Enter item number to delete: ')
        number_item = input_int(number_item) # repeatedly re-prompt the user for valid input integer
        if data:
                for index, itemlist in enumerate(data, 1): # Iterating data dictionary using enumerate to start from 1
                    temp_dictionary = itemlist # Setting item as a Dictionary to iterate
                    if int(number_item) <= len(data): # checking if index number entered does not exist
                        if int(number_item) == index: # checking if index is equal to number_item to print information
                            for itemdictionary, detail in temp_dictionary.items(): # Iterating dictionary
                                if itemdictionary == 'name': # Looking for key 'name' and the term input by user1
                                    data.pop(index - 1) # deleting item from list with index less 1
                                    save_data(data) # Saving information of the list in JSON
                                    print(detail, 'deleted.')
                            break
                    else:
                        print('Invalid index number') 
                        break    
        else:
            print('No items saved') 
        # See Point 7 of the "Requirements of admin.py" section of the assignment brief.
        # pass

        

    elif choice == 'q':
        # End the program.
        print('Goodbye!')
        break
        # See Point 8 of the "Requirements of admin.py" section of the assignment brief.
        # pass



    else:
        # Print "invalid choice" message.
        print('Invalid choice')
        # See Point 9 of the "Requirements of admin.py" section of the assignment brief.
        # pass



# If you have been paid to write this program, please delete this comment.
