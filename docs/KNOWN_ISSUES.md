# Known Issues — 0.71.4113-dev

Severity: **A** = crash/blocker, **B** = major, **C** = minor, **D** = cosmetic.

| ID | Sev | Area | Description | Status |
|----|-----|------|-------------|--------|
| B-20114 | A | Streaming | Downtown Vice City fails to stream above ~120 km/h on HDD; NVMe recommended | Open |
| B-20118 | A | Render | DXGI_ERROR_DEVICE_HUNG on RX 6000 series with RT GI enabled | Open |
| B-20131 | B | Characters | Lucia head model missing in cutscene `cs_intro_03` | Open |
| B-20140 | B | Characters | Jason hair physics explodes when entering water | In progress |
| B-20152 | C | Animation | NPCs T-pose for 1 frame after ragdoll recovery | Open |
| B-20177 | B | AI | Traffic despawns when camera rotates quickly | In progress |
| B-20183 | B | AI | Police search pattern ignores Keys bridges | Open |
| B-20190 | C | Audio | Radio station loops after ~30 seconds | Open |
| B-20194 | C | Audio | Scanner reads placeholder street names (`STREET_TMP_##`) | Open |
| B-20203 | A | UI | Phone app crashes when opening Map | Open |
| B-20211 | D | UI | Weapon wheel icons misaligned at 21:9 | Open |
| B-20229 | B | Vehicles | Boats lose buoyancy after 10 min of game time | Open |
| B-20240 | C | Weather | Hurricane cycle disabled (GPU memory spike) | Deferred |
| B-20255 | B | Physics | Boats clip through docks at Port Gellhorn | Fixed in 0.72 |
| B-20261 | — | Save | Save games are not compatible between builds | Won't fix |
| B-20270 | C | Missions | `m_heist_01` softlocks after checkpoint 3 if player swims | Open |
| B-20288 | D | World | Billboards in Little Havana show debug texture | Open |
