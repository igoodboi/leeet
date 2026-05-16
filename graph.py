"""
PROBLEM: Given a directed graph, create its adjacency matrix in order to output one of the following:
2. Find the maximum number of edges starting at any specific vertex. If there is a tie,
choose the vertex that is first numerically. Print the sum of all edges that start at that
3. Find and print the total number of paths of length 2 in the entire graph.
vertex.

The graph below is represented by 6 edges which are 12, 13, 23, 31, 34, and 41. The answer to each
characteristic stated above is:
1. 1 - There are 0 cycles of length 1 since there is no edge that starts and ends with the same vertex.
There is one cycle of length 2 which exists because 13 and 31 are both edges. The sum is 1.
2. 25 - Vertices 1 and 3 each have a maximum of 2 edges starting there. Therefore, use starting
vertex 1 since it is first numerically. The sum of all of the edges that start at vertex 1 is 12 + 13 =
25.
3. 10 - By inspection, the paths of length 2 are 123, 131, 134, 231, 234, 313, 312, 341, 412, and 413.
The total is 10.

INPUT: There will be 5 lines of input. Each line will contain a number from 1-3 to indicate which of the
above 3 characteristics to print followed by a list of 2-character strings giving all of the directed edges in
the graph. For example, the string “31” says there is a directed edge from vertex 3 to vertex 1. Graphs
will have no more than 9 vertices.
OUTPUT: Print the result of the specified characteristic (1-3) for the corresponding graph that was input.
SAMPLE INPUT:
2 12 13 23 31 34 41
1 12 23 34 11 21 32 45 53 95 43 99 29 91
3 12 23 34 41 31 52 45 61 14 21 33 55 13 54 32 56 36
1 12 11 33 34 43 55 52 41 31 25 88 79 98 45 13 42 87 35 51 21 14 78
2 12 11 33 34 43 55 52 41 31 25 88 79 98 45 13 42 87 35 51 21 14 78
SAMPLE OUTPUT:
1. 25
2. 5
3. 49
4. 10
5. 50

2020-2021 ● Contest 4: Graphs ● Junior Division

TEST INPUT:
1 12 31 41 42 43 45 51 63 64 56 16
2 12 13 22 23 24 34 42 98 71 87 17 96 67
3 12 14 21 24 25 32 41 43 59 65 91 87 76 95
2 11 12 14 15 23 25 31 43 45 51 52 68 79 87 89
3 55 77 45 54

TEST OUTPUT:
1. 0
2. 42
3. 24
4. 52
5. 6
"""


class Solution:
    def numCycle(self, graph: list[list]):
        # 1. Find and print the sum of the number of cycles of length 1
        # and cycles of length 2.
        c1 = 0
        for i in range(len(graph)):
            c1 = c1 + graph[i][i]
        c2 = 0
        for i in range(len(graph)):
            for j in range(len(graph)):
                if i != j:
                    c2 = c2 + graph[i][j] * graph[j][i]
        return c1 + c2 // 2

    def maxEdgeSum(self, graph: map):
        # "2. Find the maximum number of edges starting at any specific vertex. If there is a tie,
        # choose the vertex that is first numerically. Print the sum of all edges that start at that
        # vertex."
        container = []
        print(graph)
        for ki in graph:
            lenth = len(graph[ki])
            container.append(lenth)

        bigglenth = max(container)
        kiiys = []
        for ki in graph:
            lenth = len(graph[ki])
            if lenth == bigglenth:
                kiiys.append(ki)

        eez = 0
        theCHOSENONE = min(kiiys)
        for v in graph[theCHOSENONE]:
            e = str(theCHOSENONE) + str(v)
            eez = eez + int(e)
        return eez

    def numPath2(self, graph):
        # "3. Find and print the total number of paths of length 2 in the entire graph."
        # "vertex."
        c2 = 0
        for i in range(len(graph)):
            for j in range(len(graph)):
                for k in range(len(graph)):
                    # if i != k and k != j:
                    c2 = c2 + graph[i][k] * graph[k][j]
        return c2

    def proccess(self, lst) -> map:
        # m = {1:[2,3], 2:[3], 3:[1,4], 4:[1]}
        con = {}
        for i in lst:
            if i[0] in con:
                val = con[i[0]]
                val.append(i[1])
            else:
                con[i[0]] = [i[1]]
        return con

    def matrix(self, mp: map) -> list[list]:
        # convert adjacency map to adjacency matrix
        ll = []
        keys = list(mp.keys())
        mat = []
        for i, l in enumerate(keys):
            r = [0 for _ in range(len(keys))]
            for j, k in enumerate(keys):
                if k in mp[l]:
                    r[j] = 1
            mat.append(r)
        return mat

    def grapher(self, lst):
        # 1 parse the inputs into an adjacency matrix
        alst = self.proccess(lst[1:])
        print(alst)
        graph = self.matrix(alst)
        for row in graph:
            print(row)
        # 2,3 make all the "activities" or funct for the 1, 2, 3,funnel them into the specified funct or activities
        # 4 return the specified characteristic of the corresponding graph
        if lst[0] == "1":
            print("prob 1")
            return self.numCycle(graph)
        if lst[0] == "2":
            print("prob 2")
            return self.maxEdgeSum(alst)
        if lst[0] == "3":
            print("prob 3")
            return self.numPath2(graph)
        print("we choose none cuz lst is", lst[0])


if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(1501)
    sol = Solution()
    tests = [["2", "12", "13", "23", "31", "34", "41"],
             ["1", "12", "23", "34", "11", "21", "32", "45", "53", "95", "43", "99", "29", "91"],
             ["3", "12", "23", "34", "41", "31", "52", "45", "61", "14", "21", "33", "55", "13", "54", "32", "56", "36"],
             ["1", "12", "11", "33", "34", "43", "55", "52", "41", "31", "25", "88", "79", "98", "45", "13", "42", "87", "35", "51", "21", "14", "78"],
             ["2", "12", "11", "33", "34", "43", "55", "52", "41", "31", "25", "88", "79", "98", "45", "13", "42", "87", "35", "51", "21", "14", "78"]]
    outputs = [25,
               5,
               49,
               10,
               50]
    for i in range(len(tests)):
        lst = tests[i]
        answer = sol.grapher(lst)
        if answer == outputs[i]:
            print("👍👏👍👏👍👏👍👏👍👏👍👏👍👏Yippeee")
            print(answer)
            print(outputs[i])
        elif answer != outputs[i]:
            print("BOOOOOOOOOOOOO >:( 🤮😱🤮😱🤮😱🤮😱🤮😱🤮😱")
            print(answer)
            print(outputs[i])
