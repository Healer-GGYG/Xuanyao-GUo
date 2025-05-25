import random

def guess_the_number(pet_name,pet_emoji):
    print(f'\n{pet_emoji}{pet_name} : 🎲 Welcome to \'Guess the Number\'!')
    number = random.randint(1,100)
    attempts = 0

    while True:
        try:
            guess = input('Enter your guess(1-100)/q: ')
            if guess == 'q':
                return 0
            guess = int(guess)
            attempts += 1
            if guess < 1 or guess > 100:
                print(f'{pet_emoji}{pet_name} : Please enter a number between 1 and 100.')
            elif guess < number:
                print(f'{pet_emoji}{pet_name} : Too low! Try again.')
            elif guess > number:
                print(f'{pet_emoji}{pet_name} : Too high! Try again.')
            else:
                print(f'{pet_emoji}{pet_name} : 🎉 Correct! You guessed it in {attempts} attempts.')
                return +2 # Guessing correctly can boost your emotional value

        except ValueError:
            print(f'{pet_emoji}{pet_name} : Invalid input. Please enter a number')


def funny_quiz(pet_name,pet_emoji):
    print(f'\n{pet_emoji}{pet_name} : 🧠 Welcome to the Funny Quiz')

    quiz_pool = [
     {
            "question": "What do you call fake spaghetti?",
            "options": ["An impasta", "A spaghetti lie", "Noodle nonsense"],
            "answer": 1,
            "explanation": "It's a pun! 'Impasta' sounds like 'imposter' - fake pasta!"
        },
        {
            "question": "Why can\'t your nose be 12 inches long?",
            "options": ["It won't fit your face", "Because it would be a foot!",  "Too many nostrils"],
            "answer": 2,
            "explanation": "Because 12 inches = 1 foot. It's a wordplay joke!"
        },
        {
            "question": "What do you call cheese that isn\'t yours?",
            "options": [ "Stolen brie", "Illegal cheddar","Nacho cheese"],
            "answer": 3,
            "explanation": "It's a joke: 'Nacho cheese' = 'Not your cheese' 😂"
        },
        {
            "question": "Why did the bicycle fall over?",
            "options": ["It was two-tired", "It lost a wheel", "It crashed"],
            "answer": 1,
            "explanation": "'Two-tired' sounds like 'too tired' - classic pun!"
        },
        {
            "question": "What kind of tree fits in your hand?",
            "options": [ "A finger oak","A palm tree", "A mini maple"],
            "answer": 2,
            "explanation": "A palm fits in your hand - and 'palm tree' is the pun!"
        }   
    ]

    quiz = random.choice(quiz_pool)
    print(quiz['question'])
    for i in range(len(quiz['options'])):
        print(str(i+1) + '.'+ quiz['options'][i])
    
    try:
        choice = int(input('Your anser (1-3): '))
        if choice == quiz['answer']:
            print(f'{pet_emoji}{pet_name} : 😂 Correct! Nice one!')
            print(f'{pet_emoji}{pet_name} : 💡 Explanation:', quiz['explanation'])
            return +1
        
        else:
            print(f'{pet_emoji}{pet_name} : 😅 Oops! Not quite.')
            print(f'{pet_emoji}{pet_name} : ✅ Correct Answer: {quiz['options'][quiz['answer'] - 1]}')
            print(f'{pet_emoji}{pet_name} : 💡 Explanation:', quiz['explanation'])
            return 0
        
    except:
        print(f'{pet_emoji}{pet_name} : Invalid input! We\'ll move on for now.')
        return 0


def lucky_number(pet_name,pet_emoji):
    number = random.randint(1,100)
    print(f'\n{pet_emoji}{pet_name} : 🔢 Your lucky number today is: {number}')
    return +1
    

def lucky_colour(pet_name,pet_emoji):
    colours = ['red','blue','green','yellow','purple','orange','pink']
    colour = random.choice(colours)
    print(f'\n{pet_emoji}{pet_name} : 🎨 Your lucky colour today is: {colour.capitalize()}')
    return +1

def load_emotion_words(file_path):
    with open(file_path,'r') as f:
        return set(line.strip().lower() for line in f)

def emotional_word_chain(pet_name:str,pet_emoji):
    print(f'\n{pet_emoji}{pet_name} :🔗 Let\'s play an emotional word chain!')
    positive_words = [
        'joy', 'hope', 'smile', 'peace', 'love', 'fun', 'energy',
        'courage', 'calm', 'trust', 'kindness', 'comfort', 'confidence',
        'gratitude', 'harmony', 'delight', 'warmth', 'cheer'
    ]

    all_used_words = set()

    while True:
        user_input = input('You(Emotional word | I don\'t konw anymore)').strip().lower()

        # stop game
        if user_input == 'I don\'t konw anymore'.lower():
            print('{pet_emoji}{pet_name} :🌈 That\'s okay! Thanks for playing.')
            break

        # whether repeat?
        if user_input in all_used_words:
            print(f'{pet_emoji}{pet_name} : We\'ve already mentioned this word. Let\'s change it to another one')
            continue
        
        # add the user_input words
        all_used_words.add(user_input)

        # Indicate whether it is an emotional word
        emotion_words = load_emotion_words('emotion_words.txt')

        if user_input not in emotion_words:
            print(f'{pet_emoji}{pet_name} : Hmm... I don\'t recognize that word, but alright!')
        
        available = [w for w in positive_words if w not in all_used_words]
        if not available:
            prinr('{pet_emoji}{pet_name} :🧠 I\'ve run out of words... You did great!')
            break

        next_word = random.choice(available)
        all_used_words.add(next_word)
        print(f'{pet_emoji}{pet_name}:{next_word}')

    return +1









