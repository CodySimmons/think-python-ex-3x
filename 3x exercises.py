print("3.1")


def right_justify(word):
    wordLength = len(word)
    blankSpace = ''
    blankSpaceCount = 70 - wordLength

    for i in range(0, blankSpaceCount):
        blankSpace = blankSpace + ' '
    print(blankSpace + word)


right_justify('monty')

print("3.2")


def print_spam(arg):
    print(arg)


def do_twice(function, arg):
    function(arg)
    function(arg)


def do_four(function, arg):
    do_twice(function, arg)
    do_twice(function, arg)


do_twice(print_spam, '69 dude')
do_four(print_spam, 'No more tests.')

print("3.3.1")


def do_twice(func):
    func()
    func()


def do_four(func):
    do_twice(func)
    do_twice(func)


def printBeam():
    print("+ - - - -", end=' ')


def printPost():
    print('|         ', end='')


def printBeams():
    do_twice(printBeam)
    print('+')


def printPosts():
    do_twice(printPost)
    print("|")


def printRows():
    printBeams()
    do_four(printPosts)


def printGrid():
    do_twice(printRows)
    printBeams()


printGrid()
