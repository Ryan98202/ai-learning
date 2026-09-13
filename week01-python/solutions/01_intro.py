# 参考答案 · W1 练习 1 / 变量与输出
# 只在卡住超过 10 分钟时看。看完要关掉，自己重新敲一遍。

city = "长沙"

greeting = "你好"
year = 2026
rate = 0.75

print(type(greeting))       # <class 'str'>
print(type(year))           # <class 'int'>
print(type(rate))           # <class 'float'>

print("2026" + "1")         # 20261  ← 文字拼接
print(2026 + 1)             # 2027   ← 数字相加

print(f"我在{city}，今年是{year}年")

# ---------------- TODO 区答案 ----------------
name = "Ryan"       # TODO 1
age = 25            # TODO 2
weeks = 11          # TODO 3
# ---------------- 答案结束 ----------------

print(f"我是 {name}，{age} 岁，计划用 {weeks} 周学完 AI 应用开发。")

if weeks is None:
    print("注意：TODO 3 还没填 —— 把上面 weeks 那行的 None 换成数字就行")
else:
    print(f"按每周 48 小时算，总共要投入 {48 * weeks} 小时。")
