import sys

def greet():
    print('hi')

def robot():
    print('h e l l o')

def main():
    if len(sys.argv) > 1:
        robot()
    else:
        greet()

if __name__ == '__main__':
    main()
