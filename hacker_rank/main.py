

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


if __name__ == "__main__":
    assert pickingNumbers([4, 6, 5, 3, 3, 1]) == 3
    assert pickingNumbers([1, 2, 2, 3, 1, 2]) == 5
