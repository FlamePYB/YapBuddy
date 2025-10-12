import logging
import sys

from src.main import main

logging.basicConfig(level="DEBUG", format="[%(levelname)s] %(message)s")
lg = logging.getLogger(__name__)


def run():
    lg.info("YapBuddy started")
    running = main()
    lg.info("YapBuddy closed")
    return running


if __name__ == "__main__":
    sys.exit(run())
