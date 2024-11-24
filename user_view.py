
import tkinter as tk
from tkinter import messagebox
from user_view_model import UserViewModel

# user_view.py
class UserView:
     """Handles the user interface for user interactions."""
     def __init__(self, view_model):
         """
        Initializes the user_view instance.
        Args:
            view_model: The view model that handles user logic.
        """

         self.view_model = view_model
         self.root = tk.Tk()
         self.root.title("Alzheimer's Disease Testing Software")

         self.frame = tk.Frame(self.root)
         self.frame.pack(pady=20)

        # User Registration
         tk.Label(self.frame, text="Name").grid(row=0, column=0, padx=10, pady=5)
         self.name_entry = tk.Entry(self.frame)
         self.name_entry.grid(row=0, column=1, padx=10, pady=5)

         tk.Label(self.frame, text="Date of Birth").grid(row=1, column=0, padx=10, pady=5)
         self.dob_entry = tk.Entry(self.frame)
         self.dob_entry.grid(row=1, column=1, padx=10, pady=5)

         tk.Label(self.frame, text="Gender").grid(row=2, column=0, padx=10, pady=5)
         self.gender_entry = tk.Entry(self.frame)
         self.gender_entry.grid(row=2, column=1, padx=10, pady=5)

         tk.Label(self.frame, text="Contact Info").grid(row=3, column=0, padx=10, pady=5)
         self.contact_entry = tk.Entry(self.frame)
         self.contact_entry.grid(row=3, column=1, padx=10, pady=5)

         tk.Button(self.frame, text="Register", command=self.register_user).grid(row=4, columnspan=2, pady=10)

        # Cognitive Test
         tk.Label(self.frame, text="Cognitive Test Type").grid(row=5, column=0, padx=10, pady=5)
         self.test_type_entry = tk.Entry(self.frame)
         self.test_type_entry.grid(row=5, column=1, padx=10, pady=5)

         tk.Label(self.frame, text="Date Taken").grid(row=6, column=0, padx=10, pady=5)
         self.date_taken_entry = tk.Entry(self.frame)
         self.date_taken_entry.grid(row=6, column=1, padx=10, pady=5)

         tk.Button(self.frame, text="Submit Cognitive Test", command=self.submit_cognitive_test).grid(row=7, columnspan=2, pady=10)

        # Additional UI elements for genetic and lifestyle data...

     def register_user(self):
         """Handles user registration."""
         name = self.name_entry.get()
         dob = self.dob_entry.get()
         gender = self.gender_entry.get()
         contact = self.contact_entry.get()
         self.view_model.register_user(name, dob, gender, contact)
         messagebox.showinfo("Registration", "User registered successfully!")

     def submit_cognitive_test(self):
        """Handles the submission of cognitive test data."""
        test_type = self.test_type_entry.get()
        date_taken = self.date_taken_entry.get()
        self.view_model.submit_cognitive_test(test_type, date_taken)
        messagebox.showinfo("Cognitive Test", "Cognitive test submitted successfully!")

     def start(self):
         """Starts the Tkinter main loop."""
         self.root.mainloop()