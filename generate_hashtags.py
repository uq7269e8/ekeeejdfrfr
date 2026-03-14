import requests
import re
import random

URL = "https://my-ai-worker.anas-ai.workers.dev"

PROMPT = """
Give a list of recent and trending professional hashtags in 2026 related to:
AI, Tech, DevOps, Cloud, Cybersecurity, Startups, Programming,
Data Science, Morocco Tech, Hiring, Internships.

Return ONLY hashtags separated by spaces.
Example:
#AI #MachineLearning #DevOps
"""

def fetch_hashtags():

    response = requests.post(URL, json={"question": PROMPT})
    result = response.json()

    text = result.get("answer", "")

    hashtags = re.findall(r"#\w+", text)

    return list(set(hashtags))


def build_lines(tags, n=2000):

    lines = []

    for _ in range(n):

        if random.random() < 0.5:
            lines.append(random.choice(tags))
        else:
            lines.append(
                random.choice(tags) + " " + random.choice(tags)
            )

    return lines


def main():

    tags = []

    while len(tags) < 200:
        tags += fetch_hashtags()
        tags = list(set(tags))

    lines = build_lines(tags, 2000)

    with open("data.txt", "w", encoding="utf-8") as f:
        for l in lines:
            f.write(l + "\n")

    print("Generated:", len(lines))


main()

