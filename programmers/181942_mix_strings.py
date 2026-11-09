def solution(str1, str2):
    answer = []

    for i in range(len(str1)):
        answer.append(str1[i])
        answer.append(str2[i])

    return "".join(answer)


test_cases = [
    (("aaaaa", "bbbbb"), "ababababab"),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
