def sample_var_kv_pair(fix1, fix2, **kargs):
    print "fix1&2 is:", fix1, fix2
    for k, v in kargs.items():
        print '[%s]==>%s' % (str(k), str(v))


sample_var_kv_pair("first try", "hello world")
sample_var_kv_pair("second try", "real scenrio",
                   border=4, shape='rectangle', style='dashed')
dict1 = {'border': 4, 'shape': 'rectangle', 'style': 'dashed'}
sample_var_kv_pair("third try", "try dictionary", **dict1)
