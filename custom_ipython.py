import itertools
import sys


def get_user_input():
    for i in itertools.count():
        yield i, input("In [{0}]: ".format(i))


def exec_function(user_input):

    try:
        compile(user_input, "<stdin>", "eval")
    except SyntaxError:
        return exec
    
    return eval

def exec_user_input(i, user_input, user_globals):

    user_globals = user_globals.copy()
    try:
        retval = exec_function(user_input)(user_input, user_globals)
    except Exception as e:
        print("{0}: {1}".format(e.__class__.__name__, e))
    else:
        if retval is not None:
            print("Out [{0}]: {1}".format(i, retval))

    return user_globals

def exit():
    sys.exit()

def main():
    
    user_globals = {}

    for i, user_input in get_user_input():
        user_globals = exec_user_input(i, user_input, user_globals)

if __name__ == "__main__":
    main()