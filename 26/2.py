f = open("26/26 (2).txt")
n = int(f.readline())
boxes = sorted([int(i) for i in f], reverse=True)
answer = [boxes[0]]
for box in boxes[1:]:
    if answer[-1] - box >= 3:
        answer.append(box)
print(len(answer), answer[-1])
