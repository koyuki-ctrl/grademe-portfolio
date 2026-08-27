def rotate_right(values: list[int], steps: int) -> list[int]:
    if not values:
        return []
    steps = steps % len(values)
    return values[-steps:] + values[:-steps]
