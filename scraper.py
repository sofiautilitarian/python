from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def main(): 
    url = 'https://research.com/scientists-rankings/computer-science'

    webdriver_path = r"C:\Users\Sofia\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    
    service = Service(webdriver_path)
    driver = webdriver.Chrome(service=service)

    driver.get(url)

if __name__ == "__main__":
    main()