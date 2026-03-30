import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from check_and_save import write_to_md
class ModelSettings:
    def __init__(self, root):
        self.root = root
        self.root.title("Model Settings")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")
        self.select_label_list=["Model"]
        self.button_command=write_to_md
        
        self.title_label = tk.Label(
            self.root,
            text="details about Model",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        self.title_label.pack(pady=20)
        
        # 创建输入框容器
        self.inputs_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.inputs_frame.pack(pady=10)
        
        # 输入框配置
        self.config = [ "Select the Model:",
        "Model_Url:",
        "API_Key:"
        ]
        
        # 端口选项
        self.port_options = ["GPT4", "CLAUDE", "Gemini","Llama2","通义","deepseek"]
        
       
       
        self.frame_1 = tk.Frame(self.inputs_frame, bg="#f0f0f0")
        self.frame_1.pack(pady=15, fill=tk.X, padx=40)   # 标签
        self.label_1 = tk.Label(
            self.frame_1,
            text=self.config[0],
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#555",
            width=20,
            anchor="w"
            )
        self.label_1.pack(side=tk.LEFT, padx=10)
        self.create_multi_select_dropdown(self.frame_1, "orders", self.port_options, "selected_ports")
        # 创建新的frame用于label_2
        self.frame_2 = tk.Frame(self.inputs_frame, bg="#f0f0f0")
        self.frame_2.pack(pady=15, fill=tk.X, padx=40)

        self.label_2 = tk.Label(
            self.frame_2,
            text=self.config[1],
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#555",
            width=20,
            anchor="w"
        )
        self.label_2.pack(side=tk.LEFT, padx=10)
        self.entry_1=tk.Entry(self.frame_2, width=40)
        self.entry_1.pack(side=tk.LEFT, padx=0)

        self.frame_3 = tk.Frame(self.inputs_frame, bg="#f0f0f0")
        self.frame_3.pack(pady=15, fill=tk.X, padx=40)

        self.label_3 = tk.Label(
            self.frame_3,
            text=self.config[2],
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#555",
            width=20,
            anchor="w"
        )
        self.label_3.pack(side=tk.LEFT, padx=10)
        self.entry_2=tk.Entry(self.frame_3, width=40)
        self.entry_2.pack(side=tk.LEFT, padx=0)
        
                
      
        self.save_button_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.save_button_frame.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)
        
        self.save_button = self.create_circular_button(self.save_button_frame, "保存", "#4CAF50", self.save_settings, size=60)
        self.save_button.pack()
        
        
    def create_multi_select_dropdown(self, parent, title, options, selected_var):
        """创建下拉式多选框"""
        # 创建框架
        dropdown_frame = tk.Frame(parent, bg="#ffffff", relief=tk.SOLID, borderwidth=1)
        dropdown_frame.pack(side=tk.LEFT, fill=tk.X, expand=False)
        
        # 创建显示选中项的标签
        selected_label = tk.Label(
            dropdown_frame,
            text=f"select {title}...",

            font=("Arial", 12),
            bg="#ffffff",
            fg="#999999",
            anchor="w",
            padx=5,
            pady=2
        )
        selected_label.pack(fill=tk.X)
        
        # 创建下拉菜单框架
        dropdown_menu = tk.Toplevel(self.root)
        dropdown_menu.title(f"选择{title}")
        dropdown_menu.geometry("200x200")
        dropdown_menu.transient(self.root)
        dropdown_menu.withdraw()
        
        # 添加选项
        vars_dict = {}
        for option in options:
            var = tk.IntVar()
            vars_dict[option] = var
            checkbox = tk.Checkbutton(
                dropdown_menu,
                text=option,
                variable=var,
                bg="#ffffff",
                font=("Arial", 10),
                command=lambda opt=option, v=var, sl=selected_label, sv=selected_var, od=options, vd=vars_dict: self.toggle_option(opt, v, sl, sv, od, vd)
            )
            checkbox.pack(anchor="w", padx=10, pady=2)
        
        # 添加确定按钮
        ok_button = tk.Button(
            dropdown_menu,
            text="确定",
            font=("Arial", 10),
            bg="#4CAF50",
            fg="white",
            relief=tk.FLAT,
            command=dropdown_menu.withdraw
        )
        ok_button.pack(anchor="e", padx=10, pady=5)
        
        # 绑定点击事件
        def toggle_dropdown(event):
            if dropdown_menu.winfo_viewable():
                dropdown_menu.withdraw()
            else:
                # 计算位置
                x = selected_label.winfo_rootx()
                y = selected_label.winfo_rooty() + selected_label.winfo_height()
                dropdown_menu.geometry(f"200x200+{x}+{y}")
                dropdown_menu.deiconify()
                dropdown_menu.lift()
        
        selected_label.bind("<Button-1>", toggle_dropdown)
    
    def toggle_option(self, option, var, selected_label, selected_var, options, vars_dict):
        """切换选项的选中状态"""
        selected_list = getattr(self, selected_var)
        if var.get() == 1:
            if option not in selected_list:
                selected_list.append(option)
        else:
            if option in selected_list:
                selected_list.remove(option)
        
        # 更新显示
        if selected_list:
            selected_label.config(text=", ".join(selected_list), fg="#333333")
        else:
            selected_label.config(text=f"选择{options[0]}...", fg="#999999")
        self.select_label_list.append(option)
    

    
    def on_focus_in(self, event, entry, var, default):
        """获得焦点时的处理"""
        if var.get() == default:
            var.set("")
            entry.config(fg="#333333")
    
    def on_focus_out(self, event, entry, var, default):
        """失去焦点时的处理"""
        if var.get() == "":
            var.set(default)
            entry.config(fg="#999999")
    
    def on_enter(self, event, border):
        """鼠标进入时的处理"""
        border.config(bg="#4CAF50")
    
    def on_leave(self, event, border):
        """鼠标离开时的处理"""
        border.config(bg="#cccccc")
    
    def create_circular_button(self, parent, text, color, command, size=60):
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
                           fill="white", font=("微软雅黑", 10, "bold"))
        
        # 绑定点击事件
        canvas.bind("<Button-1>", lambda e:[self.save_entry_content(),self.button_command(self.select_label_list),self.shut_down_page()] )
        canvas.bind("<Enter>", lambda e: canvas.itemconfig("circle", fill=self.lighten_color(color)))
        canvas.bind("<Leave>", lambda e: canvas.itemconfig("circle", fill=color))
        
        return canvas
    
    def lighten_color(self, color):
        """将颜色变亮一点（用于悬停效果）"""
        color_map = {
            "#4CAF50": "#66BB6A",  # 绿色变亮
        }
        return color_map.get(color, color)
    
    def save_settings(self):
        """保存设置"""
        # 保存逻辑
        messagebox.showinfo("提示", "设置已保存！")

    def shut_down_page(self):
        """关闭页面"""
        self.root.destroy()

    def save_entry_content(self):
        content_1=self.entry_1.get()
        content_2=self.entry_2.get()
        self.select_label_list.append(content_1)
        self.select_label_list.append(content_2)
def model_setting_start():
    root = tk.Tk()
    app = ModelSettings(root)
    root.mainloop()




  
