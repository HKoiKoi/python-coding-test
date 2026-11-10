def solution(ineq, eq, n, m):
    if ineq == ">":
        if eq == "=":
            return int(n >= m)
        else:
            return int(n > m)
    else:
        if eq == "=":
            return int(n <= m)
        else:
            return int(n < m)


test_cases = [
    (("<", "=", 20, 50), 1),
    ((">", "!", 41, 78), 0),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
