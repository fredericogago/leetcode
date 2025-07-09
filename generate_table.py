import re
from pathlib import Path

LEETCODE_DIR = Path("src/leetcode/editor/en")
JOURNAL_FILE = Path("leetcode-journal.md")
TOTAL_PROBLEMS = 3611

TABLE_HEADER = """| ID  | Title             | Solution Link                                            | Patterns         |
|-----|--------------------|-----------------------------------------------------------|------------------|"""
TABLE_MARKER = "<!-- SOLUTIONS_TABLE -->"

BADGE_REGEX = r"!\[LeetCode Progress\]\(https://img\.shields\.io/badge/LeetCode-[\d]+%2F[\d]+%20Problems-blue\)"

def extract_id_and_title(filename: str) -> tuple[int, str]:
    match = re.match(r"\[(\d+)\](.+)\.py$", filename)
    if match:
        return int(match.group(1)), match.group(2).replace("_", " ").strip()
    raise ValueError(f"Invalid filename format: {filename}")

def extract_tags(file_path: Path) -> str:
    try:
        content = file_path.read_text(encoding="utf-8")
        match = re.search(r"Tags:\s*(.+)", content)
        if match:
            return match.group(1).strip()
    except Exception:
        pass
    return ""

def generate_table(files: list[Path]) -> str:
    rows = []
    for file in sorted(files):
        try:
            id_, title = extract_id_and_title(file.name)
            solution_link = f"[View Solution]({file.as_posix()})"
            patterns = extract_tags(file)
            rows.append(f"| {id_:<3} | {title:<18} | {solution_link:<59} | {patterns:<16} |")
        except ValueError:
            continue
    return "\n".join([TABLE_HEADER] + rows)

def update_journal():
    if not JOURNAL_FILE.exists():
        print("❌ journal file not found.")
        return

    content = JOURNAL_FILE.read_text()
    parts = content.split(TABLE_MARKER)
    if len(parts) != 3:
        print("❌ Missing table markers. Insert <!-- SOLUTIONS_TABLE -->.")
        return

    # Get all files
    solution_files = list(LEETCODE_DIR.glob("[[]*[]]*.py"))
    solved_count = len(solution_files)

    # Update progress badge
    badge_line = f"![LeetCode Progress](https://img.shields.io/badge/LeetCode-{solved_count}%2F{TOTAL_PROBLEMS}%20Problems-blue)"
    content = re.sub(BADGE_REGEX, badge_line, content)

    # Update table
    table = generate_table(solution_files)
    new_content = content.split(TABLE_MARKER)
    new_full_content = new_content[0] + TABLE_MARKER + "\n\n" + table + "\n\n" + TABLE_MARKER + new_content[2]

    JOURNAL_FILE.write_text(new_full_content)
    print(f"✅ Updated journal with {solved_count} problems solved.")

if __name__ == "__main__":
    update_journal()
