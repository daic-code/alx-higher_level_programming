#!/usr/bin/env python3
import sys
if __name__=="__main__":
    argv = sys.argv[1:]
    argc = len(argv)

    if argc == 0:
        print(f"0 arguments")
    elif argc == 1:
        print(f"1 argument")
    else:
        print(f"{argc} arguments")
    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")
