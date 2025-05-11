from colorama import Fore, Style
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from playwright.sync_api import sync_playwright
import nopecha
import random
import time

#API KEY HERE!! ####################
api_key = "sm88th2ak3nmnut5"
###################################

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
        print(Fore.RED + "Username file is empty!" + Style.RESET_ALL)
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
        print(Fore.RED + "Password file is empty!" + Style.RESET_ALL)
        return None
textbox_password = password(passwordfile)

firstnamefile = "first_name.csv"
def firstname(firstnamefile):
    with open(firstnamefile, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if lines:
        firstname_value = lines[0].strip()

        with open(firstnamefile, "w", encoding="utf-8") as file:
            file.writelines(lines[1:])

        return firstname_value
    else:
        print(Fore.RED + "First name file is empty!" + Style.RESET_ALL)
        return None
textbox_firstname = firstname(firstnamefile)

lastnamefile = "last_name.csv"
def lastname(lastnamefile):
    with open(lastnamefile, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if lines:
        lastname_value = lines[0].strip()

        with open(lastnamefile, "w", encoding="utf-8") as file:
            file.writelines(lines[1:])

        return lastname_value
    else:
        print(Fore.RED + "Last name file is empty!" + Style.RESET_ALL)
        return None

textbox_lastname = lastname(lastnamefile)

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   

user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
user_agents = user_agent_rotator.get_user_agents()

ua = user_agent_rotator.get_random_user_agent()

with sync_playwright() as p:

    browser = p.chromium.launch(channel="msedge", headless=False, executable_path="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe", args=["--inprivate"])
    context = browser.new_context(user_agent=ua)
    page = context.new_page()
    print(f"useragent:{page.evaluate('navigator.userAgent')}")

    # Open the sign-up page

    
    # Open the sign-up page
    page.goto("https://signup.live.com")    # Open the sign-up page
    print(Fore.GREEN + "Signup page loaded!")
    time.sleep(1.9)
    # Type username into the input field
    page.fill("#usernameInput", textbox_username)

    time.sleep(2.8)
    # Press enter to continue
    page.press("#usernameInput", "Enter")
    
    # Wait for password field to load (modify selector if needed)
    page.wait_for_selector("#Password")
    time.sleep(3.2)
    page.fill("#Password", textbox_password)
    
    page.press("#Password", "Enter")
    print(" Successfully entered username and password!")
    
    #enter name
    page.fill("#firstNameInput", textbox_firstname)
    page.fill("#lastNameInput", textbox_lastname)
    page.press("#lastNameInput", "Enter")

    page.fill("#firstNameInput", "utrehkjdfw")
    page.fill("#lastNameInput", "etigfuhjsk")
    print("Name entered!")
    page.press("#lastNameInput", "Enter")

    #enter bday
    random_day = str(random.randint(1, 31))
    random_year = str(random.randint(1979, 2005))
    page.select_option("#BirthMonth", label="May")
    page.select_option("#BirthDay", random_day)
    page.fill("#BirthYear", random_year)
    page.press("#BirthYear", "Enter")
    print("Bday entered, proceding to CAPTCHA...")
    page.pause()


