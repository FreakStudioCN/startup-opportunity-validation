# 跨 14 类 Signal：详细特征、具体案例、数据与机会漏斗

本报告不是只给机会排行榜，而是先逐类说明 14 个 Demand Behavior Signal 的行为特征、数据、案例和强弱判断，再把它们合并为跨 signal 的问题聚类、独立证据去重、Opportunity Scoring 与机会漏斗。

## 1. 数据总览
- 输入记录：14 类 Signal × 10000 条 = 140000 条。
- 去重后独立证据：125411 条。
- 映射到问题簇的独立证据：81025 条。
- 问题簇：30 个。
- 3 天实验优先机会：8 个。
- 需要付费/客户发现进一步调查：17 个。

## 2. 14 类 Signal 详细特征、数据和案例

### Signal 01：用户已经在使用解决方案

- 英文名：Existing Solution / Current Workaround
- 定义：用户已经在用 Excel、Notion、脚本、外包、多个工具、人工流程等方式解决问题。
- 本地数据量：10000 条，目标完成度：100.0%

**详细特征**
- 已经有替代行为，说明问题不是凭空想象。
- 当前方案越笨重，越适合先卖替代结果。
- 最关键数据是当前方案成本、缺陷和切换意愿。
- 强信号：用户愿意展示现有流程/截图/数据，并接受替代报价。
- 弱信号/误判：只是说“我也遇到过”，但没有当前解决方式。

**行为数据**
| 行为证据 | 命中数 |
| -- | -- |
| payment | 1053 |
| self_build | 940 |
| migration | 502 |
| workaround | 1389 |
| repetition | 572 |
| workflow | 1102 |
| sharing | 300 |
| growth | 243 |
| technology | 1795 |

**Anti-Pattern 数据**
| 负向信号 | 命中数 |
| -- | -- |
| no_budget | 751 |
| too_custom | 467 |
| low_value_attention | 423 |
| solved_by_incumbent | 95 |
| hard_to_switch | 2 |

**该 Signal 最常落入的问题簇**
| 问题簇 | 该 Signal 独立证据数 | 机会分 | 漏斗阶段 |
| -- | -- | -- | -- |
| Manual reporting and spreadsheet workflow automation | 1782 | 77.7 | Investigate with paid/customer discovery |
| Marketplace/service matching manual liquidity | 1652 | 83.2 | Worth 3-day experiment |
| AI coding agent reliability / code workflow | 1574 | 81.0 | Investigate with paid/customer discovery |
| Document/PDF/data extraction automation | 1546 | 79.3 | Investigate with paid/customer discovery |
| Creator/content repurposing and publishing workflow | 947 | 82.1 | Worth 3-day experiment |
| Education/learning/personal knowledge workflow | 715 | 82.1 | Worth 3-day experiment |
| Security, compliance, and audit evidence automation | 671 | 83.1 | Worth 3-day experiment |
| Sales/CRM/lead workflow automation | 592 | 82.3 | Worth 3-day experiment |

**具体案例 / 证据样本**
| 标题/案例 | 年份 | 分数 | 命中查询 | 证据摘录 | 来源 |
| -- | -- | -- | -- | -- | -- |
| Fuzzy Matching on Mac: Missing No More? | 2025 | 2 | workaround | Fuzzy Matching on Mac: Missing No More? ## Mac Users Got Left Out, Until Now For individuals utilizing Microsoft Excel on Mac systems, a significant limitation has persisted: the a | https://news.ycombinator.com/item?id=43367289 |
| Ask HN: Notion is withholding my company data, what can I do? | 2021 | 479 | Notion | Ask HN: Notion is withholding my company data, what can I do? I've been a paying customer from https://www.notion.so/ since 2017 with my company. In the early days, I even exchange | https://news.ycombinator.com/item?id=27612894 |
| Launch HN: BaseDash (YC S20) – Edit your database with the ease of a spreadsheet | 2020 | 191 | spreadsheet | Launch HN: BaseDash (YC S20) – Edit your database with the ease of a spreadsheet Hey everyone! I'm Max from BaseDash ( https://www.basedash.io ). BaseDash is an internal tool that  | https://news.ycombinator.com/item?id=23999124 |
| Show HN: Praxos – Webhooks for Your Life | 2025 | 7 | Google Sheets | Show HN: Praxos – Webhooks for Your Life Hello HN, Lucas and Soheil here from Praxos ( https://mypraxos.com/ )! We’ve been working on an AI personal assistant for a while now, and  | https://news.ycombinator.com/item?id=45542206 |
| Why Boring Businesses Outlast AI Hype Cycles | 2025 | 4 | manual workflow | Why Boring Businesses Outlast AI Hype Cycles Everyones building an AI company these days Every pitch deck leads with AIpowered every startup claims to be the next ChatGPT for X and | https://news.ycombinator.com/item?id=44848018 |
| Show HN: A spreadsheet tool that talks to your online store | 2023 | 2 | manual process | Show HN: A spreadsheet tool that talks to your online store Hey HN! I'm Tal, an engineer and founder of Mellow (https://www.playmellow.com) and I'm building a spreadsheet tool that | https://news.ycombinator.com/item?id=35245787 |

### Signal 02：重复劳动

- 英文名：Repetitive Work
- 定义：用户反复做同一件耗时任务，出现 daily/weekly/manually/takes hours 等行为描述。
- 本地数据量：10000 条，目标完成度：100.0%

**详细特征**
- 频率和耗时可以直接转化为 ROI。
- 高频但低价值不一定适合商业化，必须看错误成本/人工成本。
- 重复劳动常与工作流、预算、自建脚本共同出现。
- 强信号：用户能说出最近 5-10 次发生时间、每次耗时，并愿意付费代做一次。
- 弱信号/误判：只是一次性麻烦，或者频率高但用户不在乎结果质量。

**行为数据**
| 行为证据 | 命中数 |
| -- | -- |
| payment | 2055 |
| self_build | 1420 |
| migration | 776 |
| workaround | 1072 |
| repetition | 6342 |
| workflow | 2070 |
| sharing | 381 |
| growth | 650 |
| technology | 2776 |

**Anti-Pattern 数据**
| 负向信号 | 命中数 |
| -- | -- |
| no_budget | 1433 |
| too_custom | 639 |
| low_value_attention | 1153 |
| solved_by_incumbent | 133 |
| hard_to_switch | 4 |

**该 Signal 最常落入的问题簇**
| 问题簇 | 该 Signal 独立证据数 | 机会分 | 漏斗阶段 |
| -- | -- | -- | -- |
| AI coding agent reliability / code workflow | 2047 | 81.0 | Investigate with paid/customer discovery |
| Creator/content repurposing and publishing workflow | 1776 | 82.1 | Worth 3-day experiment |
| Education/learning/personal knowledge workflow | 1560 | 82.1 | Worth 3-day experiment |
| Document/PDF/data extraction automation | 1449 | 79.3 | Investigate with paid/customer discovery |
| Manual reporting and spreadsheet workflow automation | 1112 | 77.7 | Investigate with paid/customer discovery |
| Security, compliance, and audit evidence automation | 865 | 83.1 | Worth 3-day experiment |
| Sales/CRM/lead workflow automation | 763 | 82.3 | Worth 3-day experiment |
| Marketplace/service matching manual liquidity | 757 | 83.2 | Worth 3-day experiment |

**具体案例 / 证据样本**
| 标题/案例 | 年份 | 分数 | 命中查询 | 证据摘录 | 来源 |
| -- | -- | -- | -- | -- | -- |
| Why Your Customers Would Be Happier If You Charged More | 2012 |  | spreadsheet every day | Why Your Customers Would Be Happier If You Charged More The issue really is that you can't charge high rates to these people simply because they probably don't have that kind of mo | https://news.ycombinator.com/item?id=4554669 |
| Launch HN: HiGeorge (YC W21) – Real-time data visualizations for public datasets | 2021 | 89 | takes hours | Launch HN: HiGeorge (YC W21) – Real-time data visualizations for public datasets Hi HN! Anuj here. My co-founder Amir (Aazo11) and I are building HiGeorge ( https://hi-george.com/  | https://news.ycombinator.com/item?id=26194440 |
| Show HN: I built an open-source tool to make on-call suck less | 2024 | 319 | repetitive | Show HN: I built an open-source tool to make on-call suck less Hey HN, I am building an open source platform to make on-call better and less stressful for engineers. We are buildin | https://news.ycombinator.com/item?id=41086620 |
| My struggle with social marketing content creation turned into a business | 2025 | 2 | repetitive | My struggle with social marketing content creation turned into a business I run a couple of micro-SaaS businesses and, like any modern entrepreneur, I knew that being active on soc | https://news.ycombinator.com/item?id=43582801 |
| Ask HN: How do I get my PM to stop using Excel to track bugs? | 2021 |  | spreadsheet every day | Ask HN: How do I get my PM to stop using Excel to track bugs? i'm assuming you hate it just b/c it's ugly and therefore sucks. i just left a job that loved spreadsheets of all kind | https://news.ycombinator.com/item?id=28310722 |
| Show HN: Skyvern – Browser automation using LLMs and computer vision | 2024 | 422 | repetitive | Show HN: Skyvern – Browser automation using LLMs and computer vision Hey HN, we're building Skyvern ( https://www.skyvern.com ), an open-source tool that uses LLMs and computer vis | https://news.ycombinator.com/item?id=39706004 |

### Signal 03：自己造轮子

- 英文名：Self-Built Tool
- 定义：用户自己写脚本、插件、机器人、内部工具或临时自动化。
- 本地数据量：10000 条，目标完成度：100.0%

**详细特征**
- 自建工具说明用户已经付出时间成本。
- 多人独立造轮子比单个开源项目更重要。
- 开发者自建强，不代表业务买家会付费，需验证预算。
- 强信号：用户愿意迁移脚本、付费托管、购买维护或推荐同类用户。
- 弱信号/误判：只是爱折腾的技术项目，没有真实业务压力。

**行为数据**
| 行为证据 | 命中数 |
| -- | -- |
| payment | 1719 |
| self_build | 5690 |
| migration | 974 |
| workaround | 1177 |
| repetition | 1292 |
| workflow | 1867 |
| sharing | 477 |
| growth | 530 |
| technology | 3706 |

**Anti-Pattern 数据**
| 负向信号 | 命中数 |
| -- | -- |
| no_budget | 1640 |
| too_custom | 1397 |
| low_value_attention | 1559 |
| solved_by_incumbent | 270 |
| hard_to_switch | 13 |

**该 Signal 最常落入的问题簇**
| 问题簇 | 该 Signal 独立证据数 | 机会分 | 漏斗阶段 |
| -- | -- | -- | -- |
| AI coding agent reliability / code workflow | 3353 | 81.0 | Investigate with paid/customer discovery |
| Creator/content repurposing and publishing workflow | 2022 | 82.1 | Worth 3-day experiment |
| Education/learning/personal knowledge workflow | 1637 | 82.1 | Worth 3-day experiment |
| Document/PDF/data extraction automation | 1298 | 79.3 | Investigate with paid/customer discovery |
| Security, compliance, and audit evidence automation | 1193 | 83.1 | Worth 3-day experiment |
| Hardware/IoT/device configuration and fleet ops | 1108 | 77.1 | Investigate with paid/customer discovery |
| AI agent tool-call safety and permissions | 926 | 75.5 | Investigate with paid/customer discovery |
| Browser extension / cross-app workflow bridge | 813 | 72.0 | Investigate with paid/customer discovery |

**具体案例 / 证据样本**
| 标题/案例 | 年份 | 分数 | 命中查询 | 证据摘录 | 来源 |
| -- | -- | -- | -- | -- | -- |
| Launch HN: Requestly (YC W22) – Network debugging proxy for web and mobile | 2022 | 190 | I built a script | Launch HN: Requestly (YC W22) – Network debugging proxy for web and mobile Hi HN, My name is Sachin - I’m the founder of Requestly ( https://requestly.io ) and I’m very happy to be | https://news.ycombinator.com/item?id=30540735 |
| Strengthening JavaScript | 2015 |  | I wrote a Python script | Strengthening JavaScript First, you missed my point, which was clear enough from the context you cut: stagnation would have been a problem for any hypothetical Python circa version | https://news.ycombinator.com/item?id=9178765 |
| Ask HN: What is your one-person sideproject that makes over $1k/month? | 2015 |  | I created a bot | Ask HN: What is your one-person sideproject that makes over $1k/month? Improvely ( https://www.improvely.com ) and W3Counter ( https://www.w3counter.com ) both started as side proj | https://news.ycombinator.com/item?id=9423592 |
| Show HN: Xata, serverless database on top of PostgreSQL and Elasticsearch | 2022 | 47 | hacked together | Show HN: Xata, serverless database on top of PostgreSQL and Elasticsearch Hi! Xata was on HackerNews once before ( https://news.ycombinator.com/item?id=28590816 ) a bit over a year | https://news.ycombinator.com/item?id=33432425 |
| Ask HN: Is there any decent API to download a paper given its name? | 2022 | 18 | I wrote a Python script | Ask HN: Is there any decent API to download a paper given its name? I am developing a PDF viewer designed for reading research papers[1]. One very useful feature that I would like  | https://news.ycombinator.com/item?id=32724895 |
| Show HN: I built a Bitcoin DCA bot – here's why | 2025 | 6 | I built a script | Show HN: I built a Bitcoin DCA bot – here's why I started DCA’ing into BTC many years ago. I kept missing buys, buying emotionally into pumps, and forgetting during chop. So I wrot | https://news.ycombinator.com/item?id=45221852 |

### Signal 04：半成品市场

- 英文名：Semi-Finished Market
- 定义：GitHub、Chrome Extension、模板、插件、小 SaaS、开源工具反复出现。
- 本地数据量：10000 条，目标完成度：100.0%

**详细特征**
- 半成品密度高说明市场自发探索需求。
- 模板/插件/脚本是产品化前的需求影子。
- 要从单个项目转为问题簇，统计独立作者和相似功能。
- 强信号：多个独立半成品解决同一工作流，且用户要求稳定性/支持/托管。
- 弱信号/误判：开源项目很多但没有用户、付费、迁移和复用。

**行为数据**
| 行为证据 | 命中数 |
| -- | -- |
| payment | 986 |
| self_build | 2467 |
| migration | 1335 |
| workaround | 475 |
| repetition | 520 |
| workflow | 1205 |
| sharing | 811 |
| growth | 238 |
| technology | 1863 |

**Anti-Pattern 数据**
| 负向信号 | 命中数 |
| -- | -- |
| no_budget | 913 |
| too_custom | 521 |
| low_value_attention | 545 |
| solved_by_incumbent | 111 |
| hard_to_switch | 10 |

**该 Signal 最常落入的问题簇**
| 问题簇 | 该 Signal 独立证据数 | 机会分 | 漏斗阶段 |
| -- | -- | -- | -- |
| AI coding agent reliability / code workflow | 3825 | 81.0 | Investigate with paid/customer discovery |
| Browser extension / cross-app workflow bridge | 1834 | 72.0 | Investigate with paid/customer discovery |
| Templates/plugins as workflow proto-products | 1258 | 71.4 | Keep in watchlist / needs more commercial evidence |
| Creator/content repurposing and publishing workflow | 1031 | 82.1 | Worth 3-day experiment |
| Document/PDF/data extraction automation | 1019 | 79.3 | Investigate with paid/customer discovery |
| SaaS migration/export/import pain | 879 | 76.8 | Investigate with paid/customer discovery |
| Marketplace/service matching manual liquidity | 869 | 83.2 | Worth 3-day experiment |
| Education/learning/personal knowledge workflow | 769 | 82.1 | Worth 3-day experiment |

**具体案例 / 证据样本**
| 标题/案例 | 年份 | 分数 | 命中查询 | 证据摘录 | 来源 |
| -- | -- | -- | -- | -- | -- |
| Launch HN: Dendron (YC W21) – Structured note-taking for developers and teams | 2021 | 206 | Notion template | Launch HN: Dendron (YC W21) – Structured note-taking for developers and teams Hi HN, I'm Kevin, the founder of Dendron ( https://www.dendron.so ). Dendron is a local, open-source,  | https://news.ycombinator.com/item?id=29176158 |
| Show HN: Restfox – Open source lightweight alternative to Postman | 2022 | 758 | open source alternative | Show HN: Restfox – Open source lightweight alternative to Postman Last time I posted this it didn't garner much interest. There have been lots of improvements and fixes since the l | https://news.ycombinator.com/item?id=33287137 |
| Show HN: Seren Desktop – AI IDE with Publisher Store and X402 Micropayments | 2026 | 2 | Notion template | Show HN: Seren Desktop – AI IDE with Publisher Store and X402 Micropayments What makes Seren different: We're trying to build an AI IDE for non-devs, but that great devs will appre | https://news.ycombinator.com/item?id=46799839 |
| Show HN: My cookiecutter template for Python projects used at deepsense.ai | 2023 | 2 | Python package | Show HN: My cookiecutter template for Python projects used at deepsense.ai Hey, wanted to share cookiecutter template used at deepsense.ai made by me - which got open sourced recen | https://news.ycombinator.com/item?id=37673085 |
| Show HN: CodeTrackr – open-source WakaTime alternative with real-time stats | 2026 | 2 | open source alternative | Show HN: CodeTrackr – open-source WakaTime alternative with real-time stats Hi HN! I built CodeTrackr, an open-source, privacy-first alternative to WakaTime. It tracks coding activ | https://news.ycombinator.com/item?id=47282990 |
| Show HN: I'm building a platform to manage larger projects with AI agents | 2026 | 1 | plugin marketplace | Show HN: I'm building a platform to manage larger projects with AI agents I started building Frame as a terminal-first, lightweight IDE and open sourced it. Now I'm pushing it towa | https://news.ycombinator.com/item?id=47206398 |

### Signal 05：已经花钱但非常不满意

- 英文名：Existing Money + Dissatisfaction
- 定义：用户已经付费，但抱怨 expensive/overpriced/pricing/vendor lock-in。
- 本地数据量：10000 条，目标完成度：100.0%

**详细特征**
- 已有钱流是最强商业信号之一。
- 不满原因要拆成价格、功能、服务、锁定、实施成本。
- 现有价格可以直接作为测试报价锚点。
- 强信号：用户愿意分享账单、预算范围、供应商问题，并进入采购下一步。
- 弱信号/误判：只抱怨贵，但没有购买权或没有替代意愿。

**行为数据**
| 行为证据 | 命中数 |
| -- | -- |
| payment | 6257 |
| self_build | 639 |
| migration | 620 |
| workaround | 291 |
| repetition | 507 |
| workflow | 1131 |
| sharing | 160 |
| growth | 413 |
| technology | 1793 |

**Anti-Pattern 数据**
| 负向信号 | 命中数 |
| -- | -- |
| no_budget | 1219 |
| too_custom | 380 |
| low_value_attention | 584 |
| solved_by_incumbent | 80 |
| hard_to_switch | 48 |

**该 Signal 最常落入的问题簇**
| 问题簇 | 该 Signal 独立证据数 | 机会分 | 漏斗阶段 |
| -- | -- | -- | -- |
| Creator/content repurposing and publishing workflow | 1136 | 82.1 | Worth 3-day experiment |
| AI coding agent reliability / code workflow | 1114 | 81.0 | Investigate with paid/customer discovery |
| Billing, invoicing, accounting, and reconciliation | 948 | 84.3 | Worth 3-day experiment |
| Education/learning/personal knowledge workflow | 918 | 82.1 | Worth 3-day experiment |
| Security, compliance, and audit evidence automation | 774 | 83.1 | Worth 3-day experiment |
| Marketplace/service matching manual liquidity | 721 | 83.2 | Worth 3-day experiment |
| Legal/document/compliance drafting workflow | 695 | 85.2 | Worth 3-day experiment |
| SaaS migration/export/import pain | 626 | 76.8 | Investigate with paid/customer discovery |

**具体案例 / 证据样本**
| 标题/案例 | 年份 | 分数 | 命中查询 | 证据摘录 | 来源 |
| -- | -- | -- | -- | -- | -- |
| Launch HN: Lago (YC S21) – Open-source usage-based billing | 2023 | 442 | billing issue | Launch HN: Lago (YC S21) – Open-source usage-based billing Hi HN, we’re the cofounders of Lago: an open-source alternative to Stripe Billing, Chargebee, and Recurly. That is, we ma | https://news.ycombinator.com/item?id=34773442 |
| Thanks HN: You helped save a company that now helps thousands make a living | 2021 | 1364 | paying for | Thanks HN: You helped save a company that now helps thousands make a living Dear HN, I’m feeling a deep sense of gratitude this morning, and wanted to share it with you all. On thi | https://news.ycombinator.com/item?id=25792719 |
| MixPanel (YC S09); my mini review | 2009 | 38 | overpriced | MixPanel (YC S09); my mini review After spotting the mixpanel logo at the bottom of HN I decided to give it a spin on a reasonably serious site to see what it can do. I've got some | https://news.ycombinator.com/item?id=942053 |
| Tell HN: I probably spend more on piracy than if I just paid for content | 2022 | 302 | I pay | Tell HN: I probably spend more on piracy than if I just paid for content I have a confession, I pirate a lot of content. Mostly TV/Movies. That being said, piracy is pretty expensi | https://news.ycombinator.com/item?id=31409664 |
| Peer to Peer – Hone your skills by watching live coding videos | 2015 |  | overpriced | Peer to Peer – Hone your skills by watching live coding videos The pricing feels really high. $9 per 60 minutes of content is a similar price as watching to a $200 million dollar h | https://news.ycombinator.com/item?id=8861804 |
| Show HN: I replaced a $120k bowling center system with $1,600 in ESP32s | 2026 | 2935 | costs me | Show HN: I replaced a $120k bowling center system with $1,600 in ESP32s I might be the only SRE on Earth with his own bowling center. It's a more in-depth gig than you'd think. My  | https://news.ycombinator.com/item?id=48968606 |

### Signal 06：用户正在迁移

- 英文名：Migration / Switching
- 定义：用户主动寻找 alternative、switch、migrate、replace 或导出数据。
- 本地数据量：10000 条，目标完成度：100.0%

**详细特征**
- 迁移行为强于差评，因为用户愿意承担切换成本。
- 迁移痛点本身可能成为机会。
- 要识别从哪个工具迁到哪个工具、为什么离开。
- 强信号：用户已经导出数据、寻找替代、安排迁移或取消订阅。
- 弱信号/误判：只是问 alternative，但没有实际切换成本承受意愿。

**行为数据**
| 行为证据 | 命中数 |
| -- | -- |
| payment | 1044 |
| self_build | 557 |
| migration | 5102 |
| workaround | 990 |
| repetition | 375 |
| workflow | 613 |
| sharing | 176 |
| growth | 283 |
| technology | 1337 |

**Anti-Pattern 数据**
| 负向信号 | 命中数 |
| -- | -- |
| no_budget | 708 |
| too_custom | 312 |
| low_value_attention | 472 |
| solved_by_incumbent | 79 |
| hard_to_switch | 14 |

**该 Signal 最常落入的问题簇**
| 问题簇 | 该 Signal 独立证据数 | 机会分 | 漏斗阶段 |
| -- | -- | -- | -- |
| SaaS migration/export/import pain | 3573 | 76.8 | Investigate with paid/customer discovery |
| AI coding agent reliability / code workflow | 1862 | 81.0 | Investigate with paid/customer discovery |
| Open-source alternative to expensive SaaS | 985 | 70.8 | Keep in watchlist / needs more commercial evidence |
| Creator/content repurposing and publishing workflow | 804 | 82.1 | Worth 3-day experiment |
| Education/learning/personal knowledge workflow | 618 | 82.1 | Worth 3-day experiment |
| Security, compliance, and audit evidence automation | 579 | 83.1 | Worth 3-day experiment |
| Document/PDF/data extraction automation | 561 | 79.3 | Investigate with paid/customer discovery |
| Hardware/IoT/device configuration and fleet ops | 401 | 77.1 | Investigate with paid/customer discovery |

**具体案例 / 证据样本**
| 标题/案例 | 年份 | 分数 | 命中查询 | 证据摘录 | 来源 |
| -- | -- | -- | -- | -- | -- |
| Launch HN: Jitsu (YC S20) – Open-Source Segment Alternative | 2021 | 265 | alternative | Launch HN: Jitsu (YC S20) – Open-Source Segment Alternative Hey HN! Vlad here with Sergey, Ildar, and Kirill. We are building Jitsu, an open-source Segment alternative ( https://gi | https://news.ycombinator.com/item?id=29106082 |
| Google App Engine PHP Runtime now available to everyone | 2013 |  | migration path | Google App Engine PHP Runtime now available to everyone They've shut down much more than Reader (seriously, who said anything about Reader? was that even a service a developer coul | https://news.ycombinator.com/item?id=6517626 |
| Open source fork CIB seven now available as an alternative to Camunda 7 | 2024 |  | migration path | Open source fork CIB seven now available as an alternative to Camunda 7 The Munich-based software company CIB, which specializes in process automation, has delivered: Users of the  | https://news.ycombinator.com/item?id=42428890 |
| Show HN: HyperDX – open-source dev-friendly Datadog alternative | 2023 | 722 | alternative | Show HN: HyperDX – open-source dev-friendly Datadog alternative Hi HN, Mike and Warren here! We've been building HyperDX (hyperdx.io). HyperDX allows you to easily search and corre | https://news.ycombinator.com/item?id=37558357 |
| Alternatives to Notion for those on corporate VPN | 2020 | 3 | import from | Alternatives to Notion for those on corporate VPN I've been using Notion for a more than a year now, and I love the following features: * slash commands * export/import to/from mar | https://news.ycombinator.com/item?id=25126440 |
| Stripe closed our account and refuses to migrate our data to another processor | 2024 | 81 | export data | Stripe closed our account and refuses to migrate our data to another processor I'm reaching out to the official Stripe support forum here because our account has been closed and St | https://news.ycombinator.com/item?id=40529033 |

### Signal 07：现有预算

- 英文名：Existing Budget
- 定义：已有 hiring、contractor、agency、vendor、subscription、procurement 等预算来源。
- 本地数据量：10000 条，目标完成度：100.0%

**详细特征**
- 预算来源可以是软件费、工资、外包费、招聘、设备或损失成本。
- 有预算不等于能成交，仍需找到 budget owner。
- 预算型 signal 适合冷邮件和报价实验。
- 强信号：明确预算 owner、现有供应商/合同/外包/招聘支出。
- 弱信号/误判：用户有需求但预算在别的部门，或只是个人免费需求。

**行为数据**
| 行为证据 | 命中数 |
| -- | -- |
| payment | 2597 |
| self_build | 234 |
| migration | 322 |
| workaround | 195 |
| repetition | 248 |
| workflow | 948 |
| sharing | 132 |
| growth | 274 |
| technology | 935 |

**Anti-Pattern 数据**
| 负向信号 | 命中数 |
| -- | -- |
| no_budget | 667 |
| too_custom | 167 |
| low_value_attention | 309 |
| solved_by_incumbent | 40 |
| hard_to_switch | 13 |

**该 Signal 最常落入的问题簇**
| 问题簇 | 该 Signal 独立证据数 | 机会分 | 漏斗阶段 |
| -- | -- | -- | -- |
| Marketplace/service matching manual liquidity | 2404 | 83.2 | Worth 3-day experiment |
| Recruiting/hiring screening workflow | 1380 | 83.0 | Worth 3-day experiment |
| Procurement/vendor/RFP workflow | 1293 | 80.0 | Investigate with paid/customer discovery |
| Legal/document/compliance drafting workflow | 879 | 85.2 | Worth 3-day experiment |
| Security, compliance, and audit evidence automation | 792 | 83.1 | Worth 3-day experiment |
| Sales/CRM/lead workflow automation | 753 | 82.3 | Worth 3-day experiment |
| AI coding agent reliability / code workflow | 747 | 81.0 | Investigate with paid/customer discovery |
| Creator/content repurposing and publishing workflow | 658 | 82.1 | Worth 3-day experiment |

**具体案例 / 证据样本**
| 标题/案例 | 年份 | 分数 | 命中查询 | 证据摘录 | 来源 |
| -- | -- | -- | -- | -- | -- |
| We paid $634 million for the Obamacare sites and all we got was this lousy 404 | 2013 |  | procurement | We paid $634 million for the Obamacare sites and all we got was this lousy 404 There are two things which need to change: the first is that the government needs to hire more techni | https://news.ycombinator.com/item?id=6526761 |
| Ask HN: Why isn't there an Amazon for skilled 1099 contractors? | 2022 | 2 | contractor | Ask HN: Why isn't there an Amazon for skilled 1099 contractors? By 'Amazon', I mean- an online platform where hiring companies and contractors list themselves, and can find each ot | https://news.ycombinator.com/item?id=30713537 |
| Ask HN: Can all-owner firms avoid labor law complexity FTW? | 2023 | 4 | budget for | Ask HN: Can all-owner firms avoid labor law complexity FTW? I understand that labor laws are intended to protect workers and create a positive and healthy environment for everyone  | https://news.ycombinator.com/item?id=38511213 |
| Ask HN: How to move beyond “freelancer”? | 2015 | 322 | freelancer | Ask HN: How to move beyond “freelancer”? I've been doing freelance web development for the past 7 years. I have consistent work and "OK" pay. I've experimented with my rates over t | https://news.ycombinator.com/item?id=9289500 |
| Sinkhole of bureaucracy | 2014 |  | procurement | Sinkhole of bureaucracy I'm painfully familiar with some of this. My favorite example of just how dysfunctional it all is was an agency which made a small fuss about how they were  | https://news.ycombinator.com/item?id=7454082 |
| RFPs Will Kill Us All | 2009 |  | RFP | RFPs Will Kill Us All I've done some work for a Federal government agency a few years back and a provincial government within the past year. eHealth was exceptional not because of  | https://news.ycombinator.com/item?id=906429 |

### Signal 08：异常贵

- 英文名：Abnormally Expensive
- 定义：价格、API 成本、云账单、企业软件、咨询/外包费异常高。
- 本地数据量：10000 条，目标完成度：100.0%

**详细特征**
- 异常贵通常代表高价值、高复杂度或垄断。
- 高价 + 强不满 + 替代搜索是优先级组合。
- 要小心高价来自交付/合规复杂度，低价替代不一定可行。
- 强信号：用户提供账单，并愿意按节省金额或替代价格试点。
- 弱信号/误判：价格高但用户满意，或高价由不可绕过的合规/服务成本决定。

**行为数据**
| 行为证据 | 命中数 |
| -- | -- |
| payment | 8158 |
| self_build | 553 |
| migration | 985 |
| workaround | 387 |
| repetition | 546 |
| workflow | 1565 |
| sharing | 237 |
| growth | 808 |
| technology | 3304 |

**Anti-Pattern 数据**
| 负向信号 | 命中数 |
| -- | -- |
| no_budget | 1479 |
| too_custom | 634 |
| low_value_attention | 956 |
| solved_by_incumbent | 142 |
| hard_to_switch | 27 |

**该 Signal 最常落入的问题簇**
| 问题簇 | 该 Signal 独立证据数 | 机会分 | 漏斗阶段 |
| -- | -- | -- | -- |
| Hardware/IoT/device configuration and fleet ops | 1547 | 77.1 | Investigate with paid/customer discovery |
| Marketplace/service matching manual liquidity | 1423 | 83.2 | Worth 3-day experiment |
| Education/learning/personal knowledge workflow | 1302 | 82.1 | Worth 3-day experiment |
| Security, compliance, and audit evidence automation | 1287 | 83.1 | Worth 3-day experiment |
| Creator/content repurposing and publishing workflow | 1276 | 82.1 | Worth 3-day experiment |
| AI coding agent reliability / code workflow | 1137 | 81.0 | Investigate with paid/customer discovery |
| Billing, invoicing, accounting, and reconciliation | 1109 | 84.3 | Worth 3-day experiment |
| Legal/document/compliance drafting workflow | 1069 | 85.2 | Worth 3-day experiment |

**具体案例 / 证据样本**
| 标题/案例 | 年份 | 分数 | 命中查询 | 证据摘录 | 来源 |
| -- | -- | -- | -- | -- | -- |
| Launch HN: Didit (YC W26) – Stripe for Identity Verification | 2026 | 77 | high API cost | Launch HN: Didit (YC W26) – Stripe for Identity Verification Hi HN, I’m Alberto. I co-founded Didit ( https://didit.me ) with my identical twin brother Alejandro. We are building a | https://news.ycombinator.com/item?id=47324296 |
| Launch HN: Skope (YC S25) – Outcome-based pricing for software products | 2025 | 55 | high API cost | Launch HN: Skope (YC S25) – Outcome-based pricing for software products Hi HN, we’re Ben and Connor, the co-founders of Skope ( https://www.useskope.com/ ), a billing system that s | https://news.ycombinator.com/item?id=44973758 |
| Show HN: Tracecat – Open-source security alert automation / SOAR alternative | 2024 | 264 | high API cost | Show HN: Tracecat – Open-source security alert automation / SOAR alternative Hi HN, we are building Tracecat ( https://tracecat.com/ ), an open source automation platform for secur | https://news.ycombinator.com/item?id=39819458 |
| Show HN: HyperDX – open-source dev-friendly Datadog alternative | 2023 | 722 | high API cost | Show HN: HyperDX – open-source dev-friendly Datadog alternative Hi HN, Mike and Warren here! We've been building HyperDX (hyperdx.io). HyperDX allows you to easily search and corre | https://news.ycombinator.com/item?id=37558357 |
| Building an AI cost-optimizer and AI Slop Prevention tool Looking for feedback." | 2025 | 1 | agency cost | Building an AI cost-optimizer and AI Slop Prevention tool Looking for feedback." Hey — Looking for feedback on my AI cost-optimization + “AI Slop Prevention” tool I'm Zach, and I’v | https://news.ycombinator.com/item?id=46240030 |
| Show HN: LinkBin – Modern URL shortener with analytics ($15 vs. bit.ly's $35) | 2026 | 1 | enterprise pricing | Show HN: LinkBin – Modern URL shortener with analytics ($15 vs. bit.ly's $35) I built LinkBin after getting frustrated with bit.ly's pricing and outdated UX. It's a modern URL shor | https://news.ycombinator.com/item?id=46803857 |

### Signal 09：行业黑话 / 工作流

- 英文名：Industry Jargon / Workflow
- 定义：出现 workflow、process、SOP、claims、billing、procurement、audit 等具体流程语言。
- 本地数据量：10000 条，目标完成度：100.0%

**详细特征**
- 行业黑话帮助定位真实角色和流程。
- 它不是需求本身，而是绘制 Workflow Map 的入口。
- 越能抽出步骤和责任人，越适合小切口实验。
- 强信号：能还原 Who -> When -> Workflow -> Step -> Pain -> Current Solution。
- 弱信号/误判：只有行业词堆砌，没有具体行为、成本和替代方案。

**行为数据**
| 行为证据 | 命中数 |
| -- | -- |
| payment | 679 |
| self_build | 325 |
| migration | 222 |
| workaround | 244 |
| repetition | 229 |
| workflow | 4132 |
| sharing | 187 |
| growth | 133 |
| technology | 1321 |

**Anti-Pattern 数据**
| 负向信号 | 命中数 |
| -- | -- |
| no_budget | 398 |
| too_custom | 223 |
| low_value_attention | 195 |
| solved_by_incumbent | 34 |
| hard_to_switch | 4 |

**该 Signal 最常落入的问题簇**
| 问题簇 | 该 Signal 独立证据数 | 机会分 | 漏斗阶段 |
| -- | -- | -- | -- |
| AI coding agent reliability / code workflow | 1737 | 81.0 | Investigate with paid/customer discovery |
| Security, compliance, and audit evidence automation | 1200 | 83.1 | Worth 3-day experiment |
| Billing, invoicing, accounting, and reconciliation | 897 | 84.3 | Worth 3-day experiment |
| Manufacturing/industrial QA and supply chain | 896 | 78.8 | Investigate with paid/customer discovery |
| Observability/incident monitoring and debugging | 852 | 76.8 | Investigate with paid/customer discovery |
| Creator/content repurposing and publishing workflow | 620 | 82.1 | Worth 3-day experiment |
| Insurance claims and underwriting operations | 531 | 80.9 | Investigate with paid/customer discovery |
| Sales/CRM/lead workflow automation | 498 | 82.3 | Worth 3-day experiment |

**具体案例 / 证据样本**
| 标题/案例 | 年份 | 分数 | 命中查询 | 证据摘录 | 来源 |
| -- | -- | -- | -- | -- | -- |
| Show HN: Skyvern – Browser automation using LLMs and computer vision | 2024 | 422 | procurement | Show HN: Skyvern – Browser automation using LLMs and computer vision Hey HN, we're building Skyvern ( https://www.skyvern.com ), an open-source tool that uses LLMs and computer vis | https://news.ycombinator.com/item?id=39706004 |
| AI Agents That Execute Business Workflows (Claude Code for ERP) | 2026 | 4 | procurement | AI Agents That Execute Business Workflows (Claude Code for ERP) TL;DR: Built an ERP where AI agents execute workflows like procurement and invoice processing. Uses Cases (workspace | https://news.ycombinator.com/item?id=46955034 |
| Launch HN: Trellis (YC W24) – AI-powered workflows for unstructured data | 2024 | 234 | workflow | Launch HN: Trellis (YC W24) – AI-powered workflows for unstructured data Hey HN — We're Jacky and Mac from Trellis ( https://runtrellis.com/ ). We’re building AI-powered ETL for un | https://news.ycombinator.com/item?id=41236273 |
| Show HN: Tracecat – Open-source security alert automation / SOAR alternative | 2024 | 264 | incident response | Show HN: Tracecat – Open-source security alert automation / SOAR alternative Hi HN, we are building Tracecat ( https://tracecat.com/ ), an open source automation platform for secur | https://news.ycombinator.com/item?id=39819458 |
| Show HN: Fix – An open source cloud asset inventory for cloud security engineers | 2024 | 23 | procurement | Show HN: Fix – An open source cloud asset inventory for cloud security engineers Hi, we’re Lukas, Lars and Matthias, and we're building “Fix” ( https://fix.security ). Fix is an op | https://news.ycombinator.com/item?id=39842792 |
| Launch HN: Lago (YC S21) – Open-source usage-based billing | 2023 | 442 | billing | Launch HN: Lago (YC S21) – Open-source usage-based billing Hi HN, we’re the cofounders of Lago: an open-source alternative to Stripe Billing, Chargebee, and Recurly. That is, we ma | https://news.ycombinator.com/item?id=34773442 |

### Signal 10：新技术带来的新问题

- 英文名：New Technology New Problem
- 定义：AI、LLM、Agent、新 API、新法规、新平台带来新行为和新问题。
- 本地数据量：10000 条，目标完成度：100.0%

**详细特征**
- 新技术应该解释 Why Now，而不是替代需求。
- 重点找新行为带来的新问题，例如 agent 权限、LLM eval、推理成本。
- AI 机会需要验证输出可验收和交付成本。
- 强信号：新技术已导致真实预算、人工处理、风险责任或迁移行为。
- 弱信号/误判：只是“可以用 AI 做”，没有用户现有痛点。

**行为数据**
| 行为证据 | 命中数 |
| -- | -- |
| payment | 624 |
| self_build | 803 |
| migration | 288 |
| workaround | 290 |
| repetition | 339 |
| workflow | 789 |
| sharing | 195 |
| growth | 140 |
| technology | 7603 |

**Anti-Pattern 数据**
| 负向信号 | 命中数 |
| -- | -- |
| no_budget | 510 |
| too_custom | 385 |
| low_value_attention | 379 |
| solved_by_incumbent | 75 |
| hard_to_switch | 1 |

**该 Signal 最常落入的问题簇**
| 问题簇 | 该 Signal 独立证据数 | 机会分 | 漏斗阶段 |
| -- | -- | -- | -- |
| AI coding agent reliability / code workflow | 3464 | 81.0 | Investigate with paid/customer discovery |
| AI agent tool-call safety and permissions | 2625 | 75.5 | Investigate with paid/customer discovery |
| AI evaluation/model monitoring/prompt management | 1471 | 75.3 | Investigate with paid/customer discovery |
| Creator/content repurposing and publishing workflow | 886 | 82.1 | Worth 3-day experiment |
| Security, compliance, and audit evidence automation | 702 | 83.1 | Worth 3-day experiment |
| Document/PDF/data extraction automation | 487 | 79.3 | Investigate with paid/customer discovery |
| Education/learning/personal knowledge workflow | 484 | 82.1 | Worth 3-day experiment |
| Privacy/data governance/synthetic data | 411 | 77.2 | Investigate with paid/customer discovery |

**具体案例 / 证据样本**
| 标题/案例 | 年份 | 分数 | 命中查询 | 证据摘录 | 来源 |
| -- | -- | -- | -- | -- | -- |
| Launch HN: Cyberdesk (YC S25) – Automate Windows legacy desktop apps | 2025 | 73 | computer use | Launch HN: Cyberdesk (YC S25) – Automate Windows legacy desktop apps Hi HN, We’re Mahmoud and Alan, building Cyberdesk ( https://www.cyberdesk.io/ ), a deterministic computer use a | https://news.ycombinator.com/item?id=44901528 |
| Launch HN: Trellis (YC W24) – AI-powered workflows for unstructured data | 2024 | 234 | AI workflow | Launch HN: Trellis (YC W24) – AI-powered workflows for unstructured data Hey HN — We're Jacky and Mac from Trellis ( https://runtrellis.com/ ). We’re building AI-powered ETL for un | https://news.ycombinator.com/item?id=41236273 |
| Launch HN: Cekura (YC F24) – Testing and monitoring for voice and chat AI agents | 2026 | 89 | AI agent | Launch HN: Cekura (YC F24) – Testing and monitoring for voice and chat AI agents Hey HN - we're Tarush, Sidhant, and Shashij from Cekura ( https://www.cekura.ai ). We've been runni | https://news.ycombinator.com/item?id=47232903 |
| Launch HN: Chonkie (YC X25) – Open-Source Library for Advanced Chunking | 2025 | 151 | vector database | Launch HN: Chonkie (YC X25) – Open-Source Library for Advanced Chunking Hey HN! We're Shreyash and Bhavnick. We're building Chonkie ( https://chonkie.ai ), an open-source library f | https://news.ycombinator.com/item?id=44225930 |
| Launch HN: Screenpipe (YC S26) – Record how you work and turn that into agents | 2026 | 88 | agents | Launch HN: Screenpipe (YC S26) – Record how you work and turn that into agents Hi Hacker News, I'm Louis. I built Screenpipe ( https://screenpipe.com ), an app that records your sc | https://news.ycombinator.com/item?id=49024620 |
| Show HN: HoneyHive – An unified evaluation and monitoring platform for LLM apps | 2023 | 3 | vector database | Show HN: HoneyHive – An unified evaluation and monitoring platform for LLM apps Hey HN! We’re Mohak and Dhruv from HoneyHive (https://honeyhive.ai). HoneyHive is a set of tools bui | https://news.ycombinator.com/item?id=37777683 |

### Signal 11：绕过现有系统

- 英文名：System Failure / Bypass
- 定义：用户通过 hack、export/import、copy paste、scraping、bridge tools 绕过系统限制。
- 本地数据量：10000 条，目标完成度：100.0%

**详细特征**
- 绕过系统说明原产品边界失败。
- 导入导出、复制粘贴、爬取、跨工具桥接常是好切口。
- 系统失败 signal 常适合先做人工集成服务。
- 强信号：用户愿意给账号/数据/权限，让你代做桥接或迁移。
- 弱信号/误判：workaround 很轻、一次性，或平台即将原生解决。

**行为数据**
| 行为证据 | 命中数 |
| -- | -- |
| payment | 1253 |
| self_build | 1464 |
| migration | 734 |
| workaround | 3426 |
| repetition | 618 |
| workflow | 1129 |
| sharing | 328 |
| growth | 292 |
| technology | 2900 |

**Anti-Pattern 数据**
| 负向信号 | 命中数 |
| -- | -- |
| no_budget | 921 |
| too_custom | 635 |
| low_value_attention | 751 |
| solved_by_incumbent | 180 |
| hard_to_switch | 15 |

**该 Signal 最常落入的问题簇**
| 问题簇 | 该 Signal 独立证据数 | 机会分 | 漏斗阶段 |
| -- | -- | -- | -- |
| AI coding agent reliability / code workflow | 2348 | 81.0 | Investigate with paid/customer discovery |
| Creator/content repurposing and publishing workflow | 1286 | 82.1 | Worth 3-day experiment |
| Security, compliance, and audit evidence automation | 1098 | 83.1 | Worth 3-day experiment |
| SaaS migration/export/import pain | 1094 | 76.8 | Investigate with paid/customer discovery |
| Document/PDF/data extraction automation | 1014 | 79.3 | Investigate with paid/customer discovery |
| Education/learning/personal knowledge workflow | 1005 | 82.1 | Worth 3-day experiment |
| Browser extension / cross-app workflow bridge | 932 | 72.0 | Investigate with paid/customer discovery |
| Hardware/IoT/device configuration and fleet ops | 890 | 77.1 | Investigate with paid/customer discovery |

**具体案例 / 证据样本**
| 标题/案例 | 年份 | 分数 | 命中查询 | 证据摘录 | 来源 |
| -- | -- | -- | -- | -- | -- |
| Show HN: Ditch your budget app subscription. Surebeans is a modern YNAB4 | 2026 | 2 | workaround | Show HN: Ditch your budget app subscription. Surebeans is a modern YNAB4 If you liked YNAB4 (YNAB's abandoned desktop app) or have subscription fatigue, try Surebeans. It's like a  | https://news.ycombinator.com/item?id=47196050 |
| Show HN: ScrapeCopilot – Notebook Code Interface + Puppeteer + AI Copilot | 2025 | 3 | copy paste | Show HN: ScrapeCopilot – Notebook Code Interface + Puppeteer + AI Copilot Hi HN, I’m Eric, and I’m building ScrapeCopilot, an AI assistant designed to eliminate friction in browser | https://news.ycombinator.com/item?id=44072704 |
| Student-Built Apps Teach Colleges a Thing or Two | 2014 |  | no API | Student-Built Apps Teach Colleges a Thing or Two I actually had a lot of luck creating such a timetable website[0] for NTNU in Trondheim, Norway. Initial version did hacky scraping | https://news.ycombinator.com/item?id=8236714 |
| I rescued 42 ChatGPT conversations from digital lock-in (technical guide) | 2025 | 3 | copy paste | I rescued 42 ChatGPT conversations from digital lock-in (technical guide) # I Rescued 42 ChatGPT Conversations from Digital Lock-in ## The Problem ChatGPT Teams has *no bulk export | https://news.ycombinator.com/item?id=45033237 |
| Ask HN: What are your “brain hacks” that help you manage everyday situations? | 2018 | 1322 | hack | Ask HN: What are your “brain hacks” that help you manage everyday situations? I'm incredibly fortunate to have a chairman on our board who brings so much clarity of thought to the  | https://news.ycombinator.com/item?id=18588727 |
| Show HN: nextflick.tv – watch random movie trailers | 2025 | 4 | workaround | Show HN: nextflick.tv – watch random movie trailers I wanted to have a fun way of discovering movies to watch. I always thought the experience of watching a bunch of trailers, like | https://news.ycombinator.com/item?id=43100796 |

### Signal 12：用户互相传播 workaround

- 英文名：Workaround Sharing
- 定义：用户发布 guide、tutorial、template、snippet、try this、works for me。
- 本地数据量：10000 条，目标完成度：100.0%

**详细特征**
- 用户互相传播 workaround 说明解决路径已经自发扩散。
- 独立推荐人数比总转发量重要。
- 传播型 workaround 可用于发现社区和获客渠道。
- 强信号：多个独立社区反复推荐同一 workaround，且采纳者继续追问更稳定方案。
- 弱信号/误判：只是教程热度，没有付款、频率或业务压力。

**行为数据**
| 行为证据 | 命中数 |
| -- | -- |
| payment | 761 |
| self_build | 765 |
| migration | 421 |
| workaround | 317 |
| repetition | 476 |
| workflow | 1001 |
| sharing | 3223 |
| growth | 190 |
| technology | 1420 |

**Anti-Pattern 数据**
| 负向信号 | 命中数 |
| -- | -- |
| no_budget | 851 |
| too_custom | 356 |
| low_value_attention | 609 |
| solved_by_incumbent | 76 |
| hard_to_switch | 6 |

**该 Signal 最常落入的问题簇**
| 问题簇 | 该 Signal 独立证据数 | 机会分 | 漏斗阶段 |
| -- | -- | -- | -- |
| AI coding agent reliability / code workflow | 2372 | 81.0 | Investigate with paid/customer discovery |
| Creator/content repurposing and publishing workflow | 1016 | 82.1 | Worth 3-day experiment |
| Education/learning/personal knowledge workflow | 946 | 82.1 | Worth 3-day experiment |
| Templates/plugins as workflow proto-products | 710 | 71.4 | Keep in watchlist / needs more commercial evidence |
| Document/PDF/data extraction automation | 558 | 79.3 | Investigate with paid/customer discovery |
| Security, compliance, and audit evidence automation | 454 | 83.1 | Worth 3-day experiment |
| Hardware/IoT/device configuration and fleet ops | 392 | 77.1 | Investigate with paid/customer discovery |
| Meeting transcription, translation, and follow-up | 302 | 77.7 | Investigate with paid/customer discovery |

**具体案例 / 证据样本**
| 标题/案例 | 年份 | 分数 | 命中查询 | 证据摘录 | 来源 |
| -- | -- | -- | -- | -- | -- |
| Static Site Generator (SSG) as a Free Squarespace Alternative? | 2024 | 8 | I recommend | Static Site Generator (SSG) as a Free Squarespace Alternative? I'm a novice with no expertise in website building or design. I went with Squarespace for a business site because the | https://news.ycombinator.com/item?id=39216383 |
| Show HN: Continue – Open-source coding autopilot | 2023 | 298 | solution is to | Show HN: Continue – Open-source coding autopilot Hi HN, we’re Nate and Ty, co-founders of Continue, an open-source autopilot for software development built to be deeply customizabl | https://news.ycombinator.com/item?id=36882146 |
| Launch HN: Lago (YC S21) – Open-source usage-based billing | 2023 | 442 | here's how I solved it | Launch HN: Lago (YC S21) – Open-source usage-based billing Hi HN, we’re the cofounders of Lago: an open-source alternative to Stripe Billing, Chargebee, and Recurly. That is, we ma | https://news.ycombinator.com/item?id=34773442 |
| Ask HN: Anyone making games in JavaScript or interested in doing it? | 2023 | 2 | try this | Ask HN: Anyone making games in JavaScript or interested in doing it? I'm a software developer working mostly on web applications. When I was younger, I wanted to make games but I s | https://news.ycombinator.com/item?id=37302315 |
| Claude Code Unpacked : A visual guide | 2026 | 1128 | guide | Claude Code Unpacked : A visual guide Related ongoing threads: The Claude Code Source Leak: fake tools, frustration regexes, undercover mode - https://news.ycombinator.com/item?id= | https://news.ycombinator.com/item?id=47597085 |
| Ask HN: Should "I asked $AI, and it said" replies be forbidden in HN guidelines? | 2025 | 980 | guide | Ask HN: Should "I asked $AI, and it said" replies be forbidden in HN guidelines? As various LLMs become more and more popular, so does comments with "I asked Gemini, and Gemini sai | https://news.ycombinator.com/item?id=46206457 |

### Signal 13：异常行为

- 英文名：Anomalous Behavior
- 定义：突然出现 spike、surge、trend、everyone is、hiring for、lots of people 等变化。
- 本地数据量：10000 条，目标完成度：100.0%

**详细特征**
- 异常行为关注变化率，不是静态数量。
- 可观察突然增长的工具、招聘、关键词、替代搜索。
- 需要与具体行为 signal 交叉，否则容易变成趋势噪音。
- 强信号：多个来源同时出现 spike，并伴随自建、付费、迁移或招聘。
- 弱信号/误判：只有媒体热度，没有行为变化。

**行为数据**
| 行为证据 | 命中数 |
| -- | -- |
| payment | 622 |
| self_build | 205 |
| migration | 230 |
| workaround | 107 |
| repetition | 184 |
| workflow | 306 |
| sharing | 81 |
| growth | 3415 |
| technology | 1060 |

**Anti-Pattern 数据**
| 负向信号 | 命中数 |
| -- | -- |
| no_budget | 309 |
| too_custom | 104 |
| low_value_attention | 395 |
| solved_by_incumbent | 17 |
| hard_to_switch | 1 |

**该 Signal 最常落入的问题簇**
| 问题簇 | 该 Signal 独立证据数 | 机会分 | 漏斗阶段 |
| -- | -- | -- | -- |
| Creator/content repurposing and publishing workflow | 930 | 82.1 | Worth 3-day experiment |
| Recruiting/hiring screening workflow | 647 | 83.0 | Worth 3-day experiment |
| Marketplace/service matching manual liquidity | 633 | 83.2 | Worth 3-day experiment |
| AI coding agent reliability / code workflow | 536 | 81.0 | Investigate with paid/customer discovery |
| Education/learning/personal knowledge workflow | 520 | 82.1 | Worth 3-day experiment |
| Security, compliance, and audit evidence automation | 336 | 83.1 | Worth 3-day experiment |
| Healthcare admin/EHR scheduling and coordination | 300 | 80.6 | Investigate with paid/customer discovery |
| Sales/CRM/lead workflow automation | 248 | 82.3 | Worth 3-day experiment |

**具体案例 / 证据样本**
| 标题/案例 | 年份 | 分数 | 命中查询 | 证据摘录 | 来源 |
| -- | -- | -- | -- | -- | -- |
| Ask HN: Developer abused “sign in with GitHub”? | 2022 | 860 | suddenly | Ask HN: Developer abused “sign in with GitHub”? The offending website "nopecha.com", which unfortunately i found about a week ago on HN itself appeared to be another captcha servic | https://news.ycombinator.com/item?id=33917962 |
| Tell HN: Google Cloud suspended our production projects at 1am on Saturday | 2022 | 1313 | suddenly | Tell HN: Google Cloud suspended our production projects at 1am on Saturday TLDR; never use google cloud systems for production. Google cloud suspended all our projects due to the b | https://news.ycombinator.com/item?id=32547912 |
| Show HN: 2048 turned 10 this year, I built an updated version to celebrate | 2024 | 669 | suddenly | Show HN: 2048 turned 10 this year, I built an updated version to celebrate Hi all! My name is Gabriele Cirulli, I’m the original creator of 2048. Ten years ago, someone posted 2048 | https://news.ycombinator.com/item?id=41934746 |
| Tell HN: Braintree is no longer startup-friendly | 2018 | 65 | growing fast | Tell HN: Braintree is no longer startup-friendly About 3 years ago, after researching payment processing options, we chose Braintree. The thing is, they were still riding on the go | https://news.ycombinator.com/item?id=17854943 |
| Launch HN: MovingLake (YC S22) – Real-time data connectors for almost anything | 2022 | 132 | everyone is | Launch HN: MovingLake (YC S22) – Real-time data connectors for almost anything Hello HN! We are Andres and Edgar and we are building MovingLake ( https://movinglake.com ). We are c | https://news.ycombinator.com/item?id=33359870 |
| My experience as a Gazan girl getting into Silicon Valley companies | 2021 | 1723 | everyone is | My experience as a Gazan girl getting into Silicon Valley companies Hiii everyone, this is my first time posting here! I have read Hacker News sometimes but only thought about shar | https://news.ycombinator.com/item?id=26251143 |

### Signal 14：需求增长

- 英文名：Demand Acceleration
- 定义：讨论、采用、招聘、预算、项目数量出现 growing/increasing/accelerating。
- 本地数据量：10000 条，目标完成度：100.0%

**详细特征**
- 需求增长强调 demand acceleration。
- 2024/2025/2026 的变化比当前绝对量更重要。
- 增长信号应与预算、迁移、自建、半成品市场共同使用。
- 强信号：讨论量、项目数、招聘、预算、替代搜索同步增长。
- 弱信号/误判：只是关键词越来越热，但没有商业行为证据。

**行为数据**
| 行为证据 | 命中数 |
| -- | -- |
| payment | 2342 |
| self_build | 321 |
| migration | 615 |
| workaround | 297 |
| repetition | 505 |
| workflow | 882 |
| sharing | 157 |
| growth | 5105 |
| technology | 2288 |

**Anti-Pattern 数据**
| 负向信号 | 命中数 |
| -- | -- |
| no_budget | 752 |
| too_custom | 281 |
| low_value_attention | 794 |
| solved_by_incumbent | 67 |
| hard_to_switch | 6 |

**该 Signal 最常落入的问题簇**
| 问题簇 | 该 Signal 独立证据数 | 机会分 | 漏斗阶段 |
| -- | -- | -- | -- |
| Marketplace/service matching manual liquidity | 2578 | 83.2 | Worth 3-day experiment |
| Education/learning/personal knowledge workflow | 1429 | 82.1 | Worth 3-day experiment |
| Creator/content repurposing and publishing workflow | 1235 | 82.1 | Worth 3-day experiment |
| Recruiting/hiring screening workflow | 1183 | 83.0 | Worth 3-day experiment |
| Security, compliance, and audit evidence automation | 949 | 83.1 | Worth 3-day experiment |
| AI coding agent reliability / code workflow | 913 | 81.0 | Investigate with paid/customer discovery |
| Legal/document/compliance drafting workflow | 885 | 85.2 | Worth 3-day experiment |
| Sales/CRM/lead workflow automation | 804 | 82.3 | Worth 3-day experiment |

**具体案例 / 证据样本**
| 标题/案例 | 年份 | 分数 | 命中查询 | 证据摘录 | 来源 |
| -- | -- | -- | -- | -- | -- |
| AI Orchestration Market Witnesses Surge in Use Across Healthcare and BFSI | 2025 | 1 | growth rate | AI Orchestration Market Witnesses Surge in Use Across Healthcare and BFSI The global AI orchestration market is rapidly becoming a cornerstone of enterprise digital transformation, | https://news.ycombinator.com/item?id=45114189 |
| Ask HN: Who is hiring? (November 2020) | 2020 |  | demand growth | Ask HN: Who is hiring? (November 2020) Foresight Mental Health / Berkeley, CA / Senior Full Stack/Backend Engineer / Full Time / Remote (Americas) The mental health space is seeing | https://news.ycombinator.com/item?id=24969524 |
| Google Will Eat Itself | 2014 |  | increasing demand | Google Will Eat Itself > You are correct about the empirical facts (there exist some companies don't currently pay dividends), but theory is needed to understand that if those comp | https://news.ycombinator.com/item?id=7410732 |
| Launch HN: Living Carbon (YC W20) – Trees that capture and store more carbon | 2022 | 424 | growth rate | Launch HN: Living Carbon (YC W20) – Trees that capture and store more carbon Hi HN! Maddie and Patrick here. We founded Living Carbon ( https://www.livingcarbon.com ), a biotech co | https://news.ycombinator.com/item?id=30672841 |
| The ‘effective altruists’ | 2015 |  | growing demand | The ‘effective altruists’ The question of utilitarianism rests on the opprotunity cost of doing one thing versus another. Sure, some costs are relatively easy to estimate - vegging | https://news.ycombinator.com/item?id=10231905 |
| Ask HN: Who is hiring? (December 2012) | 2012 |  | rapid growth | Ask HN: Who is hiring? (December 2012) San Francisco / Fullstack Engineer, Backend Engineer and Frontend Developer / Perfect Audience What We Do: We've built the world's first and  | https://news.ycombinator.com/item?id=4857714 |

## 3. 跨 Signal 聚类与机会评分

Opportunity Score = 跨 Signal 权重 + 独立证据强度 + 商业行为证据 + 行为投入证据 + 增长证据 - Anti-Pattern 惩罚。

### Top 机会簇
| 排名 | 问题簇 | 分数 | 阶段 | 独立证据 | Signals | 作者 | 域名 | 下一步实验 |
| -- | -- | -- | -- | -- | -- | -- | -- | -- |
| 1 | Legal/document/compliance drafting workflow | 85.2 | Worth 3-day experiment | 6481 | 14 | 5106 | 586 | Sell manual contract review/extraction pilot; success is real docs + budget owner |
| 2 | Billing, invoicing, accounting, and reconciliation | 84.3 | Worth 3-day experiment | 5402 | 14 | 4507 | 965 | Offer to reconcile one month of transactions; success is paid pilot and error benchmark |
| 3 | Marketplace/service matching manual liquidity | 83.2 | Worth 3-day experiment | 10700 | 14 | 7780 | 1634 | Manually broker 10 transactions; success is completed repeat transaction |
| 4 | Security, compliance, and audit evidence automation | 83.1 | Worth 3-day experiment | 9904 | 14 | 7866 | 1947 | Sell a compliance evidence collection sprint; success is access to policies/tools + paid audit prep |
| 5 | Recruiting/hiring screening workflow | 83.0 | Worth 3-day experiment | 5923 | 14 | 4571 | 989 | Paid sourcing/screening sprint with explicit criteria; success is qualified interviews booked |
| 6 | Sales/CRM/lead workflow automation | 82.3 | Worth 3-day experiment | 6259 | 14 | 5017 | 934 | Sell a lead list + outreach concierge package; success is paid list/order and meeting rate |
| 7 | Creator/content repurposing and publishing workflow | 82.1 | Worth 3-day experiment | 13405 | 14 | 10575 | 3001 | Manual repurposing package for 5 posts/videos; success is repeat purchase |
| 8 | Education/learning/personal knowledge workflow | 82.1 | Worth 3-day experiment | 11401 | 14 | 8867 | 1701 | Test paid cohort/learning artifact service; success is repeat sessions or payment |
| 9 | Unclassified but behavior-rich demand | 81.7 | Investigate with paid/customer discovery | 2652 | 14 | 2434 | 738 | Run discovery interviews before product work |
| 10 | AI coding agent reliability / code workflow | 81.0 | Investigate with paid/customer discovery | 22977 | 14 | 17414 | 3776 | Sell a paid code-review/agent QA audit for one repo; success is repo access + paid pilot |
| 11 | Insurance claims and underwriting operations | 80.9 | Investigate with paid/customer discovery | 3769 | 14 | 3046 | 464 | Sell a claims-document triage pilot; success is sample claims + paid evaluation |
| 12 | Healthcare admin/EHR scheduling and coordination | 80.6 | Investigate with paid/customer discovery | 3619 | 14 | 3010 | 562 | Paid concierge on one admin workflow with de-identified samples; success is pilot from practice manager |
| 13 | Procurement/vendor/RFP workflow | 80.0 | Investigate with paid/customer discovery | 3190 | 14 | 2703 | 815 | Offer to source vendors for one purchase; success is real RFQ + paid sourcing fee |
| 14 | Document/PDF/data extraction automation | 79.3 | Investigate with paid/customer discovery | 9337 | 14 | 7489 | 2078 | Manually extract 20 documents and charge per batch; success is paid repeat batch |
| 15 | Manufacturing/industrial QA and supply chain | 78.8 | Investigate with paid/customer discovery | 3341 | 14 | 2757 | 634 | Sell one QA/reporting/supply-chain cleanup sprint; success is sample data + paid pilot |
| 16 | Manual reporting and spreadsheet workflow automation | 77.7 | Investigate with paid/customer discovery | 6231 | 14 | 5145 | 1727 | Cold email with a done-for-you report automation offer; success is shared spreadsheet + payment |
| 17 | Meeting transcription, translation, and follow-up | 77.7 | Investigate with paid/customer discovery | 3593 | 14 | 3223 | 830 | Offer done-for-you meeting notes/follow-up for one week; success is paid repeat usage |
| 18 | Privacy/data governance/synthetic data | 77.2 | Investigate with paid/customer discovery | 2966 | 14 | 2640 | 776 | Offer data-risk audit on one workflow; success is policy owner engagement + payment |
| 19 | Hardware/IoT/device configuration and fleet ops | 77.1 | Investigate with paid/customer discovery | 6741 | 14 | 5442 | 969 | Paid device configuration audit/automation script; success is real device list + payment |
| 20 | SaaS migration/export/import pain | 76.8 | Investigate with paid/customer discovery | 7351 | 14 | 6200 | 1965 | Sell a migration service from one named tool; success is exported data + paid migration |
| 21 | Observability/incident monitoring and debugging | 76.8 | Investigate with paid/customer discovery | 4224 | 14 | 3655 | 1003 | Analyze one incident/log sample; success is access to logs + paid remediation sprint |
| 22 | Scheduling/calendar/coordination automation | 75.6 | Investigate with paid/customer discovery | 2490 | 14 | 2204 | 447 | Manual scheduling assistant for one week; success is paid continuation |
| 23 | AI agent tool-call safety and permissions | 75.5 | Investigate with paid/customer discovery | 6379 | 14 | 5368 | 1828 | Offer a security/permission review of one agent workflow; success is real workflow logs |
| 24 | AI evaluation/model monitoring/prompt management | 75.3 | Investigate with paid/customer discovery | 3871 | 14 | 3288 | 1118 | Run an eval setup sprint for one AI workflow; success is paid eval baseline |
| 25 | Browser extension / cross-app workflow bridge | 72.0 | Investigate with paid/customer discovery | 4296 | 14 | 3736 | 1214 | Ship no-code/manual browser workflow service; success is installed extension or paid setup |

## 4. 机会漏斗
| 阶段 | 数量 | 说明 |
| -- | -- | -- |
| 原始 Signal 记录 | 140000 | 每类 10000 条，本地 CSV/JSONL 可追溯 |
| 去重后独立证据 | 125411 | 按 HN objectID/URL/title 去重，保留跨 signal 映射 |
| 行为丰富证据 | 81025 | 至少命中一个预定义问题簇，或行为信号足够强 |
| 问题簇 | 30 | 由 taxonomy 聚合为可解释问题结构 |
| 商业验证候选 | 25 | 高分或中高分，需要付费/客户发现验证 |
| 3 天实验优先机会 | 8 | 跨 signal 多、独立证据多、商业行为较强 |

## 5. 优先进入 3 天实验的机会假设
### 1. Legal/document/compliance drafting workflow

- Score：85.2
- Target User：legal/ops/compliance teams
- Hypothesis：我们观察到legal/ops/compliance teams正在因为contracts, policies, reviews, and legal docs are document-heavy and slow而采取搜索替代、自己造工具、workaround、付费或迁移动作。当前机会可能来自：LLMs reduce first draft and review cost, but liability remains。
- Evidence：6481 条独立证据，14 类 signal，5106 个独立作者，586 个外链域名。
- Behavior Counts：payment:3578; workflow:1528; budget:1182; growth:976; migration:816
- Anti-Pattern：no_budget:977; low_value_attention:716; too_custom:286; solved_by_incumbent:106; hard_to_switch:28
- Next Experiment：Sell manual contract review/extraction pilot; success is real docs + budget owner

### 2. Billing, invoicing, accounting, and reconciliation

- Score：84.3
- Target User：finance teams / SMB operators
- Hypothesis：我们观察到finance teams / SMB operators正在因为money movement workflows create direct cost, delay, and error pain而采取搜索替代、自己造工具、workaround、付费或迁移动作。当前机会可能来自：APIs and AI extraction lower back-office automation cost。
- Evidence：5402 条独立证据，14 类 signal，4507 个独立作者，965 个外链域名。
- Behavior Counts：payment:3128; workflow:2384; budget:799; repetition:724; self_build:687
- Anti-Pattern：no_budget:949; low_value_attention:494; too_custom:276; solved_by_incumbent:93; hard_to_switch:21
- Next Experiment：Offer to reconcile one month of transactions; success is paid pilot and error benchmark

### 3. Marketplace/service matching manual liquidity

- Score：83.2
- Target User：buyers/sellers of services
- Hypothesis：我们观察到buyers/sellers of services正在因为users manually search, vet, and match service supply/demand而采取搜索替代、自己造工具、workaround、付费或迁移动作。当前机会可能来自：fragmented services remain hard to search and vet。
- Evidence：10700 条独立证据，14 类 signal，7780 个独立作者，1634 个外链域名。
- Behavior Counts：budget:4703; payment:4160; growth:2157; workflow:1742; self_build:1232
- Anti-Pattern：no_budget:1482; low_value_attention:1023; too_custom:502; solved_by_incumbent:153; hard_to_switch:30
- Next Experiment：Manually broker 10 transactions; success is completed repeat transaction

### 4. Security, compliance, and audit evidence automation

- Score：83.1
- Target User：security/compliance leads / founders
- Hypothesis：我们观察到security/compliance leads / founders正在因为compliance and audit evidence collection is repetitive and high-stakes而采取搜索替代、自己造工具、workaround、付费或迁移动作。当前机会可能来自：regulation and AI risk increase evidence burden。
- Evidence：9904 条独立证据，14 类 signal，7866 个独立作者，1947 个外链域名。
- Behavior Counts：workflow:3545; payment:3381; self_build:1817; workaround:1387; budget:1272
- Anti-Pattern：no_budget:1591; low_value_attention:944; too_custom:579; solved_by_incumbent:173; hard_to_switch:43
- Next Experiment：Sell a compliance evidence collection sprint; success is access to policies/tools + paid audit prep

### 5. Recruiting/hiring screening workflow

- Score：83.0
- Target User：recruiters / hiring managers
- Hypothesis：我们观察到recruiters / hiring managers正在因为sourcing, screening, interview scheduling, and candidate evaluation are repetitive而采取搜索替代、自己造工具、workaround、付费或迁移动作。当前机会可能来自：AI can process candidate data but trust and bias risks remain。
- Evidence：5923 条独立证据，14 类 signal，4571 个独立作者，989 个外链域名。
- Behavior Counts：budget:4255; payment:1691; workflow:1242; growth:1109; repetition:792
- Anti-Pattern：no_budget:796; low_value_attention:734; too_custom:244; solved_by_incumbent:67; hard_to_switch:11
- Next Experiment：Paid sourcing/screening sprint with explicit criteria; success is qualified interviews booked

### 6. Sales/CRM/lead workflow automation

- Score：82.3
- Target User：sales teams / founders / agencies
- Hypothesis：我们观察到sales teams / founders / agencies正在因为lead research, outreach, CRM updates, and follow-up are repetitive而采取搜索替代、自己造工具、workaround、付费或迁移动作。当前机会可能来自：AI research and writing lower SDR task cost。
- Evidence：6259 条独立证据，14 类 signal，5017 个独立作者，934 个外链域名。
- Behavior Counts：payment:2572; workflow:1545; budget:1392; growth:1180; self_build:1081
- Anti-Pattern：no_budget:1103; low_value_attention:752; too_custom:482; solved_by_incumbent:119; hard_to_switch:19
- Next Experiment：Sell a lead list + outreach concierge package; success is paid list/order and meeting rate

### 7. Creator/content repurposing and publishing workflow

- Score：82.1
- Target User：creators / marketers / agencies
- Hypothesis：我们观察到creators / marketers / agencies正在因为content creation and multi-platform publishing are repetitive and output-driven而采取搜索替代、自己造工具、workaround、付费或迁移动作。当前机会可能来自：AI lowers content production cost but increases volume management。
- Evidence：13405 条独立证据，14 类 signal，10575 个独立作者，3001 个外链域名。
- Behavior Counts：payment:3952; self_build:3153; workflow:2477; repetition:2128; growth:1874
- Anti-Pattern：no_budget:2418; low_value_attention:1827; too_custom:872; solved_by_incumbent:241; hard_to_switch:31
- Next Experiment：Manual repurposing package for 5 posts/videos; success is repeat purchase

### 8. Education/learning/personal knowledge workflow

- Score：82.1
- Target User：learners / teachers / knowledge workers
- Hypothesis：我们观察到learners / teachers / knowledge workers正在因为learning, notes, flashcards, and tutoring create repeated knowledge workflows而采取搜索替代、自己造工具、workaround、付费或迁移动作。当前机会可能来自：AI tutors and content generation create new learning behavior。
- Evidence：11401 条独立证据，14 类 signal，8867 个独立作者，1701 个外链域名。
- Behavior Counts：payment:3749; workflow:2237; self_build:2099; repetition:1726; growth:1720
- Anti-Pattern：no_budget:1936; low_value_attention:1759; too_custom:592; solved_by_incumbent:230; hard_to_switch:39
- Next Experiment：Test paid cohort/learning artifact service; success is repeat sessions or payment

## 6. 单独 Signal 报告索引
每类 signal 还有一个单独聚类报告，路径如下：
- Signal 01：`demand_behavior_signal_research/opportunity_funnel/signal_cluster_reports/signal_01_cluster_report.md`
- Signal 02：`demand_behavior_signal_research/opportunity_funnel/signal_cluster_reports/signal_02_cluster_report.md`
- Signal 03：`demand_behavior_signal_research/opportunity_funnel/signal_cluster_reports/signal_03_cluster_report.md`
- Signal 04：`demand_behavior_signal_research/opportunity_funnel/signal_cluster_reports/signal_04_cluster_report.md`
- Signal 05：`demand_behavior_signal_research/opportunity_funnel/signal_cluster_reports/signal_05_cluster_report.md`
- Signal 06：`demand_behavior_signal_research/opportunity_funnel/signal_cluster_reports/signal_06_cluster_report.md`
- Signal 07：`demand_behavior_signal_research/opportunity_funnel/signal_cluster_reports/signal_07_cluster_report.md`
- Signal 08：`demand_behavior_signal_research/opportunity_funnel/signal_cluster_reports/signal_08_cluster_report.md`
- Signal 09：`demand_behavior_signal_research/opportunity_funnel/signal_cluster_reports/signal_09_cluster_report.md`
- Signal 10：`demand_behavior_signal_research/opportunity_funnel/signal_cluster_reports/signal_10_cluster_report.md`
- Signal 11：`demand_behavior_signal_research/opportunity_funnel/signal_cluster_reports/signal_11_cluster_report.md`
- Signal 12：`demand_behavior_signal_research/opportunity_funnel/signal_cluster_reports/signal_12_cluster_report.md`
- Signal 13：`demand_behavior_signal_research/opportunity_funnel/signal_cluster_reports/signal_13_cluster_report.md`
- Signal 14：`demand_behavior_signal_research/opportunity_funnel/signal_cluster_reports/signal_14_cluster_report.md`

## 7. 数据文件
- 14 类原始记录：`E:\AIHardware\假设验证研究\demand_behavior_signal_research\records`
- 14 类第一阶段 md：`E:\AIHardware\假设验证研究\demand_behavior_signal_research\signal_reports`
- 去重证据表：`E:\AIHardware\假设验证研究\demand_behavior_signal_research\opportunity_funnel\metadata\01_deduplicated_evidence.csv`
- 机会评分表：`E:\AIHardware\假设验证研究\demand_behavior_signal_research\opportunity_funnel\metadata\02_cross_signal_opportunity_scores.csv`
