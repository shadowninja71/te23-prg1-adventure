# För att importera berättelsen från en annan fil så använder vi from <filnamn> 
# import <variabel> och sedan kan vi använda variabeln i vår kod. I det här 
# fallet så har vi importerat berättelsen från redbutton.py och döpt om 
# variabeln till BOOK. Vi kan nu använda variabeln BOOK för att komma åt 
# berättelsen i vår kod. Det är viktigt att den heter BOOK (det är därför vi använder
# as BOOK) för det är variabeln som används i vår kod.
# from book import BOOK
from redbutton import adventure as BOOK

# Funktion input_int som tar en sträng som argument och returnerar ett heltal.
# Sträng-argumentet är det som skrivs ut i input prompten.
def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

# Funktion get_page som tar två argument, book_data och page_id. Den går igenom
# varje sida i book_data och om sidans id matchar page_id så returnerar den sidan.
def get_page(book_data, page_id):
    for page in book_data:
        if page["id"] == page_id:
            return page
    return None

# Funktion show_page som tar en sida som argument och skriver ut titeln, texten
# och varje alternativ på sidan.
def show_page(page):
    print(page["title"])
    print(page["text"])
    for i, option in enumerate(page["options"]):
        print(f"{i + 1}. {option['text']}")

# Main är huvudfunktionen som körs när programmet startas.
def main():
    current_id = 1
    while True and current_id is not None:
        current_page = get_page(BOOK, current_id)
        show_page(current_page)
        choice = input_int("Enter your choice: ")
        if 1 <= choice <= len(current_page["options"]):
            current_id = current_page["options"][choice - 1]["next_id"]
        else:
            print("Invalid choice. Please try again.")
            current_id = None

if __name__ == "__main__":
    main() # starta main-funktionen
