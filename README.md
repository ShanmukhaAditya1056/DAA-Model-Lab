# ==============================================================================
# PROGRAM 1: NUMBER OF DISTINCT WAYS TO CLIMB A STAIRCASE
# ==============================================================================
"""
AIM:
To find the total number of distinct ways to reach the n-th stair when you can climb 
either 1 or 2 steps at a time, utilizing an optimized iterative dynamic programming approach.

INPUT:
- An integer 'n' representing the number of stairs.
  Example: n = 5

EXPECTED OUTPUT:
- An integer representing the distinct number of ways to climb.
  Example: 8

RESULTS:
The algorithm successfully computes the number of distinct ways to climb the 
staircase. It optimizes memory performance by achieving an O(n) time complexity 
and O(1) auxiliary space complexity.
"""

def climb_stairs(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    prev2 = 1  # ways(1)
    prev1 = 2  # ways(2)
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
        
    return prev1


# ==============================================================================
# PROGRAM 2: BUBBLE SORT WITH EARLY STOPPING OPTIMIZATION
# ==============================================================================
"""
AIM:
To sort an array of elements in ascending order using the Bubble Sort algorithm, 
optimized with an early-stopping mechanism that halts execution if the array 
becomes fully sorted before completing all passes.

INPUT:
- An unsorted array of numbers.
  Example: [64, 34, 25, 12, 22, 11, 90]

EXPECTED OUTPUT:
- The sorted array along with the pass number where the algorithm stopped.

RESULTS:
The optimization successfully reduces the best-case time complexity to O(n) 
when the array is already sorted, preventing unnecessary passes while maintaining 
a worst-case time complexity of O(n^2).
"""

def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            print(f"[Bubble Sort] Early stopping triggered at pass: {i + 1}")
            break
    return arr


# ==============================================================================
# PROGRAM 3: CONVEX HULL (BRUTE-FORCE APPROACH)
# ==============================================================================
"""
AIM:
To find the convex hull (the smallest convex polygon enclosing all given points) 
from a set of 2D points using a brute-force geometric cross-product approach.

INPUT:
- A list of coordinate tuples (x, y) representing points on a 2D plane.
  Example: [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]

EXPECTED OUTPUT:
- A list of coordinate vertices that form the boundary perimeter of the convex hull.

RESULTS:
The brute-force algorithm successfully identifies all perimeter vertices defining 
the boundary hull. Because every pair of points is validated against all other points, 
the execution runs in O(n^3) time complexity.
"""

def find_side(p1, p2, p):
    val = (p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0])
    if val > 0:
        return 1  # Left side
    if val < 0:
        return -1 # Right side
    return 0      # Collinear

def convex_hull_brute_force(points):
    n = len(points)
    if n < 3:
        return points

    hull = set()
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            
            p1 = points[i]
            p2 = points[j]
            is_valid_edge = True
            initial_side = None
            
            for k in range(n):
                if k == i or k == j:
                    continue
                
                side = find_side(p1, p2, points[k])
                if side != 0:
                    if initial_side is None:
                        initial_side = side
                    elif side != initial_side:
                        is_valid_edge = False
                        break
            
            if is_valid_edge:
                hull.add(p1)
                hull.add(p2)

    return list(hull)


# ==============================================================================
# PROGRAM 4: JOB SCHEDULING FOR MAXIMUM PROFIT (GREEDY STRATEGY)
# ==============================================================================
"""
AIM:
To select and schedule a subset of jobs maximizing total profit, ensuring each 
job finishes before its deadline and no two jobs share the same time slot.

INPUT:
- A collection of jobs where each object contains an ID, a deadline, and profit.
  Example Dataset: 
    Job('J1', deadline=4, profit=20)
    Job('J2', deadline=1, profit=10)
    Job('J3', deadline=1, profit=40)
    Job('J4', deadline=1, profit=30)

EXPECTED OUTPUT:
- A sequence of scheduled Job IDs that yields maximum profit and total profit earned.

RESULTS:
By greedily picking jobs with the highest profit values first, the algorithm 
calculates the ideal maximum yield schedule within an O(n log n) sorting bottleneck 
plus O(n * max_deadline) scheduling phase.
"""

class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def schedule_jobs(jobs, max_deadline):
    jobs.sort(key=lambda x: x.profit, reverse=True)
    
    slots = [False] * (max_deadline + 1)
    scheduled_jobs = [None] * (max_deadline + 1)
    total_profit = 0

    for job in jobs:
        for j in range(min(max_deadline, job.deadline), 0, -1):
            if not slots[j]:
                slots[j] = True
                scheduled_jobs[j] = job.job_id
                total_profit += job.profit
                break

    final_schedule = [job for job in scheduled_jobs if job is not None]
    return final_schedule, total_profit


# ==============================================================================
# CENTRAL EXECUTION DRIVER
# ==============================================================================
if __name__ == "__main__":
    print("--- 1. Climb Stairs ---")
    steps = 5
    print(f"Input Steps: {steps}")
    print(f"Output Distinct Ways: {climb_stairs(steps)}\n")

    print("--- 2. Optimized Bubble Sort ---")
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    print(f"Input List: {unsorted_list}")
    print(f"Output Sorted Array: {bubble_sort_optimized(unsorted_list)}\n")

    print("--- 3. Convex Hull (Brute Force) ---")
    points_list = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
    print(f"Input Points: {points_list}")
    print(f"Output Convex Hull Points: {convex_hull_brute_force(points_list)}\n")

    print("--- 4. Job Scheduling (Greedy) ---")
    job_data = [
        Job('J1', 4, 20),
        Job('J2', 1, 10),
        Job('J3', 1, 40),
        Job('J4', 1, 30)
    ]
    print("Input Jobs: J1(4,20), J2(1,10), J3(1,40), J4(1,30)")
    schedule, max_profit = schedule_jobs(job_data, 4)
    print(f"Output Scheduled Sequence: {schedule}")
    print(f"Output Maximum Profit: {max_profit}")
