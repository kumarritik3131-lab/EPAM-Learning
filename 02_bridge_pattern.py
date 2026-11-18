# Bridge pattern: two vertical pillars joined by a horizontal deck.
# Change height, width, and deck_row to experiment.

height = 7
width = 21
deck_row = 4
pillar_width = 3
left_gap = 4

right_start = width - pillar_width

for row in range(height):
    if row == deck_row:
        # The horizontal bridge deck
        print("=" * width)
    else:
        line = [" "] * width

        # Left and right pillars
        for col in range(pillar_width):
            line[col] = "|"
            line[right_start + col] = "|"

        # Small supports below the deck
        if row > deck_row:
            for col in range(pillar_width):
                line[left_gap + col] = "|"
                line[width - left_gap - pillar_width + col] = "|"

        print("".join(line))
