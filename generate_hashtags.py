import requests
import re

URL = "https://my-ai-worker.anas-ai.workers.dev"

PROMPT = """
Generate exactly 2000 lines of recent/trending professional hashtags (1 or 2 per line) related to:
AI, Tech, DevOps, Cloud, Cybersecurity, Startups, Programming, Data Science, Morocco Tech, Hiring, Internships.

Format each line as:
#AI
#DevOps #Cloud
#CyberSecurity
Return ONLY the 2000 lines, no numbers, no explanations, no intro text.
"""

def main():
    print("Calling LLM for 2000 hashtag lines (1 call)...")
    response = requests.post(URL, json={"question": PROMPT})
    result = response.json()
    text = result.get("answer", "")
    
    lines = [line.strip() for line in text.split('\n') if line.strip() and '#' in line][:2000]
    
    if len(lines) < 2000:
        print(f"Padded to 2000 (got {len(lines)})")
        hashtags = re.findall(r"#\w+", ' '.join(lines))
        import random
        while len(lines) < 2000:
            if random.random() < 0.5 and hashtags:
                lines.append(random.choice(hashtags))
            elif len(hashtags) >= 2:
                lines.append(random.choice(hashtags) + ' ' + random.choice(hashtags))
    
    with open("data.txt", "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + '\n')
    
    print("Sample lines:", lines[:5])
    print(f"Generated: {len(lines)} lines")

main()
