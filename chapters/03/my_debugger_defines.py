import ctypes

# Windows Data Types
# https://msdn.microsoft.com/en-us/library/windows/desktop/aa383751(v=vs.85).aspx
WORD = ctypes.c_ushort
"""A 16-bit unsigned integer. The range is 0 through 65535 decimal."""
DWORD = ctypes.c_ulong
"""A 32-bit unsigned integer. The range is 0 through 4294967295
decimal.
"""
LPBYTE = ctypes.POINTER(ctypes.c_ubyte)
"""A pointer to a BYTE."""
LPTSTR = ctypes.POINTER(ctypes.c_char)
"""A pointer to a null-terminated string of 8-bit Windows (ANSI)
characters.
"""
HANDLE = ctypes.c_void_p
"""A handle to an object."""

# Process Creation Flags
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms684863(v=vs.85).aspx
DEBUG_PROCESS = 0x00000001
"""The calling thread starts and debugs the new process and all child
processes created by the new process. It can receive all related debug
events using the WaitForDebugEvent function.
A process that uses DEBUG_PROCESS becomes the root of a debugging
chain. This continues until another process in the chain is created
with DEBUG_PROCESS.
If this flag is combined with DEBUG_ONLY_THIS_PROCESS, the caller
debugs only the new process, not any child processes.
"""
CREATE_NEW_CONSOLE = 0x00000010
"""The new process has a new console, instead of inheriting its
parent's console (the default). For more information, see Creation of a
Console.
This flag cannot be used with DETACHED_PROCESS.
"""

# STARTUPINFO structure
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms686331(v=vs.85).aspx
class STARTUPINFO(ctypes.Structure):
    """Specifies the window station, desktop, standard handles, and
    appearance of the main window for a process at creation time.
    """
    _fields_ = [
        ("cb", DWORD),
        ("lpReserved", LPTSTR),
        ("lpDesktop", LPTSTR),
        ("dwX", DWORD),
        ("dwY", DWORD),
        ("dwXSize", DWORD),
        ("dwYSize", DWORD),
        ("dwXCountChars", DWORD),
        ("dwYCountChars", DWORD),
        ("dwFillAttribute", DWORD),
        ("dwFlags", DWORD),
        ("wShowWindow", WORD),
        ("cbReserved2", WORD),
        ("lpReserved2", LPBYTE),
        ("hStdInput", HANDLE),
        ("hStdOutput", HANDLE),
        ("hStdError", HANDLE)
    ]

# Related constants
STARTF_USESHOWWINDOW = 0x00000001
"""The wShowWindow member contains additional information."""
SW_HIDE = 0
"""Hides the window and activates another window.
Extra: https://msdn.microsoft.com/en-us/library/windows/desktop/ms633548(v=vs.85).aspx
"""

# PROCESS_INFORMATION structure
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms684873(v=vs.85).aspx
class PROCESS_INFORMATION(ctypes.Structure):
    """Contains information about a newly created process and its
    primary thread. It is used with the CreateProcess,
    CreateProcessAsUser, CreateProcessWithLogonW, or
    CreateProcessWithTokenW function.
    """
    _fields_ = [
        ("hProcess", HANDLE),
        ("hThread", HANDLE),
        ("dwProcessId", DWORD),
        ("dwThreadId", DWORD)
    ]
