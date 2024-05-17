import sys

from console import Console
from pathlib import Path

if __name__ == "__main__":
    paths = [Path(sys.path[0], "console")]

    kernel = Console(description="Zahlen console commands")

    kernel.auto_import(paths, "console")
    kernel.exec_()