import pyautogui
import keyboard
import pyperclip
import time
import random
import tkinter as tk
from tkinter import ttk


class ClipboardTyperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ClipBot 2055 - Automated Typing from Clipboard")

        self.typing_active = False
        self.typing_speed = 100  # Default typing speed (words per minute)

        # Create GUI elements
        self.create_widgets()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)  # Handle close event

        # Set up keyboard shortcuts (F2 = start, F4 = pause)
        keyboard.add_hotkey('f2', self.start_typing)
        keyboard.add_hotkey('f4', self.pause_typing)

    def create_widgets(self):
        """Create GUI widgets."""
        # Configure dark theme
        self.root.config(bg="#121212")  # Dark background for root window

        # Info label
        self.info_label = tk.Label(self.root, text="Clipboard Typer - Type clipboard content at a human speed.",
                                   bg="#121212", fg="#ffffff", font=("Helvetica", 14, "bold"))
        self.info_label.pack(pady=10)

        # Typing speed label
        self.speed_label = tk.Label(self.root, text="Typing Speed (WPM):", bg="#121212", fg="#ffffff",
                                    font=("Helvetica", 12))
        self.speed_label.pack(pady=5)

        # Typing speed entry
        self.speed_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.speed_entry.insert(0, str(self.typing_speed))  # Set default speed
        self.speed_entry.pack(pady=5)

        # Buttons with modern design
        self.start_button = tk.Button(self.root, text="Start Typing", command=self.start_typing,
                                      font=("Helvetica", 12), bg="#4CAF50", fg="#ffffff", relief="flat", width=15)
        self.start_button.pack(pady=10)
        self.start_button.bind("<Enter>", self.on_enter)
        self.start_button.bind("<Leave>", self.on_leave)

        self.pause_button = tk.Button(self.root, text="Pause Typing", command=self.pause_typing,
                                      font=("Helvetica", 12), bg="#f44336", fg="#ffffff", relief="flat", width=15)
        self.pause_button.pack(pady=5)
        self.pause_button.bind("<Enter>", self.on_enter)
        self.pause_button.bind("<Leave>", self.on_leave)

        self.quit_button = tk.Button(self.root, text="Quit", command=self.quit_program,
                                     font=("Helvetica", 12), bg="#9e9e9e", fg="#ffffff", relief="flat", width=15)
        self.quit_button.pack(pady=10)
        self.quit_button.bind("<Enter>", self.on_enter)
        self.quit_button.bind("<Leave>", self.on_leave)

    def human_typing_speed(self, text):
        """Simulate human-like typing with delays."""
        words_per_minute = self.typing_speed
        chars_per_second = (words_per_minute * 5) / 60  # Approximation of words to characters per second

        for char in text:
            # Check if typing is active; if not, stop typing
            if not self.typing_active:
                print("Typing has been paused.")
                break

            if char == '\n':  # Handle Enter key (newline)
                pyautogui.press('enter')  # Simulate pressing the Enter key
                time.sleep(random.uniform(0.1, 0.3))  # Random delay after pressing Enter
            else:
                pyautogui.write(char)  # Simulate pressing each character
                time.sleep(random.uniform(1 / chars_per_second, 1 / chars_per_second + 0.05))  # Random delay between key presses

    def start_typing(self):
        """Start typing from the clipboard."""
        clipboard_content = pyperclip.paste()  # Get clipboard content
        try:
            self.typing_speed = int(self.speed_entry.get())  # Get typing speed from user input
        except ValueError:
            self.typing_speed = 100  # Default speed if invalid input

        if clipboard_content:
            self.typing_active = True
            self.start_button.config(state="disabled")
            self.pause_button.config(state="normal")
            print("Typing clipboard content...")
            self.human_typing_speed(clipboard_content)  # Simulate typing
        else:
            print("Clipboard is empty!")

    def pause_typing(self):
        """Pause the typing."""
        self.typing_active = False
        self.start_button.config(state="normal")
        self.pause_button.config(state="disabled")
        print("Typing paused.")

    def quit_program(self):
        """Quit the program."""
        self.typing_active = False
        self.root.quit()

    def on_enter(self, event):
        """Hover effect on button - mouse enter."""
        event.widget.config(bg="#81C784")  # Neon green on hover

    def on_leave(self, event):
        """Hover effect on button - mouse leave."""
        if event.widget == self.start_button:
            event.widget.config(bg="#4CAF50")  # Original neon green
        elif event.widget == self.pause_button:
            event.widget.config(bg="#f44336")  # Original red
        elif event.widget == self.quit_button:
            event.widget.config(bg="#9e9e9e")  # Original gray

    def on_close(self):
        """Handle the window close event."""
        self.quit_program()


def main():
    # Create the main window
    root = tk.Tk()
    # Initialize the ClipboardTyperGUI class with the root window
    app = ClipboardTyperGUI(root)
    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
