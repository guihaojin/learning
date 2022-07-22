# Reference:
# https://stackoverflow.com/questions/8315389/how-do-i-print-functions-as-they-are-called
# https://docs.python.org/3/library/sys.html#sys.setprofile
# https://github.com/python/cpython/blob/3.10/Lib/traceback.py

import sys

def trace_calls(frame, event, arg):
    if event == 'call':
        print('Calling', frame.f_code.co_name, 'line number', frame.f_lineno)
        return trace_calls
    elif event == 'return':
        print('Done with', frame.f_code.co_name)
        return None
    return trace_calls

def foo():
    print('in foo start')
    bar()
    print('in foo end')
    return

def bar():
    print('in bar')
    return


if __name__ == '__main__':
    sys.setprofile(trace_calls)
    foo()
