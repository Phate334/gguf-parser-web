def human_readable_size(size_in_bytes: int) -> str:
    # Convert file size to a human-readable format
    for unit in ["B", "KB", "MB", "GB", "TB", "PB"]:
        if size_in_bytes < 1024:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024
    return f"{size_in_bytes:.2f} EB"


def abbreviate_number(number: int) -> str:
    # Convert large numbers to abbreviated format
    for unit, threshold in [("B", 1e9), ("M", 1e6), ("K", 1e3)]:
        if number >= threshold:
            return f"{number/threshold:.2f} {unit}"
    return str(number)
