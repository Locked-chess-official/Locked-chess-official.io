import sys
from locked_chess_game_module import *
from locked_chess_game_class import LockedChessClass


major_version=sys.version_info.major
minor_version=sys.version_info.minor
if not (major_version>=3):
    raise ImportError('The version is below 3.8 .')
elif (major_version==3 and minor_version<8):
    raise ImportError('The version is below 3.8 .')
