"""
An interactive python intrepreter very similar to Ipython.

Author: Benjamin Garrard
Dat: 6/12/2019
"""
import itertools
import sys


def get_user_input():
    """
    Get user input.

    This method will always loop until the user exits the intrepreter.  It uses
    a generator and lazily gathers user input.

    Yields
    ------
    int
        The number of user input.
    str
        The user's input.   Which should either be a statement or expression.

    """
    for i in itertools.count():
        yield i, input("In [{0}]: ".format(i))


def exec_function(user_input):
    """
    Figure out what function is needed to execute user input.

    The use of eval and exec are different.  This method will use eval to
    execute the users input first and then if that fails it must be an 
    statement that was passed since eval will evaluate an expression.

    Parameters
    ----------
    user_input: str
        The users input could be an expression, statement, or invalid

    Returns
    -------
    function
        The exec or eval function will be returned.

    """
    try:
        compile(user_input, "<stdin>", "eval")
    except SyntaxError:
        return exec
    
    return eval


def exec_user_input(i, user_input, user_globals):
    """
    Execute the users code.

    Parameters
    ----------
    i: int
        Index count of user input.
    user_input: str
        The user's input.  It could be a statement, expression, or invalid
    user_globals: dict
        A dictionary for global variables the user has inputted.

    Returns
    -------
    dict
        Returns the global variables since they are a copy of the globals and
        may have been updated.

    """
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
    """Exit the intrepreter."""
    sys.exit()

def main():
    """Run the Program."""
    user_globals = {}

    for i, user_input in get_user_input():
        user_globals = exec_user_input(i, user_input, user_globals)

if __name__ == "__main__":
    main()