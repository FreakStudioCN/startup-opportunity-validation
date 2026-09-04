# Startup Opportunity Validation

一个本地、可追溯的创业机会验证 skill。它用需求行为信号、机会结构、生命周期信号和 3–7 天实验规则，对候选机会做实验优先级判断；不预测成功率、收入或投资回报。

## 能做什么

- 评估一个机会，明确买家、替代方案、证据和关键未知项。
- 比较多个候选方向，生成统一的机会预筛分与排序。
- 从本地证据库发现问题簇，设计最小可销售 Offer 与实验卡。
- 生成 `Kill / Modify / Escalate / Deliver` 建议。

## 知识包

`knowledge-pack/` 是从 12.5 万条去重证据蒸馏出的轻量包：精确去重、中英 TF-IDF、MiniBatchKMeans 和固定证据卡模板。每个主题均保留代表证据 ID、统计量和来源，可回查；不需要模型下载、GPU 或联网。

## 在 Codex 中使用

安装后可直接提出自然语言请求，例如：

```text
评估这个创业机会是否值得用 7 天验证，并给出证据缺口和实验卡。
```

skill 本体由 `SKILL.md` 定义。详细方法见 `references/`，数据说明见 `references/data-catalog.md`，可复跑蒸馏见 `scripts/distill_corpus.py`。

## 本地资料范围

- `research/core-materials/`：核心研究与执行材料。
- `research/data/`：可追溯的派生表。
- `knowledge-pack/`：约数百 KB 的可直接检索知识蒸馏结果。

原始爬取库不被复制到安装目录；它保留在 `E:\AIHardware\假设验证研究`，用于需要更深追溯时的人工核查。
