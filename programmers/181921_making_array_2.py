def solution(l, r):
    answer = []
    return answer


test_cases = [
    ((5, 555,), [5, 50, 55, 500, 505, 550, 555]),
    ((10, 20,), [-1]),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
