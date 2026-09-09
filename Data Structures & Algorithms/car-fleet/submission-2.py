class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pos_speed = []
        for i in range(n):
            pos_speed.append([position[i], speed[i]])
        pos_speed = sorted(pos_speed, key = lambda x:x[0], reverse = True)

        result = 0
        prev = 0
        for i in range(n):
            need = target - pos_speed[i][0]
            time = need / pos_speed[i][1]
            if prev < time:
                prev = time
                result += 1
        return result



        
            
        