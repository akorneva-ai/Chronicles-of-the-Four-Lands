import sys
from pathlib import Path

_DEV_DIR = str(Path(__file__).resolve().parent)
if _DEV_DIR not in sys.path:
    sys.path.insert(0, _DEV_DIR)
