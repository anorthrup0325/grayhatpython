import ctypes

import my_debugger_defines as defines

kernel32 = ctypes.windll.kernel32

class debugger(object):
    def __init__(self):
        pass

    def load(self, path_to_exe, showGUI=False):
        """Load an exe and display process information

        path_to_exe: The path to the exe
        showGUI: True if you want to view the process when it is run
        """

        creation_flags = defines.DEBUG_PROCESS if showGUI is False\
                         else defines.CREATE_NEW_CONSOLE

        # Instantiate the structs
        startupinfo = defines.STARTUPINFO()
        process_information = defines.PROCESS_INFORMATION()

        # The following two options allow the started process
        # to be shown as a separate window.
        startupinfo.dwFlags = defines.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = defines.SW_HIDE

        # Initialize the cb to the size of the struct
        startupinfo.cb = ctypes.sizeof(startupinfo)

        # https://msdn.microsoft.com/en-us/library/windows/desktop/ms682425(v=vs.85).aspx
        if kernel32.CreateProcessA(path_to_exe, None, None, None, None,
                                   creation_flags, None, None,
                                   ctypes.byref(startupinfo),
                                   ctypes.byref(process_information)):
            print "[*] We have successfully launched the process!"
            print "[*] PID: %d" % process_information.dwProcessId
        else:
            print "[*] Error: 0x%08x." % kernel32.GetLastError()
