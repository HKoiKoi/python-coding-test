def solution(num_list):
    if num_list[-1] > num_list[-2]:
        num_list.append(num_list[-1] - num_list[-2])
    else:
        num_list.append(num_list[-1] * 2)

    return num_list


test_cases = [
    (([2, 1, 6],), [2, 1, 6, 5]),
    (([5, 2, 1, 7, 5],), [5, 2, 1, 7, 5, 10]),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
