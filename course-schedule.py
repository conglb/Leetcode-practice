class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = []
        for _ in range(numCourses):
            adj.append([])
        # number of courses that is prerequisite of course i
        pre = [0] * numCourses
        for prerequisite in prerequisites:
            adj[prerequisite[0]].append(prerequisite[1])
            pre[prerequisite[1]] += 1
            # adj[prerequisite[1]].append(prerequisite[0])
        mark = [False] * numCourses

        topo = []

        def DFS(u: int):
            mark[u] = True
            for v in adj[u]:
                if mark[v] == False:
                    DFS(v)
            topo.append(u)

        # DFS all tree
        for course in range(numCourses):
            if mark[course] == False:
                DFS(course)

        # position in topo
        pos = [0] * numCourses
        for i in range(numCourses):
            pos[topo[i]] = i

        # check prerequisite
        for prerequisite in prerequisites:
            if pos[prerequisite[0]] < pos[prerequisite[1]]:
                return False
        return True