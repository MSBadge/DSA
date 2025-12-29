# Basic
print("Basic star box")
n = 5
for i in range(n):
    for j in range(n):
        print("*", end=' ')
    print()





# Increasing Trinange pattern
print("Increasing Trinange pattern")
n = 5
for i in range(n):
    for j in range(i+1):
        print("*", end=' ')
    print()





# Decreasing Trinange pattern
print("Decreasing Trinange pattern")
n = 5
for i in range(n):
    for j in range(i,n):
        print("*", end=' ')
    print()





# Right sided Triangle
print("Right sided Triangle")
n = 5
for i in range(n):
    for j in range(i,n):
        print(" ", end=' ')
    for k in range(i+1):
        print("*", end=" ")
    print()





# Left sided Triangle
print("Left sided Triangle")
n = 5
for i in range(n):
    for j in range(i+1):
        print(" ", end=' ')
    for k in range(i,n):
        print("*", end=" ")
    print()





# Hill sided Triangle
print("Hill sided Triangle")
n = 5
for i in range(n):
    for j in range(i,n):
        print(" ", end=' ')
    for k in range(i):
        print("*", end=" ")
    for _ in range(i+1):
        print("*", end=" ")
    print()





# Reverse Hill sided Triangle
print("Reverse Hill sided Triangle")
n = 5
for i in range(n):
    for j in range(i+1):
        print(" ", end=' ')
    for k in range(i,n-1):
        print("*", end=" ")
    for _ in range(i,n):
        print("*", end=" ")
    print()





# Diamond Pattern
print("Diamond Pattern")
n = 5
for i in range(n-1):
    for _ in range(i,n):
        print(" ", end=" ")
    for _ in range(i):
        print("*", end=" ")
    for _ in range(i+1):
        print("*", end=" ")
    print()
for j in range(n):
    for _ in range(j+1):
        print(" ", end=" ")
    for _ in range(j,n-1):
        print("*", end=" ")
    for _ in range(j,n):
        print("*", end=" ")
    print()