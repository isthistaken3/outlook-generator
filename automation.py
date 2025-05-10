import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Keep browser open
driver = webdriver.Chrome(options=options)

driver.get("https://signup.live.com")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
print("Signup page loaded!")
username = "hitriosgjdf@outlook.com"
def get_username_data():
    with open("usernames.csv", newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        username = [row[0] for row in reader]  # Extract first column values
    return username

def remove_used_username():
    usernames = get_username_data()  # Load current usernames
    if usernames:
        usernames.pop(0)  # Remove first entry

        # Overwrite CSV with updated list
        with open("usernames.csv", "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            for username in usernames:
                writer.writerow([username])
        print(" Removed used username, updated CSV!")
remove_used_username()
# Locate username input fresh EVERY time using `#usernameInput`
def get_textbox():
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input#usernameInput"))
    )

try:
    textbox = get_textbox()  # Locate fresh
    textbox.send_keys(username)

    # Ensure focus before pressing Enter
    textbox.click()
    textbox = get_textbox()  # Refresh reference

    # Press Enter to proceed
    textbox.send_keys(Keys.RETURN)

    # Wait for transition
    WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
    print(" Successfully moved to password page!")

except:
    print(" Stale detected! Refreshing and retrying...")
    driver.refresh()
    textbox = get_textbox()
    textbox.send_keys(username)
    next_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "nextButton"))
)
next_button.click()

print(" Retried username entry.")
user_password = "rhowfjsklda"
print("Moving on to password page")

def get_password():
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "Password"))
    )

try:
    password_field = get_password()
    password_field.send_keys(user_password)
except:
    print("Error: Password field not found")
def get_password_data():
    with open("passwords.csv", newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        passwords = [row[0] for row in reader]  # Extract first column values
    return passwords

def remove_used_password():
    passwords = get_password_data()  # Load current usernames
    if passwords:
        passwords.pop(0)  # Remove first entry

        # Overwrite CSV with updated list
        with open("passwords.csv", "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            for password in passwords:
                writer.writerow([password])
        print(" Removed used password, updated CSV!")
remove_used_password()


#driver.quit()
