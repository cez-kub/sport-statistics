# Tool Choices and Rationale 

## Web Scraping Tools:

**Choice:** Selenium + BeautifulSoup

- **Why Selenium?** Chosen for its ability to handle dynamic websites that require JavaScript rendering (e.g., ATP and WTA websites). It allows easy interaction with web elements like clicking pagination buttons. Open-source and widely supported by many different browser projects. No vendor lock-in.
- **Why BeautifulSoup?** It’s lightweight, easy to use for parsing HTML, and works well in combination with Selenium for extracting structured data. A fully open-source project for parsing HTML/XML.
- **Alternative Considered:** Playwright (but Selenium was chosen for its stability and broader community support).  

## Browsers:

**Choice:** Firefox (GeckoDriver)

- **Why Firefox (GeckoDriver)?** Firefox is fully open-source, developed by the Mozilla Foundation, a non-profit. Using Firefox with the GeckoDriver in headless mode would meet your criteria. No vendor lock-in, and its development is driven by an open community.
- **Alternative Considered:** Chromium (Chromium is the open-source version of Google Chrome, maintained as an open project, but it's Google-backed)


## Data Storage Format:  

**Choice:** Parquet

- **Why Parquet?** Efficient columnar storage format, ideal for large datasets and sports data exploration. Parquet allows for fast reads and writes, especially for structured data. Open standard for efficient data storage, no lock-in.
- **Alternative Considered:** CSV (but Parquet provides better compression and is more suitable for large-scale data).  

## Data Processing Tools:

**Choice:** Pandas

- **Why Pandas?** It's a powerful, open-source data manipulation library that is perfect for handling tabular data. Since tennis match data is structured (with columns for player names, scores, rankings, etc.), Pandas is highly suitable. Open-source, with no lock-in.
- **Alternative Considered:** PySpark (but Pandas was chosen for simplicity given the dataset size is manageable without distributed computing).