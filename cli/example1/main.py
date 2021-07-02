""" a CLI built on argparse
"""

from argparse import ArgumentParser

from uuid import uuid4

def fetch_title_from_api(title: str, author: str = None) -> dict:
  """Fetch info for a book title from an API

  :param title: str
  :param author: str
  :return: dict
  """

  book_info = { 'title': title, 'author': author, "ISBN": str(uuid4())}

  return book_info



def main() -> None:
    """
    """
    print("example1", __file__)
    parser = ArgumentParser()
    parser.add_argument("--title", "-t", help="A book title.")
    parser.add_argument("--author", "-a", help="The author of the book.")

    results = parser.parse_args()

    book = fetch_title_from_api(results.title, results.author)

    print(book)



if __name__ == "__main__":
    main()


    
