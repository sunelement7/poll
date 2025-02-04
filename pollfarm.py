from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

# Set Chrome options for headless execution
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without UI
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Path to Chrome & Chromedriver on Render
chrome_options.binary_location = "/usr/bin/google-chrome"
service = Service("/usr/bin/chromedriver")

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Poll URL
url = "https://poll.fm/14975029"

# Radio button and vote button IDs
radio_button_id = "PDI_answer66394816"
vote_button_id = "pd-vote-button14975029"

count = 0  # Vote counter

# Function to perform the vote action
def vote():
    global count
    try:
        driver.get(url)
        time.sleep(1.5)

        # Find and click the radio button
        radio_button = driver.find_element(By.ID, radio_button_id)
        actions = ActionChains(driver)
        actions.move_to_element(radio_button).perform()
        time.sleep(random.uniform(0.5, 1.5))
        actions.click(radio_button).perform()

        # Find and click the vote button
        vote_button = driver.find_element(By.ID, vote_button_id)
        actions.move_to_element(vote_button).perform()
        time.sleep(random.uniform(0.5, 1.5))
        actions.click(vote_button).perform()

        count += 1
        print(f"Vote #{count} submitted!")

        # Check if vote was successful
        if "revoted" in driver.current_url:
            print("Cooldown triggered, waiting 60 seconds...")
            time.sleep(60)

    except Exception as e:
        print(f"Error: {e}")

# Loop to keep voting until stopped
while True:
    vote()
    time.sleep(random.uniform(2, 5))  # Small delay between votes

# Close the browser when done (won't be reached unless manually stopped)
driver.quit()
