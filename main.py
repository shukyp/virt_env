
# imports
import sys
import os

#----------------------------------
def main() -> None:
    print(f"Module name: {__name__}")
    print("Function main is running...")

#----------------------------------
if __name__ == '__main__':
    print(f"Current Path (CWD): {os.getcwd()} ")
    print(f"CLI args: {sys.argv[1:]} ")
    main()
