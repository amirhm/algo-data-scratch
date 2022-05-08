
def cansum(target, val):
    cache = {}
    def dfs(target):
        if target in cache: return cache[target]
        if target == 0 : return True
        if target < 0 : return False
        for i in val:
            if dfs(target - i):
                return True
        cache[target] = False
        return False
    return dfs(target)

print(cansum(7, [2,3]))
print(cansum(7, [5, 3, 4, 7]))
print(cansum(7, [2, 4]))
print(cansum(8, [2, 3, 5]))
print(cansum(300, [14, 7]))
