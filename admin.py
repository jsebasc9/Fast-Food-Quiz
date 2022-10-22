import json # Import the json module read and write data in JSON format.
data = []   # Define data list to fill with information from data.txt

# This function repeatedly prompts for input until an integer is entered.
def input_int(prompt):
    while True:
        try:
            response = int(prompt)
            if response <= 0:
                prompt = input('Invalid input - Try again: ')
            else:
                return response
        except ValueError:
            prompt = input('Invalid input - Try again: ')
            continue


# This function repeatedly prompts for input until something other than whitespace is entered.
def input_something(prompt):  
    while True: 
        if not prompt.strip():
            prompt = input('Invalid input - Try again: ')
        else:
            return prompt


# This function opens "data.txt" in write mode and writes data_list to it in JSON format.
def save_data(data_list):
    with open('data.txt', 'w') as file:
            json.dump(data_list, file, indent=4)
    file.close()


# Opening data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# The program should need to read anything from the file.
try:
    with open('data.txt', 'r') as file: # Open JSON File on read mode
        data = json.load(file) 
    print(data)
except FileNotFoundError: # In case there is no file
    print('File not found, will create a new one.')
    with open('data.txt', 'w') as file:  # Create a file using write mode
        json.dump(data, file, indent=4) 
file.close()


# Print welcome message, then enter the endless loop which prompts the user for a choice.
print('Welcome to the Fast-Food Quiz Admin Program.')

while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.') # Display options
    choice = input('> ').lower() # Convert input to lowercase to make choice selection case-insensitive.

    # Add a new fast-food item.    
    if choice == 'a':
        
        # Set fast food dictionary
        fast_food = {'name':'', 'energy':'', 'fat':'', 'protein':'', 'carbohydrates':'', 'sugars':'', 'sodium':''}
        
        # Repeatedly re-prompt the user for valid input no whitespace 
        # for each nutritrional component and fast food item name
        fast_food['name'] = input('Enter name of fast-food item: ')
        fast_food['name'] = input_something(fast_food['name'])          
        fast_food['energy'] = input('Enter energy in kilojoules: ')
        input_int(fast_food['energy'])
        fast_food['fat'] = input('Enter fat in grams: ')
        input_int(fast_food['fat']) 
        fast_food['protein'] = input('Enter protein in grams: ')
        input_int(fast_food['protein'])
        fast_food['carbohydrates'] = input('Enter carbohydrates in grams: ')
        input_int(fast_food['carbohydrates'])
        fast_food['sugars'] = input('Enter sugars in grams: ')
        input_int(fast_food['sugars'])
        fast_food['sodium'] = input('Enter sodium in milligrams: ')
        input_int(fast_food['sodium'])

        data.append(fast_food) # Append fast_food dictionary to data list
        save_data(data) # Save information of the list in JSON
        print('Fast-food item added.')


    # List the current fast-food items.
    elif choice == 'l':
        # Check if there is data in the list
        if data:
            for index, itemlist in enumerate(data, 1): # Iterate data list using enumerate to start from 1
                temp_dictionary = itemlist # Set item as a Dictionary to iterate
                for itemdictionary, detail in temp_dictionary.items(): # Iterate dictionary
                    if itemdictionary == 'name': # Seach for key 'name'
                        name_item = detail # Set name to display depending of key
                print(index, ') ', name_item, sep='', end='\n') # Display item        
        # In case there is no data in the list
        else:
            print('No items saved') 


    # Search for the current fast-food items.
    elif choice == 's':
        flag_search = False # Set flag to confirm available results
        index = 1 # Initizilaze index for search results
        term = input('Enter search term: ')
        term = input_something(term) # Repeatedly re-prompt the user for valid input no whitespace
        print(term)
        print('Search results: ')
        # Check if there is no data in the list
        if data:
            for itemlist in data: # Iterate data list
                temp_dictionary = itemlist # Set item as a Dictionary to iterate
                for itemdictionary, detail in temp_dictionary.items(): # Iterate dictionary
                    if itemdictionary == 'name': #  Seach for key 'name' and the term input by user
                        if term.lower() in detail.lower():
                            flag_search = True # Set flag to confirm results available
                            print(index, ') ', detail, sep='', end='\n')
                            index += 1
            # check if there is no results for the search
            if not flag_search:
                print('No results found')
        # In case there is no data in the list
        else:
            print('No items saved')


    # View a fast-food item.
    elif choice == 'v':
        number_item = input('Enter item number to view: ')
        number_item = input_int(number_item) # Repeatedly re-prompt the user for valid input integer
        # Check if there is no data in the list
        if data:
                for index, itemlist in enumerate(data, 1): # Iterate data list using enumerate to start from 1
                    temp_dictionary = itemlist # Set item as a Dictionary to iterate
                    if int(number_item) <= len(data): # Check if index number entered does not exist
                        if int(number_item) == index: # Check if index is equal to number_item to print information
                            for itemdictionary, detail in temp_dictionary.items(): # Iterate dictionary
                                if itemdictionary == 'name': # Search for key 'name'
                                    print(detail, sep='', end='\n')
                                if itemdictionary == 'energy': # Search for key 'energy' 
                                    number_calories = float(detail) / 4.184
                                    print('  Energy: ', detail, ' kilojoules (', round(number_calories),' calories)',sep='', end='\n')
                                if itemdictionary == 'fat': # Search for key 'fat'
                                    print('  Fat: ', detail, ' grams', sep='', end='\n')
                                if itemdictionary == 'protein': # Search for key 'protein'
                                    print('  Protein: ', detail, ' grams',sep='', end='\n')
                                if itemdictionary == 'carbohydrates': # Search for key 'carbohydrates'
                                    print('  Carbohydrates: ', detail, ' grams',sep='', end='\n')
                                if itemdictionary == 'sugars': # Search for key 'sugars'
                                    print('  Sugars: ', detail, ' grams',sep='', end='\n')
                                if itemdictionary == 'sodium': # Search for key 'sodium'
                                    print('  Sodium: ', detail, ' milligrams',sep='', end='\n')
                    # In case the user put a none existing index
                    else:
                        print('Invalid index number') 
                        break    
        # In case there is no data in the list
        else:
            print('No items saved') 

        
    # Delete a fast-food item.
    elif choice == 'd':  
        number_item = input('Enter item number to delete: ')
        number_item = input_int(number_item) # Repeatedly re-prompt the user for valid input integer
        # Check if there is no data in the list
        if data:
                for index, itemlist in enumerate(data, 1): # Iterate data list using enumerate to start from 1
                    temp_dictionary = itemlist # set item as a Dictionary to iterate
                    if int(number_item) <= len(data): # check if index number entered does not exist
                        if int(number_item) == index: # check if index is equal to number_item to print information
                            for itemdictionary, detail in temp_dictionary.items(): # Iterate dictionary
                                if itemdictionary == 'name': # Search for key 'name' and the term input by user
                                    data.pop(index - 1) # Delete item from list with index less 1
                                    save_data(data) # Save information of the list in JSON
                                    print(detail, 'deleted.')
                            break
                    # In case the user put a none existing index
                    else:
                        print('Invalid index number') 
                        break    
        # In case there is no data in the list
        else:
            print('No items saved') 

        
    # End the program.
    elif choice == 'q':
        print('Goodbye!') # Display 'Goodbye!'
        break # Cleanly close of the program 


    # In case user chose a non existing option
    else:
        print('Invalid choice') # Display "invalid choice" message.

