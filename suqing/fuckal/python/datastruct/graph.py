# coding:utf8

class Graph:
    """
        无向图, 邻接矩阵
    """
    def __init__(self, vertices):

        # 顶点数
        self.V = vertices
        # use dict to store graph
        self.graph = {}
        
        # To store transitive closure
        # 存储节点可达性
        self.tc = [[0] * self.V for _ in range(self.V)]


    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]



"""
    有向图相关
"""
class Node(object):
    def __init__(self, name):
        self.name = name
    
    def get_name(obj):
        if isinstance(obj, Node):
            return obj.name
        elif isinstance(obj, str):
            return obj
        else:
            return ''

    def __eq__(self, obj):
        return self.name == self.get_name(obj) 

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __ne__(self, obj):
        return self.name != self.get_name(obj)

    def __lt__(self, obj):
        return self.name < self.get_name(obj)

    def __gt__(self, obj):
        return self.name > self.get_name(obj)
    def __ge__(self, obj):
        return self.name >= self.get_name(obj)

    def __bool__(self):
        return self.name

class DirectedEdge(object):
    def __init__(self, node_from, node_to):
        self.nf = node_from
        self.nt = node_to
    def __eq__(self, obj):
        if isinstance(obj, DirectedEdge):
            return obj.nf == self.nf and obj.nt == self.nt
        return False
    
    def __repr__(self):
        return '({0} -> {1})'.format(self.nf, self.nt)

class DirectedGraph(object):
    def __init__(self, load_dict = {}):
        self.nodes = []
        self.edges = []
        self.adjmt = {}
        
        if load_dict and type(load_dict) == dict:
            for v in load_dict:
                node_from = self.add_node(v)
                self.adjmt[node_from] = []
                for w in load_dict[v]:
                    node_to = self.add_node(w)
                    self.adjmt[node_from].append(node_to)
                    self.add_edge(v, w)

    def add_node(self, node_name):
        try:
            return self.nodes[self.nodes.index(node_name)]
        except ValueError:
            node = Node(node_name)
            self.nodes.append(node)
            return node


    def add_edge(self, node_name_from, node_name_to):
        try:
            node_from = self.nodes[self.nodes.index(node_name_from)]
            node_to = self.nodes[self.nodes.index(node_name_to)]
            self.edges.append(DirectedEdge(node_from, node_to))
        except ValueError:
            pass





