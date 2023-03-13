# NAME: Zulkifli Temitope Salami	
# DATE: 12/03/2022
# PROGRAM DESCRIPTION: A Distance unit conversion GUI Application that allows initial entry for a distance to be converted to either 
# Kilometres (km) or miles (mi).
# PROGRAM NAME: Distance Unit Conversion GUI Application
#######################################################################################################################################


# Import tkinter library and tkinter tix library
from tkinter import *
from tkinter.tix import *
# Import sys for easy exit functionality
import sys

# Define functions for converting input to either kilometres or miles in relation to radio button
def calculate_output_value(_event=None):
    CONVERSION_FACTOR_MILES = 0.62137119
    CONVERSION_FACTOR_KILOMETRE = 1.609344
    # Validate input as numeric
    try:
        valid_input = float(entry_initial.get())
        # Check if initial entry is positive number. If not positive, display error message
        output_text = ''
        if valid_input > 0:
            # Calculate conversion from initial entry to kilometre if kilometre radio button selected
            if v.get() == 1:
                conversion_kilometre = valid_input * CONVERSION_FACTOR_KILOMETRE
                output_text = str(valid_input)+' mi converts to {:,.2f} km.'.format(conversion_kilometre)
            # Calculate conversion from initial entry to miles if miles radio button selected
            elif v.get() == 2:
                conversion_miles = valid_input * CONVERSION_FACTOR_MILES
                output_text = str(valid_input)+' km converts to {:,.2f} mi.'.format(conversion_miles)
            # Display Kilometre or miles output in relation to selected radio button, in output label field as 2 decimal places
        else:
            output_text ='ERROR! Initial input must be a positive number'

        label_conversion_output.configure(text=output_text)
    except:
        label_conversion_output.configure(text='ERROR! Initial Input must be numeric')

# Define function for clearing window
def clear_window(_event = None):
    # set all input and output fields to blank
    entry_initial.delete(0, END)
    label_conversion_output.configure(text='')
    # put focus back on first data entry, for fast data entry
    entry_initial.focus()
# Define function for closing window
def close_window(_event = None):
    sys.exit()

# Create and name a tk window
window = Tk()
# define window size and window minimum size
window.geometry("500x500")
window.minsize(width= 250, height= 250)
# define the title of window
window.title("Distance Unit Conversion GUI Application")

# Create a Ballon object for tooltips
tooltip = Balloon(window)

# Define radio button variable “v” as an integer
v = IntVar()
# Set initial radio button selection to kilometre
v.set(1)

# Create widgets on row 0
label_initial_entry = Label(text='Initial Distance')
label_initial_entry.grid(row=0,column=0,sticky=E,padx=5,pady=5)
entry_initial = Entry(width=15,borderwidth=5)
entry_initial.grid(row=0,column=1,padx=5,pady=5)
tooltip.bind_widget(entry_initial, msg='Enter the initial distance to be converted as a positive number.\nNOTE: negative numbers would provide error message.')
# Create widgets on row 1
radio_button = Radiobutton(text='Kilometre', value=1, variable=v)
radio_button.grid(row=1,column=0,padx=5,pady=5)
tooltip.bind_widget(radio_button, msg='Click to convert to Kilometres')
radio_button = Radiobutton(text='Miles', value=2, variable=v)
radio_button.grid(row=1,column=1,padx=5,pady=5)
tooltip.bind_widget(radio_button, msg='Click to convert to Miles')
# Create widgets on row 2
label_conversion = Label(text='Converted output')
label_conversion.grid(row=2,column=0,padx=5,pady=5,sticky=E)
label_conversion_output = Label(width=35,bd=5,relief=SUNKEN)
label_conversion_output.grid(row=2,column=1,padx=5,pady=5)
tooltip.bind_widget(label_conversion_output, msg='Displays the Converted distance')
# Create widgets on row 3
button_calculate = Button(text='Calculate', command = calculate_output_value)
button_calculate.grid(row=3,column=0,pady=20)
tooltip.bind_widget(button_calculate, msg='Press Button to Calculate and Display converted distance')
button_clear = Button(text='Clear', command= clear_window)
button_clear.grid(row=3,column=1,padx=5,pady=20)
tooltip.bind_widget(button_clear, msg='Press Button to Clear fields and start all over from begining')
button_close = Button(text='Close', command = close_window)
button_close.grid(row=3,column=2,padx=5,pady=20)
tooltip.bind_widget(button_close, msg='Press Button to Close the window')

# Add hotkeys for executing calculate function, clear function, close function
window.bind('<Return>', calculate_output_value)
window.bind('<Alt-c>', clear_window)
window.bind('<Alt-x>', close_window)



# run the UI main loop
window.mainloop()
