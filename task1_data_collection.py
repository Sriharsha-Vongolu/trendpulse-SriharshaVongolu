import requests
import time
import json
import os
from datetime import datetime
 
BASE_URL = "https://hacker-news.firebaseio.com/v0"
HEADERS = {"User-Agent": "TrendPulse/1.0"}
 
CATEGORIES = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}
 
 
def get_category(title):
    title = title.lower()
    for category, keywords in CATEGORIES.items():
        if any(keyword in title for keyword in keywords):
            return category
    return None
 
 
def main():
    print("Fetching top story IDs...")
 
    session = requests.Session()
    session.headers.update(HEADERS)
 
    try:
        response = session.get(f"{BASE_URL}/topstories.json", timeout=10)
        response.raise_for_status()
        story_ids = response.json()[:500]
    except Exception as e:
        print("Error fetching IDs:", e)
        return
 
    # Step 1: Fetch ALL stories once
    print("Fetching story details...")
    all_stories = []
 
    for story_id in story_ids:
        try:
            story = session.get(
                f"{BASE_URL}/item/{story_id}.json",
                timeout=10
            ).json()
        except Exception:
            continue
 
        if not story or "title" not in story:
            continue
 
        category = get_category(story["title"])
        if not category:
            continue
 
        all_stories.append((category, story))
 
    # Step 2: Process per category (with sleep requirement)
    stories = []
 
    for category in CATEGORIES.keys():
        print(f"\nProcessing category: {category}")
        count = 0
 
        for cat, story in all_stories:
            if cat != category:
                continue
 
            data = {
                "post_id": story.get("id"),
                "title": story.get("title"),
                "category": category,
                "score": story.get("score", 0),
                "num_comments": story.get("descendants", 0),
                "author": story.get("by", "unknown"),
                "collected_at": datetime.now().isoformat()
            }
 
            stories.append(data)
            count += 1
 
            print(f"{category}: {count}/25")
 
            if count == 25:
                break
 
        # REQUIRED sleep
        time.sleep(2)
 
    # save output
    os.makedirs("data", exist_ok=True)
    filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"
 
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(stories, f, indent=2)
 
    print(f"\nCollected {len(stories)} stories. Saved to {filename}")
 
 
if __name__ == "__main__":
    main()