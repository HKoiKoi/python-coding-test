def solution(number, n, m):
    return int(number % n == 0 and number % m == 0)


test_cases = [
    ((60, 2, 3), 1),
    ((55, 10, 5), 0),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
