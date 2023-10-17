

def countingValleys(steps, path):
    altitude, valley_count = 0, 0
    for s in path:
        if s == "D":
            altitude -= 1
        else:
            altitude += 1
            if altitude == 0:
                valley_count += 1
    return valley_count


test1 = countingValleys(8, "UDDDUDUU")
assert test1 == 1


def bonAppetit(bill, k, b):
    diff = (sum(bill) - bill[k]) / 2
    if diff != b:
        return int(b - diff)
    return "Bon Appetit"


test2 = bonAppetit([3, 10, 2, 9], 1, 12)
print("test2", test2)
assert test2 == 5

