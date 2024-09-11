import tkinter as tk
from tkinter import scrolledtext, messagebox
from Ruanmei import chat_with_ruan_mei
class FacebookChatApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Facebook Chat")
        self.geometry("700x500")

        # Create friend list
        self.friend_list_frame = tk.Frame(self, width=200, bg="lightgray")
        self.friend_list_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.friend_list_label = tk.Label(self.friend_list_frame, text="Chat bot", bg="lightgray")
        self.friend_list_label.pack(pady=10)
        self.friend_list = tk.Listbox(self.friend_list_frame)
        self.friend_list.pack(fill=tk.BOTH, expand=True)

        # Create chat area
        self.chat_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, state='disabled')
        self.chat_area.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create message input field
        self.message_frame = tk.Frame(self)
        self.message_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
        self.message_input = tk.Entry(self.message_frame)
        self.message_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)
        self.send_button = tk.Button(self.message_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

        # Populate friend list (sample data)
        self.friends = ["Ruan Mei"]
        for friend in self.friends:
            self.friend_list.insert(tk.END, friend)

    def send_message(self):
        message = self.message_input.get()
        if message.strip():
            self.display_message("You", message)
            self.message_input.delete(0, tk.END)
            # Simulate response (for demonstration)
            self.after(1000, self.receive_message, "Ruan mei", f"Reply to: {chat_with_ruan_mei(message)}")

    def receive_message(self, sender, message):
        self.display_message(sender, message)

    def display_message(self, sender, message):
        self.chat_area.configure(state='normal')
        self.chat_area.insert(tk.END, f"{sender}: {message}\n")
        self.chat_area.configure(state='disabled')
        self.chat_area.yview(tk.END)

if __name__ == "__main__":
    app = FacebookChatApp()
    app.mainloop()
