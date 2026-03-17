import requests
import re
import random

URL = "https://my-ai-worker.anas-ai.workers.dev"

PROMPT = """
Generate exactly 2000 lines of professional hashtags for job search and tech hiring.

Topics:
AI jobs, tech jobs, programming, DevOps, cloud, cybersecurity, startups,
internships, hiring, recruitment, Morocco jobs, remote jobs.

Rules:
- Exactly 2000 lines
- Each line must contain 1 or 2 hashtags
- Each hashtag must start with #
- No explanations, no numbering

Example:
#OpenToWork
#TechJobs
#DevOpsJobs #CloudJobs
#MoroccoJobs

Return ONLY the lines.
"""

TOTAL_TARGET = 10000
BATCH_SIZE = 2000


def get_hashtags():
    response = requests.post(URL, json={"question": PROMPT}, timeout=60)
    result = response.json()
    text = result.get("answer", "")

    lines = [
        line.strip()
        for line in text.split("\n")
        if line.strip() and "#" in line
    ]

    return lines[:BATCH_SIZE]


def main():
    all_lines = []

    batches = TOTAL_TARGET // BATCH_SIZE

    for i in range(batches):
        print(f"Request {i+1}/{batches}")

        try:
            lines = get_hashtags()
            all_lines.extend(lines)
            print("Received:", len(lines))
        except Exception as e:
            print("Error:", e)

    if len(all_lines) < TOTAL_TARGET:
        hashtags = list(set(re.findall(r"#\w+", " ".join(all_lines))))

        while len(all_lines) < TOTAL_TARGET:
            if random.random() < 0.5:
                all_lines.append(random.choice(hashtags))
            else:
                all_lines.append(
                    random.choice(hashtags) + " " + random.choice(hashtags)
                )

    with open("data.txt", "w", encoding="utf-8") as f:
        for line in all_lines[:TOTAL_TARGET]:
            f.write(line + "\n")

    print("Total generated:", len(all_lines[:TOTAL_TARGET]))


if __name__ == "__main__":
    main()
