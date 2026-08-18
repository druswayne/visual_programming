"""Export all task conditions by topic into a markdown file."""

from data.registry import TOPICS, TASKS_BY_TOPIC, plain_text


def main() -> None:
    lines = ["# Условия задач по всем темам", ""]
    for topic in TOPICS:
        tid = topic["id"]
        tasks = TASKS_BY_TOPIC.get(tid, [])
        lines.append(f"## {topic['title']}")
        lines.append("")
        if topic.get("description"):
            lines.append(topic["description"])
            lines.append("")
        lines.append(f"Всего задач: {len(tasks)}")
        lines.append("")
        for i, t in enumerate(tasks, 1):
            title = plain_text(t.get("title", ""))
            cond = plain_text(t.get("condition", ""))
            lines.append(f"### {i}. {title}")
            lines.append("")
            lines.append(f"**ID:** `{t.get('id', '')}`")
            lines.append("")
            lines.append("**Условие:**")
            lines.append("")
            lines.append(cond)
            lines.append("")
            hint = t.get("hint")
            if hint:
                lines.append("**Подсказка:**")
                lines.append("")
                lines.append(plain_text(hint))
                lines.append("")
        lines.append("---")
        lines.append("")

    out = "tasks_conditions.md"
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")
    print(f"Wrote {out}")
    print(f"Topics: {len(TOPICS)}")
    for topic in TOPICS:
        print(f"  {topic['id']}: {len(TASKS_BY_TOPIC.get(topic['id'], []))} tasks")


if __name__ == "__main__":
    main()
