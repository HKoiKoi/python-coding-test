def solution(arr, queries):
    for i, j in queries:
        arr[i], arr[j] = arr[j], arr[i]

    return arr


test_cases = [
    (([0, 1, 2, 3, 4], [[0, 3], [1, 2], [1, 4]],), [3, 4, 1, 0, 2]),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
