from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# URL of the web page you want to scrape

def scrap_sele(url) :
    # Initialize Chrome driver with headless option
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open the URL in the web browser
        driver.get(url)

        # Wait for the page to load (you might need to adjust the time)
        driver.implicitly_wait(10)

        # Extract the HTML content of the web page
        page_source = driver.page_source

        # Parse the HTML content with BeautifulSoup to extract text
        soup = BeautifulSoup(page_source, 'html.parser')
        text_data = soup.get_text()

        # You may need to clean and process the text data further
        # For example, removing extra spaces, newlines, or unwanted characters.

        # Print or save the scraped text data
        return(text_data)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the web browser
        driver.quit()
