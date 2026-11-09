def solution(a, b):
    return max(int(f"{a}{b}"), 2 * a * b)


test_cases = [
    ((2, 91), 364),
    ((91, 2), 912),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
