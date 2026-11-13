def solution(n):
    answer = [n]

    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

        answer.append(n)

    return answer


test_cases = [
    ((10,), [10, 5, 16, 8, 4, 2, 1]),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
