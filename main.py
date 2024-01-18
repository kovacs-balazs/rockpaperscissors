from game import set_troll
from gui import open_gui
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--notroll', action="store_true", help="troll mód kikapcsolása")

args = parser.parse_args()
set_troll(not args.notroll)

open_gui()