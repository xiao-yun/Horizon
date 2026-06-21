---
layout: default
title: "Horizon Summary: 2026-06-22 (ZH)"
date: 2026-06-22
lang: zh
---

> From 48 items, 25 important content pieces were selected
>
> ## AI 与工具
> 1. [2016 年经典重读：宁愿重复代码，不做错误抽象](#item-ai-tools-1) ⭐️ 8.0/10 · HN · 16:08
> 2. [Peter Norvig 经典教程：用 Python 编写 Lisp 解释器（2010）](#item-ai-tools-2) ⭐️ 8.0/10 · HN · 15:36
> 3. [Anthropic 要求 Claude 验证政府 ID 引发争议](#item-ai-tools-3) ⭐️ 7.0/10 · HN · 12:44
> 4. [个人网站使用 JSON-LD 结构化数据的实用指南](#item-ai-tools-4) ⭐️ 6.0/10 · HN · 18:51
> 5. [用 APL 编写的 3D 体素游戏引擎](#item-ai-tools-5) ⭐️ 6.0/10 · HN · 08:04
> ## 数据仓库
> 1. [Apache Iceberg 提议新增 Variant 数据类型](#item-data-warehouse-1) ⭐️ 8.0/10 · GitHub · 12:52
> 2. [Apache Iceberg v4 规范新增 varchar 和 char 类型提案](#item-data-warehouse-2) ⭐️ 7.0/10 · GitHub · 13:55
> 3. [Apache Iceberg REST 目录新增新鲜度感知表加载功能](#item-data-warehouse-3) ⭐️ 7.0/10 · GitHub · 00:50
> 4. [Apache Iceberg 拟增加对 Flink 水印和计算列的元数据支持](#item-data-warehouse-4) ⭐️ 7.0/10 · GitHub · 03:53
> 5. [提议：为 Iceberg Kafka Connect Worker 添加背压检测](#item-data-warehouse-5) ⭐️ 7.0/10 · GitHub · 00:01
> 6. [Delta Lake 协议新增重定向规范提案](#item-data-warehouse-6) ⭐️ 7.0/10 · GitHub · 20:12
> 7. [Apache Hudi 提出分区软删除功能提案](#item-data-warehouse-7) ⭐️ 7.0/10 · GitHub · 22:43
> 8. [Iceberg Spark 集成拟支持提交时捕获 Parquet 页脚指标](#item-data-warehouse-8) ⭐️ 6.0/10 · GitHub · 15:58
> 9. [Iceberg REST 目录拟添加表标签元数据字段](#item-data-warehouse-9) ⭐️ 6.0/10 · GitHub · 08:00
> 10. [Apache Hudi RFC-59 新功能提案](#item-data-warehouse-10) ⭐️ 6.0/10 · GitHub · 23:17
> ## GitHub 趋势
> 1. [tw93/Pake +1850⭐: Rust 工具 Pake 一键将网页转为桌面应用](https://github.com/tw93/Pake) ⭐️ 8.0/10 · GH Trending · 21:48
> 2. [DeusData/codebase-memory-mcp +1029⭐: DeusData/codebase-memory-mcp：亚毫秒级代码库知识图谱索引](https://github.com/DeusData/codebase-memory-mcp) ⭐️ 8.0/10 · GH Trending · 21:48
> 3. [calesthio/OpenMontage +993⭐: OpenMontage：首个开源智能体视频制作系统](https://github.com/calesthio/OpenMontage) ⭐️ 8.0/10 · GH Trending · 21:48
> 4. [mukul975/Anthropic-Cybersecurity-Skills +445⭐: AI 网络安全技能库发布 754 个结构化技能](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) ⭐️ 8.0/10 · GH Trending · 21:48
> 5. [bytedance/deer-flow +415⭐: ByteDance 开源长周期超级智能体框架 DeerFlow 获 415 星](https://github.com/bytedance/deer-flow) ⭐️ 8.0/10 · GH Trending · 21:48
> 6. [asgeirtj/system_prompts_leaks +366⭐: GitHub 热门仓库泄露多款 AI 模型系统提示词](https://github.com/asgeirtj/system_prompts_leaks) ⭐️ 8.0/10 · GH Trending · 21:48
> 7. [chopratejas/headroom +2617⭐: GitHub 热榜项目 headroom 大幅压缩 LLM 令牌](https://github.com/chopratejas/headroom) ⭐️ 7.0/10 · GH Trending · 21:48
> 8. [palmier-io/palmier-pro +1829⭐: macOS AI 视频编辑器 Palmier Pro 单日获 1829 星走红 GitHub](https://github.com/palmier-io/palmier-pro) ⭐️ 7.0/10 · GH Trending · 21:48
> 9. [penpot/penpot +1131⭐: 开源设计工具 Penpot 单日获 1131 星，社区热捧](https://github.com/penpot/penpot) ⭐️ 7.0/10 · GH Trending · 21:48
> 10. [tursodatabase/turso +543⭐: Turso 获 543 星：基于 Rust 的 SQLite 兼容数据库](https://github.com/tursodatabase/turso) ⭐️ 7.0/10 · GH Trending · 21:48

## AI 与工具

<a id="item-ai-tools-1"></a>
## [2016 年经典重读：宁愿重复代码，不做错误抽象](https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction) ⭐️ 8.0/10

该文章主张，在面对不确定的抽象时，应优先选择代码重复而非创建错误的抽象，近期被重新分享后引发了开发者的广泛讨论。 这一观点挑战了 DRY 原则的教条式应用，提醒开发者过度抽象可能比代码重复带来更严重的维护问题，对软件设计实践具有指导意义。 文章由知名 Ruby 开发者 Sandi Metz 撰写，基于面向对象编程经验；评论中提及函数式编程可减少抽象问题，以及‘唯一真相源’原则的重要性。

hackernews · rafaepta · Jun 21, 16:08 · [社区讨论](https://news.ycombinator.com/item?id=48620090)

**背景**: 在软件工程中，DRY（Don't Repeat Yourself）原则提倡减少代码重复，但有时过早或错误的抽象反而增加复杂性。Sandi Metz 在 2016 年的文章中提出，宁可有重复代码，也不要接受错误的抽象，因为错误的抽象比重复代码更难理解和修改。

**社区讨论**: 社区评论总体认可文章观点，但补充了‘唯一真相源’原则的重要性，认为若重复代码会导致不一致风险则仍需抽象。有开发者分享函数式编程可减少抽象问题，另有实例说明了过度抽象的困境。多数认为低工程化代码比重度过度工程化更易维护。

**标签**: `#abstraction`, `#code-duplication`, `#software-design`, `#programming-principles`, `#technical-debt`

---

<a id="item-ai-tools-2"></a>
## [Peter Norvig 经典教程：用 Python 编写 Lisp 解释器（2010）](https://norvig.com/lispy.html) ⭐️ 8.0/10

一篇 2010 年的经典教程《(How to Write a (Lisp) Interpreter (In Python))》再次被分享到 Hacker News，获得 147 分和 46 条评论，引发新一轮讨论。 该教程以极简的方式展示了从零构建 Lisp 解释器的全过程，是众多开发者入门编程语言设计的首选材料，对理解解释器、编译器原理和语言本质具有深远影响。 教程分为两部分，第一部分用 Python 实现基本的 Lisp 解释器，第二部分增加更多特性；代码量仅数百行，清晰易读，便于自学和教学。

hackernews · tosh · Jun 21, 15:36 · [社区讨论](https://news.ycombinator.com/item?id=48619831)

**背景**: Lisp 是历史悠久的编程语言，以括号语法和代码即数据的哲学著称。Peter Norvig 是知名计算机科学家、Google 研究总监，也是《人工智能：一种现代方法》的作者。该教程借助 Python 的可读性，逐步构建了一个微型 Lisp 解释器，帮助读者直观理解词法分析、解析和求值等核心环节。

**社区讨论**: 社区普遍认为这是经典之作，常被重新发布并引发讨论；不少人推荐《Crafting Interpreters》作为进阶资料，还有用户分享了类似的 Lisp 解释器项目，如 Ribbit。

**标签**: `#lisp`, `#python`, `#interpreter`, `#programming-languages`, `#tutorial`

---

<a id="item-ai-tools-3"></a>
## [Anthropic 要求 Claude 验证政府 ID 引发争议](https://support.claude.com/en/articles/14328960-identity-verification-on-claude) ⭐️ 7.0/10

Anthropic 现要求用户通过第三方服务 Persona 提交政府签发的身份证件进行身份验证，方可使用 Claude。 此举引发对隐私的严重担忧，因为 Persona 可将身份数据用于防欺诈模型训练；同时可能限制非美国用户访问，影响 AI 服务的全球可及性与公平性。 Anthropic 声明自身不将身份数据用于模型训练，但 Persona 可据此改进其防欺诈能力。验证失败可能导致永久无法使用高阶模型，且缺乏重试提示。

hackernews · bathory · Jun 21, 12:44 · [社区讨论](https://news.ycombinator.com/item?id=48618455)

**背景**: Claude 是 Anthropic 推出的大语言模型，与 OpenAI 的 ChatGPT 竞争。Persona 是一家第三方身份验证服务商，其政策允许使用用户数据改善服务。此前 OpenAI 已实施类似身份验证，失败即永久锁定。

**社区讨论**: 社区反应普遍负面，主要担忧包括：Persona 可能利用身份数据训练其模型；验证失败将永久锁定账号且缺乏明确提醒；此举可能加速美国以外大模型的发展，削弱美国 AI 的国际竞争力。部分用户类比网络中立性问题，认为 AI 访问正面临类似审查。

**标签**: `#privacy`, `#identity-verification`, `#AI-policy`, `#digital-rights`, `#Anthropic`

---

<a id="item-ai-tools-4"></a>
## [个人网站使用 JSON-LD 结构化数据的实用指南](https://hawksley.dev/blog/json-ld-explained-for-personal-websites/) ⭐️ 6.0/10

一篇博客文章详细解释了如何为个人网站添加 JSON-LD 结构化数据，以增强搜索引擎结果中的展示效果，并引发了关于在当前 AI 生成摘要时代其实际效果的讨论。 掌握 JSON-LD 可以帮助个人网站在搜索结果中获得更丰富的链接预览（如面包屑、站点名称等），可能提升点击率，但社区指出随着 AI 摘要的普及，用户可能不再点击进入原始页面，从而削弱其价值。 JSON-LD 是通过在 HTML 的<script type='application/ld+json'>标签中嵌入 JSON 数据来实现的，Google 官方文档推荐网站主使用它来提供结构化信息，但仅特定内容类型（如文章、产品、评价）能获得特殊展示。

hackernews · ethanhawksley · Jun 21, 18:51 · [社区讨论](https://news.ycombinator.com/item?id=48621517)

**背景**: JSON-LD（JSON for Linked Data）是 W3C 标准，用于在网页中嵌入结构化数据，帮助搜索引擎理解页面语义。与早期微格式和 RDFa 相比，它更易于实现，因为只需在 JSON 中声明实体及其属性。谷歌等搜索引擎利用这些数据生成富文本摘要、知识面板等。个人网站常使用 Article、Person 等类型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/JSON-LD">JSON-LD</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区讨论中，用户 JdeBP 认为在当前 AI 生成摘要的环境下，这种做法是“打赢上一场战争”，因为用户可能直接从摘要获取信息而不访问原站。klodolph 建议阅读谷歌官方文档，并指出 JSON-LD 的适用场景有限。lenkite 则质疑既然已有语义 HTML，为何还要重复表达。整体上，文章被认为有用，但对实际效果存在怀疑。

**标签**: `#json-ld`, `#seo`, `#structured-data`, `#web-development`, `#hackernews-discussion`

---

<a id="item-ai-tools-5"></a>
## [用 APL 编写的 3D 体素游戏引擎](https://github.com/namgyaaal/avoxelgame) ⭐️ 6.0/10

一位爱好者在 GitHub 上发布了名为 avoxelgame 的 3D 体素游戏引擎，完全用 APL 语言编写，展示了该语言独特的符号式编程在游戏开发中的创新应用。 这表明 APL 不仅能处理数学与数组运算，也可用于实时渲染和游戏逻辑，挑战了人们对其应用领域的传统认知，可能激发更多非主流编程语言的创造性实验。 项目 README 自嘲为‘充满 bug 的热情项目’，目前未提供与其他语言实现的性能对比，但其实现本身就是对 APL 简洁符号表示法的有力展示。

hackernews · sph · Jun 21, 08:04 · [社区讨论](https://news.ycombinator.com/item?id=48616713)

**背景**: APL 是一种诞生于 20 世纪 60 年代的数组编程语言，以密集的特殊符号和极简代码著称。体素引擎通过体积像素构建 3D 世界，常见于《我的世界》等游戏，通常采用 C++等高性能语言开发，用 APL 实现极为罕见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/APL_(programming_language)">APL (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Voxel">Voxel - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区反响积极，用户赞赏项目的诚实和创意，对开发过程充满好奇，也有人希望看到与 C++/Rust 实现的性能对比，并认为体素世界是展现 APL 符号优势的理想场景。

**标签**: `#APL`, `#game-development`, `#voxel-engine`, `#hobby-project`, `#array-programming`

---


## 数据仓库

<a id="item-data-warehouse-1"></a>
## [Apache Iceberg 提议新增 Variant 数据类型](https://github.com/apache/iceberg/issues/10392) ⭐️ 8.0/10

在 GitHub issue #10392 中，有人提议为 Apache Iceberg 新增 Variant 数据类型，用以高效编码和查询 JSON、Avro 等半结构化数据。 这将使 Iceberg 更好地处理数据湖中常见的半结构化数据，提升查询效率，并顺应行业趋势，与 Snowflake、Databricks 等系统的功能看齐。 Variant 类型将在列中保留源数据的灵活性，同时允许查询引擎更高效地操作，但具体二进制编码格式和规范细节尚待设计。

github · sfc-gh-aixu · Apr 30, 12:52

**背景**: Apache Iceberg 是由 Netflix 开发的开源表格式，用于管理数据湖中的大型分析表，支持 Spark、Trino 等多种引擎。半结构化数据（如 JSON）因模式不固定，传统处理方式效率低或需展平。Variant 类型通过内部二进制编码保留动态模式，实现高效存储和查询。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_Iceberg">Apache Iceberg</a></li>

</ul>
</details>

**标签**: `#apache-iceberg`, `#data-engineering`, `#semi-structured-data`, `#variant-type`, `#big-data`

---

<a id="item-data-warehouse-2"></a>
## [Apache Iceberg v4 规范新增 varchar 和 char 类型提案](https://github.com/apache/iceberg/pull/16829) ⭐️ 7.0/10

Apache Iceberg 社区 PR #16829 提议在 v4 规范中正式添加 varchar(N) 和 char(N) 两种带长度的字符串类型。 这将显著改善 Iceberg 与 DB2、Oracle、SQL Server 等传统 SQL 数据库的兼容性，并充分利用 Spark 3.1+ 和 Trino 已有的原生支持，降低迁移成本。 这些类型已在 Spark 3.1.0 起通过 VarcharType(length) 和 CharType(length) 提供支持，Trino 也原生支持 varchar(n) 和 char(n)。提案属于 v4 规范更新，不影响现有 v2 表格。

github · ebyhr · Jun 17, 13:55

**背景**: Apache Iceberg 是一种开源高性能表格式，专为数据湖中的大型分析表设计。它允许多种查询引擎（如 Spark、Trino、Flink 等）安全并发操作同一张表，解决了 Hive 表在大数据场景下的性能和一致性问题。该规范之前仅提供 string 类型，新增 varchar 和 char 可满足传统 SQL 系统中对固定长度和可变长度字符串的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_Iceberg">Apache Iceberg</a></li>

</ul>
</details>

**标签**: `#apache-iceberg`, `#data-engineering`, `#specification`, `#sql-compatibility`, `#data-types`

---

<a id="item-data-warehouse-3"></a>
## [Apache Iceberg REST 目录新增新鲜度感知表加载功能](https://github.com/apache/iceberg/issues/11766) ⭐️ 7.0/10

Apache Iceberg 社区在 Issue #11766 中提出为 REST 目录引入新鲜度感知的表加载 API，允许客户端仅在元数据发生变化时才重新加载表，避免不必要的全量加载。该功能已在 PR #14398 中实现并合并至主分支。 该改进能显著提升数据系统中缓存表元数据的查询引擎的性能，减少与目录服务器的通信开销，并为大规模数据湖上的实时分析场景提供更高效的元数据同步方案。 新机制通过在请求中携带上一次的元数据标识（如快照 ID 或版本号），服务端仅在有更新时返回完整数据，实现按需加载。实现上引入了 RESTTableOperations 回调，支持 SnapshotMode=REFS 的延迟快照加载模式。

github · gaborkaszab · Jun 14, 00:50

**背景**: Apache Iceberg 是一种面向数据湖的开放表格式，其 REST 目录规范通过 HTTP API 统一管理表元数据，方便各类计算引擎访问。为提高查询性能，引擎常缓存元数据，但需及时感知变更。此前缺乏原生机制，多依赖周期轮询或外部事件通知，资源消耗大且延迟不稳定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/apache/iceberg/issues/11766">Freshness aware table loading in REST catalog · Issue #11766 · apache/iceberg</a></li>
<li><a href="https://iceberg.apache.org/rest-catalog-spec/">REST Catalog Spec - Apache Iceberg™</a></li>

</ul>
</details>

**标签**: `#apache-iceberg`, `#table-metadata`, `#catalog-api`, `#performance`, `#caching`

---

<a id="item-data-warehouse-4"></a>
## [Apache Iceberg 拟增加对 Flink 水印和计算列的元数据支持](https://github.com/apache/iceberg/issues/16756) ⭐️ 7.0/10

Apache Iceberg 社区近日提出一项功能请求（issue #16756），计划在 Iceberg 表格式中扩展元数据支持，以持久化 Flink 等流处理引擎所需的水印（watermark）和计算列（computed column）定义。 水印和计算列是流式 SQL 正确进行查询规划与执行的关键元数据，该特性将使 Iceberg 表能够完整保留这些信息，显著提升 Flink 流作业在 Iceberg 上的准确性、可移植性和引擎间互操作性。 目前 Iceberg 目录大多仅保存表模式，水印和计算列等元数据在持久化过程中会丢失。该提案旨在让 Iceberg 直接存储这些信息，以避免跨引擎使用时的元数据断裂。

github · SteveStevenpoor · Jun 12, 03:53

**背景**: Apache Iceberg 是一种面向大规模分析表的高性能开放表格式，允许多种引擎（如 Spark、Flink、Trino）并发操作同一张表。Apache Flink 是流行的流处理框架，其水印机制用于处理事件时间乱序，计算列则是根据其他列表达式动态生成的虚拟列。在流式 SQL 中，水印定义了何时基于事件时间触发输出，计算列则可简化派生字段的表达。当前若用 Flink 创建 Iceberg 表，这些流式元数据不会被存入 Iceberg，导致其他引擎无法复用或重现等语义。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_Iceberg">Apache Iceberg</a></li>
<li><a href="https://medium.com/@ipolyzos_/understanding-watermarks-in-apache-flink-c8793a50fbb8">Understanding Watermarks in Apache Flink | by Giannis... | Medium</a></li>
<li><a href="https://www.sqlshack.com/an-overview-of-computed-columns-in-sql-server/">An overview of computed columns in SQL Server</a></li>

</ul>
</details>

**标签**: `#apache-iceberg`, `#apache-flink`, `#streaming`, `#metadata`, `#feature-request`

---

<a id="item-data-warehouse-5"></a>
## [提议：为 Iceberg Kafka Connect Worker 添加背压检测](https://github.com/apache/iceberg/issues/16389) ⭐️ 7.0/10

提案在 Apache Iceberg 的 Kafka Connect Sink 连接器中，为 Worker 增加对 Coordinator 进度的检测能力，当 Coordinator 过载时可自动暂停 Worker，防止控制主题消息指数级增长。 该机制解决了生产环境中 Coordinator 过载时引发的消息爆炸问题，能显著提升数据管道的稳定性和弹性，对依赖 Iceberg 进行流式入湖的场景至关重要。 提案目前仅为设计草案，具体实现细节待定，社区在邮件列表进行讨论。核心思路是让 Worker 感知 Coordinator 负载并主动限流，避免控制消息积压恶化。

github · HenryCaiHaiying · Jun 2, 00:01

**背景**: Apache Iceberg 是一种开放式表格式，广泛用于数据湖仓。其 Kafka Connect 连接器支持将 Kafka 数据流式写入 Iceberg 表，采用 Coordinator 统一管理事务提交。分布式部署时，多个 Worker 进程协同执行任务，若 Coordinator 处理能力不足，其内部的控制消息（如 commit 请求）会迅速堆积，导致故障级联。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://iceberg.apache.org/docs/latest/kafka-connect/">Kafka Connect - Apache Iceberg</a></li>
<li><a href="https://docs.confluent.io/platform/current/connect/references/allconfigs.html">Kafka Connect Worker Configuration Properties for Confluent Platform | Confluent Documentation</a></li>
<li><a href="https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-workers.html">Understand MSK Connect workers - Amazon Managed Streaming for Apache Kafka</a></li>

</ul>
</details>

**标签**: `#apache-iceberg`, `#kafka-connect`, `#backpressure`, `#proposal`, `#data-engineering`

---

<a id="item-data-warehouse-6"></a>
## [Delta Lake 协议新增重定向规范提案](https://github.com/delta-io/delta/pull/3705) ⭐️ 7.0/10

Delta Lake 协议新增一项关于重定向功能的变更提案，详细描述了该功能的定义、启用与禁用流程以及查询重定向流程。 此提案对 Delta Lake 生态系统至关重要，因为重定向功能允许表位置迁移而不中断现有工作负载，从而提升数据湖的灵活性和运维效率，并可能影响所有 Delta 客户端实现。 该 PR 属于协议变更文档，不涉及具体代码实现；提案目前缺乏实现细节与社区反馈，且未绑定特定计算引擎。

github · kamcheungting-db · Mar 14, 20:12

**背景**: Delta Lake 是一种开源数据湖存储格式，提供 ACID 事务、可扩展元数据处理等能力。每个 Delta 表都有一个协议规范，定义读取和写入所需的功能集，客户端据此判断兼容性。重定向功能允许表位置发生变更时通知客户端自动跳转到新地址，此提案旨在将其正式纳入协议规范。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://delta.io/">Home | Delta Lake</a></li>
<li><a href="https://docs.databricks.com/aws/en/delta/feature-compatibility">Delta Lake feature compatibility and protocols | Databricks on AWS</a></li>

</ul>
</details>

**标签**: `#delta-lake`, `#protocol`, `#specification`, `#data-lake`, `#pull-request`

---

<a id="item-data-warehouse-7"></a>
## [Apache Hudi 提出分区软删除功能提案](https://github.com/apache/hudi/issues/18774) ⭐️ 7.0/10

Apache Hudi 社区在 Issue #18774 中提议为分区删除操作引入软删除机制，允许用户在数据被永久清理前将其恢复。 该功能将显著降低误删分区导致的数据丢失风险，为数据湖管理提供安全网，并增强企业在关键数据操作中的容错能力。 当前 delete_partition API 会直接替换分区文件，clean 表服务随后进行物理删除。新提案将引入一个可配置的宽限期，在此期间文件仍保留在元数据表和索引中，用户可回滚操作，直至最终清理。

github · kbuci · May 18, 22:43

**背景**: Apache Hudi 是一个开源数据湖仓平台，通过表格式支持 ACID 事务与增量处理。其内置的 clean 服务负责删除过期的文件版本。分区则是按列值划分的数据组织单元，直接删除分区会使数据永久消失。软删除概念类似于回收站，旨在为误操作提供恢复窗口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hudi.apache.org/">Apache Hudi</a></li>

</ul>
</details>

**标签**: `#Apache Hudi`, `#data management`, `#soft delete`, `#partition deletion`, `#data recovery`

---

<a id="item-data-warehouse-8"></a>
## [Iceberg Spark 集成拟支持提交时捕获 Parquet 页脚指标](https://github.com/apache/iceberg/issues/16675) ⭐️ 6.0/10

Apache Iceberg 社区提出改进提案（#16675），为 Spark 写入路径增加可选机制，在提交事务时聚合数据文件的 Parquet 页脚统计信息（如行数、空值计数、最值等），并通过事件框架发布，而不持久化到表元数据。 该功能可提升数据写入的可观测性，使监控或审计系统能及时获取物理存储统计，无需额外扫描数据文件或修改元数据，有助于性能优化和数据质量保障。 该机制为可选，仅捕获 Parquet 页脚中已有的聚合统计（如 row group 级别的 value_counts、null_value_counts、min/max 值），不额外增加 I/O。当前 Iceberg 事件框架仅支持扫描事件，此提案将扩展至提交事件。

github · gtrettenero · Jun 3, 15:58

**背景**: Parquet 是一种列式存储格式，其文件页脚包含行组级别的列统计信息，常用于查询优化。Apache Iceberg 是开放表格式，其事件框架允许在表操作时通知外部系统，目前仅支持扫描事件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@sanjeets1900/how-to-access-parquet-file-metadata-26906b2dd626">How to access Parquet file metadata | by Sanjeet Shukla | Medium</a></li>
<li><a href="https://www.dremio.com/resources/guides/apache-iceberg-an-architectural-look-under-the-covers/">Apache Iceberg: An Architectural Look Under the Covers</a></li>

</ul>
</details>

**标签**: `#apache-iceberg`, `#spark`, `#parquet`, `#data-observability`, `#commit-metrics`

---

<a id="item-data-warehouse-9"></a>
## [Iceberg REST 目录拟添加表标签元数据字段](https://github.com/apache/iceberg/issues/15521) ⭐️ 6.0/10

Apache Iceberg 社区提出了一项变更，计划在 REST 目录的 LoadTableResponse 中增加一个可选的 labels 字段，用于传递由目录维护的上下文信息，如所有权、分类和成本归属。 该标准化标签字段能让开源引擎直接消费目录提供的元数据，避免厂商自定义扩展，从而提升不同系统间的互操作性，推动数据湖生态的进一步整合。 该 labels 字段为可选，具体结构和允许的标签内容尚未最终确定，不同目录实现可自行决定如何填充，但需遵循统一的 schema 以保持兼容。

github · laskoviymishka · May 12, 08:00

**背景**: Apache Iceberg 是一种高性能的开放表格式，适用于大型分析数据集，支持多种计算引擎同时操作同一张表。其 REST 目录规范定义了一套基于 REST 的 API，用于管理表元数据和执行目录操作，任何支持 Iceberg 的处理引擎均可通过该 API 加载表。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_Iceberg">Apache Iceberg</a></li>
<li><a href="https://iceberg.apache.org/rest-catalog-spec/">REST Catalog Spec - Apache Iceberg™</a></li>

</ul>
</details>

**标签**: `#apache-iceberg`, `#rest-catalog`, `#table-metadata`, `#open-source`, `#data-lake`

---

<a id="item-data-warehouse-10"></a>
## [Apache Hudi RFC-59 新功能提案](https://github.com/apache/hudi/issues/15335) ⭐️ 6.0/10

Apache Hudi 社区提交了 RFC-59 提案，详细描述了一个新功能或改进的问题背景、设计理念和代码实现方案。 该提案为 Hudi 引入新功能提供了清晰的路径，一旦接受并实现，可能增强写入性能或扩展使用场景，对依赖 Hudi 的数据湖用户具有实际价值。 提案以 RFC-59 编号提出，关联 JIRA 工单 HUDI-4612（任务类型），属于 Epic HUDI-4569 的一部分，具体技术细节待社区进一步讨论。

github · hudi-bot · Dec 11, 23:17

**背景**: Apache Hudi 是一个开源数据湖仓平台，支持在数据湖上实现 ACID 事务、高效 upsert 和删除，底层通常使用 Apache Parquet 和 Avro 存储文件。在 Hudi 社区中，RFC（Request for Comments）是用于提议重大功能或变更的正式设计文档，需经过社区讨论并达成共识后才会落地实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/hudi">Hudi</a></li>
<li><a href="https://ajithshetty28.medium.com/apache-hudi-pronounced-hoodie-e393339dbc47">Apache Hudi pronounced “hoodie”. Data has become as... | Medium</a></li>

</ul>
</details>

**标签**: `#Apache Hudi`, `#RFC`, `#data lake`, `#proposal`, `#open-source`

---