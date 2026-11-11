def solution(n, control):
    control_dict = dict(zip(["w", "s", "d", "a"], [1, -1, 10, -10]))

    return n + sum(control_dict[ch] for ch in control)


test_cases = [
    ((0, "wsdawsdassw",), -1),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
