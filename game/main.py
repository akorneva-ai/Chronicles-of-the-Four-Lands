import sys
from pathlib import Path

DEV_DIR = Path(__file__).resolve().parent / "development"
if str(DEV_DIR) not in sys.path:
    sys.path.insert(0, str(DEV_DIR))

from main import main as run_game

if __name__ == "__main__":
    run_game()
