from tkinter import *

# function to calculate result
def calculate():
    name = entry_name.get()
    
    m1 = int(entry_m1.get())
    m2 = int(entry_m2.get())
    m3 = int(entry_m3.get())

    total = m1 + m2 + m3
    avg = total / 3

    if avg >= 35:
        result = "Pass"
    else:
        result = "Fail"

    label_result.config(
        text=f"Name: {name}\nTotal: {total}\nAverage: {avg:.2f}\nResult: {result}"
    )


# main window
root = Tk()
root.title("Student Marks Calculator")
root.geometry("350x350")

# labels and entry boxes
Label(root, text="Student Name").pack()
entry_name = Entry(root)
entry_name.pack()

Label(root, text="Math Marks").pack()
entry_m1 = Entry(root)
entry_m1.pack()

Label(root, text="Science Marks").pack()
entry_m2 = Entry(root)
entry_m2.pack()

Label(root, text="English Marks").pack()
entry_m3 = Entry(root)
entry_m3.pack()

# button
Button(root, text="Calculate Result", command=calculate).pack(pady=10)

# result label
label_result = Label(root, text="")
label_result.pack()

root.mainloop()