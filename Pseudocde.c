// 1.

import json library

Try to open file using "data.txt" parameter in read mode, store as "file"
    If the file is not found, create empty list named "data"

Read all lines in JSON format of "file" into a list, store as list name "data"
Close the "file" file

// 2.

print a welcome message with "Welcome to the Fast-Food Quiz Admin Program."

while endless loop

    print a message with "Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit."
    
    Prompts the user to enter their choice "a, l, s, v, d, q"
    Convert input to lowercase to make choice selection case-insensitive.

//  3.
    if choice is "a"
        create "fast_food" dictionary
    
        for each fast-food "item_fast_food" in the "fast_food" dictionary
            Promt the user to enter the "detail_fast_food"
            Add "detail_fast_food" to "fast_food" dictionary, with "item_fast_food" as the key

        Append the "fast_food" dictionary to the "data" list
        Open file using "data.txt" parameter in write mode
        Write the "data" results in JSON format
        Close the "file" file

//  4.
    elif choice is "l"
        if "data" list is empty
            print "No items saved"
        else
            for items in "data" list
                print the name of item and index starting from 1


    
    elif choice is "s"
        Search the current fast-food items.
        See Point 5 of the "Requirements of admin.py" section of the assignment brief.

    elif choice is "v"
        View a fast-food item.
        See Point 6 of the "Requirements of admin.py" section of the assignment brief.

    elif choice is "d"
        Delete a fast-food item.
        See Point 7 of the "Requirements of admin.py" section of the assignment brief.
   
    elif choice is "q"
        End the program.
        See Point 8 of the "Requirements of admin.py" section of the assignment brief.

    else:
        Print "invalid choice" message.
        See Point 9 of the "Requirements of admin.py" section of the assignment brief.