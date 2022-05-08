
def cansum(target, val):
    result = []
    def dfs(target, ans):
        if target == 0 : 
            result.append(ans.copy())
        for i in val:
            if i <= target:
                ans.append(i)
                dfs(target - i, ans)
                ans.pop()
            else:
                return False
    dfs(target, [])
    return result

print(cansum(7, [2,3]))
print(cansum(7, [5, 3, 4, 7]))
print(cansum(7, [2, 4]))
print(cansum(8, [2, 3, 5]))
#print(cansum(300, [14, 7]))
