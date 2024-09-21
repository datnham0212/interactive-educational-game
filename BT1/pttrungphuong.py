import math

def giai_phuong_trinh_trung_phuong(a, b, c):
    return giai_phuong_trinh_bac_nhat(b, c) if a == 0 else tinh_delta(a, b, c)

def giai_phuong_trinh_bac_nhat(b, c):
    if b == 0:
        return "Phương trình vô số nghiệm" if c == 0 else "Phương trình vô nghiệm"
    else:
        return f"Phương trình có nghiệm x = {-c/b:.2f}"

def tinh_delta(a, b, c):
    delta = b**2 - 4*a*c    
    if delta < 0:
        return "Phương trình vô nghiệm"
    elif delta == 0:
        return khi_delta_bang_0(a, b)
    else:
        return khi_delta_lon_hon_0(a, b, delta)

def khi_delta_bang_0(a, b):
    x = -b / (2*a)
    if x < 0:
        return "Phương trình vô nghiệm"
    else:
        nghiem = {round(math.sqrt(x), 2), round(-math.sqrt(x), 2)}
        nghiem = {0 if x == 0 else x for x in nghiem} 
        if len(nghiem) == 0:
            return "Phương trình vô nghiệm"
        else:
            return f"Phương trình có {len(nghiem)} nghiệm: " + ", ".join(f"x{i+1} = {x:.2f}" for i, x in enumerate(sorted(nghiem)))

def khi_delta_lon_hon_0(a, b, delta):
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    nghiem = set()
    if x1 >= 0:
        nghiem.add(round(math.sqrt(x1), 2))
        nghiem.add(round(-math.sqrt(x1), 2))
    if x2 >= 0:
        nghiem.add(round(math.sqrt(x2), 2))
        nghiem.add(round(-math.sqrt(x2), 2))
    
    nghiem = {0 if x == 0 else x for x in nghiem} 

    if len(nghiem) == 0:
        return "Phương trình vô nghiệm"
    else:
        return f"Phương trình có {len(nghiem)} nghiệm: " + ", ".join(f"x{i+1} = {x:.2f}" for i, x in enumerate(sorted(nghiem)))

if __name__ == '__main__':
    a, b, c = map(float, input().split())
    print(f"({a})x⁴ + ({b})x² + ({c}) = 0", end='')
    print('\n') 

    print(giai_phuong_trinh_trung_phuong(a, b, c))
