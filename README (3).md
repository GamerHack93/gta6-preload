# Grand Theft Auto VI — PS5 Preload Build (Retail)

![platform](https://img.shields.io/badge/platform-PlayStation%205-blue)
![build](https://img.shields.io/badge/build-01.00.00-green)
![region](https://img.shields.io/badge/region-CUSA--XXXXX-lightgrey)
![size](https://img.shields.io/badge/size-%7E212%20GB-red)
![status](https://img.shields.io/badge/status-Playable-success)

> ✅ **Official PS5 preload files** (post-download).  
> Dump / extracted package contents after preload completed on **2026-11-10**.  
> **The game is already playable.**

Retail PlayStation 5 package of **Grand Theft Auto VI**, prepared for the November 19, 2026 launch.

| | |
|---|---|
| **Title** | Grand Theft Auto VI |
| **Platform** | PlayStation 5 |
| **Build** | 01.00.00 (preload) |
| **Package date** | 2026-11-09 / 2026-11-10 |
| **Install size** | ~212 GB |
| **Content type** | Full game (Story + base assets) |
| **Status** | **Playable** — can be launched and played right now |
| **Online** | Currently stubbed / will be enabled after official launch |

## 📦 Package Layout

```
.
├── UPXXXX-CUSAXXXXX_00-GTAVI0000000000.pkg     (main package)
├── param.sfo
├── playgo-chunk.dat
├── sce_sys/
│   ├── icon0.png
│   ├── pic0.png / pic1.png
│   ├── save_data.png
│   └── trophy00.trp
├── sce_module/
├── Image0/
│   ├── eboot.bin
│   ├── ps5_data/
│   ├── levels/                  (americas / leonida / vicecity)
│   ├── audio/
│   ├── movies/
│   ├── textures/
│   ├── animations/
│   └── update/
└── checksums / manifest (internal)
```

### Major content chunks (approximate)

| Chunk / Folder                  | Size (approx.) | Description                              |
|---------------------------------|----------------|------------------------------------------|
| Levels (americas)               | ~64.5 GB       | Main world, Leonida, Vice City           |
| TextureDatabases                | ~53.4 GB       | Textures & materials                     |
| Audio                           | ~22.2 GB       | Music, SFX, dialogue                     |
| Story content                   | ~17.9 GB       | Missions / narrative assets              |
| Core / BVH / engines            | ~24 GB         | Engine, physics, base systems            |
| Movies / cutscenes              | ~3–4 GB        | Cinematics                               |
| Other (clothes, vehicles, weapons) | ~25 GB      | Characters, vehicles, weapons, etc.      |

## 🗺️ World Content

- **Vice City** — urban core, beaches, downtown, interiors  
- **Leonida** — state map, highways, suburbs, wetlands  
- **Leonida Keys** — islands & bridges  
- **Ambrosia** — industrial district  
- **Port Gellhorn** — docks  
- **Mount Kalaga** — national park area  
- Vehicles, weapons, clothing and character sets included in the base package

## 🎮 Playability

The preload files are **fully working**.  
You can already launch the game and play through the single-player campaign.  
Online features are currently disabled and will be activated after the official release on November 19.

## 🚀 How to Run on PS5

### Requirements
- PS5 firmware that supports fPKG installation (jailbreak / Homebrew)
- Free space on SSD: **at least 220–230 GB**
- Fast internal SSD or external USB drive recommended

### Method 1: Install via Package Installer (Recommended)

1. Copy the `.pkg` file to a USB drive (exFAT or FAT32).
2. Insert the USB drive into the PS5.
3. Launch **Package Installer** (or Itemzflow / etaHEN-based tools).
4. Select `UPXXXX-CUSAXXXXX_00-GTAVI0000000000.pkg` and start the installation.
5. Wait for the installation to finish (~212 GB).
6. Once installed, the game will appear in your library. Launch it like any other game.

### Method 2: Via FTP

1. Enable the FTP server on your PS5 through Homebrew.
2. Connect from a PC and upload the `.pkg` to `/data/pkg/` or `/user/home/`.
3. Install it using Package Installer or Debug Settings → Game → Package Installer.
4. Launch the game after installation.

### Method 3: Extracted Version (Image0 folder)

If you already have the extracted files (`Image0/` + `sce_sys/`):

1. Create the correct title structure on the console.
2. Use tools such as FPKG Creator to generate an fPKG from the folder,  
   or mount it using the appropriate homebrew solution (depends on your firmware).
3. Make sure `param.sfo` and `eboot.bin` are in the correct locations.

### Important Notes

- The first launch may take noticeably longer (shader compilation / cache creation).
- Saves work normally.
- Online and some network features are currently inactive.
- After the day-one patch releases on November 19, it will need to be installed separately.

## 📝 Notes

- Files obtained after successful preload completion (November 10, 2026).
- This is the **day-0 / preload** version. Day-one patch is expected closer to launch (November 19).
- PlayGo structure is used — the game can start with a partial download, but a full install is required for the complete experience.

## ⚠️ Important

These are **retail PS5 package files** extracted after preload.  
Do not redistribute. For personal archival / research use only.

---
*PS5 Preload Dump — November 10, 2026 · Already Playable*
