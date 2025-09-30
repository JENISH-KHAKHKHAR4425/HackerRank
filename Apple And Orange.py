import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_positions = [a + d for d in apples]
    orange_positions = [b + d for d in oranges]

    apple_count = sum(1 for pos in apple_positions if s <= pos <= t)
    orange_count = sum(1 for pos in orange_positions if s <= pos <= t)

    # Print results
    print(apple_count)
    print(orange_count)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
