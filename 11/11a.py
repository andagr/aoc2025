connections = {
    (d := line.split(":"))[0].strip(): [t.strip() for t in d[1].strip().split(" ")]
    for line in open("input.txt", mode="r")
}

paths = 0
def trace(device, targets):
    global paths
    print(device, targets)
    if device == "out":
        paths += 1
        return
    for offset in range(0, len(targets)):
        trace(targets[offset], connections.get(targets[offset], []))
        

trace("you", connections["you"])
print(paths)