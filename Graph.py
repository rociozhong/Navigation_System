from itertools import islice
import heapq

class Node(object):
    def __init__(self, name):
        self.__name = name
        self.__property = None

    def set_property(self, prop):
        self.__property = prop

    def get_name(self):
        return self.__name

    def __eq__(self, other):
        return isinstance(other, Node) and self.get_name() == other.get_name()

    def __hash__(self):
        return hash(self.__name)

    def __str__(self):
        return self.__name

    __repr__ = __str__


class Edge(object):
    def __init__(self, start, end, dist, name, direction, type_of_rd):
        self.__start = start
        self.__end = end
        self.__length = dist
        self.__name = name
        self.__direction = direction
        self.__allaccessible = True if type_of_rd == "ADA" else False

    def get_name(self):
        return self.__name

    def get_length(self, disabled = False):
        if not disabled:
            return self.__length
        return self.__length if self.__allaccessible else float("inf")

    def get_direction(self):
        return self.__direction

    def __str__(self):
        return self.__start + "-->" + self.__end + ", dist: " + str(self.__length)

    __repr__ = __str__


class Graph(object):
    def __init__(self, csv):
        self.__graph = {}
        self.__v = {}
        self.__e = {}
        with open(csv) as f:
            for line in islice(f, 1, None):
                start, end, distance, name, direction, type_of_rd = line.strip().split(',')
                distance = float(distance)
                self.__e[start + " --> " + end] = Edge(start, end, distance, name, direction, type_of_rd)
                if start not in self.__graph:
                    self.__graph[start] = {}
                self.__graph[start][end] = start + " --> " + end
                if start not in self.__v:
                    self.__v[start] = Node(start)
                if end not in self.__v:
                    self.__v[end] = Node(end)

    def print_nodes(self):
        for attraction in sorted(self.__v.keys()):
            print(attraction)

    def shortest_path(self, start, end, disabled=False):
        if start not in self.__v or end not in self.__v:
            raise ValueError("Not a valid attraction!")
        pq = []
        expanded = set()
        heapq.heappush(pq, (0, (None, start)))
        res = float("inf")
        prev_map = {}
        while pq:
            dist, (prev, curr) = heapq.heappop(pq)
            prev_map[curr] = prev
            expanded.add(curr)
            if curr == end:
                res = dist
                break
            for neighbor, edge_key in self.__graph[curr].items():
                if neighbor not in expanded:
                    heapq.heappush(pq, (dist + self.__e[edge_key].get_length(disabled), (curr, neighbor)))
        if res < float("inf"):
            path = [end]
            while prev_map.get(end):
                path.append(prev_map[end])
                end = prev_map[end]
            return res, path[::-1]
        return res, []

    def parse_path(self, path, disabled=False):
        if len(path) == 0:
            print("No accessible path!")
            return
        if len(path) < 2:
            raise ValueError("Less than two attractions input!")
        for attraction in path:
            if attraction not in self.__v:
                raise ValueError("Attraction {} doesn't exist".format(attraction))
        for i in range(len(path) - 1):
            edge = self.__e[path[i] + " --> " + path[i + 1]]
            print(", ".join([path[i] + " --> " + path[i + 1], edge.get_name(), edge.get_direction(),
                             str(edge.get_length(disabled))]))

    def __str__(self):
        res = []
        for node, neighbors in self.__graph.items():
            tmp = []
            for end, edge_key in neighbors.items():
                tmp.append("[" + end + ", dist: " + str(self.__e[edge_key].get_length()) + "]")
            res.append(node + ": " + ", ".join(tmp))
        return '\n'.join(res)


