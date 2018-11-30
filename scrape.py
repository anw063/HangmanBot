from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def get_categories():
    """
    Downloads the page where the list of mathematicians is found
    and returns a list of strings, one per mathematician
    """
    url = 'https://www.manythings.org/vocabulary/lists/c/'
    response = simple_get(url)

    if response is not None:
        soup = BeautifulSoup(response, 'html.parser')
        names = list()
        added = ["ESL / EFL Basic Vocabulary Word Lists","English Vocabulary Word Lists with Games, Puzzles and Quizzes", "Interesting Things for ESL Students", "Copyright", "Charles Kelly", "Lawrence Kelly"]

        for category in soup.find_all('a'):
          if category.text not in added:
            names.append((category.text, category.get('href')))
            added.append(category.text)
      
        return list(names)

    # Raise an exception if we failed to get any data from the url
    raise Exception('Error retrieving contents at {}'.format(url))
  
def get_subcategories(subcategory):
    """
    Downloads the page where the list of mathematicians is found
    and returns a list of strings, one per mathematician
    """
    url = 'https://www.manythings.org/vocabulary/lists/c/' + subcategory
    response = simple_get(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        names = list()
        added = ["ESL / EFL Basic Vocabulary Word Lists","English Vocabulary Word Lists with Games, Puzzles and Quizzes", "Interesting Things for ESL Students", "Copyright", "Charles Kelly", "Lawrence Kelly"]
        for li in html.select('li'):
            for name in li.text.split('\n'):
                if len(name) > 0:
                    names.append(name.strip())
                    added.append(name.strip())
        return list(names)

    # Raise an exception if we failed to get any data from the url
    raise Exception('Error retrieving contents at {}'.format(url))