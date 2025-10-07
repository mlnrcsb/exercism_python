def transpose(text):
    # empty input -> empty output
    if text == "":
        return ""

    rows = text.split('\n')
    width = max(len(row) for row in rows)

    result_lines = []
    for col in range(width):
        # find last row that has a real character at this column
        last_contrib = -1
        for r_idx in range(len(rows) - 1, -1, -1):
            if col < len(rows[r_idx]):
                last_contrib = r_idx
                break

        # Build the transposed line only up to last_contrib (inclusive)
        if last_contrib == -1:
            # shouldn't happen because width is based on max length,
            # but keep safe fallback
            result_lines.append("")
            continue

        pieces = []
        for r_idx in range(last_contrib + 1):
            if col < len(rows[r_idx]):
                pieces.append(rows[r_idx][col])
            else:
                pieces.append(' ')   # pad with space for shorter rows above last_contrib

        result_lines.append(''.join(pieces))

    return '\n'.join(result_lines)