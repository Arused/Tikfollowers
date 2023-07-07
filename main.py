import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import init, Fore, Style

# Initialize colorama
init()

def setup_browser() -> webdriver:
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    return webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

def countdown(seconds):
    for remaining in range(seconds, 0, -1):
        os.system(f"title [!] | {time.strftime('%H:%M:%S')} Please wait {remaining // 60}m {remaining % 60}s for New Followers")
        time.sleep(1)

def solve(debug) -> None:
    while True:
        browser = setup_browser()

        browser.get("https://tikfollowers.com")  # Open the website

        # Wait until the "Tiktok Free Followers" button is visible
        followers_button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.my-btn[href='https://tikfollowers.com/tiktok-free-followers']")))

        # Perform your desired actions after detecting the button
        # For example, you can prompt the user for a choice
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print(f"{Fore.LIGHTMAGENTA_EX}[1]{Style.RESET_ALL} | {Fore.BLUE}[{current_time}]{Style.RESET_ALL} Tiktok Followers")
        choice = input(f"{Style.BRIGHT}Choice your method:{Style.RESET_ALL} ")

        # Perform different actions based on the user's choice
        if choice == "1":
            # Click the "Tiktok Free Followers" button
            browser.execute_script("arguments[0].click();", followers_button)

            # Implement the logic for the "Followers" option on the new website
            # Prompt the user for a TikTok username
            current_time = time.strftime("%H:%M:%S", time.localtime())
            print(f"{Fore.LIGHTMAGENTA_EX}[?]{Style.RESET_ALL} | {Fore.BLUE}[{current_time}]{Style.RESET_ALL} Tiktok Username > ", end="")
            username = input()

            # Find the username input element and enter the user's input
            username_input = browser.find_element(By.CSS_SELECTOR, "input.form-control.un")
            username_input.send_keys(username)

            # Find the "Find Account" button and click it
            find_account_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-block.solid-btn.border-radius.mt-4.mb-3.submit")
            find_account_button.click()

            # Wait until the "Send Followers" button is visible
            send_followers_button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Send Followers')]")))
            
            # Click the "Send Followers" button
            send_followers_button.click()

            # Wait for the success message to appear
            success_message = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2.swal2-title")))

            # Print the message and create an animation
            current_time = time.strftime("%H:%M:%S", time.localtime())
            animation_chars = ["[\\]", "[|]", "[/]", "[-]"]
            animation_index = 0

            print(f"{Fore.LIGHTMAGENTA_EX}[\\]{Style.RESET_ALL} | {Fore.BLUE}[{current_time}]{Style.RESET_ALL} Sending Followers...", end="", flush=True)

            while not success_message.is_displayed():
                animation_index = (animation_index + 1) % len(animation_chars)
                time.sleep(0.2)
                print(f"\r{animation_chars[animation_index]} | {Fore.BLUE}[{current_time}]{Style.RESET_ALL} Sending Followers...", end="", flush=True)

            print("\nFollowers sent successfully!")

            # Wait for 8 minutes before repeating the steps
            countdown(480)

            # Close the browser
            browser.quit()

# Example usage
solve(debug=True)
