import sys

def greet():
    print('hi')

def dora():
    print('hola')

def main():
    if len(sys.argv) > 1:
        dora()
    else:
        greet()

if __name__ == '__main__':
    main()
