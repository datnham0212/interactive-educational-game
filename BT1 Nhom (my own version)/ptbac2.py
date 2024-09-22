import math
def pt_bac2(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return -1, None, None # Vô số nghiệm
            else:
                return 0, None, None # Vô nghiệm
        else:
            return 1, -c / b, None # 1 nghiệm

    else:
        Delta = b ** 2 - 4 * a * c
        if Delta < 0:
            return 0, None, None # Vô nghiệm
        elif Delta == 0:
            return 1, -b / (2 * a), None # 1 nghiệm
        else:
            x1 = (-b + math.sqrt(Delta)) / (2 * a)
            x2 = (-b - math.sqrt(Delta)) / (2 * a)
            if x1 > x2:
                x1, x2 = x2, x1
            return 2, x1, x2  # 2 nghiệm

if __name__ == "__main__":
    line = input()
    a, b, c = map(float, line.split())

    sn, x1, x2 = pt_bac2(a, b, c)

    if sn == -1:
        print("Phương trình vô số nghiệm.")
    elif sn == 0:
        print("Phương trình vô nghiệm.")
    elif sn == 1:
        print(f"Phương trình có 1 nghiệm: x = {x1}")
    elif sn == 2:
        print(f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
