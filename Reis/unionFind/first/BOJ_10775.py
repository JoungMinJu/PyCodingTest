import sys

g = int(sys.stdin.readline().rstrip())

p = int(sys.stdin.readline().rstrip())

count = 0

plane_list = []
for i in range(p):
    plane_list.append(int(sys.stdin.readline().rstrip()))

gate_parent = [i for i in range(g+1)]

def find(plane):
    if gate_parent[plane] == plane:
        return plane
    gate_parent[plane] = find(gate_parent[plane])
    return gate_parent[plane]

for plane in plane_list:
    temp = find(plane)
    if temp == 0:
        break
    gate_parent[temp] = gate_parent[temp-1]
    count += 1

print(count)