import tkinter as tk
import threading
import time


class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Most Dangerous Writing App")

        # Set window size
        self.root.geometry("600x400")

        # Text widget to type in
        self.text_area = tk.Text(self.root, wrap='word', width=70, height=20)
        self.text_area.pack(pady=20)

        # Label for instructions
        self.instruction_label = tk.Label(self.root,
                                          text="Start typing. If you stop for 5 seconds, everything will be erased!",
                                          font=("Arial", 14))
        self.instruction_label.pack()

        # Timer variables
        self.timer = None
        self.last_typing_time = time.time()
        self.time_limit = 5  # Seconds before text is erased

        # Bind typing events
        self.text_area.bind('<KeyPress>', self.on_key_press)

    def on_key_press(self, event):
        # Reset the timer every time the user types
        if self.timer:
            self.timer.cancel()  # Cancel the previous timer if user types again

        # Start a new timer to check if the user has stopped typing for 5 seconds
        self.timer = threading.Timer(self.time_limit, self.erase_text)
        self.timer.start()

        # Update the time of the last keypress
        self.last_typing_time = time.time()

    def erase_text(self):
        # Erase all text in the text area if the user has not typed in the last 5 seconds
        self.text_area.delete(1.0, tk.END)
        self.instruction_label.config(text="You stopped typing! Everything is erased. Try again!")
        self.reset_timer()

    def reset_timer(self):
        # Reset timer and label after erasure
        if self.timer:
            self.timer.cancel()
        self.timer = None
        self.last_typing_time = time.time()


# Initialize the Tkinter window
root = tk.Tk()

# Create the DangerousWritingApp instance
app = DangerousWritingApp(root)

# Start the Tkinter event loop
root.mainloop()
