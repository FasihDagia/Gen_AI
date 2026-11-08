import re
from pathlib import Path

env_vars = set()

patterns = [
    r'os\.getenv\(["\'](.*?)["\']',
    r'os\.environ\.get\(["\'](.*?)["\']',
    r'os\.environ\[["\'](.*?)["\']\]',
]

for file in Path(".").rglob("*.py"):
    if ".venv" in str(file):
        continue

    content = file.read_text(encoding="utf-8", errors="ignore")

    for pattern in patterns:
        matches = re.findall(pattern, content)
        env_vars.update(matches)

print("\nEnvironment variables required/referenced:")
for var in sorted(env_vars):
    print(f"{var}=")