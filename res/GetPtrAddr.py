from pymem import *
from pymem.process import *

pm = Pymem("eldenring.exe")
gameModule = module_from_name(pm.process_handle, "eldenring.exe").lpBaseOfDll


def GetPtrAddr(base, offsets):
    addr = pm.read_longlong(base)
    for i in offsets:
        if i != offsets[-1]:
            addr = pm.read_longlong(addr + i)
    return addr + offsets[-1]
