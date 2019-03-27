from demo_pkg import sample_message


def foo(a, b):
    print "[demo35]%s" % sample_message, a ** b


def bar(a, b):
    print "[demo35]%s" % sample_message, b ** a
