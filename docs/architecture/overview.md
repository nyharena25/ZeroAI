# Architecture overview

This is the canonical architecture document for ZeroAI. It describes the **intended**
boundaries of ZeroAI 0.1 and states what exists today. Anything marked *planned* is not
implemented, and its package does not exist in the source tree yet. Package names for planned
components are provisional.

## Status at a glance

| Component | Package | Responsibility | Status |
|---|---|---|---|
| Package and CLI | `zeroai`, `zeroai.__main__` | Version, `--help` / `--version` | Implemented |
| ZeroCore | `zeroai.core` | Configuration, request orchestration, lifecycle | Planned |
| ZeroBrain | `zeroai.brain` | Local Ollama adapter: timeouts, errors, active model | Planned |
| ZeroAPI | `zeroai.api` | Local REST API on `127.0.0.1` | Planned |
| ZeroGuard | `zeroai.security` | Local authentication, deny-by-default policies, approvals | Planned |
| ZeroAgent | `zeroai.agent` | Closed allowlist of deterministic tools | Planned |
| ZeroMonitor | `zeroai.monitor` | Read-only CPU/RAM/disk/NVIDIA metrics | Planned |
| Desktop UI | `zeroai.ui` | Qt window, chat, approval dialog (owned by the UI agent) | Planned |
| User service | — | `systemd --user` unit | Planned |

## Intended request flow

```text
Desktop UI ──(authenticated local HTTP)──▶ ZeroAPI
                                            ├──▶ ZeroBrain ──▶ Ollama (local only)
                                            └──▶ ZeroGuard ──▶ ZeroAgent ──▶ ZeroMonitor
                                                  (policy +       (allowlisted tools)
                                                   approval)
```

## Boundaries that later phases must keep

- **The model never executes anything.** ZeroBrain returns text only. It has no access to
  subprocesses, the shell or D-Bus, and model output is never evaluated as a command.
- **Actions go through ZeroGuard.** Every tool call is checked against a closed allowlist and
  deny-by-default policies. Mutating actions require an explicit, single-use, expiring user
  approval bound to the exact tool and arguments.
- **Fail closed.** Unknown tools, invalid arguments, missing credentials, expired approvals or an
  unavailable backend result in refusal, never in a fallback action.
- **Local only in 0.1.** The API binds to loopback, and no data is sent to a cloud provider.
- **Least privilege.** ZeroAI runs as the desktop user. It never runs as root and never uses sudo.
- **The UI depends on the HTTP contract only**, not on internal Python modules.

The detailed API contract is defined in Phase 02.
