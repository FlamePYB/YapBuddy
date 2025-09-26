"""Launcher for YapBuddy.

This script ensures the repository root is on sys.path so `res_rc` and
top-level resource imports work, then calls `src.main.main()`.
"""
import os
import sys

# Ensure repo root (this file's parent) is on sys.path
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)
# Also expose the `src` directory on sys.path so code can import top-level modules
# written to assume they are available directly (e.g., `from UI.Compiled...`).
SRC_DIR = os.path.join(REPO_ROOT, "src")
if os.path.isdir(SRC_DIR) and SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)
# Ensure the resources directory is on sys.path so `import res_rc` (top-level)
# continues to work as expected without making `res` a package.
RES_DIR = os.path.join(REPO_ROOT, "res")
if os.path.isdir(RES_DIR) and RES_DIR not in sys.path:
    sys.path.insert(0, RES_DIR)

from src.main import main


def run():
    return main()


if __name__ == "__main__":
    sys.exit(run())
