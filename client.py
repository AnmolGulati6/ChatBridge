import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Client-side configuration
HOST = '127.0.0.1'
PORT = 5000

# Function to receive messages from the server
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                chat_display.config(state=tk.NORMAL)
                chat_display.insert(tk.END, message + "\n")
                chat_display.config(state=tk.DISABLED)
                chat_display.yview(tk.END)
        except:
            print("An error occurred!")
            client.close()
            break

# Function to send messages to the server
def send_message():
    message = f"{nickname}: {message_entry.get()}"
    client.send(message.encode('utf-8'))
    message_entry.delete(0, tk.END)

# Creating the GUI for the chat application
def build_gui():
    global message_entry, chat_display

    window = tk.Tk()
    window.title("Chat App")

    chat_display = scrolledtext.ScrolledText(window, state=tk.DISABLED)
    chat_display.pack(padx=10, pady=10)

    message_entry = tk.Entry(window, width=50)
    message_entry.pack(padx=10, pady=10)

    send_button = tk.Button(window, text="Send", command=send_message)
    send_button.pack(padx=10, pady=10)

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()

def on_closing():
    client.send(f"{nickname} has left the chat.".encode('utf-8'))
    client.close()

# Connecting to the server
nickname = input("Enter your nickname: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Start receiving messages in a background thread
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Start the GUI
build_gui()
