from res.GetPtrAddr import *


def Runes(rune_value):
    pm.write_int(GetPtrAddr(gameModule + 0x03CF1558, [0x28, 0x0, 0x30, 0x6C]), rune_value)

