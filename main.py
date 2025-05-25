from pet import Pet
from emotion import mood_to_score,score_to_mood
from activity import guess_the_number,funny_quiz, lucky_number,lucky_colour,emotional_word_chain
from logger import log_mood
from mood_visualizer import plot_mood_bar_chart
import random

random.seed()

def selected_activity(pet_name,activity_name,pet_emoji):
    if activity_name == 'Guess the Number':
        return guess_the_number(pet_name,pet_emoji)
    elif activity_name == 'Funny Quiz':
        return funny_quiz(pet_name,pet_emoji)
    elif activity_name == 'Lucky Number':
        return lucky_number(pet_name,pet_emoji)
    elif activity_name == 'Lucky Colour':
        return lucky_colour(pet_name,pet_emoji)
    elif activity_name =='Emotional Word Chain':
        return emotional_word_chain(pet_name,pet_emoji)
    else:
        print('\nUnkonwn activity')
        return 0

def main():
    print('\n🎉 Welcome to Mood Pet!')

    while True:
        start_game = input('\nDo you want to play Mood Pet today? (y/n): ').strip().lower()
        if start_game == 'n':
            print('\nOkay! See you next time 👋')
            return
        elif start_game == 'y':
            break
        else:
            print('\nPlease enter y/n')

    # 1. user choose Pet    
    print('\nChoose your pet^_^:')
    print('1. Cat🐱\n2. Dog🐶\n3. Pig🐷\n4. Dragon🐲\n5. Fox🦊')
    pet_map = {
        '1': 'Cat',
        '2': 'Dog',
        '3': 'Pig',
        '4': 'Dragon',
        '5': 'Fox'
    }
    while True:
        choice = input('\nEnter number (1-5): ')
        if choice in pet_map.keys():
            break
    user_pet = pet_map[choice]
    while True:
        pet_name = input('\nWhat would you like to name your pet?')
        if not pet_name :
            print('\nPlease Enter a name.')
            continue
        else:
            break

    pet = Pet(pet_name,user_pet)
    print(f'\n🎉Congratulations on successfully adopting a {pet.emoji} named {pet.name}')
    


    # 2. Users input theri moods
    user_mood = input(f'\n{pet.emoji}{pet.name} :How are you feeling today? \n\nhappy,excited,relaxed,neutral,\nbored,tired,sad,stressed,\nangry,anxious,frustrated,lonely\n').strip().lower()
    mood_score = mood_to_score(user_mood)

    # 3. Pet response
    response = pet.react_to_user_mood(user_mood)
    print('\n' + response)


    # 4. Pet recommend game
    total_score = 0
    mood_change = 0
    while True:
        activity_name, recommendation_message = pet.recommend_activity()

        print(f'\n{recommendation_message}')
        print(f'{pet.emoji}{pet.name} :What would you like to do?')
        print('1. Play this game.🎮')
        print('2. Change another game.🔁')
        print('3. I won\'t play games today.💔')

        user_choice = input('Enter Your Choice(1/2/3): ').strip()

        if user_choice == '3':
            print(f'\n{pet.emoji}{pet.name} : Hope to see you again soon! 😊')
            mood_change = max(0, mood_change)
            total_score = max(mood_score, total_score)
            print(f'\n Mood score today (base{mood_score} + activity{mood_change}) = {total_score}')
            print(f'📝 Interpreted mood: {score_to_mood(total_score)}')
            break
        elif user_choice == '2':
            print('\n{pet.emoji}{pet.name} : 🔁 Choosing another activity...\n')
            continue
        elif user_choice == '1':
            # 5. play game
            mood_change = selected_activity(pet.name, activity_name,pet.emoji)

            # 6. update the mood score
            total_score = max(total_score, mood_score)
            total_score += mood_change
            print(f'\n Mood score today (base{mood_score} + activity{mood_change}) = {total_score}')
            print(f'📝 Interpreted mood: {score_to_mood(total_score)}')
            

            # Ask if you want to play another activity
            again = input('\nDo you want to play another activity? (y/n): ').strip().lower()
            if again != 'y':
                print(f'\n{pet.emoji}{pet.name} : Have a wonderful day! 😊')
                break
        else:
            print(f'\n{pet.emoji}{pet.name} : ❌ Invalid input. Please choose 1, 2 or 3.')

    # Record log    
    log_mood(pet.name,pet.species, user_mood,total_score)
    # 8. mood visualizer
    print('\nWould you like to view your mood trend?')
    print('1. Last 7 days\n2. Last 14 days\n3. Last 21 days\n4. Last 30 days\n5. No thanks')
    trend_choice = input('\nEnter your choice: ')
    trend_map = {
        '1' : 'last 7',
        '2' : 'last 14',
        '3' : 'last 21',
        '4' : 'last 30'
    }

    if trend_choice in trend_map:
        plot_mood_bar_chart(pet.name, pet.species, trend_map[trend_choice])


    print('\nsee you next time! 👋')

if __name__ == '__main__':
    main()



