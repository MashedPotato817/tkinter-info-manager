"""
信息管理系统 (Information Management System)
A simple CRUD application built with Python tkinter.

功能：信息录入、删除、修改、查询、显示全部
环境：Python 3.8.3 + tkinter（内置）
第三方库：Pillow（用于背景图片）
"""

import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

# ═══════════════════════════════════════════════
#  配置信息（请替换为你的信息）
# ═══════════════════════════════════════════════
STUDENT_ID = "2024001"         # ← 替换为你的学号
STUDENT_NAME = "User"          # ← 替换为你的姓名
PASSWORD = "123456"
DATA_FILE = "data.txt"
BG_FILE = "background.png"


# ═══════════════════════════════════════════════
#  背景图片生成（使用Pillow）
# ═══════════════════════════════════════════════
try:
    from PIL import Image, ImageDraw, ImageFont
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

# ═══════════════════════════════════════════════
#  数据管理类
# ═══════════════════════════════════════════════
class DataManager:
    """负责数据的增删改查和文件存储"""

    def __init__(self, filename=DATA_FILE):
        self.filename = filename
        self.data = self._load()

    def _load(self):
        """从文件加载数据"""
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                content = f.read().strip()
                return json.loads(content) if content else []
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _save(self):
        """保存数据到文件"""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    # ── 录入 ──
    def add(self, record):
        """新增记录。返回 (成功?, 消息)"""
        name = record.get("name", "").strip()
        if not name:
            return False, "姓名不能为空！"

        # 查重
        if any(r["name"] == name for r in self.data):
            return False, f"记录 '{name}' 已存在！"

        # 字段验证
        ok, msg = self._validate(record)
        if not ok:
            return ok, msg

        self.data.append(record)
        self._save()
        return True, f"✓ 已录入 '{name}' 的信息！"

    # ── 删除 ──
    def delete(self, name):
        """按姓名删除记录"""
        for i, r in enumerate(self.data):
            if r["name"] == name:
                del self.data[i]
                self._save()
                return True, f"✓ 已删除 '{name}' 的记录！"
        return False, f"未找到 '{name}' 的记录！"

    # ── 查找 ──
    def find(self, name):
        """按姓名查找记录"""
        for r in self.data:
            if r["name"] == name:
                return r
        return None

    # ── 修改 ──
    def update(self, old_name, new_record):
        """修改记录"""
        for i, r in enumerate(self.data):
            if r["name"] == old_name:
                ok, msg = self._validate(new_record)
                if not ok:
                    return ok, msg
                self.data[i] = new_record
                self._save()
                return True, f"✓ 已修改 '{old_name}' 的记录！"
        return False, f"未找到 '{old_name}' 的记录！"

    # ── 全部 ──
    def get_all(self):
        return self.data.copy()

    # ── 验证 ──
    def _validate(self, record):
        try:
            if record.get("age"):
                age = int(record["age"])
                if not (0 <= age <= 150):
                    return False, "年龄必须在 0~150 之间！"
            if record.get("height"):
                h = float(record["height"])
                if not (30 <= h <= 250):
                    return False, "身高必须在 30~250 cm 之间！"
            if record.get("weight"):
                w = float(record["weight"])
                if not (10 <= w <= 300):
                    return False, "体重必须在 10~300 kg 之间！"
        except ValueError:
            return False, "数字格式不正确，请检查身高、体重、年龄！"
        return True, ""


# ═══════════════════════════════════════════════
#  登录窗口
# ═══════════════════════════════════════════════
class LoginWindow:
    """第一个界面：登录"""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("信息管理系统 - 登录")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.root.eval("tk::PlaceWindow . center")

        self._setup_ui()
        self.root.mainloop()

    def _setup_ui(self):
        # 背景图片
        if PIL_AVAILABLE and os.path.exists(BG_FILE):
            from PIL import ImageTk
            bg_img = Image.open(BG_FILE)
            bg_photo = ImageTk.PhotoImage(bg_img)
            bg_label = tk.Label(self.root, image=bg_photo)
            bg_label.image = bg_photo
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # 登录卡片
        card = tk.Frame(self.root, bg="white", bd=0, highlightbackground="#ddd",
                        highlightthickness=1)
        card.place(relx=0.5, rely=0.5, anchor="center", width=340, height=290)

        # 标题
        tk.Label(card, text="信息管理登录系统", font=("微软雅黑", 16, "bold"),
                 bg="white", fg="#2c3e50").pack(pady=(25, 5))
        tk.Label(card, text="tkinter Demo App", font=("微软雅黑", 9),
                 bg="white", fg="#7f8c8d").pack(pady=(0, 15))

        # 输入区域
        frame = tk.Frame(card, bg="white")
        frame.pack(pady=5)

        # 先声明变量
        self.id_var = tk.StringVar(value=STUDENT_ID)
        self.name_var = tk.StringVar(value=STUDENT_NAME)
        self.pwd_var = tk.StringVar(value=PASSWORD)

        fields = [
            ("学  号：", self.id_var, None),
            ("姓  名：", self.name_var, None),
            ("密  码：", self.pwd_var, "*"),
        ]
        for label, var, show_char in fields:
            row = tk.Frame(frame, bg="white")
            row.pack(fill="x", pady=4)
            tk.Label(row, text=label, font=("微软雅黑", 10), bg="white",
                     width=6, anchor="e").pack(side="left")
            entry = tk.Entry(row, textvariable=var, font=("微软雅黑", 10),
                             show=show_char, relief="solid", bd=1)
            entry.pack(side="right", fill="x", expand=True)

        # 登录按钮
        self.status_label = tk.Label(card, text="", font=("微软雅黑", 9),
                                     bg="white", fg="#e74c3c")
        self.status_label.pack()

        tk.Button(card, text="登  录", font=("微软雅黑", 12, "bold"),
                  bg="#3498db", fg="white", relief="flat", activebackground="#2980b9",
                  width=25, height=1, command=self._login).pack(pady=12)

    def _login(self):
        sid = self.id_var.get().strip()
        name = self.name_var.get().strip()
        pwd = self.pwd_var.get().strip()

        if pwd == PASSWORD:
            self.root.destroy()
            MainWindow(sid, name)
        else:
            self.status_label.config(text="✗ 密码错误，请重新输入！")


# ═══════════════════════════════════════════════
#  主窗口
# ═══════════════════════════════════════════════
class MainWindow:
    """第二个界面：信息管理主界面"""

    def __init__(self, student_id, name):
        self.sid = student_id
        self.sname = name
        self.dm = DataManager()

        self.root = tk.Tk()
        self.root.title("信息管理系统")
        self.root.geometry("850x600")
        self.root.eval("tk::PlaceWindow . center")
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)
        self._setup_ui()
        self.root.mainloop()

    def _setup_ui(self):
        # ── 顶部栏 ──
        header = tk.Frame(self.root, bg="#2c3e50", height=55)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(header, text=f"学号：{self.sid}  │  姓名：{self.sname}  │  信息管理系统",
                 font=("微软雅黑", 13, "bold"), bg="#2c3e50", fg="white",
                 anchor="w").pack(side="left", padx=20, pady=12)

        tk.Label(header, text="tkinter Demo App", font=("微软雅黑", 9),
                 bg="#2c3e50", fg="#bdc3c7").pack(side="right", padx=20)

        # ── 主体内容 ──
        body = tk.Frame(self.root)
        body.pack(fill="both", expand=True, padx=10, pady=10)

        # 左侧：操作面板
        left = tk.LabelFrame(body, text=" 操作面板 ", font=("微软雅黑", 11, "bold"),
                             fg="#2c3e50", padx=10, pady=10)
        left.pack(side="left", fill="y", padx=(0, 10))

        self._build_left_panel(left)

        # 右侧：数据显示
        right = tk.LabelFrame(body, text=" 数据显示 ", font=("微软雅黑", 11, "bold"),
                              fg="#2c3e50", padx=5, pady=5)
        right.pack(side="right", fill="both", expand=True)

        self._build_right_panel(right)

        # 初始显示
        self.refresh_display()

    # ── 左侧面板 ──
    def _build_left_panel(self, parent):
        # 操作选择
        tk.Label(parent, text="选择操作：", font=("微软雅黑", 10)).pack(anchor="w", pady=(5, 2))
        self.op_var = tk.StringVar(value="录入")
        ops = ["录入", "删除", "修改", "查询", "显示全部"]
        combo = ttk.Combobox(parent, textvariable=self.op_var, values=ops,
                             state="readonly", font=("微软雅黑", 10), width=18)
        combo.pack(pady=(0, 10))
        combo.bind("<<ComboboxSelected>>", lambda e: self._switch_form())

        ttk.Separator(parent, orient="horizontal").pack(fill="x", pady=5)

        # 动态表单容器
        self.form_container = tk.Frame(parent)
        self.form_container.pack(fill="x", pady=5)

        self._switch_form()

    # ── 右侧面板 ──
    def _build_right_panel(self, parent):
        # 工具栏
        toolbar = tk.Frame(parent)
        toolbar.pack(fill="x", pady=(0, 5))
        tk.Label(toolbar, text="记录列表", font=("微软雅黑", 10, "bold"),
                 fg="#2c3e50").pack(side="left")
        tk.Button(toolbar, text="🔄 刷新", font=("微软雅黑", 9),
                  command=self.refresh_display).pack(side="right")

        # 数据显示区（Treeview 表格）
        tree_frame = tk.Frame(parent)
        tree_frame.pack(fill="both", expand=True)

        columns = ("no", "name", "gender", "height", "weight", "age", "hobby")
        self.display = ttk.Treeview(tree_frame, columns=columns,
                                    show="headings", selectmode="browse")

        col_cfg = [
            ("no",     "序号",      50,  "center"),
            ("name",   "姓名",      80,  "center"),
            ("gender", "性别",      60,  "center"),
            ("height", "身高(cm)", 80,  "center"),
            ("weight", "体重(kg)", 80,  "center"),
            ("age",    "年龄",      60,  "center"),
            ("hobby",  "爱好",     160,  "w"),
        ]
        for col, heading, width, anchor in col_cfg:
            self.display.heading(col, text=heading, anchor="center")
            self.display.column(col, width=width, minwidth=width, anchor=anchor)

        # 斑马纹 + 选中高亮
        style = ttk.Style()
        style.configure("Treeview", font=("微软雅黑", 10), rowheight=26)
        style.configure("Treeview.Heading", font=("微软雅黑", 10, "bold"))
        style.map("Treeview", background=[("selected", "#3498db")],
                  foreground=[("selected", "white")])
        self.display.tag_configure("odd",  background="#ffffff")
        self.display.tag_configure("even", background="#f0f5fb")

        vbar = tk.Scrollbar(tree_frame, orient="vertical",  command=self.display.yview)
        hbar = tk.Scrollbar(tree_frame, orient="horizontal", command=self.display.xview)
        self.display.configure(yscrollcommand=vbar.set, xscrollcommand=hbar.set)

        vbar.pack(side="right", fill="y")
        hbar.pack(side="bottom", fill="x")
        self.display.pack(side="left", fill="both", expand=True)

        # 状态栏
        self.status_bar = tk.Label(parent, text="就绪", font=("微软雅黑", 9),
                                   fg="#7f8c8d", anchor="w")
        self.status_bar.pack(fill="x", pady=(5, 0))

    # ── 表单切换 ──
    def _switch_form(self):
        for w in self.form_container.winfo_children():
            w.destroy()

        op = self.op_var.get()
        {
            "录入": self._form_add,
            "删除": self._form_delete,
            "修改": self._form_update,
            "查询": self._form_query,
            "显示全部": lambda: self.refresh_display(),
        }[op]()

    # ── 录入表单 ──
    def _form_add(self):
        f = tk.Frame(self.form_container)
        f.pack(fill="x")

        fields = [
            ("姓名：", "name", tk.Entry(f, font=("微软雅黑", 10), width=20)),
            ("性别：", "gender", ttk.Combobox(f, values=["男", "女", "其他"],
                     state="readonly", font=("微软雅黑", 10), width=18)),
            ("身高(cm)：", "height", tk.Entry(f, font=("微软雅黑", 10), width=20)),
            ("体重(kg)：", "weight", tk.Entry(f, font=("微软雅黑", 10), width=20)),
            ("年龄：", "age", tk.Entry(f, font=("微软雅黑", 10), width=20)),
            ("爱好：", "hobby", tk.Entry(f, font=("微软雅黑", 10), width=20)),
        ]

        self.form_widgets = {}
        for i, (label, key, widget) in enumerate(fields):
            tk.Label(f, text=label, font=("微软雅黑", 10), anchor="e",
                     width=9).grid(row=i, column=0, sticky="e", pady=3, padx=(0, 5))
            widget.grid(row=i, column=1, pady=3, sticky="w")
            if isinstance(widget, ttk.Combobox):
                widget.set("男")
            self.form_widgets[key] = widget

        btn_frame = tk.Frame(f)
        btn_frame.grid(row=len(fields), column=0, columnspan=2, pady=12)
        tk.Button(btn_frame, text="确认录入", font=("微软雅黑", 10, "bold"),
                  bg="#27ae60", fg="white", relief="flat", padx=20,
                  command=self._do_add).pack()

    def _do_add(self):
        record = {
            "name": self.form_widgets["name"].get().strip(),
            "gender": self.form_widgets["gender"].get(),
            "height": self.form_widgets["height"].get().strip(),
            "weight": self.form_widgets["weight"].get().strip(),
            "age": self.form_widgets["age"].get().strip(),
            "hobby": self.form_widgets["hobby"].get().strip(),
        }
        ok, msg = self.dm.add(record)
        if ok:
            messagebox.showinfo("成功", msg)
            self.refresh_display()
        else:
            messagebox.showerror("错误", msg)

    # ── 删除表单 ──
    def _form_delete(self):
        f = tk.Frame(self.form_container)
        f.pack(fill="x")

        tk.Label(f, text="姓名：", font=("微软雅黑", 10)).pack(anchor="w", pady=(10, 2))
        self.del_entry = tk.Entry(f, font=("微软雅黑", 10), width=20)
        self.del_entry.pack(anchor="w")

        tk.Button(f, text="确认删除", font=("微软雅黑", 10, "bold"),
                  bg="#e74c3c", fg="white", relief="flat", padx=20,
                  command=self._do_delete).pack(anchor="w", pady=12)

    def _do_delete(self):
        name = self.del_entry.get().strip()
        if not name:
            messagebox.showerror("错误", "请输入要删除的姓名！")
            return
        if not messagebox.askyesno("确认删除", f"确定要删除「{name}」的记录吗？"):
            return
        ok, msg = self.dm.delete(name)
        if ok:
            messagebox.showinfo("成功", msg)
            self.del_entry.delete(0, tk.END)
            self.refresh_display()
        else:
            messagebox.showerror("错误", msg)

    # ── 修改表单 ──
    def _form_update(self):
        f = tk.Frame(self.form_container)
        f.pack(fill="x")

        # 查找区域
        tk.Label(f, text="输入姓名查找：", font=("微软雅黑", 10)).pack(anchor="w", pady=(5, 2))
        search_frame = tk.Frame(f)
        search_frame.pack(fill="x")

        self.upd_search_entry = tk.Entry(search_frame, font=("微软雅黑", 10), width=15)
        self.upd_search_entry.pack(side="left")
        tk.Button(search_frame, text="查找", font=("微软雅黑", 9), bg="#3498db",
                  fg="white", relief="flat", command=self._do_search_update).pack(side="left", padx=5)

        ttk.Separator(f, orient="horizontal").pack(fill="x", pady=8)

        # 修改表单
        self.upd_frame = tk.Frame(f)
        self.upd_frame.pack(fill="x")

        fields = [
            ("姓名：", "upd_name"),
            ("性别：", "upd_gender"),
            ("身高(cm)：", "upd_height"),
            ("体重(kg)：", "upd_weight"),
            ("年龄：", "upd_age"),
            ("爱好：", "upd_hobby"),
        ]

        self.upd_widgets = {}
        for i, (label, key) in enumerate(fields):
            tk.Label(self.upd_frame, text=label, font=("微软雅黑", 10),
                     anchor="e", width=9).grid(row=i, column=0, sticky="e", pady=2, padx=(0, 5))
            if key == "upd_gender":
                w = ttk.Combobox(self.upd_frame, values=["男", "女", "其他"],
                                 state="readonly", font=("微软雅黑", 10), width=18)
                w.set("男")
            else:
                w = tk.Entry(self.upd_frame, font=("微软雅黑", 10), width=20)
                w.config(state="disabled")
            w.grid(row=i, column=1, pady=2, sticky="w")
            self.upd_widgets[key] = w

        tk.Button(self.upd_frame, text="保存修改", font=("微软雅黑", 10, "bold"),
                  bg="#f39c12", fg="white", relief="flat", padx=20,
                  command=self._do_update).grid(row=len(fields), column=0, columnspan=2, pady=10)

    def _do_search_update(self):
        name = self.upd_search_entry.get().strip()
        if not name:
            messagebox.showerror("错误", "请输入姓名！")
            return
        record = self.dm.find(name)
        if record is None:
            messagebox.showerror("错误", f"未找到「{name}」的记录！")
            return

        # 填充表单
        self.upd_widgets["upd_name"].config(state="normal")
        self.upd_widgets["upd_name"].delete(0, tk.END)
        self.upd_widgets["upd_name"].insert(0, record.get("name", ""))

        self.upd_widgets["upd_gender"].set(record.get("gender", "男"))

        for key in ["upd_height", "upd_weight", "upd_age", "upd_hobby"]:
            field = key.replace("upd_", "")
            self.upd_widgets[key].config(state="normal")
            self.upd_widgets[key].delete(0, tk.END)
            self.upd_widgets[key].insert(0, record.get(field, ""))

    def _do_update(self):
        old_name = self.upd_search_entry.get().strip()
        if not old_name:
            messagebox.showerror("错误", "请先查找要修改的记录！")
            return

        new_record = {
            "name": self.upd_widgets["upd_name"].get().strip(),
            "gender": self.upd_widgets["upd_gender"].get(),
            "height": self.upd_widgets["upd_height"].get().strip(),
            "weight": self.upd_widgets["upd_weight"].get().strip(),
            "age": self.upd_widgets["upd_age"].get().strip(),
            "hobby": self.upd_widgets["upd_hobby"].get().strip(),
        }
        ok, msg = self.dm.update(old_name, new_record)
        if ok:
            messagebox.showinfo("成功", msg)
            self.refresh_display()
        else:
            messagebox.showerror("错误", msg)

    # ── 查询表单 ──
    def _form_query(self):
        f = tk.Frame(self.form_container)
        f.pack(fill="x")

        tk.Label(f, text="姓名：", font=("微软雅黑", 10)).pack(anchor="w", pady=(10, 2))
        self.qry_entry = tk.Entry(f, font=("微软雅黑", 10), width=20)
        self.qry_entry.pack(anchor="w")

        btn_frame = tk.Frame(f)
        btn_frame.pack(anchor="w", pady=8)

        tk.Button(btn_frame, text="查询", font=("微软雅黑", 10, "bold"),
                  bg="#3498db", fg="white", relief="flat", padx=15,
                  command=self._do_query).pack(side="left", padx=(0, 5))
        tk.Button(btn_frame, text="显示全部", font=("微软雅黑", 10),
                  command=self.refresh_display).pack(side="left")

    def _do_query(self):
        name = self.qry_entry.get().strip()
        if not name:
            messagebox.showerror("错误", "请输入姓名！")
            return
        record = self.dm.find(name)
        # 先显示全部，再高亮匹配行
        self.refresh_display()
        if record:
            for item in self.display.get_children():
                if self.display.item(item, "values")[1] == record.get("name", ""):
                    self.display.selection_set(item)
                    self.display.focus(item)
                    self.display.see(item)
                    break
            messagebox.showinfo("查询结果",
                f"姓名：{record.get('name','')}\n"
                f"性别：{record.get('gender','')}\n"
                f"身高：{record.get('height','')} cm\n"
                f"体重：{record.get('weight','')} kg\n"
                f"年龄：{record.get('age','')} 岁\n"
                f"爱好：{record.get('hobby','')}")
        else:
            messagebox.showerror("查询结果", f"未找到「{name}」的记录。")

    # ── 刷新显示 ──
    def refresh_display(self):
        for item in self.display.get_children():
            self.display.delete(item)
        records = self.dm.get_all()
        self.status_bar.config(text=f"共 {len(records)} 条记录")
        for i, r in enumerate(records, 1):
            tag = "odd" if i % 2 == 1 else "even"
            self.display.insert("", "end", tags=(tag,), values=(
                i,
                r.get("name", ""),
                r.get("gender", ""),
                r.get("height", ""),
                r.get("weight", ""),
                r.get("age", ""),
                r.get("hobby", ""),
            ))

    # ── 关闭事件 ──
    def _on_close(self):
        if messagebox.askokcancel("退出", "确定要退出系统吗？"):
            self.root.destroy()


# ═══════════════════════════════════════════════
#  程序入口
# ═══════════════════════════════════════════════
if __name__ == "__main__":

    # 启动登录窗口
    LoginWindow()
