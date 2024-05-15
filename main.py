import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
# author: xiaofei
# Set your configuration
api_key = "API key"  # your API key for the CAPTCHA solving service
site_key = "f7de0da3-3303-44e8-ab48-fa32ff8ccc7b"  # site key of your target site
site_url = "https://2captcha.com/demo/hcaptcha"  # URL of your target site

def get_captcha_solution(api_key, site_key, site_url):
    payload = {
        "clientKey": api_key,
        "task": {
            "type": "HCaptchaTaskProxyLess",
            "websiteKey": site_key,
            "websiteURL": site_url
        }
    }
    with requests.Session() as session:
        res = session.post("https://api.capsolver.com/createTask", json=payload)
        task_id = res.json().get("taskId")
        if not task_id:
            raise Exception("Failed to create task:", res.text)
        
        print("Waiting for CAPTCHA solution...")
        while True:
            time.sleep(5)  # Wait for 5 seconds before checking the result
            res = session.post("https://api.capsolver.com/getTaskResult", json={"clientKey": api_key, "taskId": task_id})
            result = res.json()
            if result.get("status") == "ready":
                return result["solution"]["gRecaptchaResponse"]
            if result.get("status") == "failed":
                raise Exception("CAPTCHA solve failed:", res.text)

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(site_url)

    try:
        token = get_captcha_solution(api_key, site_key, site_url)
        print("CAPTCHA Solved: ", token)
        
        # Insert token into the CAPTCHA response field
        script = f'document.querySelector(\'textarea[name="h-captcha-response"]\').value="{token}";'
        driver.execute_script(script)
        
        # Add any additional interactions here, like form submission
        # driver.find_element(By.ID, 'submit-button').click()
        
        print("CAPTCHA token injected successfully.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Keep the browser open for 10 seconds or close immediately based on your need
        time.sleep(10)
        driver.quit()

if __name__ == "__main__":
    main()
