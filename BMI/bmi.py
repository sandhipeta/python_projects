import tkinter

root = tkinter.Tk()

def calculate_bmi():
    height = int(height_textbox.get())
    weight = int(weight_textbox.get())
    
    height = height/100
    
    bmi = weight/(height*height)
    
    if bmi > 0:
        if bmi <= 16:
            result = "You are severly underweight"
        elif bmi <= 18.5:
            result = "You are underweight"
        elif bmi <= 25:
            result = "You are healthy"
        elif bmi <= 30:
            result = "You are overweight"
        else:
            result = "You are severly overweight"
    else:
        result = "Enter valid details"
    result_label.config(text=f"You are BMI report: {result}")
    
    
root.geometry('300x400')

height_label = tkinter.Label(root, text="Enter your height in centimeters:")
height_label.pack()
height_textbox = tkinter.Entry(root)
height_textbox.pack()

weight_label = tkinter.Label(root, text="Enter your weight in Kg:")
weight_label.pack()
weight_textbox = tkinter.Entry(root)
weight_textbox.pack()



calculate_btn = tkinter.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_btn.pack()

result_label = tkinter.Label(root, text="")
result_label.pack()

root.mainloop()