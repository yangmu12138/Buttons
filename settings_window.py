import tkinter as tk
from tkinter import ttk
from port_settings import port_setting_start 
from order_settings import order_setting_start
from model_settings import model_setting_start

def create_round_button(parent, text, color, command, size=60):
    """创建圆形按钮"""
    # 创建画布
    canvas = tk.Canvas(parent, width=size, height=size, 
                       bg=parent.cget('bg'), highlightthickness=0)
    
    # 绘制圆形
    padding = 2
    canvas.create_oval(padding, padding, size-padding, size-padding, 
                       fill=color, outline=color, tags="circle")
    
    # 添加文字
    canvas.create_text(size//2, size//2, text=text, 
                       fill="black", font=("微软雅黑", 10, "bold"))
    
    # 绑定点击事件
    canvas.bind("<Button-1>", lambda e: command())
    canvas.bind("<Enter>", lambda e: canvas.itemconfig("circle", fill=lighten_color(color)))
    canvas.bind("<Leave>", lambda e: canvas.itemconfig("circle", fill=color))
    
    return canvas


def lighten_color(color):
    """将颜色变亮一点（用于悬停效果）"""
    color_map = {
        "#FF6B6B": "#FF8E8E",  # 红色变亮
        "#4ECDC4": "#6EDDD6",  # 青色变亮
        "#45B7D1": "#67C5DB",  # 蓝色变亮
    }
    return color_map.get(color, color)


def settings_main(event):
    # 创建主窗口
    root = tk.Tk()
    root.title("settings")
    root.geometry("320x300+300+280")
    root.resizable(False, False)
    root.configure(bg="#f0f0f0")

    # 创建主框架
    main_frame = tk.Frame(root, bg="#f0f0f0")
    main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    # 按钮配置：文字、颜色、命令
    button_configs = [
        ("Port", "#2196F3", port_setting_start),  # 珊瑚红
        ("Order", "#FF9800", order_setting_start),  #  turquoise
        ("Model", "#E91E63", model_setting_start),  # 天蓝色
    ]

    # 创建三行按钮和标签
    for i, (text, color, cmd) in enumerate(button_configs):
        row_frame = tk.Frame(main_frame, bg="#f0f0f0")
        row_frame.pack(pady=10)

        # 创建圆形按钮
        btn = create_round_button(row_frame, text, color, cmd, size=60)
        btn.pack(side=tk.LEFT, padx=10)

        # 创建标签
        label = tk.Label(row_frame, text=f" Settings about {text}", 
                         bg="#f0f0f0", font=("微软雅黑", 12))
        label.pack(side=tk.LEFT, padx=10)

    # 运行主循环
    root.mainloop()

