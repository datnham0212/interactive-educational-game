import math

def solve_equation(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return -1, None, None  # Infinite solutions
            else:
                return 0, None, None  # No solution
        else:
            return 1, -c / b, None  # Linear equation
    else:
        Delta = b ** 2 - 4 * a * c
        if Delta < 0:
            return 0, None, None  # No real solution
        elif Delta == 0:
            return 1, -b / (2 * a), None  # Repeated solution
        else:
            x1 = (-b + math.sqrt(Delta)) / (2 * a)
            x2 = (-b - math.sqrt(Delta)) / (2 * a)
            if x1 > x2:
                x1, x2 = x2, x1
            return 2, x1, x2  # Two distinct solutions

# User inputs
if __name__ == "__main__":
    # Read a single line from standard input
    line = input()
    a, b, c = map(float, line.split())

    sn, x1, x2 = solve_equation(a, b, c)

    if sn == -1:
        print("Phương trình vô số nghiệm.")
    elif sn == 0:
        print("Phương trình vô nghiệm.")
    elif sn == 1:
        print(f"Phương trình có 1 nghiệm: x = {x1}")
    elif sn == 2:
        print(f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
