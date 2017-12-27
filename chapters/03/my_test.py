import my_debugger

def main():
    debugger = my_debugger.debugger()
    debugger.load("C:\\WINDOWS\\system32\\calc.exe", showGUI=True)

if __name__ == "__main__":
    main()
