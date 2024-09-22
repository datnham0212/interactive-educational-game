import math

def giaibac2(a, b, c):
    if a == 0:
        if b == 0:
            return (-1, None, None) if c == 0 else (0, None, None)
        x1 = -c / b
        return (1, x1, None)
    
    delta = b * b - 4 * a * c
    if delta < 0:
        return (0, None, None)
    elif delta == 0:
        x1 = -b / (2 * a)
        return (1, x1, None)
    else:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        return (2, min(x1, x2), max(x1, x2)) 

def giaipttrungphuong(a, b, c):
    if a == 0:
        return (0, None, None, None, None) if b == 0 and c != 0 else giaibac2(a, b, c)
    
    delta = b * b - 4 * a * c
    if delta < 0:
        return (0, None, None, None, None)
    elif delta == 0:
        t1 = -b / (2 * a)
        return (1, t1, None, None, None)
    
    #delta > 0
    sqrt_delta = math.sqrt(delta)
    t1 = (-b - sqrt_delta) / (2 * a)
    t2 = (-b + sqrt_delta) / (2 * a)
    
    solutions = set()  # Prevent duplicate 0
    if t1 >= 0:
        solutions.add(math.sqrt(t1))
        solutions.add(-math.sqrt(t1))
    if t2 >= 0:
        solutions.add(math.sqrt(t2))
        solutions.add(-math.sqrt(t2))
    
    #Prevent -0
    solutions = sorted(solutions)
    
    return (len(solutions), *solutions) + (None,) * (4 - len(solutions))


# Example usage
if __name__ == "__main__":
    s = list(map(float, input().split()))
    a, b, c = s
    sn, *roots = giaipttrungphuong(a, b, c)
    
    if sn == -1:
        print("Phương trình vô số nghiệm")
    elif sn == 0:
        print("Phương trình vô nghiệm")
    elif sn == 1:
        print(f"Phương trình có 1 nghiệm: {roots[0]}")
    elif sn == 2:
        print(f"Phương trình có 2 nghiệm: {roots[0]} và {roots[1]}")
    elif sn == 3:
        print(f"Phương trình có 3 nghiệm: {roots[0]}, {roots[1]} và {roots[2]}")
    elif sn == 4:
        print(f"Phương trình có 4 nghiệm: {roots[0]}, {roots[1]}, {roots[2]} và {roots[3]}")
