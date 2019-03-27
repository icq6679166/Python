import graphviz as gv

g2 = gv.Digraph(format='svg')
g2.node('A')
g2.node('B')
g2.node('C')
g2.node('D')
g2.edge('A', 'B')
g2.edge('A', 'C')
g2.edge('B', 'C')
g2.edge('B', 'D')
g2.render('graph//demo64')
