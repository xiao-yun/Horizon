# Horizon 每日速递 - 2026-05-29

> From 48 items, 27 important content pieces were selected
>
> ## AI 与工具
> 1. [只需 Postgres：用 PostgreSQL 实现持久化工作流](#item-ai-tools-1) ⭐️ 8.0/10 · HN · 18:41
> 2. [识别 LLM 文本的“气味”：常见模式与社区技巧](#item-ai-tools-2) ⭐️ 8.0/10 · HN · 19:02
> 3. [《Continue? Y/N》：60 秒模拟 AI 代理权限疲劳的游戏](#item-ai-tools-3) ⭐️ 8.0/10 · HN · 13:02
> 4. [Sam Altman 和 Dario Amodei 同时软化 AI 导致大规模失业论调](#item-ai-tools-4) ⭐️ 8.0/10 · HN · 19:43
> 5. [Anthropic 发布 Claude Opus 4.8，并预告 Project Glasswing 的 Mythos 模型](#item-ai-tools-5) ⭐️ 7.0/10 · HN · 16:49
> 6. [《永久上层乌鸦》：恶搞硅谷 CEO 的讽刺网站](#item-ai-tools-6) ⭐️ 6.0/10 · HN · 15:23
> ## 数据仓库
> 1. [Apache Iceberg REST Catalog 提案新增表与列标签元数据字段](#item-data-warehouse-1) ⭐️ 7.0/10 · GitHub · 08:00
> 2. [Apache Iceberg 提议新增 Variant 数据类型](#item-data-warehouse-2) ⭐️ 7.0/10 · GitHub · 12:52
> 3. [Apache Iceberg 提议为 VARIANT 列添加虚拟字段元数据](#item-data-warehouse-3) ⭐️ 7.0/10 · GitHub · 03:00
> 4. [Apache Iceberg 提出 File Format API 提案](#item-data-warehouse-4) ⭐️ 7.0/10 · GitHub · 11:57
> 5. [Iceberg 提议为 loadTable API 增加快照与元数据日志裁剪参数](#item-data-warehouse-5) ⭐️ 7.0/10 · GitHub · 02:33
> 6. [Delta Lake 协议新增重定向功能规范提案](#item-data-warehouse-6) ⭐️ 7.0/10 · GitHub · 20:12
> 7. [提议为 Apache Hudi 增加分区软删除功能](#item-data-warehouse-7) ⭐️ 7.0/10 · GitHub · 22:43
> 8. [Apache Hudi RFC-59 提案：设计描述与实现细节](#item-data-warehouse-8) ⭐️ 7.0/10 · GitHub · 23:17
> 9. [Apache Hudi RFC 提出新 Table API 以优化查询引擎集成](#item-data-warehouse-9) ⭐️ 7.0/10 · GitHub · 23:15
> 10. [ClickHouse Cloud 推出多阶段分布式查询执行](#item-data-warehouse-10) ⭐️ 7.0/10 · ClickHouse Blog · 08:56
> ## 综合
> 1. [uv 0.11.17 发布：支持构建时的 import-names 及新标志](#item-general-1) ⭐️ 6.0/10 · GitHub · 20:41
> ## GitHub 趋势
> 1. [Lum1104/Understand-Anything +3766⭐: Understand-Anything：代码转交互知识图谱](https://github.com/Lum1104/Understand-Anything) ⭐️ 8.0/10 · GH Trending · 22:14
> 2. [codecrafters-io/build-your-own-x +866⭐: 从零构建技术教程合集单日获 866 星](https://github.com/codecrafters-io/build-your-own-x) ⭐️ 8.0/10 · GH Trending · 22:14
> 3. [anthropics/skills +791⭐: Anthropic 开源 AI 代理技能仓库备受关注](https://github.com/anthropics/skills) ⭐️ 8.0/10 · GH Trending · 22:14
> 4. [harry0703/MoneyPrinterTurbo +4685⭐: harry0703/MoneyPrinterTurbo：AI 一键生成短视频工具，单日暴涨 4685 星](https://github.com/harry0703/MoneyPrinterTurbo) ⭐️ 7.0/10 · GH Trending · 22:14
> 5. [obra/superpowers +1726⭐: obra/superpowers：今日获 1726 星的 Shell 智能体技能框架](https://github.com/obra/superpowers) ⭐️ 7.0/10 · GH Trending · 22:14
> 6. [microsoft/markitdown +1263⭐: 微软开源 MarkItDown：Office 文档转 Markdown 的 Python 工具](https://github.com/microsoft/markitdown) ⭐️ 7.0/10 · GH Trending · 22:14
> 7. [unclecode/crawl4ai +253⭐: GitHub 热门：Crawl4AI 开源 LLM 网页爬虫日获 253 星](https://github.com/unclecode/crawl4ai) ⭐️ 7.0/10 · GH Trending · 22:14
> 8. [Leonxlnx/taste-skill +2235⭐: taste-skill 项目爆火：单日 2235 星，专治 AI 生成“无聊内容”](https://github.com/Leonxlnx/taste-skill) ⭐️ 6.0/10 · GH Trending · 22:14
> 9. [affaan-m/ECC +1388⭐: affaan-m/ECC 单日星增 1388，AI 代理性能优化引关注](https://github.com/affaan-m/ECC) ⭐️ 6.0/10 · GH Trending · 22:14
> 10. [twentyhq/twenty +495⭐: Twenty：TypeScript 开源 AI 驱动 CRM，日增 495 星](https://github.com/twentyhq/twenty) ⭐️ 6.0/10 · GH Trending · 22:14

## AI 与工具

<a id="item-ai-tools-1"></a>
## [只需 Postgres：用 PostgreSQL 实现持久化工作流](https://www.dbos.dev/blog/postgres-is-all-you-need-for-durable-execution) ⭐️ 8.0/10

一篇新文章提倡直接使用 PostgreSQL 作为持久化工作流执行的完整解决方案，强调其简单性和统一数据存储的优势，引发了社区对扩展性和替代实现的广泛讨论。 该观点为开发者省去了引入专门工作流引擎的复杂性和运维负担，尤其适合希望简化技术栈的中小规模系统，可能影响架构选型趋势。 社区提醒，当数据量扩展到 TB 级别时，Postgres 可能成为瓶颈；此外，已有基于 PostgreSQL 的轻量库 absurd，也有团队将类似模式迁移到 SQLite。

hackernews · KraftyOne · May 28, 18:41 · [社区讨论](https://news.ycombinator.com/item?id=48313530)

**背景**: 持久化执行是一种编程范式，让代码在崩溃、重启后仍可自动恢复，通过保存检查点来重放进度。传统上需依赖 Temporal、Azure Durable Functions 等专用平台，而直接用关系数据库实现持久化工作流近年来开始流行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.inngest.com/blog/principles-of-durable-execution">The Principles of Durable Execution Explained - Inngest Blog What is Durable Task? - Durable Task | Microsoft Learn Top Stories What is Durable Execution? A Definitive Guide | Restate Lambda durable functions - AWS Lambda My Favorite Technologies for Implementing Durable Workflows ... Durable execution - Docs by LangChain The definitive guide to Durable Execution | Temporal</a></li>

</ul>
</details>

**社区讨论**: 多数评论认可 Postgres 的实用性和集中管理数据的便利，但指出超大规模时需考虑拆分；有人推荐了更简单的 Postgres 实现 absurd，也有人分享了在生产环境中使用 Postgres 或 SQLite 构建持久化工作流的经验。

**标签**: `#postgresql`, `#workflows`, `#durable-execution`, `#database`, `#distributed-systems`

---

<a id="item-ai-tools-2"></a>
## [识别 LLM 文本的“气味”：常见模式与社区技巧](https://shvbsle.in/various-llm-smells/) ⭐️ 8.0/10

一篇分析 AI 生成文本中独特模式（被称为“LLM 嗅觉”）的文章引发社区热议，用户分享了大量识别 LLM 输出的具体短语和写作习惯，例如以“诚实的警告：”等词开头，以及使用“承重”“影响半径”等隐喻。 随着 LLM 在内容创作中的普及，识别 AI 生成文本有助于维护写作的真实性和原创性，同时理解其风格局限能优化人机协作，对内容创作者和读者都具有重要意义。 值得注意的细节包括：LLM 过度使用特定句式如“需要内化的事情：”，滥用“负载”“爆炸半径”等术语于非技术语境；ASCII 艺术图表被指出是 100%可靠的检测信号；评论指出 LLM 写作风格近期无明显改进，且若你认为 LLM 输出比自己好得多，可能表明你缺乏判断能力。

hackernews · speckx · May 28, 19:02 · [社区讨论](https://news.ycombinator.com/item?id=48313810)

**背景**: “气味”（smell）一词借自软件工程中的“代码异味”，指代表面症状提示更深层问题。LLM 生成文本常带有正式、华丽但缺乏个性的风格，通过模式识别可反向检测。类似话题在技术社区中已有多篇讨论，如一篇介绍“AI 气味”的文章列举了 ASCII 艺术等明显迹象。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rmoff.net/2025/11/25/ai-smells-on-medium/">(AI) Smells on Medium</a></li>

</ul>
</details>

**社区讨论**: 社区评论整体积极，分享了许多实用检测技巧：用户列出具体高频短语，指出 LLM 风格停滞不前，并建议用 LLM 改进文章结构与流畅度而非直接生成内容，同时也提醒若自觉 LLM 写作远超自己，可能因自身水平不足而产生误判。

**标签**: `#LLM`, `#writing-style`, `#AI-generated-text`, `#detection`, `#community-insights`

---

<a id="item-ai-tools-3"></a>
## [《Continue? Y/N》：60 秒模拟 AI 代理权限疲劳的游戏](https://llmgame.scalex.dev/) ⭐️ 8.0/10

一个名为《Continue? Y/N》的 60 秒浏览器游戏在 Hacker News 上引发热议，玩家需在 AI 代理的大量权限请求中快速批准或拒绝，以幽默方式展现“权限疲劳”现象。 该游戏以娱乐形式揭示了 AI 代理安全中的真实风险：用户面对过多授权请求时容易机械点击，导致安全漏洞。它引发的讨论涉及真实开发环境中的安全卫生和自动化风险，对 AI 工具设计有启发意义。 游戏设定 60 秒内处理数十个请求，单纯全部拒绝可获“安全意识工程师”徽章但导致过度拦截，评论指出部分敏感判断（如读取.zshrc）不切实际，且场景缺乏上下文，与现实工作流脱节。

hackernews · Wirbelwind · May 28, 13:02 · [社区讨论](https://news.ycombinator.com/item?id=48308376)

**背景**: AI 编码代理（如 Claude Code）在操作文件或执行命令时需用户逐一授权，频繁提示导致用户忽视安全，观察数据显示批准率高达 93%。为缓解疲劳，Anthropic 等推出了自动模式，通过本地快速过滤与服务器端扫描减少低风险请求的打扰。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://scalex.dev/blog/ai-agent-permissions/">Suffering from Agent Permission Fatigue? Find out your high score | Scale X</a></li>
<li><a href="https://molten.bot/blog/agent-approval-fatigue/">The Agent Approval Fatigue Problem (And Why Your Security Team Is Clicking "Yes" to Everything) | Molten.Bot Blog</a></li>

</ul>
</details>

**社区讨论**: 社区反应热烈：有人发现快速全部拒绝可“作弊”；许多人批评游戏中的一些敏感操作（如读取.zshrc）并不实际；还有人认为请求跳跃、缺乏上下文，未体现真实工作流中的审批疲劳。整体认可创意，但期望更贴近实际情况。

**标签**: `#AI`, `#security`, `#game`, `#developer-tools`, `#HackerNews`

---

<a id="item-ai-tools-4"></a>
## [Sam Altman 和 Dario Amodei 同时软化 AI 导致大规模失业论调](https://fortune.com/2026/05/26/sam-altman-dario-amodei-walking-back-ai-jobs-apocalypse-prophecies-ipo/) ⭐️ 8.0/10

OpenAI 首席执行官 Sam Altman 与 Anthropic 首席执行官 Dario Amodei 近期公开表态，对人工智能将引发大规模失业的早期预测做出软化调整。 作为 AI 行业最有影响力的两位领袖，他们态度的转变可能影响政策制定、企业投资和公众对 AI 劳动力影响的预期，但也引发对动机和可信度的质疑。 尽管两人缓和了先前关于就业末日的言论，但并未完全否定 AI 对就业的长期颠覆性影响，且社区质疑此举是否为 IPO 或监管压力下的公关策略。

hackernews · ianrahman · May 28, 19:43 · [社区讨论](https://news.ycombinator.com/item?id=48314363)

**背景**: 近年来，以 Sam Altman 和 Dario Amodei 为代表的 AI 领军人物曾多次警告 AI 可能取代大量人类工作岗位，引发‘就业末日’担忧。然而，随着 AI 公司估值飙升和潜在 IPO，以及公众对 AI 的警惕情绪上升，这种叙事面临挑战。他们所在的 OpenAI 和 Anthropic 是开发大语言模型 (LLM) 的头部公司，其产品如 GPT-4 和 Claude 引发了关于就业自动化的广泛争议。

**社区讨论**: 社区整体持怀疑态度，认为此转变可能出于公关目的，以安抚公众和监管者；有用户指出高管们过去的夸大承诺已导致企业误判 AI 能力，另有观点认为 AI 研究人员对复杂职业的理解不足，导致预测不靠谱，还有讽刺评论称他们是为了长期利益才改变说辞。

**标签**: `#AI`, `#employment`, `#public relations`, `#tech industry`, `#society`

---

<a id="item-ai-tools-5"></a>
## [Anthropic 发布 Claude Opus 4.8，并预告 Project Glasswing 的 Mythos 模型](https://www.anthropic.com/news/claude-opus-4-8) ⭐️ 7.0/10

Anthropic 正式发布 Claude Opus 4.8，这是一次小幅但切实的更新；同时宣布 Project Glasswing 项目，并透露部分组织已在测试用于高级网络安全任务的 Claude Mythos 预览版。 Opus 4.8 延续了前沿模型的增量迭代，并加入了用户期待的功能；而 Mythos 模型预示着比 Opus 更智能的新模型类别，可能对关键软件基础设施的安全产生深远影响。 Opus 4.8 的改进被描述为“适度但可感知”，Web 界面现已支持关闭自适应思考功能；Mythos Preview 目前仅限少数组织在网络安全领域使用，官方称还需强化安全防护措施后才能广泛发布，预计数周内推向所有客户。

hackernews · craigmart · May 28, 16:49 · [社区讨论](https://news.ycombinator.com/item?id=48311647)

**背景**: Claude Opus 是 Anthropic 目前能力最强的模型系列，其中 0.5 版本（如 Sonnet 3.5、Opus 4.5）通常代表重大能力跃升，而 4.6、4.7、4.8 则是逐步优化。Project Glasswing 是 Anthropic 在 2026 年 4 月发起的行业性网络安全计划，旨在利用先进 AI 保护关键软件基础设施。Claude Mythos 是该计划中用于发现软件漏洞的大语言模型，现阶段未公开。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing: Securing critical software for the AI era</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mythos_(model)">Mythos (model)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Project_Glasswing">Project Glasswing</a></li>

</ul>
</details>

**社区讨论**: 社区注意到这是首次出现第三个次版本号递增，并认为此次改进幅度不大。用户对可关闭自适应思考表示欢迎，指出此前该功能常导致输出质量不佳。在图像生成测试中，高思考级别生成的自行车骨架明显更优。众人对 Mythos 模型抱有期待，但也关注其安全防护和实际发布时间。

**标签**: `#AI model release`, `#Claude`, `#Anthropic`, `#incremental update`, `#large language models`

---

<a id="item-ai-tools-6"></a>
## [《永久上层乌鸦》：恶搞硅谷 CEO 的讽刺网站](https://permanent-upper-crow.jasonwu.ink/) ⭐️ 6.0/10

一个名为《永久上层乌鸦》的恶搞网站上线，循环展示 107 位 CEO 及公司名称。灵感源于《纽约时报》一篇关于硅谷‘永久下层阶级’的评论文章，而网站创建者本人竟也是一家 AI 初创公司的联合创始人。 该网站以幽默方式讽刺了硅谷 AI 创业圈中的炫耀性消费和盲目追逐名流的现象，引发了关于科技文化和社会阶层的讨论。 网站包含固定的 107 个 CEO/公司名称，循环播放，没有终点。这与创作者声称用 AI 自动化取代人工的创业方向形成反差。

hackernews · whiteblossom · May 28, 15:23 · [社区讨论](https://news.ycombinator.com/item?id=48310280)

**背景**: 灵感源自 Jasmine Sun 在《纽约时报》发表的《硅谷正为永久下层阶级做准备》一文，该文讨论了 AI 可能加剧社会不平等。网站名‘永久上层乌鸦’是对原文的戏仿，暗讽硅谷精英阶层。网站以简单的网页循环形式呈现，不涉及复杂技术。

**社区讨论**: 社区评论指出，网站创建者本人就是 AI 创业公司联合创始人，这种反讽令人深思。有用户认为，不参与炫耀性消费即可摆脱困境。还有用户澄清了网站循环 107 个名称的机制。

**标签**: `#satire`, `#AI-startup-culture`, `#conspicuous-consumption`, `#web-toy`, `#social-commentary`

---


## 数据仓库

<a id="item-data-warehouse-1"></a>
## [Apache Iceberg REST Catalog 提案新增表与列标签元数据字段](https://github.com/apache/iceberg/issues/15521) ⭐️ 7.0/10

Apache Iceberg 社区在 #15521 提案中，计划为 REST Catalog 的 LoadTableResponse 新增可选的 `labels` 字段，用于传递表所有权、分类、成本归属等目录级元数据。 此举将标准化目录元数据的传递方式，使开源引擎能跨目录消费标签信息，提升生态互操作性，并降低对厂商特定扩展的依赖。 该字段为可选，不改变现有行为；目录可自行决定是否填充标签，目前提案尚未定义具体标签键的语义规范。

github · laskoviymishka · May 12, 08:00

**背景**: Apache Iceberg 是一种开放表格式，用于数据湖中的大规模分析表。其 REST Catalog 规范旨在通过 HTTP API 统一目录实现，解决多语言客户端下的兼容性问题。LoadTableResponse 是加载表时返回的元数据结构，目前仅包含表模式、快照等物理信息，缺乏业务上下文。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_Iceberg">Apache Iceberg</a></li>
<li><a href="https://iceberg.apache.org/rest-catalog-spec/">REST Catalog Spec - Apache Iceberg™</a></li>

</ul>
</details>

**标签**: `#apache-iceberg`, `#rest-api`, `#metadata`, `#data-engineering`, `#catalog`

---

<a id="item-data-warehouse-2"></a>
## [Apache Iceberg 提议新增 Variant 数据类型](https://github.com/apache/iceberg/issues/10392) ⭐️ 7.0/10

Apache Iceberg 社区提出在表格式中增加 Variant 数据类型，以便以高效的二进制格式原生存储 JSON、Avro 等半结构化数据。该提议于 2024 年 5 月 29 日在 GitHub issue #10392 中提出。 该功能将显著提升数据湖对半结构化数据的存储和查询效率，尤其适用于日志、遥测和 IoT 等场景，帮助企业简化数据管道并降低计算成本。 Variant 类型将数据编码为紧凑的二进制表示，查询引擎可直接操作而无需解析原始文本，从而加速过滤和聚合。目前提案仍处于早期讨论阶段，具体编码格式和实现细节尚未确定。

github · sfc-gh-aixu · Apr 30, 12:52

**背景**: Apache Iceberg 是数据湖领域的主流开放表格式，擅长管理大规模结构化数据。半结构化数据通常以字符串存储，查询效率低下。Variant 类型在其他系统（如 Databricks、Snowflake）中已用于高效处理动态 schema 的数据，该提案旨在将类似能力引入 Iceberg，弥补其在半结构化数据处理上的短板。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/apache/iceberg/issues/10392">Variant Data Type Support · Issue #10392 · apache/iceberg</a></li>
<li><a href="https://www.snowflake.com/en/engineering-blog/apache-iceberg-v3-variant-type/">The Apache Iceberg™ Variant Type: Flexible Semistructured Data, Reimagined</a></li>

</ul>
</details>

**标签**: `#data-engineering`, `#apache-iceberg`, `#semi-structured-data`, `#data-storage`, `#feature-proposal`

---

<a id="item-data-warehouse-3"></a>
## [Apache Iceberg 提议为 VARIANT 列添加虚拟字段元数据](https://github.com/apache/iceberg/issues/16064) ⭐️ 7.0/10

Apache Iceberg 社区提出一项规格级提案，为半结构化（VARIANT）列引入虚拟字段元数据，使查询引擎能够透明地解析字段类型并进行谓词下推，而无需用户手动管理模式演化。 该机制能大幅提升半结构化数据的查询性能，并简化模式演化处理，使 Iceberg 在数据湖仓架构中对 VARIANT 等半结构化数据的支持更加完善，惠及使用 Spark、Trino 等引擎的大数据用户。 该提案尚处规划阶段（GitHub Issue），核心是为 VARIANT 列中已知字段路径提供类型化元数据，引擎可利用这些元数据进行谓词下推和透明列重定向，但具体实现细节有待社区讨论。

github · jeffbuser · Apr 25, 03:00

**背景**: Apache Iceberg 是一种开源高性能表格式，专为数据湖中的大规模分析表设计，支持多种计算引擎同时安全地操作同一张表。VARIANT 是 Iceberg v3 引入的半结构化数据类型，用于高效存储和查询 JSON 等灵活格式的数据。谓词下推是一种查询优化技术，通过将过滤条件下推到数据源，减少数据传输和处理量，显著提升性能。虚拟字段元数据则在表元数据中声明半结构化列内已知字段路径，使引擎无需解析整个文档即可直接访问特定字段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_Iceberg">Apache Iceberg</a></li>
<li><a href="https://github.com/apache/iceberg/issues/16064">Virtual Field Metadata for Semi-Structured (VARIANT) Columns ...</a></li>
<li><a href="https://www.dremio.com/wiki/predicate-pushdown/">What is Predicate Pushdown? - Dremio</a></li>

</ul>
</details>

**标签**: `#apache-iceberg`, `#table-format`, `#semi-structured-data`, `#query-optimization`, `#schema-evolution`

---

<a id="item-data-warehouse-4"></a>
## [Apache Iceberg 提出 File Format API 提案](https://github.com/apache/iceberg/issues/12225) ⭐️ 7.0/10

Apache Iceberg 社区提交了 File Format API 提案（#12225），旨在为 Avro、Parquet 和 ORC 等文件格式提供统一接口，解决特性支持不一致问题，并简化新格式的集成。该设计已被社区采纳，相关 API 已于 2026 年 2 月 20 日正式发布。 这一 API 消除了因不同文件格式之间实现差异导致的功能碎片化，确保 Iceberg V3 规范的新特性能够一致应用于所有格式，降低了引擎适配成本，并为 AI 数据格式等新兴场景打开了方便之门，对数据湖技术发展意义重大。 提案通过定义可插拔的文件格式接口，使 Parquet、Avro、ORC 等格式对上层引擎透明，新格式只需实现同一套 API 即可无缝集成。Iceberg 的 Java 实现中，该 API 已支持 V3 规范引入的列类型和默认值等新特性在多个格式间一致落地。

github · pvary · Apr 20, 11:57

**背景**: Apache Iceberg 是一种开源高性能表格式，广泛应用于数据湖场景，支持 Avro、Parquet 和 ORC 三种文件格式。随着 Iceberg V3 规范的演进，许多新功能需要在文件格式层面实现，但此前缺乏统一接口，各格式的功能支持进度不一。与此同时，面向 AI 等场景的新文件格式不断涌现，社区需要一个标准化的集成方式以降低开发门槛。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_Iceberg">Apache Iceberg</a></li>
<li><a href="https://iceberg.apache.org/blog/apache-iceberg-file-format-api/">Introducing the Apache Iceberg File Format API - Apache Iceberg™</a></li>
<li><a href="https://www.dremio.com/blog/beyond-parquet-the-apache-iceberg-file-format-api-and-the-ai-era/">Beyond Parquet: The Apache Iceberg File Format API and the AI Era | Dremio</a></li>

</ul>
</details>

**标签**: `#Apache Iceberg`, `#File Format`, `#API Design`, `#Data Engineering`, `#Open Source`

---

<a id="item-data-warehouse-5"></a>
## [Iceberg 提议为 loadTable API 增加快照与元数据日志裁剪参数](https://github.com/apache/iceberg/issues/15947) ⭐️ 7.0/10

Apache Iceberg 社区在 GitHub 上发起提议(#15947)，计划为 REST API 的 loadTable 响应增加查询参数，以便在加载表时裁剪 snapshot-log 和 metadata-log 这两个随着提交不断增长的无界数组。 对于拥有大量提交历史的 Iceberg 表，当前响应中包含的全量快照日志和元数据日志会导致负载显著增大，影响性能。新参数可以让客户端按需获取部分日志，从而提高效率并减少资源消耗。 snapshot-log 记录每次快照操作的 ID 和时间戳，metadata-log 记录每次提交对应的元数据文件信息，两者均随提交线性增长。提议的查询参数允许客户端指定限制或偏移量，从而仅返回最新的若干条目。

github · laserninja · Apr 12, 02:33

**背景**: Apache Iceberg 是一种面向大规模分析表的高性能开放表格式，支持快照机制实现时间旅行和读隔离。loadTable 是 Iceberg REST Catalog 中的接口，返回表的完整元数据。其中 snapshot-log 数组用于维护表变更历史，metadata-log 数组用于记录元数据文件的演变。当表经过数千次提交后，这些日志会变得非常庞大，影响数据传输和解析效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_Iceberg">Apache Iceberg</a></li>
<li><a href="https://iceberg.apache.org/docs/latest/branching/">Branching and Tagging - Apache Iceberg™</a></li>

</ul>
</details>

**标签**: `#apache-iceberg`, `#rest-api`, `#metadata`, `#scalability`, `#performance`

---

<a id="item-data-warehouse-6"></a>
## [Delta Lake 协议新增重定向功能规范提案](https://github.com/delta-io/delta/pull/3705) ⭐️ 7.0/10

该 PR 为 Delta Lake 协议添加了详细的“重定向”功能规范，包括功能的启用、禁用以及查询重定向的完整流程定义。 此协议变更可能标准化查询路由行为，影响 Delta Lake 生态中数据的访问路径与系统集成方式，对湖仓一体架构的灵活性有重要潜在影响。 规范具体描述了重定向功能的管理操作和查询时的重定向执行逻辑，但尚未包含实现细节或合并状态。

github · kamcheungting-db · Mar 14, 20:12

**背景**: Delta Lake 使用协议规范来定义表所需的功能集，通过 minReaderVersion 和 minWriterVersion 控制兼容性。协议变更提案是引入新功能的重要步骤，需要经过社区评审。重定向通常指将针对 Delta 表的查询请求转发到其他表或系统（例如 Hive 表），以支持数据迁移、联邦查询等场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/delta-io/delta/blob/master/PROTOCOL.md">delta/PROTOCOL.md at master · delta-io/delta · GitHub What is Delta Lake in Databricks? | Databricks on AWS Welcome to the Delta Lake documentation | Delta Lake Delta Lake feature compatibility and protocols - Azure ... What is Delta Lake in Azure Databricks? - Azure Databricks Home - Delta Lake Documentation Delta Lake : Internals of transaction logs - Medium</a></li>

</ul>
</details>

**标签**: `#Delta Lake`, `#Protocol`, `#Redirection`, `#Specification`, `#Documentation`

---

<a id="item-data-warehouse-7"></a>
## [提议为 Apache Hudi 增加分区软删除功能](https://github.com/apache/hudi/issues/18774) ⭐️ 7.0/10

Apache Hudi 社区在 issue #18774 中提出了一项新功能提案，旨在支持分区级别的软删除，允许用户在永久删除数据之前恢复被删除的分区。 该功能能够防止因误操作或提前清理造成的数据永久丢失，提升数据管理安全性，对需要合规审计、数据恢复或时间旅行的场景尤为关键。 目前 Hudi 的 delete_partition API 会立即替换分区内所有文件，清理服务随后将文件及元数据表（MDT）记录永久删除；新提案在软删除发生后、全清理前的窗口期内提供数据恢复机会，此后读取操作可根据配置过滤软删除的数据。

github · kbuci · May 18, 22:43

**背景**: Apache Hudi 是一个开源数据湖平台，基于 Hadoop 分布式文件系统构建，提供 ACID 事务、更新和删除等数据库式功能，底层管理 Parquet 格式的数据文件。其元数据表（MDT）和索引用于加速查询并追踪文件状态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/hudi">Hudi</a></li>

</ul>
</details>

**标签**: `#Apache Hudi`, `#Data Management`, `#Soft Delete`, `#Feature Proposal`, `#Data Lakes`

---

<a id="item-data-warehouse-8"></a>
## [Apache Hudi RFC-59 提案：设计描述与实现细节](https://github.com/apache/hudi/issues/15335) ⭐️ 7.0/10

Apache Hudi 社区提交了 RFC-59 提案，包含问题描述、设计概念和代码实现，旨在对 Hudi 引入重大变更。 该 RFC 提案标志着 Apache Hudi 的重大演进，可能引入新功能或优化，对数据湖的管理和增量处理产生深远影响。 提案提供了详细的设计概念和初步代码实现，目前处于 RFC 阶段，尚未获得社区批准。

github · hudi-bot · Dec 11, 23:17

**背景**: Apache Hudi 是一个开源数据湖平台，为数据湖提供数据库级功能，如 ACID 事务、高效更新和删除等。RFC（请求评论）是 Hudi 社区用于讨论和批准重大变更的流程，该提案是 Hudi 的 RFC-59。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hudi.apache.org/">Apache Hudi | An Open Source Data Lake Platform | Apache Hudi</a></li>

</ul>
</details>

**标签**: `#Apache Hudi`, `#RFC`, `#Data Lake`, `#Design Proposal`, `#Open Source`

---

<a id="item-data-warehouse-9"></a>
## [Apache Hudi RFC 提出新 Table API 以优化查询引擎集成](https://github.com/apache/hudi/issues/15195) ⭐️ 7.0/10

Apache Hudi 社区发起 RFC #15195，提议设计一套新的 Table API，以增强与 Trino、Presto 等查询引擎的集成。 此举将显著提升 Hudi 在数据湖仓生态中的互通性，使更多查询引擎能高效访问 Hudi 表，加速企业数据分析流程。 该 RFC 目前处于任务规划阶段，关联 JIRA HUDI-4142，属于史诗 HUDI-4141，具体 API 设计细节尚未公布。

github · hudi-bot · Dec 11, 23:15

**背景**: Apache Hudi 是一个开源数据湖平台，在数据湖上提供 ACID 事务、高效 upsert/delete 等数据库级能力。数据湖仓一体架构融合了数据湖的灵活性和数据仓库的管理特性，已成为现代数据基础设施的主流。Trino 和 Presto 是流行的分布式 SQL 查询引擎，常用于数据湖上的交互式分析。新的 Table API 旨在标准化 Hudi 表与引擎间的交互模式，简化集成工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hudi.apache.org/">Apache Hudi | An Open Source Data Lake Platform | Apache Hudi</a></li>
<li><a href="https://en.wikipedia.org/wiki/Data_lakehouse">Data lakehouse</a></li>
<li><a href="https://grokipedia.com/page/hudi">Hudi</a></li>

</ul>
</details>

**标签**: `#Apache Hudi`, `#RFC`, `#Table APIs`, `#Query Engines`, `#Data Lakehouse`

---

<a id="item-data-warehouse-10"></a>
## [ClickHouse Cloud 推出多阶段分布式查询执行](https://clickhouse.com/blog/multi-stage-distributed-query-execution-clickhouse-cloud) ⭐️ 7.0/10

ClickHouse Cloud 宣布推出多阶段分布式查询执行功能，能横跨多个节点扩展单条查询，加速大型连接和高基数聚合。 此举让 ClickHouse Cloud 在处理复杂分析查询时能更好利用集群资源，显著提升大表连接和高基数聚合的查询性能，对依赖实时分析的云用户有重要意义。 该功能基于分布式查询调度器，将查询分解为多个阶段并行执行，从而突破单节点资源限制，特别优化了 JOIN 和 COUNT(DISTINCT) 等操作。

rss · ClickHouse Blog · May 28, 08:56

**背景**: 分布式查询执行是现代分析数据库的关键能力，它通过将查询分解为多个阶段并在多个节点上并行处理，来突破单节点性能瓶颈。ClickHouse Cloud 此前已支持并行副本功能，但多阶段分布式执行提供了更细粒度的任务调度和更高效的资源利用，尤其适用于涉及大量数据重分布的连接和聚合查询。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tipranks.com/news/private-companies/clickhouse-enhances-cloud-query-performance-with-multi-stage-distributed-execution">ClickHouse Enhances Cloud Query Performance With Multi-Stage Distributed Execution - TipRanks.com</a></li>
<li><a href="https://howqueryengineswork.com/13-distributed-query.html">Distributed Query Execution - How Query Engines Work</a></li>

</ul>
</details>

**标签**: `#distributed computing`, `#query optimization`, `#ClickHouse`, `#cloud databases`, `#analytics`

---


## 综合

<a id="item-general-1"></a>
## [uv 0.11.17 发布：支持构建时的 import-names 及新标志](https://github.com/astral-sh/uv/releases/tag/0.11.17) ⭐️ 6.0/10

uv 0.11.17 版本新增了多项增强功能，包括在构建时支持 import-names 和 import-namespaces（符合 PEP 794），为多个命令添加了 --no-editable-package 标志，离线状态下跳过直接 URL 锁的新鲜度检查，以及改进了错误提示和性能。 这些改进提升了 Python 包管理的灵活性与开发体验：import-names 支持使构建命名空间包更符合规范，--no-editable-package 允许精细控制可编辑安装，离线新鲜度优化避免了网络不可用时的错误，对单仓库和多环境工作流尤其重要。 关键细节包括：通过 pyproject.toml 中的 [tool.uv] 可声明 import-names 列表以正确暴露顶层模块；--no-editable-package 接受包名参数，可指定哪些本地包不以可编辑模式安装；离线新鲜度检查仅跳过直接 URL 的锁文件验证，间接依赖仍会校验。

github · github-actions[bot] · May 28, 20:41

**背景**: uv 是 Astral 团队用 Rust 编写的高性能 Python 包与项目管理器，旨在替代 pip、pip-tools 和 virtualenv 等工具，提供类似 Cargo 的一体化体验。它支持依赖管理、虚拟环境创建、包构建与发布。0.11.17 版本进一步落实 PEP 794 标准，通过在构建配置中显式声明导入名称，解决命名空间包构建的模糊性问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gist.github.com/jzumwalt/0c4bdbd64d68199cf2e6af1e090038bd">The Definitive Guide to UV: Python Packaging in Production</a></li>
<li><a href="https://stackoverflow.com/questions/79794657/how-to-build-a-single-file-namespace-library-with-uv">How to build a single-file namespace library with uv?</a></li>

</ul>
</details>

**标签**: `#python`, `#package-manager`, `#uv`, `#release`, `#open-source`

---


