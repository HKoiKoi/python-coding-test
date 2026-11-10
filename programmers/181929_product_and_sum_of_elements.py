def solution(num_list):
    product = 1
    sqrt_sum = 0

    for num in num_list:
        product *= num
        sqrt_sum += num

    return 1 if product < sqrt_sum ** 2 else 0


test_cases = [
    (([3, 4, 5, 2, 1],), 1),
    (([5, 7, 8, 3],), 0),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
