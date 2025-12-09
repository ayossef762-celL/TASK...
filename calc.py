# يوسف احمد المحمدي 


from tkinter import *

def get_numbers():
    try:
        x = float(entry_a.get())
        y = float(entry_b.get())
        return x, y
    except ValueError:
        result_label["text"] = "Enter valid numbers"
        return None, None

def add():
    x, y = get_numbers()
    if x is None: return
    result_label["text"] = "Result: " + str(x + y)

def sub():
    x, y = get_numbers()
    if x is None: return
    result_label["text"] = "Result: " + str(x - y)

def mul():
    x, y = get_numbers()
    if x is None: return
    result_label["text"] = "Result: " + str(x * y)

def div():
    x, y = get_numbers()
    if x is None: return
    if y == 0:
        result_label["text"] = "Cannot divide by zero"
    else:
        result_label["text"] = "Result: " + str(x / y)

root = Tk()
root.title("Simple Calculator")
root.geometry("320x350") 

Label(root, text="Number 1").pack(pady=5)
entry_a = Entry(root, font=("Arial", 14))
entry_a.pack(pady=5) 

Label(root, text="Number 2").pack(pady=5)
entry_b = Entry(root, font=("Arial", 14))
entry_b.pack(pady=5) 

btn_frame = Frame(root)
btn_frame.pack(pady=15) 

Button(btn_frame, text="+", width=6, font=("Arial", 12), command=add).grid(row=0, column=0, padx=5, pady=5)
Button(btn_frame, text="-", width=6, font=("Arial", 12), command=sub).grid(row=0, column=1, padx=5, pady=5)
Button(btn_frame, text="x", width=6, font=("Arial", 12), command=mul).grid(row=1, column=0, padx=5, pady=5)
Button(btn_frame, text="/", width=6, font=("Arial", 12), command=div).grid(row=1, column=1, padx=5, pady=5)

result_label = Label(root, text="Result:", font=("Arial", 13))
result_label.pack(pady=15) 

root.mainloop()