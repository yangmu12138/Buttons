import tkinter as tk
from tkinter import messagebox
from check_and_save import write_warnings

class WarningSettings:
    def __init__(self, root):
        self.root = root
        self.root.title("warning_settings")
        self.root.geometry("600x500+970+240")
        self.root.configure(bg="#f0f0f0")
        self.warning_content=[]
        self.create_widgets()
        self.warning_save=write_warnings

        
    def create_widgets(self):
        # 大按钮
        self.big_button_canvas = tk.Canvas(
            self.root,
            width=140,
            height=140,
            bg="#f0f0f0",
            highlightthickness=0
        )
        self.big_button_canvas.pack(pady=10)
        
        # 绘制大圆形按钮
        self.big_button = self.big_button_canvas.create_oval(
            36, 33, 120, 120,
            fill="#E91E63",
            outline="#388E3C",
            width=2,
            activefill="#66BB6A",
            activeoutline="#43A047"
        )
        
        # 大按钮文字
        self.big_button_canvas.create_text(
            80, 80,
            text="+",
            fill="black",
            font=("Arial", 66, "bold")
        )
        
        # 绑定大按钮点击事件
        self.big_button_canvas.tag_bind(self.big_button, "<Button-1>",lambda e:self.create_new_window)
        self.big_button_canvas.bind("<Button-1>",lambda e:self.create_new_window())

         
        frame_1 = tk.Frame(self.root, bg="#f0f0f0")
        frame_1.pack(pady=10, fill=tk.X, padx=150)   # 标签
        label_1 = tk.Label(
            frame_1,
            text="Add more attentions",
            font=("Arial", 22, "bold"),
            bg="#f0f0f0",
            fg="#555",
            width=20,
            anchor="w"
            )
        label_1.pack(side=tk.LEFT, padx=10)
        
    
    def create_new_window(self):
        # 创建新窗口
        new_window = tk.Toplevel(self.root)
        new_window.title("Add more attentions")
        new_window.geometry("400x200+1000+300")
        new_window.configure(bg="#f0f0f0")
        
        # 创建标签
        label = tk.Label(
            new_window,
            text="write your attentions:",
            font=("Arial", 14),
            bg="#f0f0f0",
            fg="#333"
        )
        label.pack(pady=20)
        
        # 创建输入框
        entry = tk.Entry(
            new_window,
            font=("Arial", 12),
            width=30
        )
        entry.pack(pady=10)
        
        # 创建保存按钮
        def on_save():
            content = entry.get()
            if content:
                messagebox.showinfo("保存成功", f"已保存: {content}")
                self.warning_content.append(content)
                new_window.destroy()
            else:
                messagebox.showwarning("warning", "Please input your attentions！")
                new_window.destroy()
        
        save_button = tk.Button(
            new_window,
            text="保存",
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            width=10,
            command=lambda : [on_save(), self.warning_save(self.warning_content)]
        )
        save_button.pack(pady=20)

def warning_setting_start(event):
    root = tk.Tk()
    app = WarningSettings(root)
    root.mainloop()

