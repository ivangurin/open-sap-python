def reaction_path(speed):

    return speed / 10 * 3


def brake_distance(speed):

    return (speed / 10) ** 2


def stopping_distance(speed):

    return reaction_path(speed) + brake_distance(speed)


input_speed = int(input("Please enter a speed in km/h: "))

print(stopping_distance(input_speed))
