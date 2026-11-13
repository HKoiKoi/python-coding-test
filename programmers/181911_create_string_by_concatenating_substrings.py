def solution(my_strings, parts):
    answer = ''
    return answer


test_cases = [
    ((["progressive", "hamburger", "hammer", "ahocorasick"], [[0, 4], [1, 2], [3, 5], [7, 7]],), "programmers"),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
