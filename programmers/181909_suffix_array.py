def solution(my_string):
    answer = []
    return answer


test_cases = [
    (("banana",), ["a", "ana", "anana", "banana", "na", "nana"]),
    (("programmers",),
     ["ammers", "ers", "grammers", "mers", "mmers", "ogrammers", "programmers", "rammers", "rogrammers", "rs", "s"]),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
