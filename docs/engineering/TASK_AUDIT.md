# 工程任务审计契约

每次重要任务更新本文件或追加独立任务记录；下列字段不得省略。没有数据写 unknown，不写推测值。

| 字段 | 要求 |
|---|---|
| task_id / project / branch | 唯一任务、项目、隔离分支 |
| selected_model / reasoning_effort | 优先运行元数据；仅请求值须写 requested |
| agent_role / status | 真实角色与执行状态 |
| tools | 实际调用工具，读写边界 |
| evidence | 固定来源、产物、Commit、PR 或本地结果 |
| quality | 已通过、失败、未测分开记录 |
| usage_if_available | 来源及计量边界；不可获得写 unknown |

## XF-INIT-20261102

- project: XingTu FDE
- branch: feat/xf-foundation-20261102
- selected_model: gpt-6.1-sol（主任务 turn_context 已核对）
- reasoning_effort: high（同上）
- agent_role: Lead；Research / Quality 的独立记录见下
- status: 本地建设与核验；最终远端状态见交接摘要及 PR
- tools: GitHub connector、gh CLI、git、Python 标准库、Codex thread 只读查询/本聊天改名、collaboration.spawn_agent
- evidence: XSA PR #2 / #3、Learn PR #6；来源版本见 registry；验证见 VALIDATION.md；提交与 Draft PR 见 XSA_HANDOFF.md
- quality: 继承旧包并纠正过期状态；原始业务效果、机器人联调与许可证最终授权未核验
- usage_if_available: unknown（未获得本任务完整官方计费或账户额度）

## XF-R1 / XF-R2

- project / branch: XingTu FDE / feat/xf-foundation-20261102
- selected_model: gpt-6.1-sol（spawn 请求与两份子任务 turn_context 均确认）
- reasoning_effort: medium（spawn 请求与 turn_context 均确认）
- agent_role: XF-R1 Research（registry/ 写入）；XF-R2 Quality（只读审查）
- status / evidence: 以 MAINLINE_LEDGER.md 的回收和 VALIDATION.md 为准
- tools: 各自回执记载的 GitHub 读取和本地文件核查
- quality: 子任务自报须经 Lead 读回与实测；不将角色推理写成执行日志
- usage_if_available: unknown

回滚：未合并阶段关闭或更新本仓 Draft PR；不自动删除分支或仓库，不改 XSA 暂存 PR，不 force push。已合并变更须另提回退 PR。
