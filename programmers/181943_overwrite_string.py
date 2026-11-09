def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]


if __name__ == "__main__":
    test_cases = [
        (("He11oWor1d", "lloWorl", 2), "HelloWorld"),
        (("Program29b8UYP", "merS123", 7), "ProgrammerS123"),
    ]

    for i, (args, expected) in enumerate(test_cases, 1):
        result = solution(*args)
        status = "정답" if result == expected else "오답"
        print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
