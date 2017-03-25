def right_justify(word):
    wordLength = len(word)
    blankSpace = ''
    blankSpaceCount = 70 - wordLength

    for i in range(0, blankSpaceCount):
        blankSpace = blankSpace + ' '
    print blankSpace + word

right_justify('monty')


def print_spam(input):
    print(input)

def do_twice(function, arg):
    function(arg)
    function(arg)

def do_four(function, input):
    do_twice(function, arg)
    do_twice(function, arg)

do_twice(print_spam, '69 dude')
do_four(print_spam, 'No more tests.')
