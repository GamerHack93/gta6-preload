#!/usr/bin/env python3
"""Project Americas dev launcher - integrity check & RPF header decrypt.

Usage: python tools/launcher.py [--skip-verify]
"""
import json, os, random, sys, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def bar(label, seconds):
    width = 30
    for i in range(width + 1):
        sys.stdout.write("\r  {:<44} [{}{}] {:3d}%".format(label[-44:], "#" * i, "." * (width - i), i * 100 // width))
        sys.stdout.flush()
        time.sleep(seconds / width * random.uniform(0.4, 1.6))
    print("  OK")


def main():
    print("=" * 84)
    print("  PROJECT AMERICAS  |  dev launcher  |  build 0.71.4113-dev  |  CL 31847293")
    print("=" * 84)
    try:
        with open(os.path.join(ROOT, "build_manifest.json"), encoding="utf-8") as f:
            manifest = json.load(f)
        files = manifest["files"]
    except Exception:
        files = []
    total = sum(f["size"] for f in files)
    print("\n  manifest: {} files, {:.1f} GB".format(len(files), total / 1024 ** 3))

    if "--skip-verify" not in sys.argv:
        print("\n[1/4] Verifying archives (sha256)...")
        for f in [x for x in files if x["path"].endswith(".rpf")][:12]:
            bar(f["path"], 0.6)
        print("  ... {} more files".format(max(0, len(files) - 12)))

    print("\n[2/4] Decrypting RPF headers (AES-256 / NG keys)...")
    bar("key exchange", 1.2)
    bar("header table", 1.6)

    print("\n[3/4] Checking hardware...")
    for item in ["DirectX 12 Ultimate", "GPU", "VRAM", "RAM", "DirectStorage"]:
        time.sleep(0.5)
        print("  {:<24} OK".format(item))

    print("\n[4/4] Booting GTA6_dev.exe ...")
    bar("initialising RAGE", 2.2)
    bar("mounting dlcpacks (14)", 1.8)
    time.sleep(1.0)
    print("\n" + "=" * 84)
    print("""
        ____  ____  ____   __   _  _  _  _  ____  __    __
       (  _ \\(  _ \\(  _ \\ /  \\ ( \\/ )( \\/ )(  _ \\(  )  (  )
        )   / )   / ) _ ((  O ) )  /  \\  /  ) __// (_/\\/ (_/\\
       (__\\_)(__\\_)(____/ \\__/ (__/  (__/  (__)  \\____/\\____/

          Ты правда думал, что GTA 6 лежит на GitHub? :)
          Все {} "архивов" - это текстовые файлы по 130 байт.
          Лучше дождись релиза.
""".format(len(files) or "эти"))
    print("=" * 84)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n  aborted.")
