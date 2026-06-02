# tkinter-info-manager

> [English](./README.en.md) | 中文

一个基于 Python tkinter 的信息管理系统，**Python 课程设计**参考项目。支持完整的增删改查（CRUD）操作，界面简洁，数据自动持久化存储。

---

## 功能

- 🔐 **登录验证** — 密码保护
- ➕ **录入信息** — 姓名、性别、身高、体重、年龄、爱好，含输入验证
- ❌ **删除记录** — 按姓名删除，含确认弹窗防误操作
- ✏️ **修改记录** — 输入姓名自动填充原信息，修改后保存
- 🔍 **查询记录** — 按姓名精确查询
- 📋 **显示全部** — 表格形式展示所有记录
- 💾 **数据持久化** — 自动保存到 JSON 文件，重启不丢失

## 环境要求

- Python 3.8+
- tkinter（内置）
- Pillow：`pip install Pillow`

## 快速开始

```bash
pip install Pillow
python information_management.py
```

默认密码：`123456`

## 适合人群

- 🎓 正在做 Python 课设的学生
- 🧑‍💻 学习 tkinter GUI 编程的初学者
- 📚 想了解 CRUD + 文件持久化的开发者

## 项目结构

```
├── information_management.py   # 主程序
├── background.png              # 登录背景图
├── data.txt                    # 数据存储（JSON 格式）
├── README.md                   # 中文说明
├── README.en.md                # English version
└── .gitignore
```

## 许可

MIT
