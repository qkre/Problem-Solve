def check_answer(problem, user_input):

    output = open(f"../../input/{problem}_output.txt", "r").readlines()
    output = [line.strip() for line in output]

    print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

    for r, o in zip(user_input, output):
        if r != o:
            print(f"정답 : {o},     오답 : {r}")
