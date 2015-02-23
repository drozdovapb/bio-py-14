#!/usr/bin/env python3

import itertools

class Graph:
    def __init__(self, vertices):
        self._vertices = vertices
        self.edges = []

    def add_edge(self, start, end):
        if (start, end) not in self.edges and start <= self._vertices and end <= self._vertices:
            self.edges.append((start, end))

    def has_edge(self, start, end):
        return (start, end) in self.edges or (end, start) in self.edges

    def remove_edge(self, start, end):
        if (start, end) in self.edges:
            self.edges.remove((start, end))
            return True
        if (end, start) in self.edges:
            self.edges.remove((end, start))
            return True
        return False

    def print_graph(self):
        for edge in self.edges:
            print(edge)

    def complete_graph(self):
        for item in itertools.product(range(self._vertices + 1), range(self._vertices + 1)):
            if item[0] != item[1] and not self.has_edge(item[0], item[1]):
                self.add_edge(item[0], item[1])
        return self

    def neighbours(self, vertex):
        neighbs = []
        for edge in self.edges:
            if edge[0] == vertex:
                neighbs.append(edge[1])
            elif edge[1] == vertex:
                neighbs.append(edge[0])
        return neighbs

    def has_path(self, start, end):
        visited = dict()
        visited[start] = 1
        for vertex in self.neighbours(start):
            if vertex == end:
                return True
            if vertex in visited.keys():
                self.has_path(vertex, end)
        return False


#An example

g = Graph(10)

g.add_edge(2, 8)
g.add_edge(8, 4)

print(g.has_edge(1, 2))
print(g.has_edge(2, 8))

print(g.has_edge(4, 8))

print('rem')
print(g.remove_edge(2, 8))
print(g.remove_edge(2, 3))


full = Graph(5).complete_graph()
full.print_graph()


gg = Graph(5)

gg.add_edge(4,6)
gg.print_graph()

print(gg.has_edge(1,2))

print('dlfj')
g.print_graph()

full.neighbours(3)

print(full.has_path(1,3))
print(g.has_path(1,3))