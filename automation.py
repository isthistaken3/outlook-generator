from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Launch browser (set to False for visible window)
    page = browser.new_page()
    
    # Open the sign-up page
    page.goto("https://signup.live.com")
    
    # Type username into the input field
    page.fill("#usernameInput", "test45ertuihsdj@outlook.com")
    
    # Press enter to continue
    page.press("#usernameInput", "Enter")
    
    # Wait for password field to load (modify selector if needed)
    page.wait_for_selector("#Password")
    page.fill("#Password", "SuperSecurePasswo*#$rd123")
    
    page.press("#Password", "Enter")
    print(" Successfully entered username and password!")
    
    page.fill("#firstNameInput", "utrehkjdfw")
    page.fill("#lastNameInput", "etigfuhjsk")
    print("Name entered!")
    page.press("#lastNameInput", "Enter")
    page.pause()
