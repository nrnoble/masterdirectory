A = [10, 5]
B = [10, 90]

def slope(a, b):
    if (a[0] == b[0]):
        return 0

    return (b[1] - a[1]) / (b[0] - a[0])


def intercept(point, slope):
    if (slope == 0):
        # vertical line
        return point[0]
    return point[1] - slope * point[0]

m = slope(A, B)
b = intercept(A, m)

# var coordinates = [];
# for (var x = A[0]; x <= B[0]; x++) {
#     var y = m * x + b;
#     coordinates.push([x, y]);
# }

coordinates = []
x = A[0]
while x <= B[0]:
    y = m * x + b
    coordinates.append([x, y])
    print ("x=" + str(x) + ", y=" + str(y))
    x = x + 1

# for x in A[0]:
#     x = x + 1
#     if x >= B[0]:
#         break
#     y = m * x + b
#     coordinates.append([x, y])