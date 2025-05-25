from datetime import datetime
from emotion import mood_to_score
import random

# pet-->personality
pets_personality= {
    'cat': 'lazy',
    'dog': 'cheerful',
    'pig': 'funny',
    'dragon': 'proud',
    'fox': 'sneaky'
}

species_emoji = {
    'cat': '🐱',
    'dog': '🐶',
    'pig': '🐷',
    'dragon': '🐲',
    'fox': '🦊'
}

# personality -> game recommondation list
personality_activities = {
    "cheerful": ["Guess the Number", "Funny Quiz", "Lucky Colour"],
    "lazy": ["Lucky Number", "Emotional Word Chain","Lucky Colour"],
    "funny": ["Funny Quiz", "Emotional Word Chain","Lucky Number"],
    "proud": ["Guess the Number", "Emotional Word Chain","Lucky Number"],
    "sneaky": ["Guess the Number", "Funny Quiz","Lucky Number"]
}

# user mood -> pet response
def score_based_response(score: int) -> str:
    if score >= 5:
        return "You seem super joyful! Let's celebrate! 🎉"
    elif score >= 2:
        return "Nice! You're feeling good today 🤣"
    elif score == 1:
        return "Feeling a little positive, that\'s a great start 😌"
    elif score == 0:
        return "You seem neutral. Maybe I can brighten your day 🌟"
    elif score >= -2:
        return "Feeling a bit down? Let's cheer up together 🍻"
    elif score >= -5:
        return "You seem sad... I'm here for you 😢"
    else:
        return "You seem really upset... Let's do something relaxing ♨️"



class Pet:
    def __init__(self, name:str, species:str):
        '''
        param name: pet name
        param species: pet species(such as cat, dog, pig...)
        '''
        self.name = name
        self.species = species.lower()

        if self.species not in pets_personality:
            raise ValueError(f'Unsupported pet\'{self.species}\'. Please choose from: {', '.join(pets_personality.keys())}')
        self.personality = pets_personality[self.species]
        
        self.mood_log = [] # mood record
        self.emoji = species_emoji[self.species]
    
    def react_to_user_mood(self, user_mood: str) -> str:
        '''
        Based on the mood input by the user and the pet's personality,
        return the response content
        '''
        mood_key = user_mood.lower()
        score = mood_to_score(user_mood)
        base_response = score_based_response(score)
        personality_adjusted = self._personality_react(base_response)

        #log record
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.mood_log.append((timestamp, user_mood))

        return f'{self.emoji}{self.name} : {personality_adjusted}'


    def recommend_activity(self) -> str:
        '''
        According the personality to recommend an activity
        '''

        activities = personality_activities.get(self.personality, ['Lucky Number'])
        suggestion = random.choice(activities)
        message = f'\n{self.emoji}{self.name} : I thinks you should try {suggestion} 🎮\n'
        return suggestion, message

        
    def _personality_react(self, base:str) -> str:
        '''
        According personality to adjuset the response text
        '''
        if self.personality == "cheerful":
            return base + " Let's have a great day!🌹"
        elif self.personality == "lazy":
            return base + " ...but maybe after a nap. 😴"
        elif self.personality == "funny":
            return base + " Hope my laughter can infect you(hahahahhahaha)"
        elif self.personality == "proud":
            return base.upper()
        elif self.personality == "sneaky":
            return base + " Hehe... I might know a trick or two.😁"
        else:
            return base

    def get_mood_log(self) -> list:
        return self.mood_log






