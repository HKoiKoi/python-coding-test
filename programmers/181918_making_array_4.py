def solution(arr):
    stk = []
    i = 0

    while i < len(arr):
        if stk and stk[-1] >= arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])
            i += 1

    return stk


test_cases = [
    (([1, 4, 2, 5, 3],), [1, 2, 3]),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
