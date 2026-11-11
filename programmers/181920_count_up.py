def solution(start_num, end_num):
    answer = []
    return answer


test_cases = [
    ((3, 10,), [3, 4, 5, 6, 7, 8, 9, 10]),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
