#!/usr/bin/python3
def safe_function(fct, *args):
    """ Executes a function safely """
    try:
        fn_result = fct(*args)
        return (fn_result)
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return (None)
