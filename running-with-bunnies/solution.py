class AllPathIsFree(RuntimeError):
    pass


class Path:
    map = [[]]  # type: list[list[int]]
    step = []  # type: list[int]
    cost = 0

    def __init__(self, map, step, cost=0):
        self.map = map
        self.step = step[:]
        self.cost = cost

    def push(self, dst):
        if dst == self.step[-1]:
            return
        src = self.step[-1]
        self.step.append(dst)
        w = self.map[src][dst]
        self.cost += w
        return

    def pop(self):
        dst = self.step.pop()
        src = self.step[-1]
        self.cost -= self.map[src][dst]

    def valid_free_circle(self):
        if len(self.step) == 1:
            return
        if self.map[self.step[-1]][self.step[0]] + self.cost < 0:
            raise AllPathIsFree()
        return

    def __repr__(self):
        return " -> ".join([str(s) for s in self.step]) + " = " + str(self.cost)

    def __iadd__(self, other):
        if self.step[-1] != other.step[0]:
            raise RuntimeError("Unable to connect")
        self.step.extend(other.step[1:])
        self.cost += other.cost
        return self

    def __isub__(self, other):
        if self.step[-1] != other.step[-1]:
            raise RuntimeError("Unable to break")
        self.step = self.step[0:len(self.step) - len(other.step) + 1]
        self.cost -= other.cost
        return self


class Graph:
    map = [[]]

    shortest_path = [[]]

    path = None
    candidates = []
    remain_count = 0

    def __init__(self, map):
        self.map = map

        self.shortest_path = [[Path(map, [s, e], map[s][e]) for e in range(len(map))] for s in range(len(map))]

        self.candidates = [True] * len(map)
        self.remain_count = len(self.candidates)
        for s in range(len(map)):
            self.path = Path(map, [s], 0)
            self.candidates[s] = False
            self.remain_count -= 1
            self.walk_circle()
            self.candidates[s] = True

    def walk_circle(self):
        """

        :type path: Path
        """
        self.path.valid_free_circle()
        self.remain_count -= 1

        for c in range(len(self.candidates)):
            if not self.candidates[c]:
                continue
            self.path.push(c)
            self.candidates[c] = False

            if self.shortest_path[self.path.step[0]][c].cost > self.path.cost:
                self.shortest_path[self.path.step[0]][c] = Path(self.map, self.path.step, self.path.cost)

            ac = 0
            for i in range(1, len(self.path.step)):
                ac += self.map[self.path.step[i - 1]][self.path.step[i]]
                if self.shortest_path[self.path.step[i]][c].cost > self.path.cost - ac:
                    self.shortest_path[self.path.step[i]][c] = Path(self.map, self.path.step[i:], self.path.cost - ac)

            if self.remain_count > 0:
                self.walk_circle()
            else:
                self.path.valid_free_circle()

            self.path.pop()
            self.candidates[c] = True

        self.remain_count += 1

    def go(self, time_limit):
        pickup = []
        if self.shortest_path[self.path.step[-1]][len(self.map) - 1].cost <= time_limit:
            pickup = [i - 1 for i in range(1, len(self.map) - 1) if self.candidates[i] > 0]

        for i in range(1, len(self.candidates) - 1):
            if self.candidates[i] != 0:
                continue
            sp = self.shortest_path[self.path.step[-1]][i]

            self.path += sp

            for s in sp.step[1:]:
                if self.candidates[s] == 0:
                    self.remain_count -= 1
                    self.candidates[s] = 1
                else:
                    self.candidates[s] += 1

            p = self.go(time_limit - sp.cost)
            if len(p) > len(pickup) or (len(p) == len(pickup) and p < pickup):
                pickup = p
            self.path -= sp

            for s in sp.step[1:]:
                self.candidates[s] -= 1
                if self.candidates[s] == 0:
                    self.remain_count += 1
        return pickup

    def try_pickup(self, time_limit):
        self.path = Path(self.map, [0], 0)
        self.candidates = [0] * (len(self.map))
        self.candidates[0] = 1
        self.remain_count = len(self.map) - 1

        return self.go(time_limit)


def solution(times, time_limit):
    """

    :type times: list[list[int]]
    :type time_limit: int
    """

    try:
        g = Graph(times)
    except AllPathIsFree:
        return [s - 1 for s in range(1, len(times) - 1)]

    candidates = g.try_pickup(time_limit)

    return candidates
