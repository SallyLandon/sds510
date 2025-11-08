#1.  Imports

import csv, os, time #python libraries
from datetime import datetime, timezone #UTC timestamp

from selenium import webdriver #controls the Chrome browser
from selenium.webdriver.common.by import By #locating elements
from selenium.webdriver.chrome.options import Options #Chrome configurations/headless

#2.  CSV setup

CSV_PATH = "HNhits2.csv"

if not os.path.exists(CSV_PATH):  #creates csv with header 
    with open(CSV_PATH, "w", newline="", encoding="utf-8-sig") as f: #utf-8-sig helps excel read utf-8
        csv.writer(f).writerow(["timestamp_utc", "keyword", "post_text"])

#3.  Browser setup/Selenium

opts = Options()
opts.add_argument("--headless=new") #run chrome, but don't show it, added new for debugging
driver = webdriver.Chrome(options=opts) #run Chrome browser run by Selenium w/ above options

KEYWORD = "windows" #tried science, health and fitness looking for more hits, lots of variation of post topics
start_url = "https://news.ycombinator.com/news" #tried other sites, not any better

try:
    print("Opening page...", flush=True) #added these during bebugging to see progress
    titles = [] #titles stored here
    current = start_url #start on first page

#4. Loop through pages of HN, collect titles
    for _ in range(10):  # number of pages (10 pages = 300 posts)
        driver.get(current)
        time.sleep(1.5)
        els = driver.find_elements(By.CSS_SELECTOR, "span.titleline > a") #

        for e in els:
            txt = (e.text or "").strip()
            href = e.get_attribute("href") or ""
            if txt: # only keep non-empty titles
                titles.append((txt, href))

        #5.  Move to the next page using the "more" link at bottom
        more = driver.find_elements(By.CSS_SELECTOR, "a.morelink")
        if more:
            current = more[0].get_attribute("href")
        else:
            break
    
    print(f"Found {len(titles)} titles. Filtering...", flush=True)
  
            #6.  Save to matching posts to CSV
                    # Save only unique titles that match the keyword
    saved = 0
    seen = set() # 
    with open(CSV_PATH, "a", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        for text, url in titles:
            if not text or text in seen: # Skip empty or duplicate titles
                continue
            seen.add(text)
            if KEYWORD.lower() in text.lower(): #simple keyword match 
                w.writerow([datetime.now(timezone.utc).isoformat(), KEYWORD, text, url])
                saved += 1

    print(f"✅ Done. Found {len(seen)} uniqueposts, saved {saved} matches.", flush=True)

finally:
    driver.quit() #close browser when done
    print("Done")
