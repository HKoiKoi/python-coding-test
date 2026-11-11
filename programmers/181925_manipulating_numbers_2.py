def solution(numLog):
    answer = []
    control_dict = dict(zip([1, -1, 10, -10], ["w", "s", "d", "a"]))

    for i in range(1, len(numLog)):
        answer.append(control_dict[numLog[i] - numLog[i - 1]])

    return "".join(answer)


test_cases = [
    (([0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1],), "wsdawsdassw"),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
