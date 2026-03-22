DATABASE = []


def save_item(item):
    DATABASE.append(item)


''' def process_item(item):
    if not item:
        raise ValueError("Empty item 🤮")

    save_item(item)
    return "ok"  '''

def process_item(item):
    if DATABASE is None:
        raise Exception("Database crash")

    if "name" not in item:
        raise ValueError()

    DATABASE.append(item)
    return "ok"