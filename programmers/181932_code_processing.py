def solution(code):
    mode = 0
    ret = []

    for idx in range(len(code)):
        if mode == 0:
            if code[idx] == "1":
                mode = 1
            else:
                if idx % 2 == 0:
                    ret.append(code[idx])
        else:
            if code[idx] == "1":
                mode = 0
            else:
                if idx % 2 != 0:
                    ret.append(code[idx])

    if not ret:
        return "EMPTY"

    return "".join(ret)


test_cases = [
    (("abc1abc1abc",), "acbac"),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
