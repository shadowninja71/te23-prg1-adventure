adventure = [
    {
        "id": 1,
        "title": "Välj din karaktär",
        "text": "Du står inför en stor röd knapp som verkar vara en portal till en annan värld. Men innan du kan trycka på knappen, måste du välja vilken karaktär du vill vara.",
        "options": [
            {"text": "Bli en modig krigare", "next_id": 2},
            {"text": "Bli en klok trollkarl", "next_id": 3},
            {"text": "Bli en snabb tjuv", "next_id": 4},
        ],
    },
    {
        "id": 2,
        "title": "Den modiga krigaren",
        "text": "Du har valt att bli en modig krigare. Med ditt svärd i handen och rustning på kroppen, är du redo att möta alla faror som väntar på andra sidan knappen.",
        "options": [
            {"text": "Tryck på den röda knappen", "next_id": 5},
        ],
    },
    {
        "id": 3,
        "title": "Den kloka trollkarlen",
        "text": "Du har valt att bli en klok trollkarl. Med din stav och dina magiska krafter, är du redo att utforska den mystiska världen bakom den röda knappen.",
        "options": [
            {"text": "Tryck på den röda knappen", "next_id": 5},
        ],
    },
    {
        "id": 4,
        "title": "Den snabba tjuven",
        "text": "Du har valt att bli en snabb tjuv. Med dina smidiga rörelser och skarpa sinnen, är du redo att smyga dig genom den okända världen bakom den röda knappen.",
        "options": [
            {"text": "Tryck på den röda knappen", "next_id": 5},
        ],
    },
    {
        "id": 5,
        "title": "Den röda knappen",
        "text": "Du trycker på den stora röda knappen och känner hur världen runt dig förändras. Du sugs in i en virvel av ljus och färger, och när du öppnar ögonen igen, befinner du dig i en helt ny värld.",
        "options": [
            {"text": "Utforska den nya världen", "next_id": 6},
        ],
    },
]

adventure.append(
    {
        "id": 6,
        "title": "Den nya världen",
        "text": "Du befinner dig i en märklig och främmande värld. Landskapet är fyllt av märkliga växter och konstiga ljud. Plötsligt hör du ett hotfullt morrande bakom dig.",
        "options": [
            {"text": "Vänd dig om och möt hotet", "next_id": 7},
            {"text": "Försök att gömma dig", "next_id": 8},
        ],
    }
)

adventure.append(
    {
        "id": 7,
        "title": "Mötet med fienden",
        "text": "Du vänder dig om och ser en enorm varelse med glödande ögon och vassa klor. Det är en Skuggvarg, en farlig fiende som vaktar denna värld.",
        "options": [
            {"text": "Strid mot Skuggvargen", "next_id": 9},
            {"text": "Försök att fly", "next_id": 10},
        ],
    }
)

adventure.append(
    {
        "id": 8,
        "title": "Gömstället",
        "text": "Du försöker gömma dig bakom en stor sten, men Skuggvargen har redan fått upp ditt spår. Du hör dess tunga steg närma sig.",
        "options": [
            {"text": "Förbered dig på att strida", "next_id": 9},
            {"text": "Försök att distrahera den och fly", "next_id": 10},
        ],
    }
)

adventure.append(
    {
        "id": 9,
        "title": "Striden mot Skuggvargen",
        "text": "Du drar ditt vapen och förbereder dig på striden. Skuggvargen rusar mot dig med ett vrål. Det är en kamp på liv och död.",
        "options": [
            {"text": "Använd din styrka och slåss", "next_id": 11},
            {"text": "Använd din list och överlista den", "next_id": 12},
        ],
    }
)

adventure.append(
    {
        "id": 10,
        "title": "Flyktförsöket",
        "text": "Du försöker fly från Skuggvargen, men den är snabb och stark. Du måste tänka snabbt för att undkomma.",
        "options": [
            {"text": "Spring mot en säker plats", "next_id": 13},
            {"text": "Försök att förvilla den", "next_id": 14},
        ],
    }
)