import tkinter as tk
from tkinter import ttk
from buttons_functions import Buttons_adjust as adjust
# 创建主窗口
def message_window_start():
    root = tk.Tk()
    root.title("message_window")
    root.geometry("400x200")

    label = ttk.Label(root, text="input what you need",font=("Arial", 14, "bold"))
    label.pack(pady=10)
    
    entry = ttk.Entry(root, width=40)
    entry.pack(pady=10)
    def on_confirm():
        value = entry.get()
        adjust(value)
        root.destroy()

    style = ttk.Style()
    style.configure("TButton", background="#4CAF50", foreground="black")
    confirm_button = ttk.Button(root, text="confirm", style="TButton",command=on_confirm)
    confirm_button.pack(pady=20)
    
    root.mainloop()


