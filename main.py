import sys
import os

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "--show_steps":
            os.system("python src/main_steps.py")
        else:
            os.system("python src/main.py")
    else:
        os.system("python src/main.py")

if __name__ == "__main__":
    main()