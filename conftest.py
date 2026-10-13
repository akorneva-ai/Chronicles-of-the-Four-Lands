import sys
from pathlib import Path

# Добавляем корневую папку и папку game в sys.path для корректной работы pytest из любой директории
ROOT_DIR = Path(__file__).resolve().parent
GAME_DIR = ROOT_DIR / "game"
DEV_DIR = GAME_DIR / "development"

for p in (str(ROOT_DIR), str(GAME_DIR), str(DEV_DIR)):
    if p not in sys.path:
        sys.path.insert(0, p)
