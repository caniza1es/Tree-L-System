import sys
import math
import minescript

def lsystem(L, string, n):
    for i in range(n):
        string = "".join([L[a] for a in string])
    return string    

def placeblock(pos, block):
    x, y, z = [math.ceil(i) for i in pos]
    if block == "minecraft:oak_log":
        minescript.execute(f"setblock {x} {y} {z} {block}")
        return
    for dx in range(0, 2):  
        for dy in range(0, 2):  
            for dz in range(0, 2):  
                minescript.execute(f"setblock {x+dx} {y+dy} {z+dz} {block}")

def rotate_x(vec, angle):
    x, y, z = vec
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    y_new = y * cos_theta - z * sin_theta
    z_new = y * sin_theta + z * cos_theta
    return [x, y_new, z_new]

def rotate_z(vec, angle):
    x, y, z = vec
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    x_new = x * cos_theta - y * sin_theta
    y_new = x * sin_theta + y * cos_theta
    return [x_new, y_new, z]

def build(pos, rule, blocks):
    dirvector = [0, 1, 0]
    stack = []
    rot_angle = math.radians(45)
    for i in rule:
        if i == "A":
            pos = [a + b for a, b in zip(pos, dirvector)]
            placeblock(pos, blocks["A"])
            
        elif i == "B":    
            pos = [a + b for a, b in zip(pos, dirvector)]
            placeblock(pos, blocks["B"])
        elif i == "[":
            stack.append([pos, dirvector])
        elif i == "]":
            pos, dirvector = stack.pop()
        elif i == "+":
            dirvector = rotate_x(dirvector, rot_angle)
        elif i == "-":
            dirvector = rotate_x(dirvector, -rot_angle)
        elif i == "*":
            dirvector = rotate_z(dirvector, rot_angle)
        elif i == "/":
            dirvector = rotate_z(dirvector,-rot_angle)

def main():
    L = {
        "A": "AA",
        "B": "A[+B][-B][*B][/B]A[B]",
        "[": "[",
        "]": "]",
        "+":"+",
        "-":"-",
        "*":"*",
        "/":"/"
    }

    B = {
        "A": "minecraft:oak_log",
        "B": "minecraft:oak_leaves"
    }
    string, iter = sys.argv[1:]
    iter = int(iter)
    gen = lsystem(L, string, iter)
    position = minescript.player_get_targeted_block()[0]
    build(position, gen, B)

if __name__ == "__main__":
    main()
