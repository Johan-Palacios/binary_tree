def to_list(nodes: list):
    items = []
    for node in nodes:
        try:
            if int(node) not in items:
                items.append(int(node))
        except Exception:
            continue
    return items
