def what_time_is_it(angle):
    if angle < 30:
        hour = (angle + 360) // 30
    else: 
        hour = angle // 30
    minute = int((angle % 30) // (1 / 2))
    time = "%02d:%02d" % (hour, minute)
    return time


def main():
    time = what_time_is_it(20)
    print(time)


if __name__ == "__main__":
    main()