import tkinter as tk
from tkinter import messagebox
import time

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("600x400")
        
        # Sample text for typing
        self.sample_text = "The quick brown fox jumps over the lazy dog."
        
        # Initialize variables
        self.start_time = None
        self.word_count = 0
        self.is_test_running = False
        
        # GUI Components
        self.create_widgets()
    
    def create_widgets(self):
        # Instructions Label
        self.instructions_label = tk.Label(self.root, text="Type the following text as fast as you can:", font=("Arial", 14))
        self.instructions_label.pack(pady=10)
        
        # Sample text label
        self.sample_text_label = tk.Label(self.root, text=self.sample_text, font=("Arial", 12), wraplength=500)
        self.sample_text_label.pack(pady=10)
        
        # User input field
        self.text_entry = tk.Entry(self.root, font=("Arial", 12), width=50)
        self.text_entry.pack(pady=10)
        
        # Timer label
        self.timer_label = tk.Label(self.root, text="Time: 0s", font=("Arial", 12))
        self.timer_label.pack(pady=10)
        
        # Start/Reset Button
        self.start_button = tk.Button(self.root, text="Start Test", command=self.start_test, font=("Arial", 12))
        self.start_button.pack(pady=10)
        
        # Result Label
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.pack(pady=20)
    
    def start_test(self):
        if not self.is_test_running:
            # Start new test
            self.start_button.config(text="Finish Test")
            self.text_entry.delete(0, tk.END)  # Clear the entry field
            self.text_entry.focus()  # Focus the entry field for typing
            self.start_time = time.time()  # Start timer
            self.is_test_running = True
            self.word_count = 0
            self.update_timer()
        else:
            # Test finished
            elapsed_time = time.time() - self.start_time
            typed_text = self.text_entry.get().strip()
            self.word_count = len(typed_text.split())  # Count words
            wpm = self.calculate_wpm(elapsed_time)
            self.display_result(wpm)
    
    def update_timer(self):
        if self.is_test_running:
            elapsed_time = time.time() - self.start_time
            seconds = int(elapsed_time)
            self.timer_label.config(text=f"Time: {seconds}s")
            self.root.after(1000, self.update_timer)  # Update the timer every second
    
    def calculate_wpm(self, elapsed_time):
        # Calculate words per minute
        minutes = elapsed_time / 60
        wpm = self.word_count / minutes
        return round(wpm, 2)
    
    def display_result(self, wpm):
        # Show the typing speed result
        self.result_label.config(text=f"Your Typing Speed: {wpm} WPM")
        self.start_button.config(text="Restart Test")
        self.is_test_running = False
        messagebox.showinfo("Typing Speed Test", f"Your typing speed is {wpm} words per minute!")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()
