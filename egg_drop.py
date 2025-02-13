"""We have k eggs and an n-story building. The goal is to
find the highest floor(f) from which you can drop an egg
without breaking it.
.If an egg breaks, you must test lower floors.
. If an egg does not break, you must test higher floors.
. You want to minimize the worst-case number of drops.
Here i will write brute force version to find f value.
which is the value of highest floor from wher egg will not break

"""
def egg_drop_iterative(n,k): # n - floors, k- eggs
    # create dp table here dp[i][j] represents the mini
    # attempts needed for i floors and j eggs.
    dp = [[0]*(k+1)for _ in range(n+1)]
    # ------Base Case-For eggs--------
    # If there's only 1 egg, we have to do linear search
    # (Drop from every floor.)
    for i in range(1,n+1):
        # If there is 1 egg then check every floor.
        # Here i = floor, 1 = 1-egg
        dp[i][1] = i 
    #------Base Case-- For-Floors------
    # If there's 1 or 0 floor, we need at most i drops.
    for j in range(1, k+1):
        dp[1][j] = 1 # If there's 1 floor, only 1 drop is needed.
        dp[0][j] = 0 # If there are 0 floors, 0 drops are needed.
    # Solve for floors(i) and eggs(j)
    for i in range(2,n+1): # Iterate over floors.
        for j in range(2,k+1): # Iterate over eggs
            dp[i][j] = float('inf') # start with a large number
            for x in range(1,i+1): # Try dropping from each floor x
                worst_case = 1 + max(dp[x-1][j-1], dp[i-x][j])
                dp[i][j] = min(dp[i][j],worst_case)
    return dp[n][k]

print(egg_drop_iterative(10,5)) # here 10-floors, 2 -eggs