# scrape_asu_news.py
import time, re, csv, requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone
from urllib.parse import urljoin

BASE = "https://news.asu.edu/"
HEADERS = {"User-Agent": "ASU-News-Monitor/1.0 (contact: youremail@example.com)"}
DELAY = 1.5
TIMEOUT = 15

def load_keywords():
    try:
        with open("keywords.txt", encoding="utf-8") as f:
            kws = [ln.strip() for ln in f if ln.strip()]
    except FileNotFoundError:
        kws = ["medicine","breakthrough","upcoming","clinical","trial","chemical","lab","precursor"]
    return [re.compile(rf"\b{re.escape(k)}\b", re.IGNORECASE) for k in kws]

def get_links():
    r = requests.get(BASE, headers=HEADERS, timeout=TIMEOUT)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    links = set()
    for a in soup.select("a[href]"):
        href = urljoin(BASE, a["href"])
        if href.startswith(BASE) and re.search(r"/\d{8}-", href):
            links.add(href.split("#")[0])
    return sorted(links)

def fetch_article(url):
    r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
    if r.status_code != 200:
        return None
    soup = BeautifulSoup(r.text, "html.parser")
    title_el = soup.find("h1")
    title = title_el.get_text(" ", strip=True) if title_el else ""
    body_el = soup.select_one("article") or soup.select_one(".field--name-body, .story, .content, main")
    body = body_el.get_text(" ", strip=True) if body_el else soup.get_text(" ", strip=True)
    return title, body

def ensure_csv():
    try:
        open("found_hits.csv", "x", encoding="utf-8").write(
            "timestamp_scraped_utc,keyword,url,title,snippet\n"
        )
    except FileExistsError:
        pass

def main():
    ensure_csv()
    try:
        with open("seen_urls.txt", encoding="utf-8") as f:
            seen = set(line.strip() for line in f)
    except FileNotFoundError:
        seen = set()

    kws = load_keywords()
    links = get_links()
    now = datetime.now(timezone.utc).isoformat()

    wrote = 0
    with open("found_hits.csv", "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        for url in links:
            if url in seen:
                continue
            time.sleep(DELAY)
            art = fetch_article(url)
            if not art:
                continue
            title, body = art
            text = f"{title}\n{body}"
            for rx in kws:
                m = rx.search(text)
                if m:
                    i = max(m.start()-70, 0); j = min(m.end()+70, len(text))
                    snippet = text[i:j].replace("\n", " ")
                    w.writerow([now, rx.pattern.replace("\\b","").strip("^$"), url, title, snippet])
                    wrote += 1
            seen.add(url)

    with open("seen_urls.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(sorted(seen)))

    print(f"Done. Logged {wrote} new hits.")

if __name__ == "__main__":
    main()
