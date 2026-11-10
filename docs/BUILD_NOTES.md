# Build Notes — 0.71.4113-dev

## Configuration
- **Config:** BankRelease (asserts disabled, bank widgets enabled)
- **Renderer:** DX12 only. DX11 path removed in 0.66.
- **Storage:** DirectStorage 1.2 with GPU decompression. Falls back to Win32 IO on SATA drives (expect pop-in).
- **Online:** stubbed. All `NETWORK_*` natives return false.
- **Platform:** PC is an internal dev target only (workstations / QA rigs). Retail targets are PS5 and Xbox Series X|S and are built from the same changelist on separate build machines.

## Mounted content
14 DLC packs are mounted from `update/x64/dlcpacks`. Load order is defined by `<order>` in each `setup2.xml`.

## Debug console
`F8` opens the console. Useful commands:

| Command | Effect |
|---|---|
| `tp <x> <y> <z>` | Teleport player |
| `weather <name>` | Force weather (`CLEAR`, `RAIN`, `THUNDER`, `HURRICANE`) |
| `time <hh> <mm>` | Set clock |
| `spawn <model>` | Spawn vehicle by model name |
| `swap` | Switch between Lucia and Jason |
| `pool_stats` | Dump pool usage to log |
| `stream_stats` | Toggle streaming overlay |

## Crash dumps
Written to `crashdumps/` next to the executable. Symbols are in `symbols/`.
