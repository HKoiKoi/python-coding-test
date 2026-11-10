def solution(a, d, included):
    answer = 0
    return answer


test_cases = [
    ((3, 4, [True, False, False, True, True],), 37),
    ((7, 1, [False, False, False, True, False, False, False],), 10),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
