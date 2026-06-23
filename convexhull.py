def find_side(p1, p2, p):
    val = (p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0])
    if val > 0:
        return 1 
    if val < 0:
        return -1 
    return 0      

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

points_list = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
print("Points on the Convex Hull:", convex_hull_brute_force(points_list))