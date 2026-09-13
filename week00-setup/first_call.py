# -*- coding: utf-8 -*-
"""
first_call.py —— 你第一次用「代码」调用 AI 模型

它做的事很简单：把你输入的一句话发给本机运行的模型，打印出回答。
但这是一个分界线 ——
    从这里开始，你不再是通过聊天框「使用」AI，而是通过代码「调用」AI。
这两者的差别，就是「会用 AI 工具的人」和「能做 AI 应用的人」的差别。

运行方式（在这个文件所在目录打开终端）：
    python first_call.py 用一句话解释什么是大语言模型
    python first_call.py            # 不带参数 → 进入连续对话模式
    python first_call.py -s 你好     # 加 -s 观察「流式输出」：字是一个一个蹦出来的

【为什么用标准库 urllib，不用 requests？】
因为这样可以不装任何第三方包就跑通。等你以后写真正的项目，
会换成 requests 或 openai SDK —— 到那时你会明白它们帮你省掉了什么。
先看见最底层的 HTTP 长什么样，后面用封装库时才不会是黑盒。
"""

import json
import sys
import urllib.error
import urllib.request

# Ollama 服务地址：127.0.0.1 = 本机，完全没有联网
API_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "qwen3:1.7b"


def call_model(prompt, stream=False, think=False):
    """把 prompt 发给模型。

    stream=False → 等模型全部生成完再一次性返回
    stream=True  → 模型每生成一小段就立刻返回（就是你在网页版里看到的"打字机效果"）
    """
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": stream,
        "think": think,  # qwen3 支持"先思考再回答"，关掉它响应更快
    }
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    if stream:
        return _stream(req)

    with urllib.request.urlopen(req, timeout=600) as resp:
        result = json.loads(resp.read().decode("utf-8"))

    text = (result.get("response") or "").strip()

    # 下面两个字段是模型自己汇报的：生成了多少 token、花了多少纳秒
    n = result.get("eval_count", 0)
    seconds = result.get("eval_duration", 1) / 1e9
    speed = n / seconds if seconds > 0 else 0
    return text, speed


def _stream(req):
    """流式读取：逐行解析 NDJSON，每行是一个 JSON 片段"""
    chunks = []
    n_tokens = 0
    seconds = 0.0
    with urllib.request.urlopen(req, timeout=600) as resp:
        for raw in resp:                       # 一行一行读
            line = raw.decode("utf-8").strip()
            if not line:
                continue
            obj = json.loads(line)
            piece = obj.get("response") or ""
            if piece:
                print(piece, end="", flush=True)   # flush=True 是关键：立刻显示，不等缓冲
                chunks.append(piece)
            if obj.get("done"):
                n_tokens = obj.get("eval_count", 0)
                seconds = obj.get("eval_duration", 1) / 1e9
    print()
    speed = n_tokens / seconds if seconds > 0 else 0
    return "".join(chunks), speed


def explain_connection_error(err):
    """把底层报错翻译成能照着做的中文"""
    print()
    print("─" * 58)
    print("连不上本机模型服务（127.0.0.1:11434）。")
    print()
    print("最常见的原因：Ollama 后台服务没有启动。")
    print("解决办法（任选一个）：")
    print()
    print("  1. 双击桌面的「启动Ollama.cmd」，等 5 秒后重新运行本程序")
    print("  2. 在终端里执行： ollama serve")
    print("  3. 检查服务是否活着： ollama list")
    print()
    print(f"原始报错：{err}")
    print("─" * 58)


def main():
    args = sys.argv[1:]

    # -s / --stream 开关
    stream = False
    if args and args[0] in ("-s", "--stream"):
        stream = True
        args = args[1:]

    # 模式一：命令行直接传了问题 → 问一次就退出
    if args:
        prompt = " ".join(args)
        print(f"模型：{MODEL}    问题：{prompt}")
        print("-" * 58)
        try:
            text, speed = call_model(prompt, stream=stream)
        except urllib.error.URLError as e:
            explain_connection_error(e)
            return 1
        if not stream:
            print(text)
        print("-" * 58)
        print(f"生成速度：{speed:.1f} tokens/秒")
        return 0

    # 模式二：没传参数 → 进入连续对话
    print("=" * 58)
    print(f"  与本机模型对话（{MODEL}）")
    print("  直接打字提问，输入 /bye 退出，输入 /s 切换流式开关")
    print("=" * 58)
    while True:
        try:
            question = input("\n你：").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not question:
            continue
        if question in ("/bye", "/exit", "/quit"):
            break
        if question == "/s":
            stream = not stream
            print(f"[流式输出已{'开启' if stream else '关闭'}]")
            continue
        try:
            text, speed = call_model(question, stream=stream)
        except urllib.error.URLError as e:
            explain_connection_error(e)
            break
        if not stream:
            print(f"模型：{text}")
            print(f"      （{speed:.1f} tokens/秒）")
    print("再见。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
