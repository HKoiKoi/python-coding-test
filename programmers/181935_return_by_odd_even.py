def solution(n):
    if n % 2 == 0:
        return sum(n ** 2 for n in range(1, n + 1) if n % 2 == 0)
    else:
        return sum(n for n in range(1, n + 1) if n % 2 != 0)


test_cases = [
    ((7,), 16),
    ((10,), 220),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
