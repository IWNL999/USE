f1 = open('26/26_21424.txt').readlines()
f = [int(i) for i in f1]
f = sorted(f, reverse=True)
boxes = [f[0]]
neighbors = [i for i in f if i+9<=boxes[-1]]
while neighbors:
    boxes.append(neighbors[0])
    neighbors = [i for i in f if i+9<=boxes[-1]]
    
print(len(boxes), boxes[-1])