import pandas as pd
from tkinter import *

def submit_data():
    full_name = entry_1.get()
    email = entry_2.get()
    presentation = var.get()
    language = c.get()
    interested = var1.get()
    
    # Store data in a dictionary
    data = {
        "Full Name": [full_name],
        "Email": [email],
        "Presentation": [presentation],
        "Language": [language],
        "Interested": ["Yes" if interested else "No"]
    }
    
    # Create a DataFrame from the data dictionary
    df = pd.DataFrame(data)
    
    # Append data to the Excel file (if it exists) or create a new file
    file_name = "feedback_data.xlsx"
    try:
        existing_data = pd.read_excel(file_name)
        df = pd.concat([existing_data, df], ignore_index=True)
    except FileNotFoundError:
        pass  # The file doesn't exist yet, so we'll create it with the current data

    # Write the DataFrame to the Excel file
    df.to_excel(file_name, index=False)

root = Tk()
root.geometry('600x600')

label_0 = Label(root, text="FeedBack Form", width=20, font=("bold", 20))
label_0.place(x=300, y=50)

label_1 = Label(root, text="FullName", width=20, font=("bold", 10))
label_1.place(x=80, y=130)
entry_1 = Entry(root)
entry_1.place(x=240, y=130)

label_2 = Label(root, text="Email", width=20, font=("bold", 12))
label_2.place(x=68, y=180)
entry_2 = Entry(root)
entry_2.place(x=240, y=180)

label_3 = Label(root, text="Presentation", width=20, font=("bold", 12))
label_3.place(x=70, y=230)
var = IntVar()
Radiobutton(root, text="Excellent", padx=10, variable=var, value=1).place(x=235, y=230)
Radiobutton(root, text="Good", padx=20, variable=var, value=2).place(x=290, y=230)
Radiobutton(root, text="Average", padx=20, variable=var, value=3).place(x=370, y=230)

label_4 = Label(root, text="Languages", width=20, font=("bold", 12))
label_4.place(x=70, y=280)
list1 = ['Python', 'React JS', 'full stack developer', 'web designing', 'Javascript,CSS and HTML', ' front end developer','postgreSQL']
c = StringVar()
droplist = OptionMenu(root, c, *list1)
droplist.config(width=20)
c.set('Select your Languages')
droplist.place(x=240, y=280)

label_4 = Label(root, text="Do you interested course", width=20 , font=("bold", 10))
label_4.place(x=50, y=330)
var1 = IntVar()
Checkbutton(root, text="Yes", variable=var1).place(x=240, y=330)
var2 = IntVar()
Checkbutton(root, text="No", variable=var2).place(x=290, y=330)

Button(root, text='Submit', width=20, bg='green', fg='white', command=submit_data).place(x=180, y=380)
mainloop()