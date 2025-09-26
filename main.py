"""Compatibility launcher.

This file delegates to the proper repository launcher `run.py` so editors
that execute `main.py` still start the application.
"""
from run import run


if __name__ == "__main__":
    run()