import math

def giai_phuong_trinh_bac_2(a, b, c):
    return truong_hop_a_bang_0(b, c) if a == 0 else truong_hop_a_khac_0(a, b, c)

def truong_hop_a_bang_0(b, c):
    if b == 0:
        return "Phương trình có vô số nghiệm" if c == 0 else "Phương trình vô nghiệm"
    return f"Phương trình có một nghiệm: x = {-c / b}"

def truong_hop_a_khac_0(a, b, c):
    delta = b**2 - 4*a*c
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Phương trình có hai nghiệm phân biệt:\nx1 = {x1}\nx2 = {x2}"
    
    elif delta == 0:
        x = -b / (2*a)
        return f"Phương trình có nghiệm kép: x = {x}"
    
    return "Phương trình vô nghiệm"        

if __name__ == '__main__':
    a, b, c = map(float, input().split())
    print(f"({a})x² + ({b})x + ({c}) = 0", end='')
    print('\n') 

    print(giai_phuong_trinh_bac_2(a, b, c))
