import streamlit as st
import requests
from bs4 import BeautifulSoup
from app_selenium import scrap_sele
# Define a function to scrape text from a URL
def scrape_text_from_url(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        # Automatically add "http://" if the protocol is missing
        url = "http://" + url
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', }
    sess = requests.Session()
    response = sess.get(url , headers = headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        return text
    else:
        return f"Failed to retrieve the webpage. Status code: {response.status_code}"


# Streamlit app code
st.title("Incerta Web  App")

# Load the custom CSS file
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Create an input text box for the user to enter a URL
url_input = st.text_input("Enter a URL to scrape:")

# Create a submit button
if st.button("Scrape") or url_input:
    if url_input:
        # Call the function to scrape text and display the result
        scraped_text = scrap_sele(url_input)
        scraped_text = "\n".join([line for line in scraped_text.splitlines() if line.strip()])

        st.text("Scraped Text:")
        st.text_area("Result", scraped_text, height=400)
    else:
        st.warning("Please enter a URL to scrape.")



