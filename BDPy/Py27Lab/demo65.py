# encoding=UTF-8
import graphviz as gv
import functools

graph = functools.partial(gv.Graph, format='svg')
digraph = functools.partial(gv.Digraph, format='svg')

g1 = graph()
g2 = digraph()


def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            graph.node(n[0], **n[1])
        else:
            graph.node(n)
    return graph


def add_edges(graph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            graph.edge(*e[0], **e[1])
        else:
            graph.edge(*e)
    return graph


from itertools import combinations, permutations

nodes = ['A', 'B', 'C', 'D']
# edges = [e for e in combinations(nodes, 2)]
edges = [e for e in permutations(nodes, 2)]
g1 = add_nodes(g1, nodes)
g1 = add_edges(g1, edges)
g1.render('graph//demo65_g1')
g2 = add_nodes(g2, nodes)
g2 = add_edges(g2, edges)
g2.render('graph//demo65_g2')

nodes2 = [('A', {'label': 'Lexus'}),
          ('B', {'label': 'Toyota'}),
          ('C', {'label': u'馬自達'}),
          ('D', {})]
edges = [(('A', 'B'), {'label': 'same holding company'}),
         (('A', 'C'), {'label': 'racing competitor'}),
         (('B', 'C'), {'label': u'大眾市場'}),
         (('B', 'D'), {})]
g3 = digraph()
g3 = add_edges(add_nodes(g3, nodes2), edges)
g3.render('graph//demo65_g3')
