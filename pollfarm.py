from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import random
import time

# Set Chrome options to run in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource issues

# Use the temporary profile without caching
driver = webdriver.Chrome(options=chrome_options)

# Replace 'https://example.com' with your target webpage URL
url = 'https://poll.fm/14975029'

# Replace 'radio_button_id' with the actual ID of the radio button you want to click
radio_button_id = 'PDI_answer66394816'

# Replace 'vote_button_name' with the actual name attribute of the 'Vote' button
vote_button_id = 'pd-vote-button14975029'

count = 0

# Function to perform the vote action
def vote():
    try:
        driver.get(url)
        time.sleep(1.5)  # Add a delay (1.5 seconds in this example)

        # Find the radio button by its ID
        radio_button = driver.find_element(By.ID, radio_button_id)
        
        # Simulate mouse movement to the radio button and click
        actions = ActionChains(driver)
        actions.move_to_element(radio_button).perform()
        time.sleep(random.uniform(0.5, 1.5))  # Add a small delay
        actions.click(radio_button).perform()

        # Find the Vote button by its ID
        vote_button = driver.find_element(By.ID, vote_button_id)
        
        # Simulate mouse movement to the vote button and click
        actions.move_to_element(vote_button).perform()
        time.sleep(random.uniform(0.5, 1.5))  # Add a small delay
        actions.click(vote_button).perform()
        global count
        count += 1
        print(count)

        # If the redirect URL contains the word "revoted", your vote won't count, therefore we begin a cooldown period
        get_url = driver.current_url
        if "revoted" in get_url:
            print("Cooldown activated.")
            time.sleep(60)
    except Exception as e:
        print(f"Error: {e}")

# Define the number of times to repeat the action
num_votes = 1000  # Change this number to the desired number of repetitions

for _ in range(num_votes):
    vote()

# Close the browser
driver.quit()
