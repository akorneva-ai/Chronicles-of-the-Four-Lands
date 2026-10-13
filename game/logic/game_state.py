import sys
from pathlib import Path

DEV_DIR = Path(__file__).resolve().parents[1] / "development"
if str(DEV_DIR) not in sys.path:
    sys.path.insert(0, str(DEV_DIR))

from game import Game as GameState

__all__ = ["GameState"]
