import tkinter as tk
from random import sample

class BingoCallerSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Bingo Caller System Ver.1")
        
        self.numbers = list(range(1, 76))  # 1-75
        self.called_numbers = []  # Store called numbers
        
        # Create and place label for current number
        self.current_label = tk.Label(root, text="Press 'Call Number' to start", font=("Helvetica", 24))
        self.current_label.pack(pady=20)
        
        # Create and place call number button
        self.call_button = tk.Button(root, text="Call Number", font=("Helvetica", 18), command=self.call_number)
        self.call_button.pack(pady=10)
        
        # Create and place listbox for history
        self.history_listbox = tk.Listbox(root, font=("Helvetica", 16), height=15, width=15)
        self.history_listbox.pack(pady=20)
        
    def call_number(self):
        if self.numbers:
            # Randomly select a number and remove it from the list of available numbers
            number = sample(self.numbers, 1)[0]
            self.numbers.remove(number)
            self.called_numbers.append(number)
            
            # Update the label and history listbox
            self.current_label.config(text=f"Current Number: {number}")
            self.history_listbox.insert(tk.END, number)
        else:
            self.current_label.config(text="All numbers have been called!")

# Create the root window
root = tk.Tk()
bingo_system = BingoCallerSystem(root)
root.mainloop()
