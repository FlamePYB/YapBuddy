from src.main import main
import sys
import logging as lg

lg.basicConfig(level="DEBUG", format="[%(levelname)s] %(message)s")


def run():
    lg.info("YapBuddy started")
    running = main()
    lg.info("YapBuddy closed")
    return running


if __name__ == "__main__":
    sys.exit(run())
