def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges = [badge_maker(name) for name in names]
    return badges


def assign_rooms(names):
    rooms = [f"Hello, {name}! You'll be assigned to room {names.index(name) +1}!" for name in names]
    return rooms

def printer(names):
    badges = batch_badge_creator(names)
    badges = [print(badge) for badge in badges]
    rooms = assign_rooms(names)
    rooms = [print(room) for room in rooms]
