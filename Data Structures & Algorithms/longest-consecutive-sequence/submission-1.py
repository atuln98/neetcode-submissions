class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        out=0
        visited={}
        for i in nums:
            if i in visited:
                continue
            if i-1 in visited and i+1 in visited:
                visited[i]=visited[i-1]+1+visited[i+1]
                visited[i-visited[i-1]]=visited[i]
                visited[i+visited[i+1]]=visited[i]
            elif i-1 in visited:
                visited[i]=visited[i-1]+1
                visited[i-visited[i-1]]=visited[i]
            elif i+1 in visited:
                visited[i]=1+visited[i+1]
                visited[i+visited[i+1]]=visited[i]
            else:
                visited[i]=1
            if visited[i]>out:
                out=visited[i]
        return out

        