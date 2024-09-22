import math

def giaibac2(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return (-1, None, None)
            else:
                return (0, None, None)
        else:
            return (1, -c / b, None)
    else:
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
        if b == 0 and c != 0:
            return (0, None, None, None, None)
        else:
            return giaibac2(a, b, c)
    
    else:
        delta = b * b - 4 * a * c
        if delta < 0:
            return (0, None, None, None, None)
        elif delta == 0:
            t1 = -b / (2 * a)
            return (1, t1, None, None, None)
        else:
            sqrt_delta = math.sqrt(delta)
            t1 = (-b - sqrt_delta) / (2 * a)
            t2 = (-b + sqrt_delta) / (2 * a)

            solutions = set() #Tránh trường hợp lặp nghiệm
            if t1 >= 0:
                solutions.add(math.sqrt(t1))
                solutions.add(-math.sqrt(t1))
            if t2 >= 0:
                solutions.add(math.sqrt(t2))
                solutions.add(-math.sqrt(t2))
            
            solutions = sorted(solutions) # Tránh -0
    return (len(solutions), *solutions) + (None,) * (4 - len(solutions))

if __name__ == "__main__":
    a, b, c = list(map(float, input().split()))
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
