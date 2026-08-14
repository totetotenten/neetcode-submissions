class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        i = 1
        d = {}
        for course in prerequisites:
            before, after = course
            d.setdefault(after, []).append(before)
        if not d:
            return True

        def search(out_seen, in_seen, course):
            if course in in_seen:
                return False
            if course in out_seen:
                return True
            in_seen.add(course)
            out_seen.add(course)

            if course not in d:
                in_seen.remove(course)
                return True
            a = True
            for before in d[course]:
                if not search(out_seen, in_seen, before):
                    a = False
            in_seen.remove(course)
            return a
        
        out_seen = set()
        b = True
        for i in range(0, numCourses):
            in_seen = set()
            if not search(out_seen, in_seen, i):
                b = False
            
        return b
        