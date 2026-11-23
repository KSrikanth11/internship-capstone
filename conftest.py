"""Shared test setup: every test runs offline with the mock LLM, so CI never needs a key."""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
os.environ["LLM_PROVIDER"] = "mock"
