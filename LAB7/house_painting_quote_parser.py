def clean_colour_name(name):
    """Return a cleaned colour code, or None for invalid input."""
    if not isinstance(name, str):
        return None

    name = name.strip()
    if not name:
        return None

    return name.lower().replace(" ", "_")


def room_area(text):
    """Return room area, or None for invalid dimensions."""
    if not isinstance(text, str):
        return None

    parts = text.lower().split("x")
    if len(parts) != 2:
        return None

    try:
        length = int(parts[0])
        width = int(parts[1])
    except ValueError:
        return None

    if length <= 0 or width <= 0:
        return None

    return length * width


def total_wall_area(text):
    """Return the total area, or None if any entry is invalid."""
    if not isinstance(text, str) or not text.strip():
        return None

    try:
        areas = [int(area) for area in text.split(";")]
    except ValueError:
        return None

    if any(area < 0 for area in areas):
        return None

    return sum(areas)

def main():
    print("==== Running clean_colour_name ====")
    value = input("Enter a paint colour name (e.g. Ocean Blue): ")
    print("Colour code:", clean_colour_name(value))

    print("\n==== Running room_area ====")
    while True:
        value = input(
            "Enter room size as LENGTHxWIDTH in feet (e.g. 12x10): "
        )
        area = room_area(value)

        if area is None:
            print("Invalid size. Enter two positive whole numbers, e.g. 12x10.")
        else:
            print("Room area (sq ft):", area)
            break

    print("\n==== Running total_wall_area ====")
    value = input("Enter wall areas separated by ; (e.g. 120;95;110): ")
    print("Total wall area (sq ft):", total_wall_area(value))

if __name__ == "__main__":
    main()
