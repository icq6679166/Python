def sample_var_args_call(fix1, fix2, *args):
    print "fix part=%s,%s" % (str(fix1), str(fix2))
    for arg in args:
        print "variable args:", arg


sample_var_args_call("first try", "put any")
sample_var_args_call("second try", "put some", 'hi', 'I am', "Mark HO")
sample_var_args_call("third try", "different type", '500', 135, 123.45, None)
a1 = ['500', 135, 123.45, None]
sample_var_args_call("fourth try", "different", a1)
sample_var_args_call("fifth try", "but", *a1)
a2 = ('sun', 'mon', 'tue')
sample_var_args_call("sixth try", "tuple", *a2)
a3 = set(list('APPLEBANANACITRON'))
sample_var_args_call("seventh try", 'set', *a3)
a4 = {'name': "BDPY", "duration": "24hr", 'instructor': 'Mark'}
sample_var_args_call("eight try", "dict", *a4)
