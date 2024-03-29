def max_pairwise_product(numbers):
    n = len(numbers)

    first = -1
    second = -1

    for i in range(n):
        if first == -1 or numbers[i] >= numbers[first]:
            first = i

    for j in range(n):
        if (j != first) and (second == -1 or numbers[j] >= numbers[second]):
            second = j

    max_product = numbers[first] * numbers[second]
    return max_product


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
