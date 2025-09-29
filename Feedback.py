import tkinter as tk

# Function to run when Submit button is pressed
def submit_feedback():
    # Get the text entered by the user
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    feedback = feedback_entry.get("1.0", tk.END).strip()  # "1.0" means line 1, character 0

    # Only proceed if there's some feedback
    if feedback:
        print("---- Customer Feedback ----")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Feedback: {feedback}")
        print("---------------------------\n")

        # Clear all fields
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        feedback_entry.delete("1.0", tk.END)

# Create main window
window = tk.Tk()
window.title("Customer Feedback Form")
window.geometry("400x350")

# Title label
title_label = tk.Label(window, text="Please provide feedback on your experience",
                       font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Frame to keep form elements organized
form_frame = tk.Frame(window)
form_frame.pack(pady=5)

# Name field
name_label = tk.Label(form_frame, text="Name:")
name_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
name_entry = tk.Entry(form_frame, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Email field
email_label = tk.Label(form_frame, text="Email:")
email_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
email_entry = tk.Entry(form_frame, width=30)
email_entry.grid(row=1, column=1, padx=5, pady=5)

# Feedback field
feedback_label = tk.Label(form_frame, text="Feedback:")
feedback_label.grid(row=2, column=0, sticky="nw", padx=5, pady=5)
feedback_entry = tk.Text(form_frame, height=6, width=30)
feedback_entry.grid(row=2, column=1, padx=5, pady=5)

# Submit button
submit_button = tk.Button(window, text="Submit", command=submit_feedback)
submit_button.pack(pady=15)

# Run the Tkinter app
window.mainloop()
