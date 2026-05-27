---
layout: default
title: "Horizon Summary: 2026-05-21 (ZH)"
date: 2026-05-21
lang: zh
---

> From 18 items, 13 important content pieces were selected

---

## AI 与工具
1. [谷歌在 AI 搜索中测试新广告格式并扩展 Direct Offers](#item-1) ⭐️ 9.0/10
2. [1945 年三位一体核试验遗失影像被修复](#item-2) ⭐️ 8.0/10
3. [Rmux：可编程终端复用器，提供 Playwright 风格 SDK](#item-3) ⭐️ 8.0/10
4. [SpaceX S-1 文件披露：Anthropic 每月 12.5 亿美元租用 COLOSSUS 超算](#item-4) ⭐️ 8.0/10
5. [Flipper One 开源 ARM 计算机寻求社区支持](#item-5) ⭐️ 7.0/10
6. [Python 3.15 的低调新特性：线程安全迭代器与 Counter 集合操作](#item-6) ⭐️ 7.0/10
7. [Google Antigravity 诱饵调包：IDE 被悄然替换](#item-7) ⭐️ 7.0/10
8. [AI 训练是更庞大的未经授权抄袭](#item-8) ⭐️ 7.0/10
9. [Vivaldi 8.0 发布](#item-9) ⭐️ 6.0/10
10. [10 令牌/秒到底有多快？可视化工具帮你直观感受](#item-10) ⭐️ 6.0/10
## 数据仓库
11. [DuckDB 集成 Lance 湖仓格式，支持向量与混合搜索](#item-11) ⭐️ 7.0/10
12. [利用 Databricks 实现从排放报告到脱碳决策](#item-12) ⭐️ 6.0/10
13. [从“发生了什么”到“将会发生什么”：Databricks 推进预测分析](#item-13) ⭐️ 6.0/10

---

## AI 与工具

<a id="item-1"></a>
## [谷歌在 AI 搜索中测试新广告格式并扩展 Direct Offers](https://blog.google/products/ads-commerce/google-marketing-live-search-ads/) ⭐️ 9.0/10

谷歌宣布正在搜索的 AI 模式中测试新的广告格式，并扩展其 Direct Offers 试点项目，引入 AI 生成的促销、原生结账和旅游优惠等功能。 此举标志着搜索引擎广告的一次重大转变，直接将广告植入 AI 生成的回答中，可能从根本上改变用户搜索体验，并对广告拦截工具的有效性和对话式 AI 的伦理边界带来深远影响。 AI 模式基于 Gemini 模型，能够处理复杂查询并生成综合回答，而 Direct Offers 则可在检测到购买意图时自动展示折扣，但社区担忧这种整合会规避广告拦截器，并使广告更难以从内容中区分。

hackernews · sofumel · May 21, 09:49 · [社区讨论](https://news.ycombinator.com/item?id=48220105)

**背景**: AI 模式是谷歌于 2025 年 3 月推出的实验性搜索功能，用户输入复杂问题后，系统会利用 Gemini 模型生成全面的 AI 回复。Direct Offers 则是谷歌在 AI 驱动的购物体验中嵌入的结构化促销广告，最初于 2026 年 1 月启动试点，旨在向高意向购物者展示定向折扣。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_AI_Mode">Google AI Mode</a></li>
<li><a href="https://adtechradar.com/2026/01/12/google-direct-offers-ai-shopping/">Google Brings Deal-Based Ads to AI Search With Direct Offers</a></li>

</ul>
</details>

**社区讨论**: 社区评论普遍持批评态度，认为谷歌此举是为了绕过广告拦截器牟利，担忧 AI 模型会被训练成操纵用户，并质疑 AI 回答的中立性；有用户表示因此转向 DuckDuckGo 等替代搜索引擎。

**标签**: `#advertising`, `#AI ethics`, `#search`, `#user experience`, `#ad-blocking`

---

<a id="item-2"></a>
## [1945 年三位一体核试验遗失影像被修复](https://spectrum.ieee.org/trinity-nuclear-test) ⭐️ 8.0/10

1945 年三位一体核试验的一批遗失影像经修复后重新公开，引发对试验人力成本与历史背景的讨论。 这些影像让人们重新审视核试验对人类的影响，特别是对当年居住在试验场周边、至今未获充分补偿的“下风口居民”群体的关注，可能推动历史认知与政策改变。 修复影像的技术细节尚未明确，但从讨论中可知，1990 年《辐射暴露补偿法》将三位一体试验场周边人群排除在外，这些居民癌症发病率升高，却未获得承认与支持。

hackernews · pseudolus · May 21, 11:02 · [社区讨论](https://news.ycombinator.com/item?id=48220639)

**背景**: 三位一体核试验是美国于 1945 年 7 月 16 日在新墨西哥州进行的首次核试验，是曼哈顿计划的一部分，直接推动了原子弹在广岛和长崎的使用。试验产生的放射性落尘对周边居民造成长期健康危害，但该群体长期未获官方承认与补偿。

**社区讨论**: 社区讨论聚焦于历史悲剧：多位评论提及一部揭示当地居民受忽略的纪录片，指出他们因辐射致病却未能像其他下风口居民那样获偿；也有人从科学史与哲学角度，感慨抽象理论最终化为毁灭性力量，并批评电影《奥本海默》中爆炸场景的不真实。

**标签**: `#history`, `#nuclear`, `#photography`, `#restoration`, `#ethics`

---

<a id="item-3"></a>
## [Rmux：可编程终端复用器，提供 Playwright 风格 SDK](https://github.com/helvesec/rmux) ⭐️ 8.0/10

Rmux 是一个用 Rust 从头构建的全新终端复用器，除了兼容 tmux 的 CLI（约 90 个命令），还提供了一个类型安全的异步 Rust SDK，支持稳定的窗格 ID、结构化快照和定位器式等待，实现了类似 Playwright 的终端自动化。 它为终端自动化带来了 Playwright 式的可靠性，通过稳定标识和显式等待取代了传统 grep+sleep 的脆弱模式，能够显著改善代理工具在终端中的可重复性和可调试性，对依赖终端代理的开发者意义重大。 Rmux 原生支持 Linux、macOS 和 Windows（使用原生 ConPTY，无需 WSL），SDK 提供稳定窗格 ID 和快照等待机制；作为新项目，其 CLI 接近 tmux 的完整兼容性，但社区及插件生态尚未成熟。

hackernews · shideneyu · May 21, 09:22 · [社区讨论](https://news.ycombinator.com/item?id=48219918)

**背景**: 终端复用器（如 tmux）允许在单个窗口中管理多个终端会话，是开发者的常用工具。Playwright 是微软开源的浏览器自动化库，以其可靠的等待和快照机制闻名，避免了传统基于 sleep 的不稳定性。Rmux 将这一理念引入终端，旨在解决脚本化终端交互中长期存在的输出抓取不可靠问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Playwright_(software)">Playwright (software) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区讨论热烈：多数人认可 Playwright 风格快照/等待层对终端自动化的改善，指出稳定窗格 ID 和显式等待将简化调试和重放；有人纠正 tmux 实为 C 而非 C++；也有用户质疑 tmux 式耦合会话持久化与窗口管理的设计是否最优，并提及分离职责的替代方案；此外，有人期待 rmux 能与现有 tmux 工具生态良好集成。

**标签**: `#terminal-multiplexer`, `#rust`, `#automation`, `#developer-tools`, `#tmux`

---

<a id="item-4"></a>
## [SpaceX S-1 文件披露：Anthropic 每月 12.5 亿美元租用 COLOSSUS 超算](https://simonwillison.net/2026/May/20/spacex-s1/#atom-everything) ⭐️ 8.0/10

SpaceX 在 SEC 的 S-1 文件中披露，2026 年 5 月与 AI 公司 Anthropic 签订云服务协议，以每月 12.5 亿美元的价格提供 COLOSSUS 和 COLOSSUS II 超算集群的算力，协议持续至 2029 年 5 月，初始两个月费用有折扣。 这笔每月 12.5 亿美元、总价超 540 亿美元的合同是 AI 基础设施领域史上最大交易，凸显顶级 AI 企业对算力的极度渴求，也标志着 SpaceX/xAI 从自研 AI 向算力商业化转型，可能重塑云计算市场格局。 协议允许任一方提前 90 天通知终止；Anthropic 将使用 COLOSSUS 1 的全部算力，而 SpaceX 同时也在 COLOSSUS II 上训练自家的 Grok 5 模型；两个超算中心均位于美国田纳西州。

rss · Simon Willison · May 20, 22:26

**背景**: COLOSSUS 是 xAI 于 2024 年建成的全球最大 AI 超级计算机，位于田纳西州孟菲斯，主要用于训练 Grok 聊天机器人。COLOSSUS II 是后续扩建项目。Anthropic 是领先的 AI 研究机构，推出 Claude 大模型，与 OpenAI 竞争。SpaceX 提交 S-1 文件旨在进行首次公开募股（IPO）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Colossus_(supercomputer)">Colossus (supercomputer) - Wikipedia</a></li>
<li><a href="https://finance.yahoo.com/news/anthropic-to-rent-all-ai-capacity-at-spacexs-colossus-data-center-180327774.html">Anthropic to rent all AI capacity at SpaceX's Colossus data center</a></li>
<li><a href="https://www.wired.com/story/spacex-ipo-anthropic-compute-finances-risks/">SpaceX IPO Filing Reveals Anthropic Is Paying $15 Billion... | WIRED</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Anthropic`, `#AI infrastructure`, `#cloud computing`, `#S-1 filing`

---

<a id="item-5"></a>
## [Flipper One 开源 ARM 计算机寻求社区支持](https://blog.flipper.net/flipper-one-we-need-your-help/) ⭐️ 7.0/10

Flipper Devices 团队正式推出 Flipper One 项目，一款基于 Rockchip RK3576 SoC 的开源 ARM 便携式计算机，配备 8GB RAM 和 RP2350 协处理器，目标是实现完整的 Linux 主线内核支持，并向社区征集开发协助。 该项目尝试打造一个从硬件到软件完全开放的 ARM Linux 平台，若成功实现主线支持，将为开源硬件生态提供重要参考，并有望推动更多 ARM 设备获得长期可维护的内核驱动。 Flipper One 搭载 Rockchip RK3576 八核 Cortex-A72/A53 处理器，支持 M.2 扩展、GPIO、Wi-Fi 和卫星通信，但 HDMI 接口因授权费用无法完全开放，且社区担忧功能过于庞杂可能导致项目延期。

hackernews · sandebert · May 21, 11:03 · [社区讨论](https://news.ycombinator.com/item?id=48220647)

**背景**: 主线 Linux 支持意味着硬件驱动直接并入 Linux 内核主线，无需依赖厂商提供的定制内核，从而获得更广泛的社区维护和长期支持。HDMI 标准由 HDMI 论坛管理，采用该接口需支付许可费，且不允许开源实现完整的 HDMI 2.1 驱动，因此限制了硬件完全开放的理想。Flipper Devices 此前以 Flipper Zero 便携式多工具闻名，Flipper One 是其向更强大 ARM 计算平台的扩展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnx-software.com/2026/05/21/flipper-one-a-rockchip-rk3576-powered-portable-arm-linux-computer-and-networking-multi-tool/">Flipper One - A Rockchip RK3576-powered portable Arm Linux computer and networking multi-tool - CNX Software</a></li>
<li><a href="https://en.wikipedia.org/wiki/Linux_kernel">Linux kernel - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/HDMI">HDMI - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区普遍赞赏项目的开源理念，但质疑 HDMI 接口因授权问题未能做到彻底开放，有悖‘最开放 ARM 计算机’的目标。不少用户认为功能清单过于庞大，存在范围蔓延风险，可能重蹈‘第二系统效应’的覆辙，也有评论对本地 AI 特性和缺乏键盘的可用性表示担忧。

**标签**: `#open-source hardware`, `#ARM`, `#Linux`, `#HDMI`, `#community discussion`

---

<a id="item-6"></a>
## [Python 3.15 的低调新特性：线程安全迭代器与 Counter 集合操作](https://blog.changs.co.uk/python-315-features-that-didnt-make-the-headlines.html) ⭐️ 7.0/10

Python 3.15 引入了线程安全迭代器，使其在自由线程环境下运行更可靠；同时为 collections.Counter 增加了完整的集合操作（如并集、交集、对称差集），方便计数统计。 这些改进让多线程 Python 程序减少并发错误，并简化了计数数据的比较与运算，尤其适合数据分析和后端服务。 线程安全迭代器在与无 GIL 模式配合时效果最佳；Counter 的集合操作仅保留正计数，零或负计数会被忽略或移除。

hackernews · rbanffy · May 21, 11:10 · [社区讨论](https://news.ycombinator.com/item?id=48220696)

**背景**: Python 3.13 起开始支持自由线程（no-GIL）模式，允许真正并行执行多线程，但这要求内置类型提供线程安全保证。collections.Counter 是字典子类，常用于统计元素出现次数，新增的集合操作（如 +、&、|、^）让多个计数器间的数学运算更直观。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.python.org/3/library/collections.html">collections — Container datatypes — Python 3.14.5 documentation</a></li>
<li><a href="https://realpython.com/python-counter/">Python 's Counter : The Pythonic Way to Count Objects – Real Python</a></li>

</ul>
</details>

**社区讨论**: 社区讨论中，有人对线程安全迭代器的影响提出疑问，并提到了延迟导入的关联；有人指出 Counter 对称差集在实际中的应用，并分享了 Python 内部自由线程实现的访谈链接。整体反响积极，但对部分特性的实用性存在不同看法。

**标签**: `#Python`, `#Python3.15`, `#programming-languages`, `#software-development`, `#hackernews`

---

<a id="item-7"></a>
## [Google Antigravity 诱饵调包：IDE 被悄然替换](https://www.0xsid.com/blog/antigravity-bait-n-switch) ⭐️ 7.0/10

Google 在未充分告知用户的情况下，突然将原有的 Antigravity IDE 替换为一款完全不同的产品，导致现有用户更新后感到困惑和强烈不满。 该事件暴露了依赖科技巨头闭源开发工具的锁入风险，可能促使更多开发者重新评估工具链，转向更灵活的开源替代方案。 更新使原有用户措手不及，且 Google 此前对该 IDE 投入甚少，长期存在未修复的关键错误，此次切换凸显了其产品策略的不稳定性。

hackernews · ssiddharth · May 21, 13:50 · [社区讨论](https://news.ycombinator.com/item?id=48222529)

**背景**: Antigravity IDE 是 Google 推出的实验性 AI 代理开发环境，旨在支持 AI 代理自主完成代码编写、终端操作等复杂任务。该工具此前更新缓慢，用户基础有限。此次事件中，Google 用名称相同但功能迥异的产品直接覆盖了原 IDE，被指责为“诱饵调包”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://antigravity.google/product/antigravity-ide?ref=producthunt">Google Antigravity - Antigravity IDE</a></li>
<li><a href="https://antigravityide.net/">Antigravity IDE - Agent-First AI Development Platform by Google</a></li>

</ul>
</details>

**社区讨论**: 社区普遍对 Google 的突然更换表示惊讶和不满，指责其缺乏对开发者工具的持续投入。多数评论认为使用闭源 IDE 存在严重锁入风险，而开源 IDE 搭配 CLI 代理更具灵活性。部分用户批评 Google 在 AI 编码市场已落后，原因在于其反复无常的产品策略。

**标签**: `#google`, `#antigravity`, `#developer-tools`, `#product-fail`, `#user-trust`

---

<a id="item-8"></a>
## [AI 训练是更庞大的未经授权抄袭](https://axelk.ee/ai-is-just-unauthorised-plagiarism-at-a-bigger-scale/) ⭐️ 7.0/10

一篇观点文章指出，AI 模型训练本质上是对大量内容进行未经授权的复制，构成大规模抄袭，由此引发关于版权与内容所有权的激烈讨论。 该问题直接关系内容创作者权益与互联网生态的可持续性，若 AI 无偿使用原创作品，可能打击创作动力，影响内容多样性与质量。 讨论中特别提到 AI 对小众内容（如地方报纸）的利用可能更为有害，且有人质疑‘知识产权’概念本身的法律合理性。

hackernews · speckx · May 21, 13:38 · [社区讨论](https://news.ycombinator.com/item?id=48222383)

**背景**: 现代 AI 模型（如大型语言模型）的训练依赖从互联网收集的海量数据，其中包含大量受版权保护的文章、图片等。批评者认为，未经许可使用这些数据与抄袭无异，只是规模更大、更难追溯。

**社区讨论**: 社区意见存在分歧：一方强调网站运营者付出成本却未获回报，另一方则认为这有助于打破不合理的版权壁垒，支持非商业场景下的自由使用。

**标签**: `#AI ethics`, `#copyright`, `#plagiarism`, `#discussion`, `#opinion`

---

<a id="item-9"></a>
## [Vivaldi 8.0 发布](https://vivaldi.com/blog/vivaldi-on-desktop-8-0/) ⭐️ 6.0/10

Vivaldi 8.0 正式发布，尽管更新内容相对平淡，但其发布引发了社区对浏览器选择、隐私和 Chromium 单一文化的热烈讨论。 此次讨论凸显了在 Chromium 几乎垄断的背景下，Vivaldi 作为一款独立运营、注重隐私和用户控制的浏览器的重要性与矛盾性，其闭源模式也引发了信任问题。 Vivaldi 8.0 未集成任何 AI 功能，部分组件闭源，且基于 Chromium 内核；社区指出其商业模型依赖内置广告拦截和免费提供，但闭源特性使得用户对隐私保护存疑。

hackernews · OuterVale · May 21, 07:21 · [社区讨论](https://news.ycombinator.com/item?id=48219060)

**背景**: Vivaldi 是由前 Opera CEO 创立的挪威浏览器，基于 Chromium 但专为高级用户设计，内置邮件客户端、标签页管理等功能。Chromium 是 Google 主导的开源浏览器引擎，被 Chrome、Edge 等大量浏览器采用，导致浏览器引擎单一化，影响 Web 标准的多元发展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vivaldi_browser">Vivaldi browser</a></li>
<li><a href="https://dev.to/kenbellows/chromium-and-the-browser-monoculture-problem-420n">Chromium and the browser monoculture problem - DEV Community</a></li>

</ul>
</details>

**社区讨论**: 社区意见分歧，支持者赞赏其出色的广告拦截、打印功能和可持续商业模型；反对者则担忧其闭源性质加剧浏览器单一文化，并质疑其隐私数据收集方式。部分用户因 Vivaldi 没有捆绑 AI 而表示欢迎。

**标签**: `#Vivaldi`, `#browser`, `#Chromium`, `#privacy`, `#open-source`

---

<a id="item-10"></a>
## [10 令牌/秒到底有多快？可视化工具帮你直观感受](https://simonwillison.net/2026/May/20/tokens-per-second/#atom-everything) ⭐️ 6.0/10

开发者 Mike Veerman 创建了一个小型网页应用，可模拟 LLM 从每秒 5 到 800 令牌的输出速度，帮助用户直观理解不同生成速率的实际表现。 用户常看到模型标称的“30 令牌/秒”等指标，却难以想象实际感受，此工具将抽象数字转化为视觉体验，有助于评估 LLM 的交互流畅度。 该工具覆盖从每秒 5 令牌（接近阅读速度）到 800 令牌的高速区间，以单页 HTML 实现且源码公开，可直观对比不同模型的生成速率。

rss · Simon Willison · May 20, 17:57

**背景**: LLM 生成文本时以“令牌”为单位逐词输出，每秒令牌数直接影响用户感知的响应速度。大约 5-10 令牌/秒接近人类阅读速度，是流畅对话的基本门槛；30 令牌/秒以上则几乎无延迟感。不同模型及部署环境（如云端或本地）的令牌生成速度差异巨大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://droid4x.com/llm-tokens-per-second-inference-speed-simulator-tool/">LLM Tokens Per Second : Guide Measure Inference Speed Fast</a></li>
<li><a href="https://blog.decryption.net.au/posts/local_llms_1.html">decryption's blog - My Notes on Running LLMs Locally (Part 1)</a></li>

</ul>
</details>

**标签**: `#llms`, `#tokens`, `#visualization`, `#ai`

---


## 数据仓库

<a id="item-11"></a>
## [DuckDB 集成 Lance 湖仓格式，支持向量与混合搜索](https://duckdb.org/2026/05/21/test-driving-lance.html) ⭐️ 7.0/10

DuckDB 现已支持 Lance 湖仓格式，用户可在 SQL 中直接执行快速的向量搜索和混合搜索，无需离开分析流程。 此举将向量搜索能力无缝嵌入分析型 SQL 引擎，显著简化了 AI 驱动分析的工作流，并降低了多模态数据处理的门槛。 Lance 是面向多模态 AI 的开放湖仓格式，集成后的 DuckDB 展示了相关基准测试结果；混合搜索结合了关键词匹配与语义相似度。

rss · DuckDB Blog · May 21, 00:00

**背景**: Lance 是一种专为 AI 工作负载设计的开源湖仓格式，包含列式文件格式、版本化表格式和目录规范。DuckDB 是一款嵌入式列式分析数据库。混合搜索融合了基于关键词的传统搜索与基于向量的语义搜索，能兼顾精确匹配和语义相似度，提升检索效果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lance.org/">Documentation for Lance , an open lakehouse format for Multimodal AI</a></li>
<li><a href="https://www.elastic.co/what-is/hybrid-search">What is hybrid search? How it works and when to use it | Elastic</a></li>

</ul>
</details>

**标签**: `#Lance`, `#DuckDB`, `#lakehouse`, `#vector-search`, `#AI-workloads`

---

<a id="item-12"></a>
## [利用 Databricks 实现从排放报告到脱碳决策](https://www.databricks.com/blog/emissions-reporting-decarbonization-decisions) ⭐️ 6.0/10

Databricks 发布了一篇博客文章，介绍了如何利用其数据与 AI 平台进行 ESG 报告和脱碳智能分析，帮助企业将排放报告转化为数据驱动的脱碳决策。 这对企业可持续发展实践具有指导意义，展示了数据工程与 AI 技术在推动绿色转型中的实际应用，可帮助企业更有效地实现减排目标。 文章可能详细说明了如何基于 Databricks 的湖仓一体架构整合多源排放数据，并应用机器学习模型识别减排机会，具体技术实现需查阅完整内容。

rss · Databricks Blog · May 21, 10:37

**背景**: ESG 报告是企业可持续发展的合规要求，而脱碳决策涉及实际的碳排放减少行动。Databricks 提供统一的数据与 AI 平台，能够支持企业从数据收集、处理到分析的全流程，从而更好地支撑排放报告和脱碳策略制定。

**标签**: `#ESG`, `#decarbonization`, `#data engineering`, `#sustainability`, `#Databricks`

---

<a id="item-13"></a>
## [从“发生了什么”到“将会发生什么”：Databricks 推进预测分析](https://www.databricks.com/blog/what-happened-what-will-happen) ⭐️ 6.0/10

Databricks 发布博文，探讨如何借助数据和 AI 将商业分析从描述“发生了什么”转向预测“将会发生什么”。 这标志着商业智能从后见之明向前瞻性决策的演进，有望帮助企业提前洞察趋势、优化运营，对数据驱动型组织具有重要影响。 博文强调了 Databricks 统一分析平台在支持从数据清洗到机器学习模型训练的全流程分析能力，但未透露具体新工具或版本信息。

rss · Databricks Blog · May 21, 09:50

**背景**: 描述性分析帮助企业理解历史数据（如报表和仪表盘），而预测性分析利用统计模型和机器学习预测未来趋势。Databricks 是一个基于 Apache Spark 的云统一分析平台，支持大规模数据处理、数据工程、数据科学和机器学习工作负载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@achanandhi.m/what-is-databricks-why-everyone-is-using-it-af94463a852a">What is Databricks , Why Everyone is using it?? | Medium</a></li>
<li><a href="https://www.databricks.com/glossary/unified-data-analytics-platform">What is the Databricks Unified Data Analytics Platform ?</a></li>

</ul>
</details>

**标签**: `#business-intelligence`, `#predictive-analytics`, `#databricks`, `#AI`, `#data-analytics`

---