import sys

def cat():
    print('meow')

def default():
    print('hello')

def dog():
    print('bark')

def main():
<<<<<<< HEAD
    if sys.argv[1] == 'cat':
        cat()
=======
    if sys.argv[1] == 'dog':
        dog()
>>>>>>> dog
    else:
        default()

if __name__ == '__main__':
    main()
