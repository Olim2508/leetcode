

def countingValleys(steps, path):
    is_valley = False
    altitude, valley_count = 0, 0
    for s in path:
        if s == "D":
            altitude -= 1
            if altitude < 0 and not is_valley:
                valley_count += 1
                is_valley = True
        else:
            altitude += 1
            if altitude == 0 and is_valley:
                is_valley = False
    return valley_count


test1 = countingValleys(8, "UDDDUDUU")
assert test1 == 1

