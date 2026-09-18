class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars=sorted(zip(position,speed),reverse=True)
        fleets=0
        currfleetreach=0
        for i in cars:
            reachat=(target-i[0])/i[1]
            if reachat>currfleetreach:
                fleets+=1
                currfleetreach=reachat
        return fleets