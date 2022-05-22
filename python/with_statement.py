# https://docs.python.org/3/reference/compound_stmts.html#the-with-statement

# with EXPRESSION as TARGET:
#     SUITE

# is semantically equivalent to:

# manager = (EXPRESSION)
# enter = type(manager).__enter__
# exit = type(manager).__exit__
# value = enter(manager)
# hit_except = False

# try:
#     TARGET = value
#     SUITE
# except:
#     hit_except = True
#     if not exit(manager, *sys.exc_info()):
#         raise
# finally:
#     if not hit_except:
#         exit(manager, None, None, None)

