# 参考答案 · W1 练习 3 / 循环（while）
# 只在卡住超过 10 分钟时看。看完要关掉，自己重新敲一遍。

secret = 7
tries = 0
guess = 0

# ---------------- TODO 区答案 ----------------
while guess != secret:
    guess = int(input("猜一个 1 到 10 的数字："))
    tries = tries + 1
    if guess > secret:
        print("太大了")
    elif guess < secret:
        print("太小了")
# ---------------- 答案结束 ----------------

print(f"猜对了！你一共猜了 {tries} 次。")

# 几个容易写错的地方，对照检查：
#   1) 循环体里漏了给 guess 重新赋值 → 条件永远成立，程序停不下来（要 Ctrl + C 停）
#   2) 循环体里漏了 tries = tries + 1 → 能跑通，但最后会显示"猜了 0 次"
#   3) 判断提示写在 input 之前 → 用的是上一轮的值，提示会慢一拍
#   4) tries 那行忘了缩进 → 它变成"循环结束后才执行"，
#      而且 while 循环会在第一次进入时找不到 tries 的更新动作
#
# 小技巧：tries = tries + 1 有个简写 —— tries += 1，效果完全一样。
#         Python 里 += -= *= 都是这个套路，后面会经常见到。
