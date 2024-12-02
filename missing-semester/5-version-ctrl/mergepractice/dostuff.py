import sys

def greet():
    print('hi')

def robot():
    print('h e l l o')

def dora():
    print('hola')

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'robot':
            robot()
        elif sys.argv[1] == 'dora':
            dora()
    else:
        greet()

if __name__ == '__main__':
    main()
