class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        def search(row, col, ocean):
            if (row, col) in ocean:
                return None
            ocean.add((row, col))
            for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= row + dr <= len(heights)-1 and 0 <= col + dc <= len(heights[0])-1:
                    if heights[row][col] <= heights[row+dr][col+dc]:
                        search(row + dr, col + dc, ocean)
        for i in range(0, len(heights[0])):
            search(0, i, pacific)
            search(len(heights)-1, i, atlantic)
        for j in range(0, len(heights)):
            search(j, 0, pacific)
            search(j, len(heights[0])-1, atlantic)
        result_list = []
        for result in pacific & atlantic:
            result_list.append(list(result))
        return result_list