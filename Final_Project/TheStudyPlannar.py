import tkinter as tk
from datetime import datetime, timedelta
from tkinter import messagebox
from tkinter import ttk
import tkinter.filedialog as filedialog
from tkinter import *
from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry
import tkinter.font as tkfont
import webbrowser
import matplotlib.pyplot as plt
import csv
import os
import numpy as np
import threading
import time
MAX_SUBJECTS = 10  # Define the maximum number of subjects allowed
MIN_SUBJECTS = 1   # Define the minimum number of subjects allowed
num_subjects = 0   # Initialize the number of subjects to 

# Create a GUI
#, font=("Impact", "24"),fg="royal blue"
# Create the main window
window = tk.Tk()
window.title("Study Planner")
window.geometry('700x700')

# Create a Notebook widget
notebook = ttk.Notebook(window)
notebook.pack(fill=tk.BOTH, expand=True)


# Create multiple frames as pages
page1 = ttk.Frame(notebook)
page2 = ttk.Frame(notebook)
page3 = ttk.Frame(notebook)
page4 = ttk.Frame(notebook)
#page5 = ttk.Frame(notebook)
page6 = ttk.Frame(notebook)
page7 = ttk.Frame(notebook)
page8 = ttk.Frame(notebook)

  
# Define font styles for each page
page1_font = tkfont.Font(family="Impact", size=24, weight="bold")
page2_font = tkfont.Font(family="Merriweather", size=12)


page1_font_color = "Royal blue"
page2_font_color = "black"

# Add the frames to the notebook with corresponding titles
notebook.add(page1, text="Home")
notebook.add(page2, text="Student Details")
notebook.add(page3, text="Questionnaire")
notebook.add(page4, text="Show Plan")
#notebook.add(page5, text="Review/Progress")
notebook.add(page6, text="Add event")
notebook.add(page7, text="Personalized Study Notes")
notebook.add(page8, text="Other")

notebook.tab(page3, state="hidden")
notebook.tab(page4, state="hidden")
#notebook.tab(page5, state="hidden")
notebook.tab(page6, state="hidden")
notebook.tab(page7, state="hidden")
notebook.tab(page8, state="hidden")

# Create a Label widget for the background image
background_image = Label(page2)
background_image.place(x=0, y=0, relwidth=1, relheight=1)
background_image.image = ImageTk.PhotoImage(Image.open("photo.png"))
background_image.configure(image=background_image.image)
# Create a Label widget for the background image
background_image = Label(page3)
background_image.place(x=0, y=0, relwidth=1, relheight=1)
background_image.image = ImageTk.PhotoImage(Image.open("photo.png"))
background_image.configure(image=background_image.image)
# Create a Label widget for the background image
background_image = Label(page4)
background_image.place(x=0, y=0, relwidth=1, relheight=1)
background_image.image = ImageTk.PhotoImage(Image.open("photo.png"))
background_image.configure(image=background_image.image)
# Create a Label widget for the background image
background_image = Label(page6)
background_image.place(x=0, y=0, relwidth=1, relheight=1)
background_image.image = ImageTk.PhotoImage(Image.open("photo.png"))
background_image.configure(image=background_image.image)
# Create a Label widget for the background image
background_image = Label(page7)
background_image.place(x=0, y=0, relwidth=1, relheight=1)
background_image.image = ImageTk.PhotoImage(Image.open("photo.png"))
background_image.configure(image=background_image.image)

background_image = Label(page8)
background_image.place(x=0, y=0, relwidth=1, relheight=1)
background_image.image = ImageTk.PhotoImage(Image.open("photo.png"))
background_image.configure(image=background_image.image)

#Adding contents to each page

#PAGE1-HOME_PAGE
frame =Frame(page1, width=100, height=100)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
home_img = ImageTk.PhotoImage(Image.open("home.webp"))

# Create a Label Widget to display the text or Image
label =tk.Label(frame, image = home_img)

label1=tk.Label(frame, text="Welcome to \nTHE STUDY PLANNER", font=("Impact", "24"),fg="royal blue")
label1.pack()
label.pack()

#Flashing home page
def mainwindow():
   page1.destroy()
   window.geometry("700x700")

page1.after(5000, mainwindow)


#PAGE-2 BASIC STUDENT DETAILS

label1=tk.Label(page2, text="User login", font=("Impact", "18"),fg="Black", bg="#F5F5F5")
label1.pack(padx=15, pady=15)

if not os.path.isfile('credentials.csv'):
    with open('credentials.csv', 'w+', newline=''):
        pass
# Function to handle login button click
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if the credentials exist in the CSV file
    with open('credentials.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == username and row[1] == password:
                #new_label = tk.Label(page2, text="Login Successful",padx=20,pady=20)
                #new_label.pack()
                messagebox.showinfo("Login", "Login Successful")
                notebook.tab(page3, state="normal")
                notebook.tab(page4, state="normal")
                #notebook.tab(page5, state="normal")
                notebook.tab(page6, state="normal")
                notebook.tab(page7, state="normal")
                notebook.tab(page8, state="normal")

                notebook.select(page3)
                return

    messagebox.showerror("Login", "Invalid username or password")
    #new1_label = tk.Label(page2, text="Invalid username or password",padx=20,pady=20)
    #new1_label.pack()


# Function to handle signup button click
def signup():
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username already exists in the CSV file
    with open('credentials.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == username:
                messagebox.showerror("Signup", "Username already exists")
                #new2_label = tk.Label(page2, text="Username already exists",padx=20,pady=20)
                #new2_label.pack()
                return

    # Insert new user into the CSV file
    with open('credentials.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([username, password])

    #messagebox.showinfo("Signup", "Signup Successful")
    new3_label = tk.Label(page2, text="Signup Successful")
    new3_label.pack()

# Create username label and entry
username_label = tk.Label(page2 , text="Username:", font=page2_font,bg="#F5F5F5", fg="black", width=20)
username_label.pack(padx=10, pady=10)
username_entry = tk.Entry(page2, width=30, bg="#F5F5F5")
username_entry.pack(padx=10, pady=10)

# Create password label and entry
password_label = tk.Label(page2, text="Password:", font=page2_font, bg="#F5F5F5",fg="black", width=20)
password_label.pack(padx=10, pady=10)
password_entry = tk.Entry(page2, show="*", width=30, bg="#F5F5F5")
password_entry.pack(padx=10, pady=10)

# Create login and signup buttons
login_button = tk.Button(page2, text="Login", command=login, font=page2_font, width=10, bg="#F5F5F5", fg="black")
login_button.pack(padx=5, pady=5)
signup_button = tk.Button(page2, text="Signup", command=signup, font=page2_font, width=10,bg="#F5F5F5", fg="black" )
signup_button.pack(padx=5, pady=5)



#PAGE-3 Questionnair 


class CustomTooltip:
    """Custom tooltip implementation."""

    def __init__(self, widget, text):
        self.widget = widget
        self.tooltip_text = text
        self.tooltip_window = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip_window = tk.Toplevel(self.widget)
        self.tooltip_window.wm_overrideredirect(True)
        self.tooltip_window.wm_geometry(f"+{x}+{y}")
        label = tk.Label(
            self.tooltip_window,
            text=self.tooltip_text,
            background="#FFFFE0",
            relief="solid",
            borderwidth=1,
        )
        label.pack()

    def hide_tooltip(self, event):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None


# Create subjects.csv file if it doesn't exist
if not os.path.isfile("subjects.csv"):
    with open("subjects.csv", "w+", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Subject", "Complexity Weight", "Marks Weight", "Recommended Study Hours"])

def add_subject_entry():
    global num_subjects

    if num_subjects < MAX_SUBJECTS:
        subject_label = tk.Label(
            page3, text=f"Subject {num_subjects + 1}", font=page2_font, padx=10, pady=5, bg="#F5F5F5", fg="black"
        )
        subject_label.grid(row=num_subjects + 1, column=0)

        subject_entry = tk.Entry(page3, bg="#F5F5F5")
        subject_entry.grid(row=num_subjects + 1, column=1)
        subject_entries.append(subject_entry)  # Add the entry widget to the list

        num_subjects += 1

        
   # subject_label = tk.Label(page3, text=" ",font=page2_font)
    #subject_label.grid(row=num_subjects, column=0, padx=10, pady=5)
    
    subject_entry = tk.Entry(page3, bg="#F5F5F5")
    subject_entry.grid(row=num_subjects, column=1, padx=10, pady=5)
    
    complexity_label = tk.Label(page3, text="Complexity Weight ",font=page2_font, bg="#F5F5F5", fg="black")
    complexity_label.grid(row=num_subjects, column=2, padx=10, pady=5)
    
    complexity_entry = tk.Entry(page3, bg="#F5F5F5")
    complexity_entry.grid(row=num_subjects, column=3, padx=10, pady=5)
    add_tooltip(complexity_entry, "Enter a value between:\n        1 : Very easy\n2 : Easy\n       3 : Average\n      4 : Difficult\n              5 : Very Difficult")

    marks_label = tk.Label(page3, text="Marks Weight ",font=page2_font, bg="#F5F5F5", fg="black")
    marks_label.grid(row=num_subjects, column=4, padx=10, pady=5)
    
    marks_entry = tk.Entry(page3, bg="#F5F5F5")
    marks_entry.grid(row=num_subjects, column=5, padx=10, pady=5)
    add_tooltip(marks_entry, "Enter a marks range value:\n 1 : 32-40\n 2 : 26-32\n 3 : 19-26\n 4 : 11-18\n 5 : 00-17")


    subject_labels.append(subject_label)
    subject_entries.append(subject_entry)
    complexity_labels.append(complexity_label)
    complexity_entries.append(complexity_entry)
    marks_labels.append(marks_label)
    marks_entries.append(marks_entry)



def add_tooltip(widget, tooltip_text):
    """Adds a tooltip to the given widget."""
    tooltip = CustomTooltip(widget, tooltip_text)


def remove_subject_entry():
    global num_subjects

    if num_subjects > MIN_SUBJECTS:
        subject_labels[-1].destroy()
        subject_entries[-1].destroy()
        complexity_labels[-1].destroy()
        complexity_entries[-1].destroy()
        marks_labels[-1].destroy()
        marks_entries[-1].destroy()

        subject_labels.pop()
        subject_entries.pop()
        complexity_labels.pop()
        complexity_entries.pop()
        marks_labels.pop()
        marks_entries.pop()

        num_subjects -= 1

def calculate_study_hours(subjects, complexity_weights, marks_weights, total_study_hours):
    # Step 1: Calculate complexity and marks weights totals
    total_complexity_weight = sum(complexity_weights)
    total_marks_weight = sum(marks_weights)

    # Step 2: Calculate study hours for each subject
    study_hours = []
    for i in range(len(subjects)):
        subject_complexity = complexity_weights[i]
        subject_marks = marks_weights[i]

        # Step 4: Calculate study hours for the subject
        recommended_hours = (
            subject_complexity / total_complexity_weight
        ) * total_study_hours * (subject_marks / total_marks_weight)

        study_hours.append(recommended_hours)

    # Step 3: Check and adjust the sum of study hours
    calculated_total_hours = sum(study_hours)
    adjustment_factor = total_study_hours / calculated_total_hours

    # Step 5a: Proportional adjustment
    study_hours = [hours * adjustment_factor for hours in study_hours]

    # Step 6: Recalculate the sum of study hours and check
    recalculated_total_hours = sum(study_hours)

    # Step 7: Repeat adjustment until the sum matches the total study hours
    while recalculated_total_hours != total_study_hours:
        if recalculated_total_hours < total_study_hours:
            # Adjust study hours for subjects with higher complexity or marks weight
            max_index = study_hours.index(max(study_hours))
            study_hours[max_index] += 1
        else:
            # Adjust study hours for subjects with lower complexity or marks weight
            min_index = study_hours.index(min(study_hours))
            study_hours[min_index] -= 1

        recalculated_total_hours = sum(study_hours)

    return study_hours


def clear_frame(frame):
    """Clears all widgets from the frame."""
    for widget in frame.winfo_children():
        widget.destroy()

def submit():

    background_image = Label(page4)
    background_image.place(x=0, y=0, relwidth=1, relheight=1)
    background_image.image = ImageTk.PhotoImage(Image.open("photo.png"))
    background_image.configure(image=background_image.image)
    # Clear the result frame
    #clear_frame(page4)

    # Retrieve the input values
    subjects = []
    complexity_weights = []
    marks_weights = []

    for i in range(num_subjects):
        subject = subject_entries[i].get()
        complexity_weight = int(complexity_entries[i].get())
        marks_weight = int(marks_entries[i].get())

        subjects.append(subject)
        complexity_weights.append(complexity_weight)
        marks_weights.append(marks_weight)

    total_study_hours = int(total_study_hours_entry.get())  # Get the total study hours

    # Calculate study hours
    recommended_study_hours = calculate_study_hours(
        subjects, complexity_weights, marks_weights, total_study_hours
    )

    # Display the results
    subject_label = tk.Label(
        page4, text="Subject", font=page2_font, bg="#F5F5F5", fg="black", width="12"
    )
    subject_label.grid(row=0, column=0, padx=10, pady=5)
    hours_label = tk.Label(
        page4, text="Recommended Study Hours", font=page2_font, bg="#F5F5F5", fg="black"
    )
    hours_label.grid(row=0, column=1, padx=10, pady=5)
    progress_label = tk.Label(
        page4, text="Actual Study Hours", font=page2_font, bg="#F5F5F5", fg="black"
    )
    progress_label.grid(row=0, column=2, padx=10, pady=5)

    progress1_label = tk.Label(
    page4, text="Progress %", font=page2_font, bg="#F5F5F5", fg="black"
    )
    progress1_label.grid(row=0, column=3, padx=10, pady=5)

    actual_hours_entries = []
    progress_labels = []  # List to store the progress labels

    for i in range(len(subjects)):
        subject_label = tk.Label(
            page4, text=f"Subject {i+1}", font=page2_font, padx=15, pady=15, bg="#F5F5F5", fg="black"
        )
        subject_label.grid(row=i + 1, column=0, padx=10, pady=5)

        recommended_hours_label = tk.Label(
            page4, text=recommended_study_hours[i], font=page2_font, padx=15, pady=15, bg="#F5F5F5", fg="black"
        )
        recommended_hours_label.grid(row=i + 1, column=1, padx=10, pady=5)

        actual_hours_entry = tk.Entry(page4)
        actual_hours_entry.grid(row=i + 1, column=2, padx=10, pady=5)
        actual_hours_entries.append(actual_hours_entry)

        progress_label = tk.Label(
            page4, text="", font=page2_font, padx=5, pady=5, bg="#F5F5F5", fg="black", width=10,
        )
        progress_label.grid(row=i + 1, column=3)
        progress_labels.append(progress_label)

       #background_image = Label(page4)
       #background_image.place(x=0, y=0, relwidth=1, relheight=1)
       #background_image.image = ImageTk.PhotoImage(Image.open("photo.png"))
       #background_image.configure(image=background_image.image)
        
        
        

    def show_progress():
        # Update the progress labels based on the entered actual hours
        for i in range(len(subjects)):
            try:
                recommended_hours = recommended_study_hours[i]
                actual_hours = int(actual_hours_entries[i].get())
                progress = (actual_hours / recommended_hours) * 100
                progress_labels[i].config(text=f"{progress:.2f}%")
            except ValueError:
                pass
        # Calculate progress for the last row
        try:
            recommended_hours = recommended_study_hours[-1]
            actual_hours = int(actual_hours_entries[-1].get())
            progress = (actual_hours / recommended_hours) * 100
            progress_labels[-1].config(text=f"{progress:.2f}%")
        except ValueError:
            pass
            
    show_progress_button = tk.Button(
        page4,
        text="Show Progress",
        font=page2_font,
        padx=5,
        pady=10,
        width=18,
        command=show_progress,
        bg="#F5F5F5",
    )
    show_progress_button.grid(row=len(subjects) + 1, column=1, columnspan=2)

    # Update the result frame
    page4.update_idletasks()
    
    
    
    

def close_window():
    window.destroy()
def show_page(page_index):
    notebook.select(page_index)
   
def new():
    show_page(2)
    #calculate_study_hours()
    submit()

# Add subject input fields
num_subjects = 0
subject_labels = []
subject_entries = []
complexity_labels = []
complexity_entries = []
marks_labels = []
marks_entries = []
hours_labels = []
hours_entries = []

add_subject_entry()

# Add total study hours entry field
total_study_hours_label = tk.Label(
    page3, text="Total Study Hours", font=page2_font,fg="black",bg="#F5F5F5"
)
total_study_hours_label.grid(row=0, column=0, padx=10, pady=5)

total_study_hours_entry = tk.Entry(page3,bg="#F5F5F5")
total_study_hours_entry.grid(row=0, column=1, padx=10, pady=5)

# Add buttons for adding/removing subjects
add_subject_button = tk.Button(page3, text="Add Subject", command=add_subject_entry , width=18, bg="#F5F5F5", fg="black" , font=page2_font)
add_subject_button.grid(row=0, column=2, padx=10, pady=5, sticky="e")

remove_subject_button = tk.Button(
    page3,
    text="Remove Subject",
    font=page2_font,
    command=remove_subject_entry,
     width=18, bg="#F5F5F5", fg="black"
     
)
remove_subject_button.grid(row=0, column=3, padx=10, pady=5, sticky="e")

# Add submit button
submit_button = tk.Button(page3, text="Submit", command=new, width=18, bg="#F5F5F5", fg="black", font=page2_font)
submit_button.grid(row=0, column=4, padx=10, pady=5, sticky="e")

#PAGE-5 PROGRESS


#PAGE-6 ADD EVENT

label1=tk.Label(page6, text="Add important events and reminders here", font=("Impact", "18"),fg="Black", bg="#F5F5F5")
label1.pack(padx=15, pady=15)
reminders = []

def set_reminder():
    selected_date = calendar.get_date()
    reminder_time = time_entry.get()
    event_name = event_entry.get()

    try:
        reminder_datetime = datetime.combine(selected_date, datetime.strptime(reminder_time, "%H:%M").time())
        current_datetime = datetime.now()

        if reminder_datetime < current_datetime:
            messagebox.showwarning("Invalid Date/Time", "Please enter a future date/time.")
        else:
            reminder = {
                "event_name": event_name,
                "selected_date": selected_date,
                "reminder_time": reminder_time
            }
            reminders.append(reminder)

            time_difference = reminder_datetime - current_datetime
            seconds_difference = time_difference.total_seconds()
            page6.after(int(seconds_difference * 1000), lambda: show_reminder(event_name, selected_date))
            event_listbox.insert(tk.END, f"{event_name} - {selected_date.strftime('%Y-%m-%d')}")

            messagebox.showinfo("Reminder Set", "Reminder has been set successfully.")
    except ValueError:
        messagebox.showwarning("Invalid Format", "Please enter a valid date and time.")

def show_reminder(event_name, selected_date):
    messagebox.showinfo("Reminder", f"{event_name} - {selected_date.strftime('%Y-%m-%d')}")

def add_reminder():
    event_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    calendar.delete(0, tk.END)

def clear_reminders():
    reminders.clear()
    event_listbox.delete(0, tk.END)

event_label = tk.Label(page6, text="Event Name:", bg="#F5F5F5", fg="black", font=page2_font, width=20)
event_label.pack(padx=10,pady=10)

event_entry = tk.Entry(page6, width=30, bg="#F5F5F5")
event_entry.pack(padx=10,pady=10)

date_label = tk.Label(page6, text="Reminder Date:", bg="#F5F5F5", fg="black", font=page2_font, width=20)
date_label.pack(padx=10,pady=10)

calendar = DateEntry(page6, width=12, background='darkblue', foreground='white', borderwidth=2)
calendar.pack(padx=10,pady=10)

time_label = tk.Label(page6, text="Reminder Time (HH:MM):", bg="#F5F5F5", fg="black", font=page2_font, width=20)
time_label.pack(padx=10,pady=10)

time_entry = tk.Entry(page6, width=30, bg="#F5F5F5")
time_entry.pack(padx=10,pady=10)

button_frame = tk.Frame(page6)
button_frame.pack(padx=10,pady=10)

set_button = tk.Button(button_frame, text="Set Reminder", command=set_reminder, bg="#F5F5F5", fg="black", font=page2_font, width=18)
set_button.pack(side=tk.LEFT,padx=10,pady=10)

add_button = tk.Button(button_frame, text="Add Reminder", command=add_reminder, bg="#F5F5F5", fg="black", font=page2_font, width=18)
add_button.pack(side=tk.LEFT,padx=10,pady=10)

clear_button = tk.Button(button_frame, text="Clear Reminders", command=clear_reminders, bg="#F5F5F5", fg="black", font=page2_font, width=18)
clear_button.pack(side=tk.LEFT,padx=10,pady=10)

event_listbox = tk.Listbox(page6, width=80, height=20, bg="#F5F5F5")
event_listbox.pack(padx=10,pady=10)



#PAGE-7 PERSONALIZED STUDY NOTES

label1=tk.Label(page7, text="Make your personalized notes here:", font=("Impact", "18"),fg="Black", bg="#F5F5F5")
label1.pack(padx=15, pady=15)

def create_subject_folder():
    if not os.path.exists("subjects"):
        os.mkdir("subjects")


def create_notes(subject):
    notes_file = f"subjects/{subject}.txt"
    if not os.path.exists(notes_file):
        with open(notes_file, "w"):
            pass


def open_notes(subject):
    create_notes(subject)
    display_notes_frame(subject)


def save_notes(subject, notes_text):
    notes = notes_text.get("1.0", "end-1c")
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialdir="subjects/",
                                             initialfile=f"{subject}.txt", title="Save Notes")
    if file_path:
        with open(file_path, "w") as file:
            file.write(notes)
        messagebox.showinfo("Notes Saved", "Notes have been saved successfully.")


def display_notes_frame(subject):
    notes_window = Toplevel(page7)
    notes_window.title("Notes")
    
    notes_label = Label(notes_window, text="Notes:")
    notes_label.pack()

    notes_text = Text(notes_window, height=10, width=50)
    notes_text.pack()

    save_button = Button(notes_window, text="Save Notes", width=10, command=lambda: save_notes(subject, notes_text), bg="#F5F5F5", fg="black", font=page2_font)
    save_button.pack()

    # Retrieve and display existing notes if available
    notes_file = f"subjects/{subject}.txt"
    if os.path.isfile(notes_file):
        with open(notes_file, "r") as file:
            existing_notes = file.read()
            notes_text.insert("end", existing_notes)
    
    notes_window.mainloop()


def add_subject():
    subject = subject_entry.get()
    if subject:
        subject_button = Button(subject_buttons_frame, text=subject, width=12,font=page2_font,bg="#F5F5F5",
                                command=lambda subject=subject: open_notes(subject))
        subject_button.pack(side="left",padx=10, pady=10)
        subjects.append(subject)
        subject_entry.delete(0, "end",bg="#F5F5F5")


def main():
    global root, subject_buttons_frame, subject_entry, subjects
    
    create_subject_folder()

    subjects_label = Label(page7, text="Subjects:", bg="#F5F5F5", fg="black", font=page2_font)
    subjects_label.pack(padx=10, pady=10)

    subject_buttons_frame = Frame(page7)
    subject_buttons_frame.pack()

    subjects = []  # Empty list for subjects

    subject_entry_frame = Frame(page7,bg="#F5F5F5")
    subject_entry_frame.pack()

    subject_label = Label(subject_entry_frame, text="Enter Subject:", bg="#F5F5F5", fg="black", font=page2_font, width=15)
    subject_label.pack(side="left",padx=10, pady=10)

    subject_entry = Entry(subject_entry_frame,bg="#F5F5F5")
    subject_entry.pack(side="left",padx=10, pady=10)

    add_subject_button = Button(subject_entry_frame, text="Add Subject", command=add_subject, bg="#F5F5F5", fg="black", font=page2_font, width=15)
    add_subject_button.pack(side="left",padx=10, pady=10)


if __name__ == "__main__":
    main()


#PAGE-8 Others

label1=tk.Label(page8, text="A students guide to MANAGE STRESS", font=("Impact", "18"),fg="Black", bg="#F5F5F5")
label1.pack()
# Create a frame for the top pictures
top_frame = Frame(page8)
top_frame.pack()

# Create a frame for the bottom pictures
bottom_frame = Frame(page8)
bottom_frame.pack()

# Open and resize the images
image1 = Image.open("other_1.jpg")
image1 = image1.resize((300, 300))  # Adjust the desired width and height

image2 = Image.open("other_2.jpg")
image2 = image2.resize((300, 300))  # Adjust the desired width and height

image3 = Image.open("OTHER_33.jpg")
image3 = image3.resize((300, 300))  # Adjust the desired width and height

image4 = Image.open("other_4.jpg")
image4 = image4.resize((300, 300))  # Adjust the desired width and height


# Create ImageTk objects for the resized images
image1_tk = ImageTk.PhotoImage(image1)
image2_tk = ImageTk.PhotoImage(image2)
image3_tk = ImageTk.PhotoImage(image3)
image4_tk = ImageTk.PhotoImage(image4)

# Create Label widgets for the top pictures
label1 = Label(top_frame, image=image1_tk)
label2 = Label(top_frame, image=image2_tk)

# Create Label widgets for the bottom pictures
label3 = Label(bottom_frame, image=image3_tk)
label4 = Label(bottom_frame, image=image4_tk)

# Grid placement for the top Label widgets
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)

# Grid placement for the bottom Label widgets
label3.grid(row=0, column=0)
label4.grid(row=0, column=1)


# Create Label widgets for the text below images
text1 = Label(top_frame, text="Exercise Regularly", font=page2_font)
text2 = Label(top_frame, text="Have a proper 8 hour sleep cycle",font=page2_font)
text3 = Label(bottom_frame, text="Have healthy meals at \n regular intervals",font=page2_font)
text4 = Label(bottom_frame, text="Take breaks and keep your \n Mental health on check",font=page2_font)

# Grid placement for the top Label widgets
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)

# Grid placement for the bottom Label widgets
label3.grid(row=0, column=0)
label4.grid(row=0, column=1)

# Grid placement for the text Label widgets
text1.grid(row=1, column=0, pady=10)
text2.grid(row=1, column=1, pady=10)
text3.grid(row=1, column=0, pady=10)
text4.grid(row=1, column=1, pady=10)

# Create a Label widget for the initial text
initial_text = tk.Label(page8, text="Know stress managment texhniques:", font=page2_font)
initial_text.pack(padx=10, pady=30)

# Create a function to handle the hyperlink click
def open_hyperlink():
    webbrowser.open("https://www.student.com/articles/the-best-stress-relief-methods-for-studying")

# Create a Label widget for the hyperlink
hyperlink_text = tk.Label(page8, text="Click here to know a few quick stress managment techniques during exams", fg="blue", cursor="hand2", font=page2_font)
hyperlink_text.pack()

# Bind the hyperlink to the function
hyperlink_text.bind("<Button-1>", lambda e: open_hyperlink())

# Set the Label widget to appear at the bottom center
hyperlink_text.place(relx=0.5, rely=1, anchor=tk.S)

# Run the main loop

window.title("Study Hour Calculator")
window.protocol("WM_DELETE_WINDOW", close_window)
window.mainloop()
