# 参考答案 · W1 练习 2 / 判断（if）
# 只在卡住超过 10 分钟时看。看完要关掉，自己重新敲一遍。

# 进阶部分（可选）需要这行，不用时可删
import random

secret = random.randint(1, 10)

guess = int(input("猜一个 1 到 10 的数字："))

# ---------------- TODO 区答案 ----------------
if guess > secret:
    print("太大了")
elif guess < secret:
    print("太小了")
else:
    print("猜对了！")
# ---------------- 答案结束 ----------------

print("游戏结束。")

# 几个容易写错的地方，对照检查：
#   1) 冒号 : 漏了        → SyntaxError
#   2) print 那几行没缩进  → IndentationError
#   3) 用了 = 而不是 ==    → 在 if 里会变成"赋值"，结果永远是 True
#   4) int() 忘了套        → 猜的是文字，比大小会报 TypeError
