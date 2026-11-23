"""One-line laugh entry: write a single funny sentence to /output/entry.txt."""

import os

LINE = "My plant only started thriving the day I stopped watering it, which says a lot about both of us."

OUTPUT_PATH = "/output/entry.txt"


def check_not_blank(line: str) -> str | None:
    if not line:
        return "line is blank"
    return None


def check_length(line: str) -> str | None:
    if not 1 <= len(line) <= 200:
        return f"line must be 1-200 characters, got {len(line)}"
    return None


def check_single_sentence(line: str) -> str | None:
    if line.count(".") != 1 or not line.endswith("."):
        return "line must be a single sentence ending with one period"
    return None


def validate(line: str) -> str | None:
    for check in (check_not_blank, check_length, check_single_sentence):
        error = check(line)
        if error is not None:
            return error
    return None


def prepare_output_dir() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)


def write_line(line: str) -> None:
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, OUTPUT_PATH)


def main() -> int:
    line = LINE.strip()
    error = validate(line)
    if error is not None:
        print(f"error: {error}")
        return 1
    prepare_output_dir()
    write_line(line)
    print(f"wrote {len(line)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
