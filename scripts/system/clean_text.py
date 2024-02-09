from bs4 import BeautifulSoup

def clean_text(text):
    """
    Cleans the given text by removing HTML tags and unwanted characters.

    Parameters:
    - text (str): The input text.

    Returns:
    - str: The cleaned text.
    """
    # Remove HTML tags
    soup = BeautifulSoup(text, "html.parser")
    cleaned_text = soup.get_text(separator=" ")

    # Remove unwanted characters
    cleaned_text = cleaned_text.replace("\n", " ").strip()

    return cleaned_text