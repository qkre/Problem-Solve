def check_answer(problem, user_input):
    output = open(f"../input/{problem}o.txt", "r").readlines()
    output = [line.strip() for line in output]

    print("--------------- 오답 -----------------")

    for u, o in zip(user_input, output):
        if u != o:
            print(f"내 풀이 : {u}, 정답 : {o}")