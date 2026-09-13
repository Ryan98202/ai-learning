# -*- coding: utf-8 -*-
"""
hello.py —— 你的第一个 Python 程序

运行方式（在这个文件所在目录打开终端）：
    python hello.py

这个文件故意写得很短。它的作用不是"学会了 Python"，
而是确认三件事：解释器能跑、文件编码没问题、你能看到自己的输出。
"""

print("你好，Ryan。")
print("这是我的第一个 Python 程序。")
print()
print("解释器版本:", __import__("sys").version.split()[0])

# 变量：把值存起来，起个名字
name = "Ryan"
days = 11

# f-string：Python 3.6+ 的字符串格式化写法，花括号里可以直接放变量
print(f"{name} 计划用 {days} 周学完 AI 应用开发。")
print(f"平均每周要完成 {days} 个阶段中的 {round(77/days, 1)}% —— 开个玩笑，不是这么算的。")

# for 循环：把列表里的每一项依次取出来
skills = ["Python", "大模型应用", "RAG 知识库", "Agent 智能体", "工程化部署"]
print()
print("要攻克的技能：")
for i, s in enumerate(skills, start=1):
    print(f"  {i}. {s}")

print()
print("如果上面这些词你现在一个都不懂，那是对的 —— 这正是接下来 11 周要解决的事。")
