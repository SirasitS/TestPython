def find_roots(a, b, c):
    results = ()
    root_1 = (-b + (((b**2)-(4*a*c))**0.5))/(2*a)
    root_2 = (-b - (((b**2)-(4*a*c))**0.5))/(2*a)
    results = (root_1, root_2)
    return results

print(find_roots(2, 10, 8));