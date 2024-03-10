import tkinter as tk
from tkinter import messagebox
import pyautogui
import os
import datetime

# Define consistent font styles
FONT_FAMILY = "Arial"
FONT_SIZE = 18
FONT_WEIGHT = "normal"  # Options: "normal", "bold", "italic", "bold italic"

# Define custom colors
BUTTON_BG_COLOR = "#4CAF50"  # Green
BUTTON_FG_COLOR = "white"     # White
BUTTON_FONT_COLOR = "black"   # Black
WINDOW_BG_COLOR = "#F0F0F0"   # Light Gray

def take_screenshot():
    try:
        # Hide the main application window temporarily
        root.withdraw()

        # Taking the screenshot
        my_screenshot = pyautogui.screenshot()

        # Specify the directory where you want to save the screenshot        
        save_directory = ("place your directory location")

        # Generate a timestamp to append to the filename
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Save the screenshot with a unique filename
        file_name = f"screenshot_{timestamp}.png"
        my_screenshot.save(os.path.join(save_directory, file_name))
        messagebox.showinfo("Success", "Screenshot saved successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    finally:
        # Show the main application window again
        root.deiconify()

# Create the main application window
root = tk.Tk()
root.title("Screenshot App")
root.configure(bg=WINDOW_BG_COLOR)  # Set background color of the window

# Set consistent font styles
root.option_add("*Font", (FONT_FAMILY, FONT_SIZE, FONT_WEIGHT))

# Create a label
info_label = tk.Label(root, text="Click the button to capture a screenshot.", bg=WINDOW_BG_COLOR)
info_label.pack(pady=10)

# Create a button to capture the screenshot
capture_button = tk.Button(root, text="Capture Screenshot", command=take_screenshot, 
                           bg=BUTTON_BG_COLOR, fg=BUTTON_FONT_COLOR, font=(FONT_FAMILY, FONT_SIZE, FONT_WEIGHT),
                           activebackground=BUTTON_BG_COLOR, activeforeground=BUTTON_FONT_COLOR)
capture_button.pack(pady=5)

# Run the application
root.mainloop()
