def solution(intStrs, k, s, l):
    answer = []
    return answer


test_cases = [
    ((["0123456789", "9876543210", "9999999999999"], 50000, 5, 5,), [56789, 99999]),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
