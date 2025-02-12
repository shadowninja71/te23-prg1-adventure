# Äventyr

Vad är det okej att använda AI till i programmeringen?

Exempelvis att skriva en berättlse, skapa ett innehåll. Problemlösningen är ditt jobb. AI kan hjälpa dig att skapa innehållet.

## Prompter

Du är en expert på att skriva äventyr i formatet [choose your own adventure]. Du har en väldigt lång erfarenhet av att skriva engagerande berättelser för [ungdomar] i det här formatet. 
Jag behöver din hjälp med skrivandet. Du kommer att svara i formatet av en python lista med dicts.
Jag klistrar in formatet som du ska svara i. Bekräfta att du förstår.

### Formatet 

Här är formatet för att skriva en berättelse i formatet [choose your own adventure]. 

```
format = [
    {
        "id": 1,
        "title": "String title for page",
        "text": "String text for page",
        "options": [
            {"text": "Option 1 with next page id", "next_id": 2},
            {"text": "Option 2 with next page id", "next_id": 3},
        ],
    },
]
```

## Nu är det dags att skriva en berättelse

Du har förberett AI med förutsättningarna. Vill du styra ännu mer över vad den kommer att skriva så skriv så mycket om förutsättningarna som möjligt. Vad är det för kontext, vilka karaktärer finns det, vilka är de viktigaste händelserna?

# App.py

Det här är delvis en uppgift i att läsa och förstå någon annans kod. Det är en väldigt viktig färdighet att ha som programmerare.

Programmet ni har fått med finns i app.py och historient sparas i en annan fil som importeras till `app.py`.

För att importera historien till app.py används import, det är viktigt att redigera den så att den stämmer med ditt filnamn och variabelnamn.

```python
from <filnamn> import <variabelnamnet> as BOOK
```

I `app.py` så finns det ett antal funktioner som används för att köra äventyret. Funktionerna startas från `main()`.

## input_int

Funktionen används för att användaren ska kunna mata in ett heltal och hanterar det så att programmet inte kraschar om användaren matar in något annat än ett heltal.

```python
def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
```

1. `def input_int(prompt):` - Definierar en funktion som heter input_int som tar ett argument `prompt`.
2. `while True:` - Startar en oändlig loop som fortsätter tills ett giltigt heltal har angetts.
3. `try:` - Försöker köra koden inom blocket.
4. `return int(input(prompt))` - Visar prompten för användaren och försöker konvertera användarens inmatning till ett heltal. Om det lyckas, returneras heltalet och funktionen avslutas.
5. `except ValueError:` - Om en `ValueError` uppstår (vilket händer om inmatningen inte kan konverteras till ett heltal), fångas undantaget och följande kod körs:
6. `print("Invalid input. Please enter a number.")` - Skriver ut ett felmeddelande som informerar användaren om att inmatningen var ogiltig och att de ska ange ett nummer.

## get_page

Funktionen används för att hämta ut en specifik sida från den `lista` med `dicts` som representerar boken. För att hitta sidan används parametern `page_id`. Se formatet för boken ovan.

```python
def get_page(book_data, page_id):
    for page in book_data:
        if page["id"] == page_id:
            return page
    return None
```

1. `def get_page(book_data, page_id):` - Definierar en funktion som heter `get_page` som tar två argument: `book_data` (en lista med sidor) och `page_id` (ID för den sida som ska hämtas).
2. `for page in book_data:` - Loopar igenom varje sida i `book_data`.
3. `if page["id"] == page_id:` - Kontrollerar om sidans ID matchar det angivna `page_id`.
4. `return page` - Om en matchande sida hittas, returneras den sidan.
5. `return None` - Om ingen matchande sida hittas efter att ha loopat igenom alla sidor, returneras `None`.

## show_page

Funktionen används för att visa en specifik sida från boken. Den tar in en sida som en `dict` och skriver ut dess titel, text och tillgängliga alternativ. Se formatet för boken ovan.

```python
def show_page(page):
    print(page["title"])
    print(page["text"])
    for i, option in enumerate(page["options"]):
        print(f"{i + 1}. {option['text']}")
```

1. `def show_page(page):` - Definierar en funktion som heter `show_page` som tar en sida som argument.
2. `print(page["title"])` - Skriver ut titeln på sidan.
3. `print(page["text"])` - Skriver ut texten på sidan.
4. `for i, option in enumerate(page["options"]):` - Loopar igenom varje alternativ på sidan och använder `enumerate` för att få både index (`i`) och alternativet (`option`).
5. `print(f"{i + 1}. {option['text']}")` - Skriver ut indexet för alternativet (börjar från 1 istället för 0) och texten för alternativet.

## main

Funktionen `main` är huvudfunktionen som körs för att starta äventyret. Den innehåller en loop som fortsätter tills användaren når slutet av boken.

```python
def main():
    current_page_id = 1
    while current_page_id is not None:
      # logik för att hämta och visa sidan
```

# Uppgift

Du ska arbeta med att ta fram en berättelse. Du ska sedan använda den färdiga koden för att visa upp berättelsen. Du ska skapa en ny fil för din berättelse och importera den till `app.py`.

1. Skapa en berättelse i formatet [choose your own adventure](https://en.wikipedia.org/wiki/Choose_Your_Own_Adventure) med minst 5 sidor.
2. Skapa en ny fil för din berättelse och spara den i formatet som en `lista` med `dicts`.
3. Importera din berättelse till `app.py` genom att använda `import`.
4. Kör programmet och testa din berättelse.

Det är grunden för uppgiften. 

## Utveckling
Här finns en lista med förslag på hur du kan utveckla din berättelse och programmet:

1. **Fler sidor och alternativ**: Lägg till fler sidor och valmöjligheter i din berättelse för att göra den mer komplex och engagerande.
2. **Huvudmeny**: Skapa en huvudmeny där spelaren kan välja att starta ett nytt spel eller avsluta. Använd en loop för att hantera menyn.
3. **Historik och återgång**: Spara en historik över spelarens val så att de kan gå tillbaka till tidigare sidor. Använd en lista för att spara valen och skapa en funktion för att spela upp historiken.
4. **Spara och ladda spel**: Lägg till funktioner för att spara och ladda spelet så att spelaren kan fortsätta där de slutade.
5. **Stridssystem**: Implementera stridssekvenser där spelaren måste välja rätt alternativ för att vinna. Använd sten, sax, påse som grund för striderna och skapa en funktion som hanterar striden.
6. **Karaktärsval**: Låt spelaren välja en karaktär i början av spelet som påverkar hur spelet utvecklas.
7. **Föremål och inventarie**: Skapa ett system där spelaren kan samla och använda föremål för att lösa problem. Använd en lista för att hantera spelarens inventarie.
8. **Poängräknare**: Lägg till en poängräknare som ökar eller minskar beroende på spelarens val.
9. **Tidsbegränsade val**: Inför en tidsbegränsning för att göra val, där spelaren måste välja inom en viss tid eller förlora.

Dessa förslag kan hjälpa dig att göra din berättelse och programmet mer interaktivt och engagerande för spelaren.
