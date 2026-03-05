from github_client import fetch_repositories
from analyzer import analyze_languages, save_markdown, generate_chart


def main():
    print("Fetching repositories...")
    repos = fetch_repositories()

    print("Analyzing languages...")
    ranking = analyze_languages(repos)

    print("Saving results...")
    save_markdown(ranking)
    generate_chart(ranking)

    print("Done.")


if __name__ == "__main__":
    main()