# Eldoria: The Enigma

Welcome to **Eldoria: The Enigma**, a text-based adventure game that takes you into the mystical realm of Eldoria. You will join the Adventurer's Guild, face dark forces, and embark on a journey to save the realm.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

**Eldoria: The Enigma** is a story-driven text-based game where players create a character and interact with the world through a series of prompts and responses. The game is set in the mystical realm of Eldoria, where the player must defeat the Shadow Cult and save the Crystal of Eternity.

## Features

- **Character Creation**: Players can set up their profile, including gender, name, and age.
- **Interactive Story**: Engage in conversations with NPCs (Non-Playable Characters) and progress through the storyline.
- **Save Profile**: The player's profile is saved in a file, allowing for persistent game states.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ciphersyntax1/eldorias-enigma.git
    ```

2. Navigate to the project directory:

    ```bash
    cd eldorias-enigma
    ```

3. Ensure that you have Python installed on your system. This game requires Python 3.x.

4. Run the game:

    ```bash
    python main.py
    ```

## How to Play

1. **Start the Game**: Run `main.py` to begin your adventure.
2. **Character Setup**: You will be prompted to enter your gender, name, and age. This information is stored in a file for future reference.
3. **Follow the Story**: After setting up your profile, you will be guided through the story. Read the text carefully and respond to prompts as needed.
4. **Progress**: Your decisions and responses will shape the course of the adventure.

## Project Structure

Here's a quick overview of the project's structure:

```bash
eldoria-the-enigma/
│
├── data/
│   └── inventory.py          # Placeholder for inventory management
│
├── com.eldoria.enigma/       # Directory for saving profile data
│   └── profile.enigma        # Saved profile data (generated after running the game)
│
├── main.py                   # Entry point for the game
└── README.md                 # Project documentation
```

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository, create a new branch, and submit a pull request. Make sure to follow the existing code style and add comments where necessary.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
