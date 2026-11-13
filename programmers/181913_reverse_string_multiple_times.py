def solution(my_string, queries):
    answer = ''
    return answer


test_cases = [
    (("rermgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]],), "programmers"),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
