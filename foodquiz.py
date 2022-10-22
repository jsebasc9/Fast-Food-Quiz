import tkinter  # Import the tkinter library to execute GUI on Python.
import tkinter.messagebox  # Import messagebox module to show errors and info.
import json  # Import the json module read and write data in JSON format.
import random  # Import random to generate random components

# Class denifition
class MyGUI: 
    def __init__(self):  # Constructor definition.

        self.main_window = tkinter.Tk()  # Create the main window.
        self.main_window.title('Fast-Food Quiz')  # Main window title.
        self.main_window.geometry('300x100')  # Main window size.
        self.main_window.eval('tk::PlaceWindow . center')  # Running Main window in the centre.
        self.main_window.resizable(0, 0)  # Prevent the main window from being resized.

        # Create three frames.
        self.top_frame = tkinter.Frame(self.main_window)  # One frame for label 'Which one has more? text'.
        self.middle_frame = tkinter.Frame(self.main_window)  # Another frame for label fast-food item.
        self.bottom_frame = tkinter.Frame(self.main_window)  # Another frame for regular buttons widgets.


        # Opening data.txt and read the data into a "self.data".
        # If the file does not exist or does not contain enough 
        # JSON data, Missing/Invalid message is showed instead.
        try:
            with open('data.txt', 'r') as file:  # Opening JSON File on read mode.
                self.data = json.load(file) 
            # If number of items in JSON data is less than 2 
            # display Invalid file message and ends program cleanly.
            if len(self.data) < 2:
                tkinter.messagebox.showerror('Error','Invalid File, data.txt contain less than 2 items')
                self.main_window.destroy()
                return

        except FileNotFoundError:  # Exception in case there is no file.
            tkinter.messagebox.showerror('Error','Missing data.txt file')
            self.main_window.destroy()
            return
        file.close()  # Close file.

        # Set components containing different fast foodcomponents as strings.
        self.components = ['energy','fat','protein','carbohydrates','sugars','sodium'] 

        # Create one label call 'Which one has more...'.
        self.label1 = tkinter.Label(self.top_frame, text='Which one has more...')
        # Pack Label 'Which one has more...'.
        self.label1.pack(side='top')

        # Create one label of Nutritional Component.
        self.label2 = tkinter.Label(self.middle_frame, font=10)
        # Pack Label Fillings.
        self.label2.pack(side='top')

        # Create a left button and call check_answer funtion.
        self.left_button = tkinter.Button(self.bottom_frame, text='', padx=10, command=lambda: self.check_answer('left'))
        # Create a middle button and call check_answer funtion.
        self.middle_button = tkinter.Button(self.bottom_frame, text='Roughly Equal', padx=10, command=lambda: self.check_answer('middle'))
        # Create a right button and call check_answer funtion.
        self.right_button = tkinter.Button(self.bottom_frame, text='', padx=10, command=lambda: self.check_answer('right'))

        # Pack the Buttons.
        self.left_button.pack(side='left')
        self.middle_button.pack(side='left')
        self.right_button.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        # Display the first question in the GUI.
        self.show_question()  
        
        # Start the mainloop.
        tkinter.mainloop()

    # Responsible for randomly selecting two fast-food items and a nutritional component.
    def show_question(self):
        
        self.nutrional_component = random.choice(self.components)  # Select one random nutritional component from components.
        self.label2.config(text=self.nutrional_component.upper())  # Set text on label with uppercase letters.

        self.random_items = random.sample(self.data, 2)  # Select two random items from data.
        self.left_button.config(text='')  # Clear Left Button Text when there is next question in the GUI.
        self.right_button.config(text='')  # Clear Right Button Text there is next question in the GUI.

        for itemlist in self.random_items:  # Iterate list.
                temp_dictionary = itemlist  # Set list as a Dictionary to iterate.
                for itemdictionary, detail in temp_dictionary.items():  # Iterate dictionary.
                    if itemdictionary == 'name':  # Check for key 'name' and the term input by user.
                        temp_left = self.left_button.cget('text')  # Get inital text to set text on buttons.
                        if temp_left == '': # Check if left button is empty.
                            self.left_button.config(text=detail)  # Set name of item to the left button.
                        else:
                            self.right_button.config(text=detail)  # Set name of item to the right button 

    # Responsible for determining whether the user answered correctly.
    def check_answer(self, choice):  
        temp_value_left = 0  # Initialize value for left choice to compare.
        temp_value_right = 0  # Initialize value for right choice to compare.

        for itemlist in self.random_items:  # Iterate list.
            temp_dictionary = itemlist  # Set list as a Dictionary to iterate.
            for itemdictionary, detail in temp_dictionary.items():  # Iterate dictionary.
                if itemdictionary == self.nutrional_component:  # Check for key nutritional component.
                    
                    if temp_value_left == 0: # Check if left button is empty.
                        temp_value_left = int(detail)  # Set detail of the nutricional component for left button choice.
                    else :
                        temp_value_right = int(detail)  # Set detail of the nutricional component for right button choice.

        # Check if left button choice is correct or incorrect.
        if choice == 'left':
            if temp_value_left > temp_value_right: # Check if left value component is greater than right component value.
                tkinter.messagebox.showinfo('Correct!', 'You got it right.') 
            if temp_value_left < temp_value_right:  # Check if left value component is less than right component value.
                tkinter.messagebox.showerror('Incorrect!', 'You got it wrong.')
            if temp_value_left == temp_value_right:  # Check if left value component is equal to right component value.
                tkinter.messagebox.showerror('Incorrect!', 'You got it wrong.')
        
        # Check if right button choice is correct or incorrect.
        if choice == 'right':
            if temp_value_left < temp_value_right:  # Check if left value component is less than right component value.
                tkinter.messagebox.showinfo('Correct!', 'You got it right.')  
            if temp_value_left > temp_value_right:  # Check if left value component is greater than right component value.
                tkinter.messagebox.showerror('Incorrect!', 'You got it wrong.')  
            if temp_value_left == temp_value_right:  # Check if left value component is equal to right component value.
                tkinter.messagebox.showerror('Incorrect!', 'You got it wrong.')  

        # Check if middle button choice is correct or incorrect    
        if choice == 'middle':
            smaller_value = min(temp_value_left, temp_value_right)  # Set the smaller value between both nutritional components.
            higher_value = max(temp_value_left, temp_value_right)  # Set the higher value between both nutritional components.
            percentage_value = float(smaller_value * 1 / higher_value)  # Calculate percentage to compare if is at least 90 %.

            # Check the smaller value is at least 90 % of the higher value to select corret or incorrect.
            if percentage_value >= 0.9 and percentage_value <= 1.0:
                tkinter.messagebox.showinfo('Correct!', 'You got it right.')
            else:
                tkinter.messagebox.showerror('Incorrect!', 'You got it wrong.')

        # Display the next question in the GUI.
        self.show_question()  

# Create an instance of the MyGUI class.
my_gui = MyGUI()