def solution(record):
    db = {}

    chat = []

    for message in record:
        command = message.split()[0]
        uid = message.split()[1]

        if command == "Enter":
            name = message.split()[2]

            db[uid] = name

            chat.append(f"{uid} 님이 들어왔습니다.")

        elif command == "Leave":
            chat.append(f"{uid} 님이 나갔습니다.")

        elif command =="Change":
            name = message.split()[2]

            db[uid] = name

    answer = []

    for message in chat:
        uid = message.split()[0]
        message = message.replace(uid, db[uid])
        message = message.split()[0] + message.split()[1] + f" {message.split()[2]}"

        answer.append(message)

    return answer


print(solution(
    ["Enter uid1234 Muzi",
     "Enter uid4567 Prodo",
     "Leave uid1234",
     "Enter uid1234 Prodo",
     "Change uid4567 Ryan"]))
