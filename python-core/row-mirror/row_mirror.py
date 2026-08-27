def mirror_rows(grid: list[list[int]]) -> list[list[int]]:
    return [liste[::-1] for liste in grid]