from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import os
import time
import pandas as pd
from datetime import datetime

# Get the project root directory (assuming the script is in src/extractors/wta/) and construct the path to the GeckoDriver executable
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print(project_root)
geckodriver_path = os.path.join(project_root, "drivers", "geckodriver") 

# Initialize the Firefox webdriver with options
options = Options()
options.add_argument("--headless")
service = Service(executable_path=geckodriver_path) # Use Service to specify the GeckoDriver path (for compatibility)
driver = webdriver.Firefox(service=service, options=options) # Fallback to default Firefox if the secret is not found

# Navigate to the  URL

url = 'https://www.wtatennis.com/rankings/singles'
driver.get(url)

current_url = driver.current_url
print(f"Current URL: {current_url}")

wait = WebDriverWait(driver, 30)
section_element = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//section[@class='rankings widget widget--fullwidth-header' and @data-widget='rankings']")))

# Handle the "Load More" button
click_count = 1
while True:
    try:
        print("Trying to find 'Load More' button...")
        load_more_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn.rankings__show-more.js-mobile-load-more")))
        print("'Load More' button found! Clicking it...")
        load_more_button.click()
        print(f"Clicked 'Load More' {click_count} times. Waiting for data to load...")
        time.sleep(5)  # Adjust as needed
        click_count += 1
    except:
        print("'Load More' button not found. Assuming all data is loaded.")
        break  # Exit the loop

# Get the page source
page_source = driver.page_source

# Save the HTML to a file for further analysis or debugging
output_html_path = os.path.join(project_root, "src", "extractors", "wta", "wta_rankings_page_source.html")
print("Path: ", output_html_path)
with open(output_html_path, 'w', encoding='utf-8') as file:
    file.write(page_source)
print(f"HTML of the page saved to {output_html_path}")


# Pass the HTML to BeautifulSoup for further scraping
soup = BeautifulSoup(page_source, 'html.parser')

# Find the rankings table
rankings_table = soup.find("table", class_="rankings__list.rankings__list--overview.js-rankings-list")
headers = [th.text.strip() for th in rankings_table.find("thead").find_all("th")] # Extract table headers
rows_data = [] # Extract table rows data
for row in rankings_table.find("tbody").find_all("tr"):
    row_data = [td.text.strip() for td in row.find_all("td")]
    rows_data.append(row_data)

# Create a Pandas DataFrame from the extracted data
df = pd.DataFrame(rows_data, columns=headers)

# Get the current date and time for file naming
now = datetime.now().strftime("%Y-%m-%d-%H%M%S")

# Save the DataFrame to a CSV file
output_csv_path = os.path.join(project_root, "data", "raw", f"wta-{now}.csv")
df.to_csv(output_csv_path, index=False)

print(f"WTA rankings data saved to {output_csv_path}")


# Close the Selenium driver
driver.quit()