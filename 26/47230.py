i = 0
k = 1
with open("26-47230.txt") as f:
    boxes = list(map(int, f.readlines()))
    n = boxes[0]
    boxes = boxes[1:]
    boxes.sort(reverse=True)
    while i < len(boxes) - 1:
        if boxes[i] - boxes[i + 1] >= 3:
            k += 1
            i += 1
        else:
            boxes.remove(boxes[i + 1])
    print(k)
    print(boxes[len(boxes) - 1])
