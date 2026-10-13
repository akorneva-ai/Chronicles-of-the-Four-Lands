import sys
from pathlib import Path

DEV_DIR = Path(__file__).resolve().parents[1] / "development"
if str(DEV_DIR) not in sys.path:
    sys.path.insert(0, str(DEV_DIR))

from events import EVENTS, random_event, apply_event, roll_event

__all__ = ["EVENTS", "random_event", "apply_event", "roll_event"]
