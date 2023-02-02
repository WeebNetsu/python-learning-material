# The file python is running directly is called the __main__ module
# __name__ returns the current file/module name
import first_module

def main():
    print(f"This is the {__name__} module")

# the below code will execute if you: "$> python3 main.py"
if __name__ == '__main__': # if this file is being run directly by python
    main()