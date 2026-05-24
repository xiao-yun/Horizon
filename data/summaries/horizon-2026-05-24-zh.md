# Horizon 每日速递 - 2026-05-24

> From 17 items, 10 important content pieces were selected
>
> ## 数据仓库
> 1. [Apache Iceberg 提议统一文件格式 API 以协调多格式功能支持](#item-data-warehouse-1) ⭐️ 8.0/10 · GitHub · 11:57
> 2. [Apache Iceberg 提议增加行级并发支持](#item-data-warehouse-2) ⭐️ 7.0/10 · GitHub · 00:42
> 3. [Apache Iceberg 提议支持 Variant 数据类型](#item-data-warehouse-3) ⭐️ 7.0/10 · GitHub · 12:52
> 4. [Apache Iceberg 提议为 VARIANT 列添加虚拟字段元数据](#item-data-warehouse-4) ⭐️ 7.0/10 · GitHub · 03:00
> 5. [Apache Iceberg REST API 新增查询参数裁剪日志数组](#item-data-warehouse-5) ⭐️ 7.0/10 · GitHub · 02:33
> 6. [Delta Lake 协议变更：新增表重定向规范提案](#item-data-warehouse-6) ⭐️ 7.0/10 · GitHub · 20:12
> 7. [Apache Hudi 1.2.0 发布，新增验证 API 及 Demo 应用](#item-data-warehouse-7) ⭐️ 6.0/10 · GitHub · 23:22
> 8. [Iceberg REST 目录新增标签元数据提案](#item-data-warehouse-8) ⭐️ 6.0/10 · GitHub · 08:00
> 9. [Apache Hudi 提议增加分区软删除功能](#item-data-warehouse-9) ⭐️ 6.0/10 · GitHub · 22:43
> 10. [Apache Hudi RFC-59 新功能设计提案](#item-data-warehouse-10) ⭐️ 6.0/10 · GitHub · 23:17

## 数据仓库

<a id="item-data-warehouse-1"></a>
## [Apache Iceberg 提议统一文件格式 API 以协调多格式功能支持](https://github.com/apache/iceberg/issues/12225) ⭐️ 8.0/10

Apache Iceberg 社区提出一项提案（issue #12225），旨在引入统一的文件格式 API。该 API 旨在协调 Avro、Parquet 和 ORC 三种文件格式对 V3 规范新增特性的支持，避免各格式实现不一致。 该提案有助于确保 Iceberg 支持的所有文件格式能平等地实现新功能，提高数据一致性，对依赖 Iceberg 构建数据湖的企业和引擎生态有重要影响。 V3 规范引入了新的列类型和默认值等特性，这些特性需要在各文件格式底层进行实现。目前不同开发者独立添加功能，导致各格式支持程度不一，且新兴文件格式的出现使统一接口的需求更为迫切。

github · pvary · Apr 20, 11:57

**背景**: Apache Iceberg 是一种大型分析表的高性能开源表格式，支持 Spark、Trino 等多种引擎安全地并发操作同一张表。V3 规范是 Iceberg 的最新版本，增加了批流一体、AI 可读性以及新列类型等能力。Avro、Parquet 和 ORC 是数据湖中常用的列式存储文件格式，各有不同的实现方式和功能支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_Iceberg">Apache Iceberg - Wikipedia</a></li>
<li><a href="https://iceberg.apache.org/">Apache Iceberg - Apache Iceberg™</a></li>
<li><a href="https://llms3.com/node/iceberg-v3-spec">Iceberg V 3 Spec | LLMS3</a></li>

</ul>
</details>

**标签**: `#apache-iceberg`, `#data-engineering`, `#file-formats`, `#api-design`, `#big-data`

---

<a id="item-data-warehouse-2"></a>
## [Apache Iceberg 提议增加行级并发支持](https://github.com/apache/iceberg/issues/14613) ⭐️ 7.0/10

提交了议题 #14613，建议为 Apache Iceberg 添加行级并发（row-level concurrency）功能，基于即将发布的 Iceberg v3 中引入的 row lineage 和 deletion vectors 特性。 行级并发可以减少并发写操作之间的冲突，通过检测行级变更并自动解决冲突，即使不同操作修改同一数据文件的不同行。这能显著提升数据湖仓的写入并发性，使 Iceberg 提供与专有系统 (如 Databricks) 类似的能力。 该功能需要依赖 row lineage 为每行分配唯一标识，以及 deletion vectors 以标记行级变更而无需重写整个 Parquet 文件。目前仅是提案，尚未有具体实现细节。

github · Neuw84 · May 18, 00:42

**背景**: Apache Iceberg 是一种开放式表格式，广泛用于数据湖仓。Iceberg v3 规范正在制定，引入了 row lineage 和 deletion vectors。Row lineage 用于追踪每一行的创建和变更历史，为每行分配唯一 ID；deletion vectors 通过标记删除行来避免重写整个 Parquet 文件。结合这些特性，行级并发能够检测并发写入是否修改了同一行，从而避免冲突，提升写入性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/azure/databricks/optimizations/isolation/row-level-concurrency">Row-level concurrency - Azure Databricks | Microsoft Learn</a></li>
<li><a href="https://github.com/apache/iceberg/issues/11129">Row Lineage for V3 · Issue #11129 · apache/iceberg</a></li>
<li><a href="https://docs.databricks.com/aws/en/delta/deletion-vectors">Deletion vectors in Databricks | Databricks on AWS</a></li>

</ul>
</details>

**标签**: `#apache-iceberg`, `#row-level-concurrency`, `#data-lakehouse`, `#table-format`, `#concurrency`

---

<a id="item-data-warehouse-3"></a>
## [Apache Iceberg 提议支持 Variant 数据类型](https://github.com/apache/iceberg/issues/10392) ⭐️ 7.0/10

Apache Iceberg 社区提出增加 Variant 数据类型（Issue #10392），旨在通过高效的二进制编码来存储和查询 JSON、Avro 等半结构化数据。 这将显著提升数据湖中半结构化数据的处理效率，使查询引擎能更灵活地操作动态数据，契合行业对“ schema-on-read ” 的需求，进一步巩固 Iceberg 在分析型表格式中的竞争力。 Variant 类型在内部采用紧凑的二进制表示，既能保留源数据的灵活性，又能避免解析开销；该特性目前处于提案阶段，具体规范尚未发布。

github · sfc-gh-aixu · Apr 30, 12:52

**背景**: Apache Iceberg 是一种高性能开源表格式，支持 Spark、Trino、Flink 等多种查询引擎在大型数据湖上安全地并发读写。传统上，半结构化数据常以字符串形式存储，查询时需动态解析，性能较低。Variant 类型借鉴了 Spark 和 Delta Lake 中的类似实现，通过原生的二进制格式优化读取路径，让半结构化数据也能享受列式存储的优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://iceberg.apache.org/">Apache Iceberg - Apache Iceberg™</a></li>

</ul>
</details>

**标签**: `#apache iceberg`, `#variant type`, `#data types`, `#semi-structured data`, `#feature proposal`

---

<a id="item-data-warehouse-4"></a>
## [Apache Iceberg 提议为 VARIANT 列添加虚拟字段元数据](https://github.com/apache/iceberg/issues/16064) ⭐️ 7.0/10

2026 年 4 月 20 日，Apache Iceberg 提出一项规范级增强，允许为半结构化（VARIANT）列声明“虚拟字段”，提供类型化元数据，以便引擎解析类型、下推谓词并透明地将查询重定向到物理列。 该机制可大幅提升半结构化数据查询性能，简化用户对模式演化的手动管理，增强 Iceberg 作为主流数据湖表格式的竞争力。 提案在表元数据中增加虚拟字段数组，每个条目包含 VARIANT 列内的字段路径和类型信息；引擎可利用这些元数据优化查询计划，但虚拟字段本身不存储实际数据。

github · jeffbuser · Apr 25, 03:00

**背景**: Apache Iceberg 是一种开放表格式，广泛应用于数据湖中的大规模结构化与半结构化数据。Iceberg V3 引入了 VARIANT 类型，旨在高效存储和查询 JSON 等半结构化数据，但目前在过滤 VARIANT 字段时易出现类型推断错误或性能问题。虚拟字段元数据正是为了解决此类瓶颈而设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/apache/iceberg/issues/16064">Virtual Field Metadata for Semi-Structured (VARIANT) Columns · Issue #16064 · apache/iceberg - GitHub</a></li>
<li><a href="https://www.dremio.com/blog/apache-iceberg-v3/">What’s New in Apache Iceberg Format Version 3? | Dremio</a></li>
<li><a href="https://github.com/apache/iceberg/issues/14071">Filtering on VARIANT fields does not return expected results Iceberg ...</a></li>

</ul>
</details>

**标签**: `#apache-iceberg`, `#data-engineering`, `#semi-structured-data`, `#table-format`, `#variant-type`

---

<a id="item-data-warehouse-5"></a>
## [Apache Iceberg REST API 新增查询参数裁剪日志数组](https://github.com/apache/iceberg/issues/15947) ⭐️ 7.0/10

Apache Iceberg 社区提出在 loadTable REST API 中新增查询参数，允许客户端请求时裁剪 snapshot-log 和 metadata-log 数组，以减少返回的元数据体积。 此改进针对大表场景下无界日志数组导致的响应膨胀问题，能够显著提升 REST API 的可扩展性与传输效率，减轻客户端解析压力。 新增的查询参数为可选特性，客户端需主动指定才能获得裁剪后的日志数组，默认行为保持不变；该优化属于增量改进，不涉及格式或协议重大变更。

github · laserninja · Apr 12, 02:33

**背景**: Apache Iceberg 是一种面向大规模分析表的高性能开放表格式。其表元数据中包含 snapshot-log（记录每次快照操作）和 metadata-log（记录元数据文件变更），用于支持时间旅行等功能。然而，随着表提交次数增加，这些数组会无限增长，导致 loadTable 响应体积膨胀，影响传输效率与客户端解析性能。本次提案即针对此问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_Iceberg">Apache Iceberg - Wikipedia</a></li>
<li><a href="https://iceberg.apache.org/">Apache Iceberg - Apache Iceberg</a></li>

</ul>
</details>

**标签**: `#apache-iceberg`, `#rest-api`, `#scalability`, `#performance`, `#data-engineering`

---

<a id="item-data-warehouse-6"></a>
## [Delta Lake 协议变更：新增表重定向规范提案](https://github.com/delta-io/delta/pull/3705) ⭐️ 7.0/10

此 PR 提交了 Delta Lake 协议的重定向（Redirection）特性规范，详细描述了重定向的定义、启用与禁用流程，以及查询重定向机制。 重定向特性允许将 Delta Lake 表无缝指向其他表（如 Hive 表），可能改变表的访问模式，并影响使用 Delta Lake 的查询引擎与生态系统的兼容性。 这是一份纯协议规范文档，属于 Protocol Change，不涉及具体代码实现，旨在统一不同计算引擎对重定向行为的理解与支持。

github · kamcheungting-db · Mar 14, 20:12

**背景**: Delta Lake 是一种开源存储层，为数据湖提供 ACID 事务和可靠性。此前，Trino 等引擎已初步支持从 Delta 表到 Hive 表的重定向，但缺乏统一的协议规范。本次提案在协议层面标准化重定向行为，确保不同工具和引擎之间的互操作性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://trino.io/docs/current/connector/delta-lake.html">Delta Lake connector — Trino 481 Documentation</a></li>
<li><a href="https://github.com/delta-io/delta/blob/master/PROTOCOL.md">delta/PROTOCOL.md at master - GitHub</a></li>

</ul>
</details>

**标签**: `#delta-lake`, `#protocol`, `#feature-proposal`, `#data-engineering`, `#spec-change`

---

<a id="item-data-warehouse-7"></a>
## [Apache Hudi 1.2.0 发布，新增验证 API 及 Demo 应用](https://github.com/apache/hudi/releases/tag/release-1.2.0) ⭐️ 6.0/10

Apache Hudi 1.2.0 正式发布，新增了存储 LP 审计验证 API 和全新的 Hudi 演示笔记本应用（hudi-notebooks），同时修复了包括 Spark Schema Evolution 嵌套列处理、Flink 流读键选择器类型提取在内的大量错误。 这些改进增强了 Hudi 的数据管理能力与稳定性，验证 API 有助于审计合规，演示笔记本降低了用户入门门槛，多项关键修复提升了数据湖仓平台的生产就绪程度。 该版本包含验证与清理 API、Spark 嵌套列 Schema 演进修复、元数据表分区点查询修复、HFile 日志块内存优化等；演示笔记本简化了上手流程，同时修复了 MERGE INTO 语句的错误提示、二级索引的删除更新处理等问题。

github · yihua · May 23, 23:22

**背景**: Apache Hudi 是一个开源数据湖仓平台，基于高性能开放表格式，为数据湖提供 ACID 事务、高效 upsert/deletes 等数据库级能力，与 Hadoop、Spark、Flink 等生态紧密集成，广泛应用于流式数据处理场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/hudi">Hudi</a></li>
<li><a href="https://medium.com/aimonks/from-swamp-to-stream-how-apache-hudi-transforms-the-modern-data-lake-8a938f517ea1">From Swamp to Stream: How Apache Hudi Transforms the... | Medium</a></li>

</ul>
</details>

**标签**: `#apache-hudi`, `#data-lake`, `#release`, `#big-data`, `#open-source`

---

<a id="item-data-warehouse-8"></a>
## [Iceberg REST 目录新增标签元数据提案](https://github.com/apache/iceberg/issues/15521) ⭐️ 6.0/10

该提案建议在 Iceberg REST 目录的 LoadTableResponse 中添加一个可选的 labels 字段，以便目录服务能够传递表的所有权、分类、成本归属等上下文元数据。 这将使开源引擎能够以标准方式消费目录中的上下文信息，提升不同目录之间的互操作性，避免厂商特定的扩展。 该字段为可选，属于功能请求，尚未实现。已有的 LoadTableResponse 仅返回模式、快照和文件位置等元数据，缺少此类上下文。

github · laskoviymishka · May 12, 08:00

**背景**: Apache Iceberg 是一种开放的表格式，用于数据湖上的大规模数据管理。其 REST 目录规范定义了标准的 API 用于管理表元数据。LoadTableResponse 是加载表时返回的响应结构。目前，各目录实现通常需要自定义扩展来传递表的业务上下文，缺乏统一机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://iceberg.apache.org/rest-catalog-spec/">REST Catalog Spec - Apache Iceberg</a></li>
<li><a href="https://medium.com/datastrato/introduction-to-rest-catalogs-for-apache-iceberg-5ee4b6d05eaa">Introduction to REST Catalogs for Apache Iceberg | Medium</a></li>

</ul>
</details>

**标签**: `#apache-iceberg`, `#rest-catalog`, `#metadata`, `#open-source`, `#data-engineering`

---

<a id="item-data-warehouse-9"></a>
## [Apache Hudi 提议增加分区软删除功能](https://github.com/apache/hudi/issues/18774) ⭐️ 6.0/10

Apache Hudi 社区在 #18774 号提案中讨论为分区删除 API 引入软删除（soft delete）机制，允许用户在彻底清理前恢复被删除的分区数据。 该功能可防止误删分区导致的数据永久丢失，为用户提供了数据恢复的窗口期，提升了数据管理的安全性和容错能力。 软删除后，分区文件不会立即被清理服务移除，而是保留至满足清理条件；在此期间用户可恢复数据，待清理条件触发后才会真正删除文件和元数据。

github · kbuci · May 18, 22:43

**背景**: Apache Hudi 是一个开源数据湖平台，支持在数据湖上实现 ACID 事务、高效更新和删除等数据库功能。目前 Hudi 的 delete_partition API 会直接替换分区文件，并由清理服务在满足条件时彻底删除这些文件和元数据，没有提供恢复选项。软删除是一种常见的延迟删除策略，通过在保留期内隐藏数据而非物理删除，为误操作留出补救空间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hudi.apache.org/">Apache Hudi | An Open Source Data Lake Platform | Apache Hudi</a></li>
<li><a href="https://grokipedia.com/page/hudi">Hudi</a></li>

</ul>
</details>

**标签**: `#apache-hudi`, `#data-management`, `#partition-deletion`, `#soft-delete`, `#data-recovery`

---

<a id="item-data-warehouse-10"></a>
## [Apache Hudi RFC-59 新功能设计提案](https://github.com/apache/hudi/issues/15335) ⭐️ 6.0/10

Apache Hudi 社区发布了 RFC-59 设计提案，详细描述了一项新功能的问题、设计概念和代码实现方案。 该提案旨在增强 Hudi 的数据管理能力，可能提升数据湖在事务处理、更新效率等方面的性能和可靠性。 提案包含问题描述、设计概念和代码实现，关联 JIRA 任务 HUDI-4612 和史诗 HUDI-4569。

github · hudi-bot · Dec 11, 23:17

**背景**: Apache Hudi 是一个开源数据湖仓平台，为数据湖提供 ACID 事务、高效更新和删除等数据库功能，基于高性能开放表格式构建。它常用于大数据场景，与 Hadoop 生态紧密集成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_Hadoop">Apache Hadoop</a></li>
<li><a href="https://grokipedia.com/page/hudi">Hudi</a></li>

</ul>
</details>

**标签**: `#apache-hudi`, `#rfc`, `#data-lake`, `#design-proposal`, `#open-source`

---


