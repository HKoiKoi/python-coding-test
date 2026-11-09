def solution(arr):
    return "".join(arr)


test_cases = [
    ((["a", "b", "c"],), "abc"),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
