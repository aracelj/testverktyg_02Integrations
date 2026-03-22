DATABASE = []


def save_item(item):
    DATABASE.append(item)


def process_item(item):
    # some “logic”
    if not item:
        raise ValueError("Empty item 🤮")

    save_item(item)
    return "ok"