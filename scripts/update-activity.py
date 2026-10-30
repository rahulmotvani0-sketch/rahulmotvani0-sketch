#!/usr/bin/env python3
import json
import re
import urllib.request
from datetime import datetime, timezone

USERNAME = "rahulmotvani0-sketch"
API_URL = f"https://api.github.com/users/{USERNAME}/events/public"
README_PATH = "README.md"
START_MARKER = "<!-- RECENT_ACTIVITY_START -->"
END_MARKER = "<!-- RECENT_ACTIVITY_END -->"

ICONS = {
    "PushEvent": "🚀 Pushed code to",
    "CreateEvent": "📦 Created repository/branch in",
    "WatchEvent": "⭐ Starred",
    "PullRequestEvent": "🔀 Pull Request in",
    "IssuesEvent": "🐛 Issue in",
    "ForkEvent": "🍴 Forked",
    "ReleaseEvent": "🏷️ Published release in"
}

def fetch_events():
    req = urllib.request.Request(API_URL, headers={"User-Agent": "GitHub-Profile-Sync"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())

def format_activity_table(events):
    lines = [
        "| Activity | Target Repository | Date |",
        "| :--- | :--- | :--- |"
    ]
    seen = set()
    count = 0
    for e in events:
        etype = e.get("type", "")
        repo_name = e.get("repo", {}).get("name", "")
        created = e.get("created_at", "")[:10]
        action = ICONS.get(etype, f"📌 {etype} on")
        
        # Deduplicate same action on same repo on same date
        key = (etype, repo_name, created)
        if key in seen:
            continue
        seen.add(key)
        
        lines.append(f"| {action} | [`{repo_name}`](https://github.com/{repo_name}) | `{created}` |")
        count += 1
        if count >= 6:
            break

    if count == 0:
        lines.append("| 🚀 Active development | [`portfolio`](https://github.com/rahulmotvani0-sketch/portfolio) | `Recently` |")

    return "\n".join(lines)

def update_readme():
    try:
        events = fetch_events()
        table = format_activity_table(events)
    except Exception as err:
        print(f"Error fetching events: {err}")
        return

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    replacement = f"{START_MARKER}\n\n{table}\n\n*Updated automatically via GitHub Actions • Last synced: {now_utc}*\n\n{END_MARKER}"

    pattern = re.compile(f"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}", re.DOTALL)
    if pattern.search(content):
        new_content = pattern.sub(replacement, content)
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Successfully updated README.md with recent activity.")
    else:
        print("Markers not found in README.md.")

if __name__ == "__main__":
    update_readme()
