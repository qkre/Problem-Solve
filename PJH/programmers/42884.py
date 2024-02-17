def solution(routes):
    answer = 0

    routes.sort(key= lambda x : x[1])
    cameras = []

    while routes:
        s, e = routes.pop(0)
        if not cameras:
            cameras.append(e)
            continue

        if s <= cameras[-1] <= e:
            continue

        cameras.append(e)

    answer = len(cameras)


    return answer