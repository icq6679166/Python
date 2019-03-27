import graphviz as gv
print gv.__version__

#g1 = gv.Graph(format='svg')
#g1 = gv.Graph(format='pdf')
g1 = gv.Graph(format='png')
g1.node('A')
g1.node('B')
g1.node('C')
g1.edge('A','B')
g1.edge('B','C')
g1.edge('C','C')
print g1.source
g1.render('graph\\demo63')
