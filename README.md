# ai-learning

Ryan 的 AI 应用开发学习仓库。起点：2026-09-13。

**目标**：11 周内从零基础到能独立开发 AI 应用。
**节奏**：每天 8 小时 × 每周 6 天 ≈ 48 小时/周，共约 528 小时。

---

## 目录结构

```
ai-learning/
├── week00-setup/       阶段 0：环境 + 认知
│   ├── hello.py        第一个 Python 程序
│   └── first_call.py   第一次用代码调用 AI 模型
└── (week01 ~ week11 陆续创建)
```

---

## 怎么运行

在这个目录下打开终端（VS Code 里按 `Ctrl + ~` 最快），然后：

```bash
cd week00-setup
python hello.py
python first_call.py 什么是大语言模型
python first_call.py -s 什么是大语言模型     # -s = 流式输出
python first_call.py                        # 不带参数 = 连续对话
```

---

## 环境备忘

| 组件 | 版本 | 位置 |
|---|---|---|
| Python | 3.12.10 | `%LOCALAPPDATA%\Programs\Python\Python312` |
| VS Code | 1.137.0 | `%LOCALAPPDATA%\Programs\Microsoft VS Code` |
| Git | 2.55.0.windows.5 | `%LOCALAPPDATA%\Programs\Git` |
| Ollama | 0.34.0 | `%LOCALAPPDATA%\Programs\Ollama` |
| 模型 | qwen3:1.7b | 1.27 GB，实测约 12 tok/s |

**Ollama 服务没响应时**：双击桌面的 `启动Ollama.cmd`，等 5 秒再试。
正常情况下它会随 Windows 登录自动启动，并有守护进程每 40 秒检查一次。

---

## Git 首次配置（必须做一次）

`git commit` 需要知道"是谁提交的"。在终端里执行下面两条，
把 `你的名字` 和 `你的邮箱` 换成你自己的（邮箱建议用你注册 GitHub 时用的那个）：

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

验证：

```bash
git config --global --list
```

---

## 验收标准（阶段 0）

- [ ] `python hello.py` 能输出中文，不报错
- [ ] `python first_call.py 你好` 能拿到模型回答
- [ ] `git config --global --list` 能看到 user.name / user.email
- [ ] 本仓库有至少 1 个 commit

---

## 为什么这个仓库存在

它不只是练习代码的存放处。11 周后，**它就是你唯一的能力证明**。

面试官不看你说"我学过 Python"，他看你的 commit 记录：
从第 1 天的 `print`，到第 11 周能跑起来的 RAG 系统和 Agent。
60 个工作日的持续提交，比任何简历描述都有说服力。

所以：**每天至少一次 commit**。哪怕只改了 3 行。
## 学习日志

- 2026-09-13 环境搭建完成，首个提交已推送到 GitHub