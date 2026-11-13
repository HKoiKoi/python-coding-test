def solution(my_string, index_list):
    answer = ''
    return answer


test_cases = [
    (("cvsgiorszzzmrpaqpe", [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7],), "programmers"),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
