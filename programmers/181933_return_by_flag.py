def solution(a, b, flag):
    return a + b if flag else a - b


test_cases = [
    ((-4, 7, True), 3),
    ((-4, 7, False), -11),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
