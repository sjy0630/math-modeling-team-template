# Mathematical Modeling Team Template

一个面向三人数学建模队伍的轻量协作仓库模板，适用于高教社杯、MCM/ICM 等限时建模训练与比赛。

它不预设某种模型，而是帮助队伍把一份结果从原始数据稳定地推进到可复现代码、图表和论文：

```text
data/raw
  -> data/interim
  -> data/processed
  -> notebooks / src
  -> outputs
  -> paper
```

## 开始使用

1. 点击 GitHub 页面上的 **Use this template** 创建你们自己的仓库。
2. 在 README 顶部补充题目、队员和截止时间。
3. 通过私有渠道共享题目附件，把文件放进本地 `data/raw/`；原始数据默认不进入 Git。
4. 三位队员分别复制 `templates/01_individual_problem_analysis.md`，先独立拆题。
5. 合并为 `templates/02_team_problem_tree.md`，确定第一个 baseline、负责人和复核人。
6. 从个人分支提交 Pull Request，至少一位队友复核后再合并到 `main`。

第一次使用建议直接照着 [比赛前两小时](docs/first-two-hours.md) 推进；交卷前逐项执行 [提交检查表](docs/submission-checklist.md)。

## 目录

```text
.
├── data/               # 原始、中间、模型输入数据及数据字典
├── notebooks/          # 快速探索；不作为最终唯一事实源
├── src/                # 可复用、可从根目录运行的正式代码
├── outputs/            # 论文引用的最终图、表和指标
├── paper/              # 论文正文、符号表和图表清单
├── references/         # 官方规则、资料与引用记录
├── team_notes/         # 独立拆题、会议纪要与交接
├── templates/          # 可复制的协作模板
├── docs/               # 开局流程与提交检查表
├── tests/              # 数据口径、公式和约束的最小检查
├── decision_log.md     # 关键口径与模型选择的理由
└── ai_usage_log.md     # AI 用途、采纳情况与人工核验
```

## 环境

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 scripts/check_structure.py
python3 scripts/run_pipeline.py
python3 -m pytest
```

Windows PowerShell 激活命令为 `.venv\Scripts\Activate.ps1`。依赖稳定后，建议额外生成本题自己的锁定版本文件。

## 三人协作原则

- 角色是第一责任，不是知识孤岛；每个关键结论必须有另一人复核。
- notebook 用于探索，论文采用的结论要迁移到 `src/` 并生成稳定的 `outputs/`。
- 改变单位、样本范围、缺失值、目标函数或约束时，更新 `decision_log.md`。
- AI 可以辅助检索、编程和表达，但核心建模判断、验证与最终一致性由队伍负责并留痕。
- 原始数据、大文件、密钥和个人绝对路径不提交 Git。

## 设计依据

本模板借鉴 [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/) 的数据分层思想，并针对限时数学建模做了减法。GitHub 的模板仓库机制见[官方说明](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)。

相较于 [HZMath/MathModelingTemplate](https://github.com/HZMath/MathModelingTemplate)，本模板保留 Python 与 LaTeX 自动检查入口，并补充数据血缘、三人协作、模型验证、论文追溯与 AI 使用记录。若队伍使用 Word，可删除 `paper/main.tex` 和 LaTeX 工作流，其余结构不受影响。

本项目采用 [MIT License](LICENSE)。
