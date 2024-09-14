import tkinter as tk
import pandas as pd
from tkinter import messagebox

df = pd.read_csv('Student-info.csv')
def mark_attendance():
    global df
    name = entry_name.get().strip()
    roll = entry_roll.get().strip()
    if name in df['Name'].values:
        df.loc[df['Name']==name,'Attendance']='Present'
        messagebox.showinfo("Attendance",f"{name} marked Present")
    else:
        messagebox.showwarning("Not Register",f"{name} not found!Please Register.")
        roll = entry_roll.get()
        if roll:
            new_student = pd.DataFrame({'Name':[name],'Roll':[roll],'Attendance':['Present']})
            df = pd.concat([df,new_student],ignore_index=True)

        df.to_csv('Student-info.csv',index=False)

# Main window
root = tk.Tk()
root.title("Student Attendance")
root.geometry("400x300")

# Entries from student
label_name = tk.Label(root,text="Enter your Name: ")
label_name.pack(pady=10)
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

label_roll = tk.Label(root,text="Enter your Roll: ")
label_roll.pack(pady=10)
entry_roll = tk.Entry(root)
entry_roll.pack(pady=5)



# button for submiit
btn_attendance = tk.Button(root,text = "Submit",command = mark_attendance)
btn_attendance.pack(pady=20)

root.mainloop()
