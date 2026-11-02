# 来源登记表（2026-11-02 固定版本）

`L1` 表示读取原件或核对路径，不等于独立复核业务事实。`commit` 是仓库修订版，`blob` 是文件内容对象，两者不能互换。机器证据见 [snapshot.json](snapshot.json)。`source_claim` 为来源自述，`hypothesis` 为设计假设；prototype/research 仅作成熟度。

| ID | 主题 / 固定原件 | 来源及主张 | 版本证据 / 边界 |
|---|---|---|---|
| <a id="fde-src-001"></a>FDE-SRC-001 | [进场、在场、离场](https://github.com/xingtu1996/xingtu-articles/blob/a892537f7f52f7b65abd0a47336db7dec74895d6/articles/2026/09/2026-09-25-fde-working-method-three-stages.md) | first_party / source_claim | commit `a892537f7f52f7b65abd0a47336db7dec74895d6`；blob `12f6df3a76b52c2cda771cce916f5e898fe0f7a2`；L1。作者方法与经验自述；效果未复测。 |
| <a id="fde-src-002"></a>FDE-SRC-002 | [资金报表改造](https://github.com/xingtu1996/xingtu-articles/blob/a892537f7f52f7b65abd0a47336db7dec74895d6/articles/2026/10/2026-10-28-fde-fund-report.md) | third_party / source_claim | commit `a892537f7f52f7b65abd0a47336db7dec74895d6`；blob `e8563a37c6cbfacf8aa1f8678bec9dee038e7b11`；L1。第三方案例转述；九天交付与银行账户数量等未独立核实。 |
| <a id="fde-src-003"></a>FDE-SRC-003 | [多平台评论数据清洗](https://github.com/xingtu1996/xingtu-articles/blob/a892537f7f52f7b65abd0a47336db7dec74895d6/articles/2026/10/2026-10-28-fde-data-cleaning.md) | third_party / source_claim | commit `a892537f7f52f7b65abd0a47336db7dec74895d6`；blob `b1e591f15b4dd7f4bec514ba1c85c473588479b8`；L1。第三方从业者案例转述；数据与效果未复测。 |
| <a id="fde-src-004"></a>FDE-SRC-004 | [四道质量门禁](https://github.com/xingtu1996/xingtu-articles/blob/a892537f7f52f7b65abd0a47336db7dec74895d6/articles/2026/10/2026-10-26-four-quality-gates.md) | third_party / source_claim | commit `a892537f7f52f7b65abd0a47336db7dec74895d6`；blob `cf67d386834d09ab8064246a3075995ec5d109a4`；L1。主体流程及数字转述公开分享，原文§8明示非本人实测；仅§7缩小版为作者个人实践。 |
| <a id="fde-src-005"></a>FDE-SRC-005 | [DSH Superagent README](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/6337fc823ce20251c8de8085948165c81aaa701e/README.md) | official / source_claim | commit `6337fc823ce20251c8de8085948165c81aaa701e`；blob `39e1c4af122f11dd72ac0d2b34b79d6f8ae259ea`；L1。官方来源自述；研究原型/开发者预览；未安装或复测。 |
| <a id="fde-src-006"></a>FDE-SRC-006 | [DSH Superagent docs 000–008](https://github.com/deepseek-ai/dsh-superagent-prototype/tree/6337fc823ce20251c8de8085948165c81aaa701e/docs) | official / source_claim | commit `6337fc823ce20251c8de8085948165c81aaa701e`；tree `e7247c39739f274e92651df72a00138427e22957`；L1。官方来源自述；研究原型/开发者预览；未安装或复测。 |
| <a id="fde-src-007"></a>FDE-SRC-007 | [DeepSeek Harness README](https://github.com/deepseek-ai/deepseek-harness/blob/ce7073d51254c26cd63b22a60835b8f948deb447/README.md) | official / source_claim | commit `ce7073d51254c26cd63b22a60835b8f948deb447`；blob `7941e30f7bdca9391befe39b9115d211157fa42d`；L1。官方来源自述；研究原型/开发者预览；未安装或复测。 |
| <a id="fde-src-008"></a>FDE-SRC-008 | [XSA FDE 产品设计研究](https://github.com/xingtu1996/xingtu-super-agent/blob/9ac07724bd312ce1be5ef4b8c1f2e45a313c8f0d/docs/research/FDE_PRODUCT_BLUEPRINT.md) | first_party / hypothesis；成熟度 design | commit `9ac07724bd312ce1be5ef4b8c1f2e45a313c8f0d`；blob `d05072ee1f7ddf5250ac34fb3f0e2b0a8be9a49f`；L1。固定设计修订版，非部署成果。 |
| <a id="fde-src-009"></a>FDE-SRC-009 | [Event Bridge 离线实验](https://github.com/xingtu1996/xingtu-harness/blob/7e3d12b04bab9032dbc0530bd4c20a698a06ff56/experiments/event-bridge-v0.1/PRODUCT_README.md) | first_party / source_claim；成熟度 prototype | commit `7e3d12b04bab9032dbc0530bd4c20a698a06ff56`；blob `dc5bda8cf4119bcc932814ba49c5f7ae9131bcc3`；L1。路径已核实；未执行测试。 |
| <a id="fde-src-010"></a>FDE-SRC-010 | [FDE 学习卡](https://github.com/xingtu1996/xingtu-learn/blob/c13dc92b1ea3af83f75e84de014623282f650dbb/10-tech/xsa-super-agent/2026-11-02-dsh-superagent-fde-knowledge-commons.md) | first_party / source_claim；成熟度 research | commit `c13dc92b1ea3af83f75e84de014623282f650dbb`；blob `16c53ec4268cb992237969511344edd2e2a873ae`；L1。学习记录存在；未作为业务效果证据。 |
| <a id="fde-src-011"></a>FDE-SRC-011 | [项目范围失控与护栏](https://github.com/xingtu1996/xingtu-articles/blob/a892537f7f52f7b65abd0a47336db7dec74895d6/articles/2026/10/2026-10-21-project-scope-out-of-control-fde.md) | third_party / source_claim | commit `a892537f7f52f7b65abd0a47336db7dec74895d6`；blob `5a1ad7083581d06a27bd7ad4292414cb2382295f`；L1。核心项目及254/172/51%为第三方转述，§4含作者实践；原始分享未获可访问直链，不以此授权无限追加范围。 |
| <a id="fde-src-012"></a>FDE-SRC-012 | [XSA PR3 来源包](https://github.com/xingtu1996/xingtu-super-agent/blob/59aa30daee3522f192ea9d55e093148ccc6f8ba1/incubation/xingtu-fde/README.md) | first_party / source_claim；成熟度 incubation | commit `59aa30daee3522f192ea9d55e093148ccc6f8ba1`；blob `760e8b17b483ef3e4bdd9ae15d451fe5f683eaaa`；L1。固定迁移来源；不代表所有包内声明已核实。 |

来源006的000–008九份文档分别记录 blob SHA 与固定 URL 于 snapshot；本轮核对全部文件存在，未逐份重审设计。来源008/009/010/012对应 XSA PR2、Harness PR4、Learn PR6、XSA PR3；保留固定版本，不跟随 PR 最新 head 漂移。

更正：来源004主体为第三方转述，作者缩小版实践独立区分；来源009/010使用合法 claim_status 枚举，不把 prototype/research 当证据等级。范围失控案例新增为011。

版权：articles 原仓标示 CC BY-SA；本表仅链接并给出独立摘要。其他资料遵守原许可证，未知时 link_only。没有复制文章、技能或研究文档全文。

核实范围：远端版本、对象类型、路径与五篇文章的来源归属。未核实：业务效果、案例原始分享与数字、运行兼容性。权限影响：只读 GitHub，本地 registry 三文件更新；回退：恢复登记文件前一版本。
