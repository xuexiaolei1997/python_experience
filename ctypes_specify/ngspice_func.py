"""
use ngspice
"""
import ctypes


# Array translate to point
class DoubleArrayType:
    def from_param(self, param):
        typename = type(param).__name__
        if hasattr(self, 'from_' + typename):
            return getattr(self, 'from_' + typename)(param)
        elif isinstance(param, ctypes.Array):
            return param
        else:
            raise TypeError("Can't convert %s" % typename)

    # Cast from array.array objects
    def from_array(self, param):
        if param.typecode != 'd':
            raise TypeError('must be an array of doubles')
        ptr, _ = param.buffer_info()
        return ctypes.cast(ptr, ctypes.POINTER(ctypes.c_double))

    # Cast from lists/tuples
    def from_list(self, param):
        val = ((ctypes.c_double)*len(param))(*param)
        return val

    from_tuple = from_list

    # Cast from a numpy array
    def from_ndarray(self, param):
        return param.ctypes.data_as(ctypes.POINTER(ctypes.c_double))


_mod = ctypes.cdll.LoadLibrary('ngspice.dll')

# pdapi_ngSpice_Init
_pdapi_ngSpice_Init = _mod.pdapi_ngSpice_Init
_pdapi_ngSpice_Init.restype = ctypes.c_int


def pdapi_ngSpice_Init():
    return _pdapi_ngSpice_Init()


# pdapi_ngSpice_Command
_pdapi_ngSpice_Command = _mod.pdapi_ngSpice_Command
# _pdapi_ngSpice_Command.argtypes = (ctypes.c_char_p)
_pdapi_ngSpice_Command.restype = ctypes.c_int


def pdapi_ngSpice_Command(cmd):
    cmd = ctypes.c_char_p(cmd.encode())
    return _pdapi_ngSpice_Command(cmd)


# pdapi_sweep
_pdapi_sweep = _mod.pdapi_sweep
DoubleArray = DoubleArrayType()
_pdapi_sweep.argtypes = (ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, DoubleArray)
_pdapi_sweep.restype = ctypes.c_int


def pdapi_sweep(simuType, sweepCmdPtr, outCmdPtr, optCmdPtr, resPtr):
    sweepCmdPtr = ctypes.c_char_p(sweepCmdPtr.encode())
    outCmdPtr = ctypes.c_char_p(outCmdPtr.encode())
    optCmdPtr = ctypes.c_char_p(optCmdPtr.encode())
    return _pdapi_sweep(simuType, sweepCmdPtr, outCmdPtr, optCmdPtr, resPtr)


# pdapi_remCirc
_pdapi_remCirc = _mod.pdapi_remCirc
# _pdapi_remCirc.argtypes = ctypes.c_char_p
_pdapi_remCirc.restype = ctypes.c_int


def pdapi_remCirc(cmd):
    cmd = ctypes.c_char_p(cmd.encode())
    return _pdapi_remCirc(cmd)


# pdapi_adjust_param
_pdapi_adjust_param = _mod.pdapi_adjust_param
# _pdapi_adjust_param.argtypes = ctypes.c_char_p
_pdapi_adjust_param.restype = ctypes.c_int


def pdapi_adjust_param(cmd):
    cmd = ctypes.c_char_p(cmd.encode())
    return _pdapi_adjust_param(cmd)
