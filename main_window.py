import tkinter as tk
from tkinter import messagebox
import auto_or_steer_window
from settings_window import settings_main
from warning_window import warning_setting_start
from auto_or_steer_window import auto_or_steer_settings

class Buttons_model:
    def __init__(self, root):
        super().__init__(root)


class RoundButtonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BUTTONS")
        self.root.geometry("400x400+550+320")
        self.root.configure(bg="#f0f0f0")
        
        self.create_widgets()
        
    def create_widgets(self):
        # 大按钮
        self.big_button_canvas = tk.Canvas(
            self.root,
            width=160,
            height=160,
            bg="#f0f0f0",
            highlightthickness=0
        )
        self.big_button_canvas.pack(pady=30)
        
        # 绘制大圆形按钮
        self.big_button = self.big_button_canvas.create_oval(
            10, 10, 150, 150,
            fill="#4CAF50",
            outline="#388E3C",
            width=2,
            activefill="#66BB6A",
            activeoutline="#43A047"
        )
        
        # 大按钮文字
        self.big_button_canvas.create_text(
            80, 80,
            text="Auto",
            fill="black",
            font=("Arial", 36, "bold")
        )
        
        # 绑定大按钮点击事件
        self.big_button_canvas.bind("<Button-1>", lambda e: auto_or_steer_settings())
        
        # 底部小按钮容器
        self.buttons_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.buttons_frame.pack()
        
        # 小按钮颜色
        self.small_button_colors = ["#2196F3", "#FF9800", "#E91E63"]
        self.small_button_texts = ["Setting", "Teach", "warning"]
        self.small_button_functions = [
            settings_main,
            self.on_small_button2_click,
            warning_setting_start
        ]
        
        # 创建三个小按钮
        for i in range(3):
            canvas = tk.Canvas(
                self.buttons_frame,
                width=80,
                height=80,
                bg="#f0f0f0",
                highlightthickness=0
            )
            canvas.pack(side=tk.LEFT, padx=20)
            
            # 绘制小圆形按钮
            button = canvas.create_oval(
                5, 5, 75, 75,
                fill=self.small_button_colors[i],
                outline=self.darken_color(self.small_button_colors[i]),
                width=2,
                activefill=self.lighten_color(self.small_button_colors[i]),
                activeoutline=self.darken_color(self.small_button_colors[i])
            )
            
            # 小按钮文字
            canvas.create_text(
                40, 40,
                text=self.small_button_texts[i],
                fill="black",
                font=("Arial", 12, "bold")
            )
            
            # 绑定小按钮点击事件
            canvas.tag_bind(button, "<Button-1>", self.small_button_functions[i])
            canvas.bind("<Button-1>", self.small_button_functions[i])
    def darken_color(self, color):
        """颜色变暗"""
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        r = max(0, r - 40)
        g = max(0, g - 40)
        b = max(0, b - 40)
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def lighten_color(self, color):
        """颜色变亮"""
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        r = min(255, r + 40)
        g = min(255, g + 40)
        b = min(255, b + 40)
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def on_big_button_click(self, event):
        messagebox.showinfo("提示", "你点击了大按钮！")
    
    def on_small_button1_click(self):
        messagebox.showinfo("提示", "你点击了按钮1！")
    
    def on_small_button2_click(self,event):
        messagebox.showinfo("info", "it not be implemented")
    
    def on_small_button3_click(self,event):
        messagebox.showinfo("提示", "你点击了按钮3！")

def start_interface():
    root = tk.Tk()
    app = RoundButtonApp(root)
    root.mainloop()



if __name__ == "__main__":
    start_interface()
