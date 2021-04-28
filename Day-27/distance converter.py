from tkinter import Tk, StringVar, ttk,messagebox
from tkinter import *


root = Tk()
root.title("Distance Converter")
root.geometry("670x300")
root.configure(bg="black")
# =======FRAME============

top_frame = Frame(root, width=1000, height=50, bd=16, relief="raise")
top_frame.pack(side=TOP)
left_frame = Frame(root, width=450, height=300, bd=8, relief="raise")
left_frame.pack(side=LEFT)
right_frame = Frame(root, relief="raise", width=300, height=300, bd=8)
right_frame.pack(side=RIGHT)

# ============Variable================================
value = StringVar()
convert = DoubleVar()
distance = DoubleVar()


# ================Functions============================
def convert_distance():
    try:

        if value.get() == "Miles to Kilometers":
            value1 = round(float(convert.get() * 1.609344), 3)
            value2 = str(value1), "Kilometers"
            distance.set(value2)
        elif value.get() == "Kilometers to Miles":
            value1 = round(float(convert.get()/1.609433), 3)
            value2 = str(value1), "Miles"
            distance.set(value2)
        elif value.get() == "":
            messagebox.showinfo('Convert', "Make a selection from the SpinBox")
    except TclError:
        messagebox.showerror("Alert","That was no valid number. Try again...")

def exit_app():
    exit_app= messagebox.askyesno("Exit App", "Do you rally want to quit?")
    if exit_app > 0:
        root.destroy()
        return
def reset_default():
    value.set("")
    distance.set("0.0")
    convert.set("0.0")




# ==================LABEL & Entry=============================
title_label = Label(top_frame, font=("arial", 50, 'bold'), text="Distance Converter", padx=2, pady=2, bd=11, fg='black'
                    , relief='groove')
title_label.grid()

box = ttk.Combobox(left_frame, font=("arial", 20, 'bold'), width=30, state='readonly', textvariable=value)
box['values'] = ('', "Miles to Kilometers", "Kilometers to Miles")
box.current(0)
box.grid(row=0, column=0)

user_input = Entry(left_frame, textvariable=convert, font=("arial", 20, 'bold'), width=31, justify='center', bd=2)
user_input.grid(row=1, column=0)

converted_data = Entry(left_frame, textvariable=distance, font=("arial", 20, 'bold'), width=31, justify='center', bd=2,
                       relief='sunken')
converted_data.grid(row=2, column=0)

space_info = Label(left_frame, text="RFM APP", font=("arial", 20, 'bold'), width=31, justify='center', bd=2)

space_info.grid(row=3, column=0)

# =====================BUTTON=====================================
convert_button = Button(right_frame, text="Convert", width=9, bd=3, font=("arial", 20, 'bold',), bg="#c0ded9",
                        fg='black', pady=5, command=convert_distance).grid(row=0, column=0)
reset_button = Button(right_frame, text="Reset", width=9, bd=3, font=("arial", 20, 'bold',), bg="#c0ded9",
                      fg='black', pady=2, command=reset_default).grid(row=1, column=0)
exit_button = Button(right_frame, text="Exit", width=9, bd=4, font=("arial", 20, 'bold',), bg="#c0ded9",
                     fg='black', pady=5, command=exit_app).grid(row=2, column=0)

root.mainloop()
