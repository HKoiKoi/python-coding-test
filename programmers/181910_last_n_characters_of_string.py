def solution(my_string, n):
    answer = ''
    return answer


test_cases = [
    (("ProgrammerS123", 11,), "grammerS123"),
    (("He110W0r1d", 5,), "W0r1d"),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
