import csv
from playwright.sync_api import sync_playwright

usernamefile = "usernames.csv"
def username(usernamefile):
    with open(usernamefile, "r", encoding="utf-8") as file:
        lines = file.readlines()  # ✅ Read all lines into a list

    if lines:
        username_value = lines[0].strip()  # ✅ Get first value & remove extra spaces

        # ✅ Write back all lines *except* the first one
        with open(usernamefile, "w", encoding="utf-8") as file:
            file.writelines(lines[1:])  # ✅ Remove first entry

        return username_value  # ✅ Return stored value
    else:
        print("File is empty!")
        return None
textbox_username = username(usernamefile)

passwordfile = "passwords.csv"
def password(passwordfile):
    with open(passwordfile, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if lines:
        password_value = lines[0].strip()

        with open(passwordfile, "w", encoding="utf-8") as file:
            file.writelines(lines[1:])

        return password_value
    else:
        print("File is empty!")
        return None
textbox_password = password(passwordfile)


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) # Launch browser (set to False for visible window)
    page = browser.new_page()
    
    # Open the sign-up page
    page.goto("https://signup.live.com")
    
    # Type username into the input field
    page.fill("#usernameInput", textbox_username)
    
    # Press enter to continue
    page.press("#usernameInput", "Enter")
    
    # Wait for password field to load (modify selector if needed)
    page.wait_for_selector("#Password")
    page.fill("#Password", textbox_password)
    
    page.press("#Password", "Enter")
    print(" Successfully entered username and password!")
    
    page.fill("#firstNameInput", "utrehkjdfw") 
    page.fill("#lastNameInput", "etigfuhjsk") 
    print("Name entered!") 
    page.press("#lastNameInput", "Enter") 
    page.pause()
