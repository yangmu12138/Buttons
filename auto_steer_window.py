import tkinter as tk
from tkinter import ttk
from buttons_functions import Buttons_adjust as adjust
from message_window import message_window_start
class SettingsPage:
    def __init__(self, root):
        self.root = root
        self.root.title("auto_steer_settings")
        self.root.geometry("400x300")
        self.adjust=adjust
        self.message_window_start=message_window_start
        
        # 创建主框架
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(expand=True, fill=tk.BOTH)
        
        # 标题标签
        title_label = ttk.Label(main_frame, text="select mode", font=("Arial", 26, "bold"))
        title_label.pack(pady=(0, 20))
        
        # 按钮容器框架，用于并排显示
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(expand=True)
        
        # 创建两个并排的圆形按钮
        self.create_circle_button_1(button_frame, "auto", "#4CAF50", 0 ,self.adjust)
        self.create_circle_button_2(button_frame, "steer", "#2196F3", 1,self.message_window_start)
    def shutdown_page(self):
        self.root.destroy()
    def create_circle_button_1(self, parent, text, color, column, event):
        # 创建Canvas来绘制圆形按钮
        canvas_size = 80
        canvas = tk.Canvas(parent, width=canvas_size, height=canvas_size, 
                          highlightthickness=0, bg=self.root.cget('bg'))
        canvas.grid(row=0, column=column, padx=20)
        
        # 绘制圆形
        padding = 4
        circle = canvas.create_oval(padding, padding, 
                                   canvas_size - padding, canvas_size - padding,
                                   fill=color, outline="#388E3C", tags="circle",activefill="#66BB6A", activeoutline="#43A047")
        
        # 添加文字
        text_item = canvas.create_text(canvas_size // 2, canvas_size // 2,
                                      text=text, fill="white",
                                      font=("Arial", 10, "bold"))
        
        # 绑定点击事件
        canvas.bind("<Button-1>", lambda e: [event(None),self.shutdown_page()])
        canvas.bind("<Enter>", lambda e, c=canvas, ci=circle: self.on_hover(c, ci, True))
        canvas.bind("<Leave>", lambda e, c=canvas, ci=circle: self.on_hover(c, ci, False))
        
        # 鼠标样式
        canvas.config(cursor="hand2")


    def create_circle_button_2(self, parent, text, color, column, event):
        # 创建Canvas来绘制圆形按钮
        canvas_size = 80
        canvas = tk.Canvas(parent, width=canvas_size, height=canvas_size, 
                          highlightthickness=0, bg=self.root.cget('bg'))
        canvas.grid(row=0, column=column, padx=20)
        
        # 绘制圆形
        padding = 4
        circle = canvas.create_oval(padding, padding, 
                                   canvas_size - padding, canvas_size - padding,
                                   fill=color, outline="#388E3C", tags="circle",activefill="#66BB6A", activeoutline="#43A047")
        
        # 添加文字
        text_item = canvas.create_text(canvas_size // 2, canvas_size // 2,
                                      text=text, fill="white",
                                      font=("Arial", 10, "bold"))
        
        # 绑定点击事件
        canvas.bind("<Button-1>", lambda e: event())
        canvas.bind("<Enter>", lambda e, c=canvas, ci=circle: self.on_hover(c, ci, True))
        canvas.bind("<Leave>", lambda e, c=canvas, ci=circle: self.on_hover(c, ci, False))
        
        # 鼠标样式
        canvas.config(cursor="hand2")
    
    def get_message(self, button_text):
        print(f"点击了 {button_text}")
    
    def on_hover(self, canvas, circle, is_hover):
        # 悬停效果：改变圆形颜色亮度
        if is_hover:
            canvas.itemconfig(circle, stipple="hourglass")
        else:
            canvas.itemconfig(circle, stipple="")

def auto_or_steer_settings():
    root = tk.Tk()
    app = SettingsPage(root)
    root.mainloop()

