def solution(num_list):
    answer = 0
    return answer


test_cases = [
    (([3, 4, 5, 2, 1],), 393),
    (([5, 7, 8, 3],), 581),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
