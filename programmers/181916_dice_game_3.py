def solution(a, b, c, d):
    answer = 0
    return answer


test_cases = [
    ((2, 2, 2, 2,), 2222),
    ((4, 1, 4, 4,), 1681),
    ((6, 3, 3, 6,), 27),
    ((2, 5, 2, 6,), 30),
    ((6, 4, 2, 5,), 2),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
