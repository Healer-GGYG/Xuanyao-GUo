# Xuanyao-GUO
# 🌈 Mood Pet User Guide

**Mood Pet** is an interactive emotion-tracking program. Users can engage with various virtual pets to log their daily moods, boost emotions through mini-games, and visualize their mood trends over time.

---

## 🐾 How to Start

Make sure all the following files are placed in the same directory:

| File | Description |
|------|-------------|
| `main.py` | Main program entry, handles user interaction |
| `pet.py` | Defines pet attributes, personalities, and reactions |
| `emotion.py` | Maps moods to scores and vice versa |
| `activity.py` | Contains all interactive games |
| `logger.py` | Handles CSV log creation, reading, and writing |
| `mood_visualizer.py` | Generates mood trend bar charts |
| `emotion_words.txt` | Emotion word list used in the word chain game |

To launch the program, run in the terminal: **python main.py**

## 🎮 User Flow
### Step 1: Launch the Program
⦿ The system will ask if you'd like to use Mood Pet.

⦿ Enter y to begin or n to exit.

### Step 2: Choose and Name Your Pet
⦿ Choose a pet type (e.g., Dog, Cat, Dragon, etc.).

⦿ Give your pet a name.

(The combination of pet type + pet name = user_id, which is used to track and retrieve your mood history.)

### Step 3: Input Your Current Mood
⦿ You must enter one of the following moods (case-insensitive):

happy, excited, relaxed, neutral,  
bored, tired, sad, stressed,  
angry, anxious, frustrated, lonely

(If you enter a mood outside of the above list, the system will treat it as neutral.)

### Step 4: Pet Reaction + Game Recommendation
⦿ Your pet will respond based on your mood and its personality.
(Each pet speaks with a unique tone and offers mood-specific feedback.)

⦿ The pet will recommend a mini-game for you to try. You can:

      1. Play the recommended game
      
      2. Change to a different game
      
      3. Skip the game section

### Step 5: Mini-Game Interaction
You can play one of the following games:
| Game                   | Description                                              |
| ---------------------- | -------------------------------------------------------- |
| `Guess the Number`     | Guess a number between 1–100; correct guesses boost mood |
| `Funny Quiz`           | Answer pun-based jokes for emotional uplift              |
| `Lucky Number`         | Receive your lucky number of the day                     |
| `Lucky Colour`         | Reveal your lucky color for the day                      |
| `Emotional Word Chain` | Take turns with your pet saying emotional words          |

Each pet supports 2–3 specific games. The game list varies by pet personality.

### Step 6: Mood Score & Logging
⦿ After the game, a total mood score will be displayed (base mood + game bonus).

⦿ The system will prompt whether to save today’s mood log.

If a log already exists for today, you'll be asked if you want to overwrite it.

### Step 7: Mood Trend Visualization (Optional)
⦿ You can choose to view a bar chart of your mood trend from the past:

   **·** 7 days
   
   **·** 14 days
   
   **·** 21 days
   
   **·** 30 days

## 📊 Mood Score Interpretation
Your mood input is converted to a score (see emotion.py):

The higher the score, the more positive your emotional state.

## 📁 Mood Logging Overview
Mood data is automatically saved to mood_log.csv, which contains:

   **·** Timestamp
   
   **·** User ID (pet name + species)
   
   **·** Input mood
   
   **·** Final mood score
