import tkinter as tk

# Function to run when button is clicked
def on_button_click():
    user_input = entry.get()  # Get text from the textbox
    output_label.config(text=f"You typed: {user_input}")  # Show output

# Create main window
window = tk.Tk()
window.title("My First Tkinter App")
window.geometry("300x200")  # Set window size (width x height)

# Text box (Entry widget)
entry = tk.Entry(window, width=25)
entry.pack(pady=10)  # Adds padding for spacing

# Button
button = tk.Button(window, text="Submit", command=on_button_click)
button.pack(pady=5)

# Output label
output_label = tk.Label(window, text="Your output will appear here", fg="blue")
output_label.pack(pady=10)

# Run the application
window.mainloop()
