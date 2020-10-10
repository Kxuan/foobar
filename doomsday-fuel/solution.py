from fractions import Fraction, gcd


def lcm(a, b):
    return a * b / gcd(a, b)


def lcms(*numbers):
    s = numbers[0]
    for i in range(1, len(numbers)):
        s = lcm(s, numbers[i])
    return s


class Graph:
    nodes = []

    def __init__(self, node_count):
        self.nodes = []
        for i in range(node_count):
            self.nodes.append(Node(self, i))

    def add_relation(self, si, di, possibility):
        s = self.nodes[si]
        d = self.nodes[di]
        Relation.link(s, d, possibility)

    def remove_intermediate(self, i):
        self.nodes[i].transfer_in()


class Relation:
    src = None  # type: Node
    dst = None  # type: Node
    possibility = Fraction(0)

    def __init__(self, src, dst, possibility):
        self.src = src
        self.dst = dst
        self.possibility = possibility

    @staticmethod
    def link(src, dst, possibility):
        if src.rel_out.has_key(dst.i):
            src.rel_in[dst.i].possibility += possibility
        else:
            r = Relation(src, dst, possibility)
            src.add_out(r)
            dst.add_in(r)

    def split_to(self, rel_out):
        """

        :type rel_out: dict<int,Relation>
        """
        rels = []
        for r in rel_out.values():
            rels.append(Relation(self.src, r.dst, self.possibility * r.possibility))

        self.src.del_out(self)
        self.dst.del_in(self)

        for r in rels:
            if r.src.rel_out.has_key(r.dst.i):
                r.src.rel_out[r.dst.i].possibility += r.possibility
            else:
                r.dst.add_in(r)
                r.src.add_out(r)

    def merge_with(self, b):
        if self.src != b.src or self.dst != b.dst:
            raise RuntimeError("Bug")
        self.possibility += b.possibility

        self.src.del_out(b)
        self.dst.del_in(b)

    def __str__(self):
        return '%s -> %s: %s' % (self.src, self.dst, self.possibility)


class Node:
    graph = None
    i = -1
    rel_out = {}
    rel_in = {}  # type: dict[int,Relation]

    def __init__(self, graph, i):
        self.graph = graph
        self.i = i
        self.rel_in = {}
        self.rel_out = {}

    def add_out(self, relation):
        if relation.src != self:
            raise RuntimeError()
        self.rel_out[relation.dst.i] = relation

    def del_out(self, relation):
        del self.rel_out[relation.dst.i]

    def add_in(self, relation):
        if relation.dst != self:
            raise RuntimeError()
        self.rel_in[relation.src.i] = relation

    def del_in(self, relation):
        del self.rel_in[relation.src.i]

    def break_circle(self):
        if not self.rel_in.has_key(self.i):
            return
        r = self.rel_in[self.i]

        self.del_out(r)
        self.del_in(r)

        if r.possibility == 1:
            return
        s = Fraction(1) / (1 - r.possibility)
        for child in self.rel_out.values():
            child.possibility *= s

    def transfer_in(self):
        self.break_circle()
        while len(self.rel_in) > 0:
            k = self.rel_in.keys()[0]
            self.rel_in[k].split_to(self.rel_out)

    def __str__(self):
        return str(self.i)


def solution(m):
    if len(m) == 0 or len(m[0]) == 0:
        return [0]

    node_count = len(m)
    graph = Graph(node_count)

    for si in range(node_count):
        denominator = sum(m[si])
        for di in range(node_count):
            if m[si][di] != 0:
                graph.add_relation(si, di, Fraction(m[si][di], denominator))

    terminal_states = []

    for n in graph.nodes:
        if len(n.rel_out) == 0:
            terminal_states.append(n)
        else:
            n.transfer_in()

    for n in graph.nodes:
        n.break_circle()

    reachable_denominator = [n.rel_in[0].possibility.denominator for n in terminal_states if n.rel_in.has_key(0)]
    if len(reachable_denominator) == 0:
        return [1, 1]
    denominator = lcms(*reachable_denominator)
    result = []
    for n in terminal_states:
        if n.rel_in.has_key(0):
            result.append((n.rel_in[0].possibility * denominator).numerator)
        else:
            result.append(0)
    result.append(denominator)
    return result
