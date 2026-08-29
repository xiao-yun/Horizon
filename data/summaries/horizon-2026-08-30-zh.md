# Horizon 每日速递 - 2026-08-30

> From 38 items, 25 important content pieces were selected
>
> ## AI 与工具
> 1. [腾讯发布并开源混元 Hy4 Preview 模型](#item-ai-tools-1) ⭐️ 8.0/10 · HN · 19:33
> 2. [DHS 利用冷门法律调查记者与公民团体](#item-ai-tools-2) ⭐️ 8.0/10 · HN · 18:44
> 3. [良好工程文化是最大生产力提升，而非 AI](#item-ai-tools-3) ⭐️ 8.0/10 · HN · 17:19
> 4. [三星处理内内存（PIM）架构深度分析：AI 加速潜力与集成挑战](#item-ai-tools-4) ⭐️ 8.0/10 · HN · 06:06
> 5. [仅凭漏洞传闻，AI 编码代理即可找到安全漏洞利用](#item-ai-tools-5) ⭐️ 8.0/10 · Simon Willison · 22:12
> ## 数据仓库
> 1. [Apache Iceberg 提议为字符串类型引入列级排序规则](#item-data-warehouse-1) ⭐️ 8.0/10 · GitHub · 22:56
> 2. [Apache Iceberg 提议新增自动化增量聚类功能。](#item-data-warehouse-2) ⭐️ 7.0/10 · GitHub · 02:52
> 3. [Apache Iceberg 提议新增 Variant 数据类型支持](#item-data-warehouse-3) ⭐️ 7.0/10 · GitHub · 05:39
> 4. [Apache Iceberg 提议在 CDC 场景中对等值删除进行去重优化](#item-data-warehouse-4) ⭐️ 7.0/10 · GitHub · 00:11
> 5. [Apache Iceberg 提议在表规范中支持相对路径](#item-data-warehouse-5) ⭐️ 7.0/10 · GitHub · 22:56
> 6. [Iceberg 提案：高效列级更新以支持宽表 AI/ML 工作负载](#item-data-warehouse-6) ⭐️ 7.0/10 · GitHub · 22:14
> 7. [Apache Iceberg RFC 提出派生列支持](#item-data-warehouse-7) ⭐️ 7.0/10 · GitHub · 12:22
> 8. [Apache Iceberg 提议支持默认值表达式](#item-data-warehouse-8) ⭐️ 6.0/10 · GitHub · 00:51
> 9. [Apache Iceberg 提议改进列统计信息存储方式](#item-data-warehouse-9) ⭐️ 6.0/10 · GitHub · 22:56
> 10. [Apache Hudi 提出分区软删除功能提案](#item-data-warehouse-10) ⭐️ 6.0/10 · GitHub · 22:43
> ## GitHub 趋势
> 1. [K-Dense-AI/scientific-agent-skills +1604⭐: K-Dense-AI/scientific-agent-skills：科学技能库单日获 1604 星](https://github.com/K-Dense-AI/scientific-agent-skills) ⭐️ 8.0/10 · GH Trending · 22:42
> 2. [THU-MAIC/OpenMAIC +907⭐: THU-MAIC/OpenMAIC 单日新增 907 星：开源多智能体互动课堂](https://github.com/THU-MAIC/OpenMAIC) ⭐️ 8.0/10 · GH Trending · 22:42
> 3. [calesthio/OpenMontage +809⭐: OpenMontage 开源智能视频制作系统单日获 809 星](https://github.com/calesthio/OpenMontage) ⭐️ 8.0/10 · GH Trending · 22:42
> 4. [tailscale/tailcat +790⭐: Tailscale 开源 tailcat：无需控制平面的类 netcat 安全连接工具](https://github.com/tailscale/tailcat) ⭐️ 8.0/10 · GH Trending · 22:42
> 5. [anthropics/claude-plugins-official +356⭐: Anthropic 发布 Claude Code 官方插件精选目录](https://github.com/anthropics/claude-plugins-official) ⭐️ 8.0/10 · GH Trending · 22:42
> 6. [tt-a1i/archify +3927⭐: tt-a1i/archify：AI Agent 图表生成技能获爆发式关注](https://github.com/tt-a1i/archify) ⭐️ 7.0/10 · GH Trending · 22:42
> 7. [bilawalsidhu/gods-eye-view +1870⭐: 开源项目 God's Eye View：在浏览器中用真实空间数据模拟间谍卫星](https://github.com/bilawalsidhu/gods-eye-view) ⭐️ 7.0/10 · GH Trending · 22:42
> 8. [abi/screenshot-to-code +558⭐: AI 截图转代码工具 abi/screenshot-to-code 今日获 558 星](https://github.com/abi/screenshot-to-code) ⭐️ 7.0/10 · GH Trending · 22:42
> 9. [every-app/open-seo +517⭐: 开源 SEO 工具 open-seo 单日获 517 星](https://github.com/every-app/open-seo) ⭐️ 7.0/10 · GH Trending · 22:42
> 10. [workweave/router +284⭐: workweave/router 单日涨 284 星，面向智能体系统的 Go 模型路由器](https://github.com/workweave/router) ⭐️ 7.0/10 · GH Trending · 22:42

## AI 与工具

<a id="item-ai-tools-1"></a>
## [腾讯发布并开源混元 Hy4 Preview 模型](https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/) ⭐️ 8.0/10

腾讯发布了新一代混合专家（MoE）旗舰模型 Hy4 preview，并将权重开源；该模型拥有 7700 亿总参数、490 亿激活参数，且在训练中首次参与了自动优化训练方法、数据策略、评估框架和底层算子，形成早期递归自我改进回路。 作为大型厂商开源的旗舰 MoE 模型，Hy4 preview 使开发者能够使用和微调高性能模型；其在训练中实现的早期递归自我改进可能为未来 AI 系统自主优化提供新思路，并凭借低成本快速获得大量实际调用，影响开源模型生态格局。 该模型总参数 770B、激活 49B，已有人压缩为约 200GB 的 GGUF 并保持约 98% 性能；其在 OpenRouter 上缓存成本仅 5%，低于常见的 10%/20%，但预览版尚未经过充分后训练，官方正式版基准分数会更高。

hackernews · shenli3514 · Aug 29, 19:33 · [社区讨论](https://news.ycombinator.com/item?id=49492632)

**背景**: 混合专家（MoE）模型通过每次只激活部分参数（Hy4 为 490 亿）来降低推理成本；OpenRouter 是一个聚合多个大模型的统一 API 平台，方便开发者切换和结算。递归自我改进通常指 AI 系统自己改进自身代码或训练流程，Hy4 preview 此处特指它参与优化训练方法、数据策略等自动化流程，而非直接修改自身权重。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/tencent/Hy4-preview">tencent/Hy4-preview - Hugging Face</a></li>
<li><a href="https://openrouter.ai/tencent/hy4-preview">Hy4 preview - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self - improvement - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区讨论总体积极：有人认为 LLM 能完成底层优化但缺少品味，反而提升人类价值；有人引述模型参与训练优化的递归自我改进回路，并讨论其与预测的关联；也有用户关注其在 OpenRouter 上惊人的 token 处理量（数天内数万亿 token）和仅 5% 的缓存成本，同时批评官方发布图表存在“制图罪”（排序和突出方式误导）。

**标签**: `#AI`, `#LLM`, `#open-source`, `#Tencent`, `#machine-learning`

---

<a id="item-ai-tools-2"></a>
## [DHS 利用冷门法律调查记者与公民团体](https://www.theguardian.com/us-news/2026/aug/29/trump-dhs-1509-summons-records-journalists-nonprofits) ⭐️ 8.0/10

据报道，美国国土安全部（DHS）正利用一项冷门的海关法条——1509 传票——获取记者、非营利组织和工会的记录；在某些案件中，DHS 在被告上法庭后撤回传票，以避免法院裁定其合法性。具体案件中，T-Mobile 提供了记者 Fort 六个月超过 1 万条通话和短信记录，而 Google 未予配合。 这使行政机构可在没有事先司法授权的情况下获取敏感通信记录，直接威胁新闻自由和公民社会的隐私；如果此类传票被普遍滥用，可能产生寒蝉效应，压制调查报道和工会活动。 1509 传票源自《美国法典》第 19 编第 1509 条，本应仅用于海关和进口相关的刑事调查，但 DHS 正将其用于其他目的；法律上，被调查方可以不配合，DHS 若想强制执行必须向法院起诉，而公司选择遵守与否会显著影响后果。

hackernews · firefax · Aug 29, 18:44 · [社区讨论](https://news.ycombinator.com/item?id=49492219)

**背景**: 第 1509 条授权海关及边境保护局（CBP）等机构签发行政传票，调取与进出口和关税有关的账簿、记录和证人证言，无需事先获得法官批准。此前美国国土安全部监察长办公室已批评 CBP 滥用该传票权力。此次报道显示，该工具正被扩大用于记者、非营利组织和工会，引发法律和隐私争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.business-humanrights.org/en/latest-news/usa-ice-has-been-abusing-1509-summonses-to-obtain-data-from-tech-companies-without-judicial-oversight/">USA: ICE has been abusing 1509 summonses to obtain data from...</a></li>
<li><a href="https://www.oig.dhs.gov/news/press-releases/2017/11162017/dhs-oig-cites-cbp-misuse-summons-power">DHS OIG Cites CBP for Misuse of Summons Power | Office of...</a></li>
<li><a href="https://www.law.cornell.edu/uscode/text/19/1509">19 U.S. Code § 1509 - Examination of books and witnesses | U.S. Code</a></li>

</ul>
</details>

**社区讨论**: 评论区普遍批评 DHS 滥用传票，并认为其撤回传票是故意规避法院对合法性的审查；有人强调公司本可不配合，T-Mobile 的屈服与 Google 的拒绝形成对比。也有人建议记者自建邮件基础设施或使用小平台，但担忧小平台被制裁及暴露个人信息。

**标签**: `#surveillance`, `#privacy`, `#civil-liberties`, `#legal`, `#journalism`

---

<a id="item-ai-tools-3"></a>
## [良好工程文化是最大生产力提升，而非 AI](https://newsletter.eng-leadership.com/p/good-culture-is-the-biggest-productivity) ⭐️ 8.0/10

一篇工程领导力通讯文章提出，健康的工程文化比采用 AI 更能提升团队生产力，并在 Hacker News 上引发了关于团队动力与技术炒作的深入讨论。 在 AI 工具被广泛宣传的背景下，这一观点提醒技术管理者不要忽视组织文化、信任和协作等基础因素，对提升长期生产力、创新和员工留存具有重要现实意义。 评论中有人指出 AI 只会加速既有方向——若团队方向错误，AI 会让你更快到达错误地点；也有人认为 AI 采用应由一线人员自下而上推动，而这需要文化鼓励员工自主性。

hackernews · gpi · Aug 29, 17:19 · [社区讨论](https://news.ycombinator.com/item?id=49491568)

**背景**: 工程文化指团队内部协作方式、信任、心理安全感和决策习惯，它影响员工积极性和工作质量。生产力提升不仅取决于工具，还取决于组织环境是否支持高效协作。Hacker News（HN）是一个知名技术社区，常围绕此类管理与技术话题展开深入讨论。

**社区讨论**: 评论总体认同文章观点，并分享了正反经验：有人批评把 Jira 工单自动转化为 PR 的系统令人沮丧且无成果；也有人提到团队成员彼此喜欢、低离职率带来了十年高生产力。多位评论者认为 AI 会加速既有文化，好文化下 AI 助益，坏文化下 AI 加剧问题，并主张 AI 采用应由一线自下而上推动。另有一条简短评论表示自己公司既有良好文化也采用了 AI，暗示两者并非互斥。

**标签**: `#engineering-culture`, `#productivity`, `#AI`, `#leadership`, `#software-engineering`

---

<a id="item-ai-tools-4"></a>
## [三星处理内内存（PIM）架构深度分析：AI 加速潜力与集成挑战](https://chipsandcheese.com/p/hot-chips-2026-samsungs-processing) ⭐️ 8.0/10

Chips and Cheese 对三星在 Hot Chips 2026 上展示的 Processing-in-Memory（PIM）架构进行了技术分析，重点探讨其在 AI 工作负载中的潜力，以及将计算单元集成到内存中所面临的架构和软件挑战。 PIM 通过在内存中直接进行计算来减少数据搬运，有望突破传统冯·诺依曼架构的“内存墙”瓶颈，对高数据密集的 AI 推理/训练和低功耗加速器具有重要意义；三星作为主要内存厂商的推进可能加速该技术的产业落地。 分析指出 PIM 虽能减少数据移动，但矩阵乘法等算子仍需要大量数据在芯片内移动，且软件开发需要精确管理数据位置，限制较多；评论中也提到类似方案在行业会议上并不罕见，实际落地较少。

hackernews · ingve · Aug 29, 06:06 · [社区讨论](https://news.ycombinator.com/item?id=49487341)

**背景**: Processing-in-Memory（PIM）将处理逻辑集成到内存芯片中（如高带宽内存 HBM），以减少内存与处理器之间的数据搬移；Hot Chips 是聚焦高性能芯片和计算机体系结构的年度会议，常发布前沿加速器设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Processing-in-memory">Processing-in-memory</a></li>
<li><a href="https://hotchips.org/">Hot Chips</a></li>

</ul>
</details>

**社区讨论**: 社区讨论整体认可 PIM 是未来方向，但对三星当前实现持怀疑态度：评论指出数据位置管理对多数应用不友好，矩阵乘法仍需要大量数据移动；有人回忆 1980 年代已有类似概念，并提到许多展会上出现的加速器最终未能落地。

**标签**: `#Processing-in-Memory`, `#Hardware`, `#AI Accelerators`, `#Hot Chips`, `#Samsung`

---

<a id="item-ai-tools-5"></a>
## [仅凭漏洞传闻，AI 编码代理即可找到安全漏洞利用](https://simonwillison.net/2026/Aug/28/just-a-rumour-of-a-bug/) ⭐️ 8.0/10

剑桥大学教授、OCaml 核心维护者 Anil Madhavapeddy 报告，OCaml 项目的补丁在讨论分享后约 10 分钟内就出现针对百分号编码路径遍历的探测，其 AI 编码代理仅凭漏洞传闻就能找到利用方法（Claude Fable 拒绝后改用 DeepSeek V4 Pro）。rclone 维护者 Nick Craig-Wood 证实，该项目的 GitHub 安全披露过去一个月超过 40 起，远高于此前十年约 20 起。 这说明 AI 编码代理已将漏洞利用开发时间从数天压缩到数分钟，攻击者可利用公开补丁或讨论的细微线索快速武器化漏洞。它直接冲击传统协同漏洞披露和补丁发布节奏，要求开源项目几乎即时修复，并催生新的安全流程以应对自动化威胁。 探测针对百分号编码目录遍历序列，表明有自动化监视程序持续关注公开仓库。rclone 披露的命中率约 75%，但 GitHub 的 CVE 分配从 2-3 天延迟到 3-4 周，导致维护者只能带着 CVE-PENDING 发布点版本。

rss · Simon Willison · Aug 28, 22:12

**背景**: 协同漏洞披露（CVD）通常要求发现者先私下通知维护者，待补丁完成后再公开，以免攻击者利用时间差。编码代理是能自主理解代码、生成修复和测试的 AI 工具，可以从公开提交和讨论中推断漏洞位置。百分号编码的路径遍历序列（如%2e%2e%2f）用于尝试访问服务器上受限目录之外的文件，是常见攻击手法。开源项目此前依赖数天至数周的修复窗口，但自动化攻击缩短了这一窗口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_coding_agent">AI coding agent</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vulnerability_disclosure">Vulnerability disclosure</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的 rclone 维护者 Nick Craig-Wood 表示，该项目安全披露数量激增，虽然 AI 工具帮助分类和起草修复，但仍占用大量时间；同时 CVE 分配延迟到 3-4 周，导致点版本只能以 CVE-PENDING 发布。他并未否认 AI 攻击趋势，而是证实了维护者面临的实际压力。

**标签**: `#security`, `#AI`, `#vulnerability disclosure`, `#software exploits`, `#coding agents`

---


## 数据仓库

<a id="item-data-warehouse-1"></a>
## [Apache Iceberg 提议为字符串类型引入列级排序规则](https://github.com/apache/iceberg/issues/17620) ⭐️ 8.0/10

Apache Iceberg 提案 #17620 建议在表规范中增加列级排序规则：字符串字段可携带 provider 限定的排序规则（如 icu.en_US-ci），实现大小写不敏感、重音不敏感或区域感知的比较与排序。底层存储仍保持 UTF-8，仅比较逻辑改变；同时存储排序规则感知的最小/最大值，以保证排序规则列的裁剪能力。 目前 Iceberg 仅按 UTF-8 字节比较字符串，无法声明列的大小写/重音不敏感或区域排序；该提案补齐这一能力，使其与 Snowflake、Oracle、PostgreSQL 等系统的排序规则能力对齐。若落地，数据工程师可在 Iceberg 中实现更自然的字符串查询和排序，并保持多引擎协作与分区裁剪效率。 提案中的排序规则采用 provider 限定格式，例如 icu.en_US-ci 表示 ICU provider 下的美国英语大小写不敏感排序规则；存储仍为 UTF-8，只是比较语义改变。新增的排序规则感知最小/最大值会写入元数据，用于分区裁剪和文件跳过，避免全表扫描，但方案目前仍是 Proposal，尚无实现。

github · laskoviymishka · Aug 12, 22:56

**背景**: Apache Iceberg 是一种高性能开源表格式，适用于大型分析表，让 Spark、Trino、Flink、Presto、Hive 等引擎能够安全地同时读写同一张表。排序规则决定字符串如何比较，直接影响排序与等值判断，传统数据库如 Oracle、PostgreSQL、SQL Server 已支持列级或数据库级排序规则。Snowflake 也为 Iceberg 表提供 ICEBERG_DEFAULT_DDL_COLLATION 参数来设置默认排序规则。该提案借鉴这些能力，尝试为 Iceberg 规范补充字符串列级排序规则。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_Iceberg">Apache Iceberg - Wikipedia</a></li>
<li><a href="https://www.postgresql.org/docs/current/collation.html">PostgreSQL: Documentation: 18: 23.2. Collation Support</a></li>
<li><a href="https://docs.snowflake.com/en/user-guide/tables-iceberg">Apache Iceberg™ tables | Snowflake Documentation</a></li>

</ul>
</details>

**标签**: `#apache-iceberg`, `#collation`, `#database-specification`, `#data-engineering`, `#big-data`

---

<a id="item-data-warehouse-2"></a>
## [Apache Iceberg 提议新增自动化增量聚类功能。](https://github.com/apache/iceberg/issues/15473) ⭐️ 7.0/10

Apache Iceberg issue #15473 提议为 Iceberg 增加自动化的增量聚类能力，使相关行在物理文件中就近存放，从而提升数据跳过效率与查询性能。该提案指出，当前 Iceberg 规范对细粒度物理文件聚类尚缺乏一等支持，并提供了详细设计文档。 该功能填补了 Iceberg 在细粒度数据跳过方面的关键空白，有助于减少无关文件扫描、降低 I/O 并加快分析查询。由于 Iceberg 被 Spark、Trino、Flink 等主流引擎广泛采用，这一改进有望惠及大型数据湖上的重要工作负载。 现有 Iceberg 已支持分区演进和隐藏分区，可在不重写数据的情况下调整逻辑布局，但无法在文件内部对相关行进行细粒度物理聚类。提案设计文档见 Google Docs 链接，但 issue 内容未给出具体算法、性能基准或发布时间表。

github · PuspenduBanerjee · Aug 28, 02:52

**背景**: Apache Iceberg 是一种面向大型分析表的高性能开源表格式，允许 Spark、Trino、Flink 等引擎安全地并发操作同一张表。数据跳过通过收集每个文件的统计信息（如最小值/最大值、空值数、行数）来在查询时跳过无关文件。增量聚类则是随着数据更新逐步将相关行组织到同一文件中，而不是全表重写，以维持数据跳过带来的查询性能收益。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_Iceberg">Apache Iceberg</a></li>
<li><a href="https://docs.databricks.com/aws/en/tables/data-skipping">Data skipping | Databricks on AWS</a></li>

</ul>
</details>

**标签**: `#Apache Iceberg`, `#Data Lake`, `#Clustering`, `#Data Skipping`, `#Database`

---

<a id="item-data-warehouse-3"></a>
## [Apache Iceberg 提议新增 Variant 数据类型支持](https://github.com/apache/iceberg/issues/10392) ⭐️ 7.0/10

Apache Iceberg 在 issue #10392 中提议新增 Variant 数据类型，用于对 JSON、Avro、Parquet 等动态半结构化数据进行高效二进制编码。该类型将被实现为 Variant 列，在保留源数据灵活性的同时，让查询引擎能更高效地操作这些数据。 该提议若被采纳，将增强 Apache Iceberg 对半结构化数据的处理能力，使 Spark、Trino、Flink 等查询引擎在访问动态数据时获得更好的性能和更低的存储开销。这对数据湖和开放表格式生态具有重要意义。 该提案侧重于在 Iceberg 中采用列式二进制表示来存储半结构化数据，与 Snowflake 的 VARIANT 和 SQL Server 的 sql_variant 有相似目标，但针对开放表格式进行了优化。目前该 issue 尚未提供完整实现细节或局限性说明。

github · sfc-gh-aixu · Aug 22, 05:39

**背景**: Apache Iceberg 是一种高性能开源表格格式，用于管理大型分析表，允许多种查询引擎（如 Spark、Trino、Flink）在同一数据上安全协作。半结构化数据（如 JSON、Avro、Parquet 文档）常常缺少固定模式，Variant 类型则用于存储任意类型值，以二进制方式封装，Snowflake 等系统已经引入类似概念。Avro 是一种紧凑的二进制序列化框架，适合存储和传输带有模式的数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_Iceberg">Apache Iceberg</a></li>
<li><a href="https://docs.snowflake.com/en/sql-reference/data-types-semistructured">Semi-structured data types | Snowflake Documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apache_Avro">Apache Avro</a></li>

</ul>
</details>

**标签**: `#apache-iceberg`, `#variant-type`, `#semi-structured-data`, `#query-engines`, `#data-engineering`

---

<a id="item-data-warehouse-4"></a>
## [Apache Iceberg 提议在 CDC 场景中对等值删除进行去重优化](https://github.com/apache/iceberg/issues/15336) ⭐️ 7.0/10

Apache Iceberg 在 issue #15336 中提出一项优化：为 Flink CDC 工作负载增加检查点级（checkpoint-scoped）的去重缓存，以跳过同一检查点内对相同行键的冗余等值删除操作。该方案旨在减少不必要的删除文件生成，缓解 HDFS NameNode 的 RPC 压力。 在 CDC 管道中，UPDATE 会产生 DELETE + INSERT，Flink 逐条处理会导致删除记录膨胀 5-10 倍，产生大量小删除文件并加重 NameNode 负载。该优化有望显著降低文件开销和元数据压力，提升 Iceberg 在实时 CDC 场景下的可扩展性。 该提案针对 Flink CDC 工作负载，由于每个 UPDATE 生成 DELETE + INSERT，且 Flink 缺乏批量去重机会，同一检查点内同一行键常被删除多次。通过检查点级去重缓存跳过冗余删除，可减少 5-10 倍删除记录；目前该优化仍在提案/讨论阶段（issue #15336）。

github · wangyum · Aug 16, 00:11

**背景**: Apache Iceberg 中的等值删除（equality delete）按列值标记删除行，例如 `id = 5`，并以 equality delete file 形式存储；与位置删除（position delete）不同，它不依赖具体文件位置。CDC（变更数据捕获）用于将数据库增量变更同步到数据仓库/数据湖，其中 UPDATE 通常表现为先删除后插入。HDFS NameNode 维护文件和目录元数据并处理所有 RPC 请求；大量小文件或删除文件会增加 RPC 调用，影响集群响应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://iceberg.apache.org/spec/">Spec - Apache Iceberg</a></li>
<li><a href="https://risingwave.com/blog/the-equality-delete-problem-in-apache-iceberg/">The Equality Delete Problem in Apache Iceberg | RisingWave</a></li>
<li><a href="https://support.huaweicloud.com/intl/en-us/cmpntguide-mrs/mrs_01_1672.html">Optimizing HDFS NameNode RPC QoS_ HDFS Performance...</a></li>

</ul>
</details>

**标签**: `#apache-iceberg`, `#cdc`, `#flink`, `#deduplication`, `#performance-optimization`

---

<a id="item-data-warehouse-5"></a>
## [Apache Iceberg 提议在表规范中支持相对路径](https://github.com/apache/iceberg/issues/13141) ⭐️ 7.0/10

Apache Iceberg 社区在 #13141 号提案中，提议在表规范中新增相对路径支持，并让新建表默认使用相对路径，以消除表迁移时的元数据重写。 这一改动将显著简化 Iceberg 表的迁移与可移植性：移动表位置（例如跨云或跨存储桶）时无需重写元数据文件中的绝对路径，从而减少运维成本并降低出错风险。 提案目前仅涉及 Table 规范（View 与 REST 尚未勾选），完整设计见 s.apache.org/iceberg-spec-relative-path；当前 Iceberg 使用绝对 URI 记录文件路径，移动表时必须进行元数据重写。

github · talatuyarer · Aug 12, 22:56

**背景**: Apache Iceberg 是一种开源大规模分析表格式，通过表规范定义元数据、文件路径等，使 Spark、Trino、Flink 等引擎能同时安全操作同一张表。Iceberg 表元数据中记录了数据文件、清单文件的路径；现有表规范使用绝对 URI，因此移动表位置后需要重写这些路径以保持一致性。所谓的表规范（Table Spec）是 Iceberg 社区维护的规范文档，不同版本定义兼容特性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mail-archive.com/issues@iceberg.apache.org/msg173342.html">[I] Relative Path Support In Table Spec [iceberg]</a></li>
<li><a href="https://iceberg.apache.org/spec/">Spec - Apache Iceberg™</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apache_Iceberg">Apache Iceberg</a></li>

</ul>
</details>

**标签**: `#apache-iceberg`, `#data-engineering`, `#table-format`, `#metadata-management`, `#data-lake`

---

<a id="item-data-warehouse-6"></a>
## [Iceberg 提案：高效列级更新以支持宽表 AI/ML 工作负载](https://github.com/apache/iceberg/issues/15146) ⭐️ 7.0/10

Apache Iceberg 社区于 2026 年 1 月 26 日提交了 issue #15146 提案，提出引入列级更新机制，使引擎能够只将发生变更的列写入独立的列文件，而将未变更的列保留在原始基础文件中，读取时再高效拼接。该提案旨在解决现有行级原语在处理宽表时产生的写放大问题。 在特征存储和向量数据库等场景中，表通常包含数千列，而更新往往只涉及少量特征（如刷新嵌入、标签或模型分数）。当前 Copy-on-Write 和 Merge-on-Read 原语均以行为粒度操作，会导致大量不必要的数据重写与 I/O；列级更新可显著降低写放大、提升性能，对 AI/ML 数据基础设施具有重要价值。 该设计明确不覆盖部分行更新（即只影响部分行的更新），专注于全表的列变更；引擎写入独立列文件后，读取时需要将基础文件与新列文件拼接，可能引入额外的读放大或查询复杂度。

github · anuragmantri · Aug 12, 22:14

**背景**: Apache Iceberg 是一种开源高性能分析表格式，支持 Spark、Flink、Trino 等多个引擎并发读写同一张表。其更新原语包括 Copy-on-Write（COW）和 Merge-on-Read（MOR）：COW 在更新时重写整个数据文件，MOR 将更新写入单独文件并在读取时合并，两者都以行为单位操作。特征存储和向量数据库常采用宽表存储机器学习特征、嵌入向量等，更新少数列时行级操作会造成巨大的存储和计算浪费，即写放大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/apache/iceberg/issues/15146">Efficient column updates in Iceberg · Issue #15146 · apache/iceberg</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apache_Iceberg">Apache Iceberg</a></li>

</ul>
</details>

**标签**: `#apache-iceberg`, `#data-engineering`, `#machine-learning`, `#database-internals`, `#performance`

---

<a id="item-data-warehouse-7"></a>
## [Apache Iceberg RFC 提出派生列支持](https://github.com/apache/iceberg/issues/15923) ⭐️ 7.0/10

Apache Iceberg 在 RFC #15923 中提议将派生列（derived columns）加入表格式规范，并提供了提案文档链接。 如果该提案被采纳，派生列可以让查询直接使用预计算或基于表达式的列，减少重复计算并提高分析查询效率，对使用 Iceberg 的数据仓库和数据湖生态有潜在影响。 该 RFC 目前仅勾选了 Table 和 Other 规范项，尚未涉及 View、REST、Puffin 或 Encryption；提案仍处于讨论阶段，尚无实现细节。

github · ScrapCodes · Aug 10, 12:22

**背景**: Apache Iceberg 是一种面向大规模分析表的高性能开源表格式，解决了 Hive 表在数据湖中的性能和一致性问题，支持 Spark、Trino、Flink 等引擎并发访问同一张表。派生列通常指由常量、表达式或函数计算得出的列，而非存储在源数据中的原始列。在表格式规范中支持派生列，意味着可以在元数据中定义这类计算列，供查询引擎直接使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_Iceberg">Apache Iceberg</a></li>
<li><a href="https://www.ibm.com/docs/en/db2-for-zos/12.0.0?topic=statement-selecting-derived-columns">Selecting derived columns</a></li>

</ul>
</details>

**标签**: `#apache-iceberg`, `#data-engineering`, `#table-format`, `#rfc`, `#derived-columns`

---

<a id="item-data-warehouse-8"></a>
## [Apache Iceberg 提议支持默认值表达式](https://github.com/apache/iceberg/issues/17616) ⭐️ 6.0/10

Apache Iceberg 议题 #17616 提出将默认值支持从字面常量扩展到值表达式，并附上了规范 PR #16777 和设计文档链接。 该提案若被采纳，可让 Iceberg 表模式支持更灵活、更贴近 SQL 的默认值表达式，减少数据摄取时的特殊处理，并提升与 Spark、Trino、Flink 等 SQL 引擎的兼容性。 该变更属于表规范（Table 已勾选，View、REST 等未勾选），参考了 Apache 邮件列表中《Extending Iceberg expressions》的讨论；目前提案仍在讨论阶段，未有社区评论。

github · danielcweeks · Aug 15, 00:51

**背景**: Apache Iceberg 是一种开源的大规模分析表格式，让 Spark、Trino、Flink 等引擎能安全地在同一数据湖表上协作。SQL 中的 DEFAULT 约束可为列指定默认值，通常默认值是字面常量；MySQL 等数据库已经允许使用表达式作为默认值，并用括号与字面常量区分。该提案希望将类似能力引入 Iceberg 表规范，使建表时可以用表达式生成默认值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_Iceberg">Apache Iceberg</a></li>
<li><a href="https://dev.mysql.com/doc/refman/8.4/en/data-type-defaults.html">MySQL 8.4 Reference Manual :: 13.6 Data Type Default Values</a></li>
<li><a href="https://www.w3schools.com/sql/sql_ref_default.asp">SQL DEFAULT</a></li>

</ul>
</details>

**标签**: `#apache-iceberg`, `#database-schema`, `#data-engineering`, `#sql`, `#table-format`

---

<a id="item-data-warehouse-9"></a>
## [Apache Iceberg 提议改进列统计信息存储方式](https://github.com/apache/iceberg/issues/13153) ⭐️ 6.0/10

Apache Iceberg 在 issue #13153 中提出改进列统计信息存储的方案，指出当前基于映射（map）的存储结构在列数增加时会导致内存开销过大，并且无法按需投影特定统计值（如仅读取某列的空值计数），同时还存在类型擦除问题。 该提案旨在解决大规模宽表的性能瓶颈，如果实现，可降低查询规划阶段的内存占用并提升数据跳过效率，对依赖 Iceberg 的数据湖和 Spark、Trino、Flink 等查询引擎用户有实际影响。 当前列统计信息存储为字段 ID 到值的映射，涵盖上下界、value/null 计数和大小等；问题特别指出无法对特定统计列进行投影，且类型擦除导致原始类型信息（如上下界的原始类型）在运行时不可用。

github · nastra · Aug 12, 22:56

**背景**: Apache Iceberg 是一种开源高性能分析表格式，用于管理数据湖中的大规模表，支持 Spark、Trino、Flink 等多个引擎同时对同一数据集进行操作。列统计信息是数据库中记录列数据分布（如最小值、最大值、空值计数）的元数据，查询优化器可利用这些信息做分区裁剪和数据跳过。当前 Iceberg 将这些统计信息以字段 ID 到值的映射形式存储，因此必须整体读取，而不能只读取某列或某类统计值；此外，映射中的通用值类型在编译后会被擦除，导致无法在运行时恢复原始类型信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_Iceberg">Apache Iceberg</a></li>
<li><a href="https://en.wikipedia.org/wiki/Type_erasure">Type erasure</a></li>

</ul>
</details>

**标签**: `#apache-iceberg`, `#data-engineering`, `#column-statistics`, `#storage-format`, `#database-internals`

---

<a id="item-data-warehouse-10"></a>
## [Apache Hudi 提出分区软删除功能提案](https://github.com/apache/hudi/issues/18774) ⭐️ 6.0/10

Apache Hudi 在 issue #18774 中提出了分区软删除支持提案。该提案允许在执行 delete_partition 后暂时保留文件和元数据表（MDT）及索引中的引用，直到后续清理阶段才真正删除，用户在此期间可以恢复数据。 该功能可以降低因误删或过早清理分区导致的数据丢失风险，使数据湖上的分区管理更加安全。这与云对象存储中常见的软删除保护机制一致，对需要频繁删除和恢复分区的大数据工程团队尤其有价值。 目前 Hudi 的 delete_partition API 会替换分区内的所有文件，clean 表服务在满足条件后会从 MDT 删除文件和条目。该提案仍是 WIP（进行中）讨论，尚未实现；软删除与最终清理之间的保留期将是恢复窗口。

github · kbuci · May 18, 22:43

**背景**: Apache Hudi 是一个开源数据湖仓平台，为数据湖提供 ACID 事务、高效的更新与删除（upsert/delete）等数据库能力。分区是表的逻辑划分，便于按维度管理数据生命周期；delete_partition 删除分区文件，clean 服务随后从元数据表（MDT）和索引中清除相关条目。软删除是存储系统中的常见做法，例如 Google Cloud Storage 和 Azure Blob 都支持在保留期内恢复被删除或覆盖的对象。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hudi.apache.org/">Apache Hudi | An Open Source Data Lake Platform | Apache Hudi</a></li>
<li><a href="https://docs.cloud.google.com/storage/docs/soft-delete">Soft delete overview | Cloud Storage | Google Cloud Documentation</a></li>

</ul>
</details>

**标签**: `#apache-hudi`, `#data-lake`, `#partition-management`, `#soft-delete`, `#data-engineering`

---


