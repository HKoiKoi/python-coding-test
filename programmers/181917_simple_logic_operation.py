def solution(x1, x2, x3, x4):
    answer = True
    return answer


test_cases = [
    ((False, True, True, True,), True),
    ((True, False, False, False,), False),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
