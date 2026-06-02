# tkinter-info-manager

> Python 课设作业样本 — 基于 tkinter 的信息管理系统
> Python Course Project Sample — Information Management System with tkinter GUI

一个简洁、完整的信息管理系统，使用 Python 标准库 tkinter 构建，适合作为**Python 课程设计**的参考项目。支持完整的增删改查（CRUD）操作，带有图形界面和数据持久化功能。

A clean and complete information management system built with Python tkinter. Ideal as a **Python course project reference**. Features full CRUD operations with a graphical interface and data persistence.

---

## 功能 Features

| 中文 | English |
|------|---------|
| 🔐 登录验证 | Login with password protection |
| ➕ 录入信息（姓名、性别、身高、体重、年龄、爱好） | Add records with input validation |
| ❌ 按姓名删除（含确认弹窗） | Delete records with confirmation dialog |
| ✏️ 修改信息（输入姓名自动填充原数据） | Update records with auto-fill |
| 🔍 按姓名查询 | Query individual records |
| 📋 表格形式显示全部记录 | View all records in table format |
| 💾 自动保存到 JSON 文件 | Auto-save to JSON file |

## 效果预览 Preview

> 截图已移除，可自行运行程序查看界面效果。
> Screenshots removed. Run the program to see the UI.

## 环境要求 Requirements

- Python 3.8+
- tkinter（内置）
- Pillow（`pip install Pillow`）— 用于背景图片

## 快速开始 Quick Start

```bash
pip install Pillow
python information_management.py
```

默认密码 Default password: `123456`

## 项目结构 Project Structure

```
├── information_management.py   # 主程序 Main application
├── background.png              # 登录背景图 Login background
├── data.txt                    # 数据存储（JSON 格式）
├── .gitignore
└── README.md
```

## 适合人群 Suitable for

- 🎓 Python 课设学生，寻找参考项目
- 🧑‍💻 tkinter 初学者，学习 GUI 编程
- 📚 想了解 CRUD 和数据持久化的开发者

## 许可 License

MIT
