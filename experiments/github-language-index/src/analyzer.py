from collections import Counter
import os
import matplotlib.pyplot as plt
from .config import OUTPUT_DIR


def analyze_languages(repositories):
    languages = [
        repo["language"]
        for repo in repositories
        if repo.get("language")
    ]

    counter = Counter(languages)
    total = sum(counter.values())

    ranking = [
        {
            "language": lang,
            "count": count,
            "percentage": round((count / total) * 100, 2),
        }
        for lang, count in counter.most_common()
    ]

    return ranking


def save_markdown(ranking):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "language_index.md")

    with open(path, "w", encoding="utf-8") as f:
        f.write("# GitHub Language Usage Index\n\n")
        f.write("| Rank | Language | Count | Percentage |\n")
        f.write("|------|----------|-------|------------|\n")

        for i, item in enumerate(ranking, 1):
            f.write(
                f"| {i} | {item['language']} | {item['count']} | {item['percentage']}% |\n"
            )

    print(f"Markdown saved to {path}")


def generate_chart(ranking):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    top = ranking[:10]
    languages = [x["language"] for x in top]
    values = [x["count"] for x in top]

    plt.figure(figsize=(10, 6))
    plt.bar(languages, values)
    plt.xticks(rotation=45, ha="right")
    plt.title("Top Programming Languages on GitHub")
    plt.tight_layout()

    path = os.path.join(OUTPUT_DIR, "language_chart.png")
    plt.savefig(path)
    plt.close()

    print(f"Chart saved to {path}")