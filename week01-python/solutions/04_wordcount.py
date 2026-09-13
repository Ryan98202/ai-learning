# 参考答案 · W1 练习 4 / 函数 + 列表 + 字典
# 只在卡住超过 10 分钟时看。看完要关掉，自己重新敲一遍。

text = "学习人工智能，先学Python，再学大模型，最后学怎么把模型用起来"


def count_chars(s):
    """统计字符串 s 里每个字出现的次数，返回一个字典。"""
    result = {}

    # ---------------- TODO 区答案 ----------------
    for ch in s:
        if ch in result:
            result[ch] = result[ch] + 1
        else:
            result[ch] = 1
    # ---------------- 答案结束 ----------------

    return result


freq = count_chars(text)

print(f"这句话共有 {len(freq)} 个不同的字。")
print()

top5 = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)[:5]

print("出现最多的五个字：")
for ch, n in top5:
    print(f"  {ch}    {n} 次")

# 几个容易写错的地方，对照检查：
#   1) return 忘了缩进到函数外面 → 它变成循环体的一部分，循环跑第一次就返回了
#      （函数会在 return 处直接结束，后面的字都不会被统计）
#   2) 把 result = {} 写在 for 循环里面 → 每转一圈就清空一次，最后只剩一个字
#   3) 只有 if 没有 else → 新字会被漏掉，"学"之外的字符全都统计不到
#   4) 函数定义好了但忘了调用（少了 freq = count_chars(text) 这行）→ freq 不存在
