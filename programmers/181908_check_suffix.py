def solution(my_string, is_suffix):
    answer = 0
    return answer


test_cases = [
    (("banana", "ana",), 1),
    (("banana", "nan",), 0),
    (("banana", "wxyz",), 0),
    (("banana", "abanana",), 0),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
