def solution(arr, queries):
    for s, e, k in queries:
        for i in range(s, e + 1):
            if not i % k:
                arr[i] += 1

    return arr


test_cases = [
    (([0, 1, 2, 4, 3], [[0, 4, 1], [0, 3, 2], [0, 3, 3]],), [3, 2, 4, 6, 4]),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
