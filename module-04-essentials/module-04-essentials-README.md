ChatGPT wrote my summary under my guidance, with some additions and corrections (by me):
Overview 
This assignment builds a Python script that:
1.	Opens a website
2.	Searches for posts containing a chosen keyword
3.	Uses Selenium to interact with a webpage
4.	Follows pagination to load additional posts
5.	Extracts post content
6.	Saves results in a CSV
7.	Behaves politely (small delays, limited requests, headless browser)
I originally attempted Mastodon, but after extensive testing I switched to Hacker News, which provided reliable keyword results and met the technical requirements of the assignment.
________________________________________
✅ Tools Used
1. Visual Studio Code
Used to write and run the Python script. VS Code’s Python extension, autocomplete, and debugger made the workflow easier (sometimes).
2. Selenium WebDriver (Python)
Installed Selenium and automated Chrome in headless mode.
VS Code + Python handled ChromeDriver automatically on this machine.
________________________________________
✅ What the Script Does (Hacker News Version)
Although the script file is named mastodon_keyword_scrape.py, it currently scrapes Hacker News due to Mastodon’s structural limitations.
The script:
1.	Opens the Hacker News “news” page
2.	Follows the “more” link several times to gather multiple pages
3.	Extracts every headline using the CSS selector:
4.	span.titleline > a
5.	Stores all headline text in a list
6.	Removes duplicates (HN pages overlap slightly)
7.	Performs a case-insensitive keyword search
8.	Writes matching posts to HNhits.csv with:
o	UTC timestamp
o	Keyword used
o	Headline text
o	URL
________________________________________
✅ Why the Scraper Is Polite
•	Uses a headless browser
•	Includes small sleep delays
•	Limits to ~10 pages
•	Extracts only text already visible in the DOM
•	Avoids rapid or repetitive requests
________________________________________
✅ Why I Used CSS Selectors Instead of Other Selenium Methods
CSS selectors worked best for this scraper because they are:
•	More flexible and precise than class-name selectors
•	Able to match nested relationships, like span.titleline > a
•	Stable across Hacker News pages (HN’s HTML is simple and consistent)
•	Directly applied to the live, fully rendered DOM
•	Easier to test in DevTools before coding
Since Hacker News uses clean static HTML, CSS selectors provided reliable extraction without requiring additional parsing tools like BeautifulSoup.
________________________________________
✅ Use of Assistance
I used class examples, VS Code suggestions, GitHub Copilot, and ChatGPT for debugging ideas. However, I:
•	Reviewed all code myself
•	Rewrote portions to make them clearer
•	Added explanatory comments
•	Verified functionality step by step
•	Kept the script simple to support learning and retention
•	Understood what was going on to the best of my ability (although some is over my head)
________________________________________
✅ Files in This Folder
•	mastodon_keyword_scrape.py
•	HNhits2.csv
•	Module-04-essentials-README.md
(I’m not sure I completely understand this, but this was chatgpt’s explanation of why using Beautiful Soup followed by CSS selectors didn’t work on Mastodon)
✅ Why I Switched from Mastodon
 I originally scraped Mastodon, but Selenium could not reliably extract the full text of posts—even when the words were clearly visible on screen. For example, I manually saw the word “the” in dozens of posts, but the scraper only detected it twice out of ~400. This showed that the issue was not only keyword frequency, but how Mastodon exposes text to automation tools.
Mastodon renders much of its post content using Shadow DOM, dynamic components, and JavaScript updates. These elements do not consistently appear in the standard HTML that Selenium receives through driver.page_source. As a result, the scraper only captured a small fraction of the visible text, even though the posts were not empty. BeautifulSoup would not solve this, because it can only parse the HTML Selenium can see.

________________________________________
✅ Why Hacker News Worked
Hacker News uses simple, static HTML with predictable structure. Each headline appears inside:
<span class="titleline"><a>Headline</a></span>
There is no Shadow DOM, no hidden text, no dynamic post rendering, and pagination is handled through a consistent “more” link. As a result, the scraper consistently found multiple keyword matches and behaved exactly as expected, making Hacker News a reliable platform for demonstrating Selenium scraping.
