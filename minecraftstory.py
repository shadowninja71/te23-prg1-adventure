adventure_story = [
    {
        "id": 1,
        "title": "Minecraft Adventure Begins",
        "text": "You wake up in a strange, blocky world with nothing but your bare hands. The sun is rising, and you can see the vast landscape of forests, mountains, and rivers. In the distance, you notice a small village.",
        "options": [
            {"text": "Head towards the village to seek shelter and resources.", "next_id": 2},
            {"text": "Venture into the forest to gather wood and explore.", "next_id": 3},
        ],
    },
    {
        "id": 2,
        "title": "Village Discovery",
        "text": "As you approach the village, you see friendly villagers going about their day. They welcome you and offer some basic supplies. You notice a blacksmith's shop and a farm nearby.",
        "options": [
            {"text": "Visit the blacksmith's shop to see what tools you can find.", "next_id": 4},
            {"text": "Help the farmers with their crops to earn some food.", "next_id": 5},
        ],
    },
    {
        "id": 3,
        "title": "Forest Exploration",
        "text": "You enter the forest and begin gathering wood for tools. You hear strange noises and spot a cave entrance nearby. The sun is still up, but you feel a sense of urgency.",
        "options": [
            {"text": "Investigate the cave and see what secrets it holds.", "next_id": 6},
            {"text": "Continue gathering wood and stay away from the cave.", "next_id": 7},
        ],
    },
]
adventure_story.extend([
    {
        "id": 4,
        "title": "Blacksmith's Shop",
        "text": "Inside the blacksmith's shop, you find an assortment of tools and weapons. The blacksmith offers to trade you an iron sword for some of the wood you've gathered.",
        "options": [
            {"text": "Trade some wood for the iron sword.", "next_id": 8},
            {"text": "Decline the offer and look around the village for other opportunities.", "next_id": 9},
        ],
    },
    {
        "id": 5,
        "title": "Helping the Farmers",
        "text": "The farmers are grateful for your help with the crops. In return, they give you some bread and point out a hidden chest in a nearby barn.",
        "options": [
            {"text": "Investigate the hidden chest in the barn.", "next_id": 10},
            {"text": "Thank the farmers and continue exploring the village.", "next_id": 9},
        ],
    },
    {
        "id": 6,
        "title": "Cave Exploration",
        "text": "You cautiously enter the cave and discover a hidden mineshaft. The eerie silence is broken by the sound of distant footsteps. You see a minecart and some abandoned tools.",
        "options": [
            {"text": "Take the minecart deeper into the mineshaft.", "next_id": 11},
            {"text": "Grab the abandoned tools and exit the cave.", "next_id": 12},
        ],
    },
    {
        "id": 7,
        "title": "Gathering Wood",
        "text": "You continue gathering wood and find an abundance of resources. As the sun begins to set, you realize you need to build a shelter to survive the night.",
        "options": [
            {"text": "Build a small wooden hut for shelter.", "next_id": 13},
            {"text": "Create a makeshift campfire and stay alert.", "next_id": 14},
        ],
    },
    {
        "id": 8,
        "title": "Iron Sword Acquired",
        "text": "You trade some wood for the iron sword. Now armed, you feel more confident about venturing into the unknown. The blacksmith mentions rumors of a hidden treasure in the nearby mountains.",
        "options": [
            {"text": "Head to the mountains to seek the hidden treasure.", "next_id": 15},
            {"text": "Explore the rest of the village to gather more information.", "next_id": 9},
        ],
    },
    {
        "id": 9,
        "title": "Village Exploration",
        "text": "You explore the village and talk to the villagers. They share stories about dangerous creatures that come out at night and the importance of having a secure shelter.",
        "options": [
            {"text": "Build a strong shelter before nightfall.", "next_id": 13},
            {"text": "Ask the villagers for more advice on survival.", "next_id": 16},
        ],
    },
])
adventure_story.extend([
    {
        "id": 10,
        "title": "Hidden Chest in the Barn",
        "text": "You carefully open the hidden chest and find some valuable resources, including iron ingots and a map. The map seems to point to a hidden treasure deep in the forest.",
        "options": [
            {"text": "Follow the map to the hidden treasure in the forest.", "next_id": 17},
            {"text": "Keep the map for later and explore more of the village.", "next_id": 9},
        ],
    },
    {
        "id": 11,
        "title": "Deeper into the Mineshaft",
        "text": "You ride the minecart deeper into the mineshaft and discover an underground lake. There are abandoned boats and mining equipment around.",
        "options": [
            {"text": "Take a boat and explore the underground lake.", "next_id": 18},
            {"text": "Look through the mining equipment for useful tools.", "next_id": 19},
        ],
    },
    {
        "id": 12,
        "title": "Leaving the Cave",
        "text": "You grab the abandoned tools and quickly leave the cave. The sun is starting to set, and you need to find or build a shelter for the night.",
        "options": [
            {"text": "Build a small wooden hut for shelter.", "next_id": 13},
            {"text": "Create a makeshift campfire and stay alert.", "next_id": 14},
        ],
    },
    {
        "id": 13,
        "title": "Building a Wooden Hut",
        "text": "You build a small but sturdy wooden hut to keep yourself safe through the night. As the stars come out, you hear the distant sounds of creatures lurking in the darkness.",
        "options": [
            {"text": "Stay inside and wait for morning.", "next_id": 20},
            {"text": "Venture outside and investigate the noises.", "next_id": 21},
        ],
    },
    {
        "id": 14,
        "title": "Campfire Vigil",
        "text": "You create a makeshift campfire and stay alert throughout the night. The fire keeps some of the creatures at bay, but you catch glimpses of glowing eyes in the shadows.",
        "options": [
            {"text": "Stay close to the fire and keep it burning.", "next_id": 22},
            {"text": "Use the fire to forge a stronger weapon.", "next_id": 23},
        ],
    },
    {
        "id": 15,
        "title": "Mountain Treasure Hunt",
        "text": "You head towards the mountains, equipped with your iron sword. The journey is tough, but you finally reach a cave entrance that matches the rumors.",
        "options": [
            {"text": "Enter the cave to search for the hidden treasure.", "next_id": 24},
            {"text": "Set up camp outside the cave and rest before entering.", "next_id": 25},
        ],
    },
    {
        "id": 16,
        "title": "Survival Advice",
        "text": "The villagers share their knowledge about crafting better tools, finding food, and defending against monsters. You feel more prepared for the challenges ahead.",
        "options": [
            {"text": "Build a strong shelter before nightfall.", "next_id": 13},
            {"text": "Venture into the forest to put your new skills to the test.", "next_id": 3},
        ],
    },
])
adventure_story.extend([
    {
        "id": 17,
        "title": "Forest Treasure Hunt",
        "text": "You follow the map deep into the forest. After a long journey, you find a hidden cave entrance covered by vines. Inside, you see the faint glint of something shiny.",
        "options": [
            {"text": "Enter the cave and uncover the hidden treasure.", "next_id": 26},
            {"text": "Set up camp outside the cave and rest before exploring.", "next_id": 27},
        ],
    },
    {
        "id": 18,
        "title": "Underground Lake",
        "text": "You take a boat and explore the underground lake. As you row, you notice an underwater tunnel leading to another part of the cave.",
        "options": [
            {"text": "Dive into the underwater tunnel to see where it leads.", "next_id": 28},
            {"text": "Stay on the boat and explore the rest of the lake.", "next_id": 29},
        ],
    },
    {
        "id": 19,
        "title": "Mining Equipment",
        "text": "You look through the mining equipment and find a pickaxe and some torches. These tools will be useful for further exploration.",
        "options": [
            {"text": "Use the pickaxe to mine for valuable resources.", "next_id": 30},
            {"text": "Leave the cave and find a safe place to spend the night.", "next_id": 12},
        ],
    },
    {
        "id": 20,
        "title": "Night in the Hut",
        "text": "You stay inside the wooden hut and wait for morning. The sounds of creatures outside grow louder, but the hut keeps you safe.",
        "options": [
            {"text": "Stay inside until the sun rises.", "next_id": 31},
            {"text": "Peek outside to see what creatures are lurking.", "next_id": 32},
        ],
    },
    {
        "id": 21,
        "title": "Investigating the Noises",
        "text": "You venture outside and investigate the noises. Suddenly, you are confronted by a group of zombies! You must act quickly.",
        "options": [
            {"text": "Fight the zombies with your iron sword.", "next_id": 33},
            {"text": "Run back to the safety of your hut.", "next_id": 20},
        ],
    },
    {
        "id": 22,
        "title": "Keeping the Fire Burning",
        "text": "You stay close to the campfire and keep it burning. The creatures stay at a distance, but you remain vigilant throughout the night.",
        "options": [
            {"text": "Stay awake and keep watch until morning.", "next_id": 34},
            {"text": "Try to get some rest by the fire.", "next_id": 35},
        ],
    },
    {
        "id": 23,
        "title": "Forging a Stronger Weapon",
        "text": "Using the fire, you manage to forge a stronger weapon. Now better equipped, you feel more confident facing the dangers that lie ahead.",
        "options": [
            {"text": "Venture into the forest to test your new weapon.", "next_id": 3},
            {"text": "Head towards the village to share your success.", "next_id": 9},
        ],
    },
    {
        "id": 24,
        "title": "Entering the Cave",
        "text": "You enter the cave and discover a labyrinth of tunnels. As you navigate the twists and turns, you find a hidden chamber filled with treasure.",
        "options": [
            {"text": "Take some treasure and head back to the village.", "next_id": 36},
            {"text": "Explore the hidden chamber for more secrets.", "next_id": 37},
        ],
    },
    {
        "id": 25,
        "title": "Camping Outside the Cave",
        "text": "You set up camp outside the cave to rest before entering. As you sleep, you dream of the adventures that await inside.",
        "options": [
            {"text": "Enter the cave when you wake up.", "next_id": 24},
            {"text": "Return to the village to gather more supplies.", "next_id": 9},
        ],
    },
])