

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


assert countingValleys(8, "UDDDUDUU") == 1


def bonAppetit(bill, k, b):
    diff = (sum(bill) - bill[k]) / 2
    if diff != b:
        return int(b - diff)
    return "Bon Appetit"


assert bonAppetit([3, 10, 2, 9], 1, 12) == 5


def findDigits(n):
    counter = 0
    for i in str(n):
        if int(i) != 0 and n % int(i) == 0:
            counter += 1
    return counter


assert findDigits(1012) == 3


def pickingNumbers(a):
    # Create a dictionary to count the occurrences of each number in the array
    num_counts = {}
    for num in a:
        num_counts[num] = num_counts.get(num, 0) + 1

    max_length = 0

    # Iterate through the unique numbers in the array
    for num in num_counts:
        # Check the length of subarray considering the current number and the next one
        max_length = max(max_length, num_counts[num] + num_counts.get(num + 1, 0))

    return max_length


def taumBday(b, w, bc, wc, z):
    initial_p = b * bc + w * wc
    changed_p = float("inf")
    if bc > wc:
        for i in range(1, b + 1):
            p = (b - i) * bc + (w + i) * wc + z * i
            if p < initial_p:
                changed_p = p
    elif bc < wc:
        for i in range(1, w + 1):
            p = (b + i) * bc + (w - i) * wc + z * i
            if p < initial_p:
                changed_p = p
    else:
        return initial_p

    return changed_p if changed_p < initial_p else initial_p


if __name__ == "__main__":
    res = taumBday(b=3, w=6, bc=9, wc=1, z=1)
    print(res)
    assert res == 12
    # assert taumBday(b=3, w=5, bc=3, wc=4, z=1) == 29

