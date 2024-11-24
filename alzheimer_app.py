import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from login_view_model import LoginViewModel
from genetic_data import GeneticData
from lifestyle_data import LifestyleData
from cognitive_test import CognitiveTest

# alzheimer_app.py
class AlzheimerApp:
    def __init__(self, root):
        """
        Initializes the alzheimer_app instance.
        Args:
            root: The main Tkinter window.
        """

        self.root = root
        self.root.title("Alzheimer's Disease Testing Software")
        self.login_view_model = LoginViewModel()  # Initialize the LoginViewModel
        self.show_login()

        # Initialize data objects
        self.genetic_data = GeneticData()
        self.lifestyle_data = LifestyleData()
        self.cognitive_test = CognitiveTest()

    def show_login(self):
        """Displays the login interface for the user."""
        self.clear_frame()
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(pady=60)
        
        tk.Label(self.login_frame, text="Username").grid(row=0, column=0, padx=20, pady=5)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1, padx=20, pady=5)
        
        tk.Label(self.login_frame, text="Password").grid(row=1, column=0, padx=20, pady=5)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=20, pady=5)
        
        tk.Button(self.login_frame, text="Login", command=self.login).grid(row=2, columnspan=2, pady=10)

    def login(self):
        """Handles user login."""
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if self.login_view_model.login_user(username, password):
            self.show_dashboard()
        else:
            messagebox.showerror("Login Error", "Invalid username or password")
            
    def show_dashboard(self):
        """Displays the dashboard after successful login."""
        self.clear_frame()
        self.dashboard_frame = tk.Frame(self.root)
        self.dashboard_frame.pack(pady=20)
        
        profile_img = Image.open("profile_pic.png")
        profile_img = profile_img.resize((100, 100), Image.ANTIALIAS)
        profile_img = ImageTk.PhotoImage(profile_img)
        tk.Label(self.dashboard_frame, image=profile_img).grid(row=0, columnspan=2)
        tk.Label(self.dashboard_frame, text="Welcome, Josh!").grid(row=1, columnspan=2, pady=10)
        
        self.profile_img = profile_img  # Keep reference to avoid garbage collection

        self.nav_frame = tk.Frame(self.dashboard_frame)
        self.nav_frame.grid(row=2, columnspan=2, pady=10)

        tk.Button(self.nav_frame, text="Cognitive Tests", command=self.show_cognitive_tests).grid(row=0, column=0, padx=10)
        tk.Button(self.nav_frame, text="Lifestyle Data", command=self.show_lifestyle_data).grid(row=0, column=1, padx=10)
        tk.Button(self.nav_frame, text="Genetic Data", command=self.show_genetic_data).grid(row=0, column=2, padx=10)
        tk.Button(self.nav_frame, text="View Results", command=self.show_view_results).grid(row=0, column=3, padx=10)
        tk.Button(self.nav_frame, text="Logout", command=self.logout).grid(row=0, column=4, padx=10)  # Logout button

    def logout(self):
        """Logs out the user and returns to the login screen."""
        self.clear_frame()
        self.show_login()  # Show the login screen again

    def show_cognitive_tests(self):
        """Displays the cognitive tests interface and shows the score."""
        self.clear_frame()
        self.cognitive_test.administer_test()  # Simulate administering the test
        tk.Label(self.root, text="Cognitive Test Score: {}".format(self.cognitive_test.score)).pack(pady=20)
        tk.Button(self.root, text="Back to Dashboard", command=self.show_dashboard).pack(pady=10)

    def show_lifestyle_data(self):
        """Displays the lifestyle data collected from the user."""
        self.clear_frame()
        self.lifestyle_data.collect_data()  # Simulate data collection
        tk.Label(self.root, text="Lifestyle Data:").pack(pady=20)
        tk.Label(self.root, text=f"Diet: {self.lifestyle_data.diet_info}, Exercise: {self.lifestyle_data.exercise_info}, Sleep: {self.lifestyle_data.sleep_info}").pack(pady=10)
        tk.Button(self.root, text="Back to Dashboard", command=self.show_dashboard).pack(pady=10)

    def show_genetic_data(self):
        """Displays the genetic data collected from the user."""
        self.clear_frame()
        self.genetic_data.collect_data()  # Simulate data collection
        tk.Label(self.root, text="Genetic Markers: {}".format(self.genetic_data.genetic_markers)).pack(pady=20)
        tk.Button(self.root, text="Back to Dashboard", command=self.show_dashboard).pack(pady=10)

    def show_view_results(self):
        """Displays the results page with options to view submitted data."""
        self.clear_frame()
        tk.Label(self.root, text="Results Page").pack(pady=20)
        tk.Button(self.root, text="Lifestyle Data Submitted", command=lambda: self.show_result_message("Lifestyle data is submitted")).pack(pady=5)
        tk.Button(self.root, text="Cognitive Data Submitted", command=lambda: self.show_result_message("Cognitive data is submitted")).pack(pady=5)
        tk.Button(self.root, text="Genetic Data Submitted", command=lambda: self.show_result_message("Genetic data is submitted")).pack(pady=5)
        tk.Button(self.root, text="Back to Dashboard", command=self.show_dashboard).pack(pady=10)

    def show_result_message(self, message):
        """Displays a message box with the result message."""
        messagebox.showinfo("Result", message)

    def clear_frame(self):
        """Clears the current frame."""
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AlzheimerApp(root)
    root.mainloop()
