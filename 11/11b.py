connections = {
    (d := line.split(":"))[0].strip(): [t.strip() for t in d[1].strip().split(" ")]
    for line in open("input.txt", mode="r")
}


def trace(cache, curr, end):
    targets = connections.get(curr)
    count = 0
    if curr == end:
        return 1
    if targets is None:
        return 0
    for target in targets:
        sub_target_count = cache.get(target)
        if sub_target_count is None:
            sub_target_count = trace(cache, target, end)
        count += sub_target_count
    cache[curr] = count
    return count


svr_fft_count = trace(dict(), "svr", "fft")
fft_dac_count = trace(dict(), "fft", "dac")
dac_out_count = trace(dict(), "dac", "out")
print(svr_fft_count * fft_dac_count * dac_out_count)
