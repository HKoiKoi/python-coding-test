def solution(arr, queries):
    answer = []

    for s, e, k in queries:
        min_value = arr[s]

        for i in range(s + 1, e + 1):
            if arr[i] <= k:
                continue

            if min_value <= k:
                min_value = arr[i]

            min_value = min(arr[i], min_value)

        if min_value <= k:
            answer.append(-1)
        else:
            answer.append(min_value)

    return answer


test_cases = [
    (([0, 1, 2, 4, 3], [[0, 4, 2], [0, 3, 2], [0, 2, 2]],), [3, 4, -1]),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
