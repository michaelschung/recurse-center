import sys

def greet():
    print('hi')

<<<<<<< HEAD
def robot():
    print('h e l l o')

||||||| 4e34ab7
=======
def dora():
    print('hola')

>>>>>>> dora
def main():
<<<<<<< HEAD
    if len(sys.argv) > 1:
        robot()
    else:
        greet()
||||||| 4e34ab7
    greet()
=======
    if len(sys.argv) > 1:
        dora()
    else:
        greet()
>>>>>>> dora

if __name__ == '__main__':
    main()
