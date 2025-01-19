def badge_maker(name):
    return (f"Hello, my name is {name}.")

def batch_badge_creator(names):
    return [(f"Hello, my name is {name}.") for name in names]

def assign_rooms(names):
    return [(f"Hello, {name}! You'll be assigned to room {names.index(name) + 1}!") for name in names]

def printer(names):
    badge_messages = batch_badge_creator(names)
    room_messages = assign_rooms(names)

    for message in badge_messages:
        print(message)
    for message in room_messages:
        print(message)

