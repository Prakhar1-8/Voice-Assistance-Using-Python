import tkinter as tk
import pyttsx3
import os
import webbrowser
from datetime import datetime   # ✅ FIXED: This import was missing

# Initialize Text-to-Speech
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# AI Response + Commands
def ai_response(user_input):
    user_input = user_input.lower().strip()

    # ---------- SYSTEM COMMANDS ----------
    # Open websites
    if "open google" in user_input:
        webbrowser.open("https://www.google.com")
        return "Opening Google..."

    if "open youtube" in user_input:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube..."

    if "open spotify" in user_input:
        webbrowser.open("https://open.spotify.com")
        return "Opening Spotify..."

    # Open Windows apps
    if "open notepad" in user_input:
        os.system("notepad")
        return "Opening Notepad..."

    if "open calculator" in user_input or "open calc" in user_input:
        os.system("calc")
        return "Opening Calculator..."

    # ---------- NORMAL AI TALK ----------
    if "hello" in user_input:
        return "Hello! How can I help you today?"

    elif "your name" in user_input:
        return "I am your desktop AI assistant."

    elif "time" in user_input:
        return "The time is " + datetime.now().strftime("%I:%M %p")

    elif "date" in user_input:
        return "Today's date is " + datetime.now().strftime("%d %B %Y")

    elif "bye" in user_input:
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I didn't understand that."

# Handle send button
def handle_input():
    user_text = entry.get()

    if user_text.strip() == "":
        return

    chat_window.insert(tk.END, f"You: {user_text}\n", "user")

    response = ai_response(user_text)
    chat_window.insert(tk.END, f"Assistant: {response}\n\n", "bot")

    speak(response)
    entry.delete(0, tk.END)

# Tkinter Window
root = tk.Tk()
root.title("AI Desktop Assistant")
root.geometry("600x650")
root.minsize(500, 550)
root.configure(bg="#bbdefb")  

# Main Frame
main_frame = tk.Frame(root, bg="#ffffff", bd=3, relief="ridge")
main_frame.place(relx=0.5, rely=0.5, anchor="center", width=540, height=580)

main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=0)
main_frame.columnconfigure(0, weight=1)

# Chat Window
chat_frame = tk.Frame(main_frame, bg="#e3f2fd")
chat_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

chat_frame.rowconfigure(0, weight=1)
chat_frame.columnconfigure(0, weight=1)

chat_window = tk.Text(
    chat_frame,
    bg="#e3f2fd",
    fg="black",
    font=("Arial", 12),
    wrap="word",
    relief="flat"
)
chat_window.grid(row=0, column=0, sticky="nsew")

# Scrollbar
scrollbar = tk.Scrollbar(chat_frame, command=chat_window.yview)
scrollbar.grid(row=0, column=1, sticky='ns')
chat_window.config(yscrollcommand=scrollbar.set)

# Chat text styling
chat_window.tag_config("user", foreground="#0d47a1", font=("Arial", 12, "bold"))
chat_window.tag_config("bot", foreground="#1b5e20", font=("Arial", 12))

# Input Area
input_frame = tk.Frame(main_frame, bg="#ffffff")
input_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
input_frame.columnconfigure(0, weight=1)

entry = tk.Entry(
    input_frame,
    font=("Arial", 14),
    bg="#ffffff",
    fg="black",
    relief="groove",
    bd=3
)
entry.grid(row=0, column=0, sticky="ew", padx=(0, 10))

send_button = tk.Button(
    input_frame,
    text="Send",
    command=handle_input,
    bg="#1976d2",
    fg="white",
    activebackground="#1565c0",
    relief="flat",
    width=10
)
send_button.grid(row=0, column=1)

root.mainloop()
