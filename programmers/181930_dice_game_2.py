def solution(a, b, c):
    answer = 0
    return answer


test_cases = [
    ((2, 6, 1,), 9),
    ((5, 3, 3,), 473),
    ((4, 4, 4,), 110592),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
