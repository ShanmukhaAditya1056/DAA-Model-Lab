def climb_stairs(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    prev2 = 1  
    prev1 = 2  
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
        
    return prev1
steps = 5
print(f"Number of distinct ways to climb {steps} stairs: {climb_stairs(steps)}")