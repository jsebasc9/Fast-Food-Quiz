import tkinter
from tkinter import font
import tkinter.messagebox
import json
from typing import Sized
import random


class MyGUI:
    def __init__(self):

        self.main_window = tkinter.Tk() # Create the main window.
        self.main_window.title('Fast-Food Quiz') # main window title
        self.main_window.geometry('300x100') # main window size
        self.main_window.resizable(0, 0) # Prevent the main window from being resized
        # Create three frames. One for the Radiobuttons
        # and another for the regular Button widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)


        try:
            with open('data.json', 'r') as file: # Opening JSON File on read mode
                self.data = json.load(file) 
            
            if not len(self.data) >= 2:
                self.main_window.destroy()
                return
            # else:
            #     print(self.data)
            #     print(len(self.data))

        except FileNotFoundError: # In case there is no file
            print('Missing/Invalid file')
            self.main_window.destroy()
            return

        file.close()

        self.components = ['energy','fat','protein','carbohydrates','sugars','sodium'] # attribute named “self.components” and set it to a list containing different strings

        # Create one label call Which one has more...
        self.label1 = tkinter.Label(self.top_frame, text='Which one has more...')

        # Pack Label Which one has more.
        self.label1.pack(side='top')

        # Create one label call Fillings:
        self.label2 = tkinter.Label(self.middle_frame, text='Fillings:', font=10)

        # Pack Label Fillings
        self.label2.pack(side='top')

        # Create a left button
        self.left_button = tkinter.Button(self.bottom_frame, text='', padx=10, command=lambda: self.check_answer('left'))
        # Create a middle button
        self.middle_button = tkinter.Button(self.bottom_frame, text='Roughly Equal', padx=10, command=lambda: self.check_answer('middle'))
        # Create a right button
        self.right_button = tkinter.Button(self.bottom_frame, text='', padx=10, command=lambda: self.check_answer('right'))

        # Pack the Buttons
        self.left_button.pack(side='left')
        self.middle_button.pack(side='left')
        self.right_button.pack(side='left')

        # Pack the frames 
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        self.show_question() # method to display the first question in the GUI
        
        # Start the mainloop.
        tkinter.mainloop()

    # responsible for randomly selecting two fast-food items and a nutritional component
    def show_question(self):
        
        self.nutrional_component = random.choice(self.components) # select one random nutritional component from components
        self.label2.config(text=self.nutrional_component.upper()) # setting text on label with uppercase letters

        self.random_items = random.sample(self.data, 2) # select two random items from data
        print(self.random_items)
        for itemlist in self.random_items: # Iterating data dictionary
                temp_dictionary = itemlist # Setting item as a Dictionary to iterate
                for itemdictionary, detail in temp_dictionary.items(): # Iterating dictionary
                    if itemdictionary == 'name': # Looking for key 'name' and the term input by user
                        temp_left = self.left_button.cget('text') # getting inital text to set text on buttons
                        if temp_left == '':
                            self.left_button.config(text=detail) # setting name of item to the left button 
                        else:
                            self.right_button.config(text=detail) # setting name of item to the right button 

    # responsible for determining whether the user answered correctly
    def check_answer(self, choice):  
        temp_value_left = 0  # Initialzing value for left to compare
        temp_value_right = 0 # Initialzing value for right to compare

        for itemlist in self.random_items: # Iterating data dictionary
            temp_dictionary = itemlist # Setting item as a Dictionary to iterate
            for itemdictionary, detail in temp_dictionary.items(): # Iterating dictionary
                if itemdictionary == self.nutrional_component: # Looking for key nutritional component
                    
                    if temp_value_left == 0: 
                        temp_value_left = int(detail) # Setting detail of the nutricional component for left button choice
                        print('L: ', temp_value_left)
                    else :
                        temp_value_right = int(detail) # Setting detail of the nutricional component for right button choice
                        print('R: ',temp_value_right)

                    # print(detail, sep='', end='\n')
                    
        # conditions to check if choice is correct or incorrect
        if choice == 'left':
            if temp_value_left > temp_value_right:
                tkinter.messagebox.showinfo('Correct!', 'You got it right.')
            if temp_value_left < temp_value_right:
                tkinter.messagebox.showerror('Incorrect!', 'You got it wrong.')
        
        if choice == 'right':
            if temp_value_left < temp_value_right:
                tkinter.messagebox.showinfo('Correct!', 'You got it right.')
            if temp_value_left > temp_value_right:
                tkinter.messagebox.showerror('Incorrect!', 'You got it wrong.')
            

        # if choice == 'middle':

        # self.show_question()


# Create an instance of the MyGUI class.
my_gui = MyGUI()