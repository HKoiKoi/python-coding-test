def solution(my_string, k):
    return my_string * k


test_cases = [
    (("string", 3), "stringstringstring"),
    (("love", 10), "lovelovelovelovelovelovelovelovelovelove"),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
