mood_score_map = {
    'happy': 4,
    'excited':6,
    'relaxed':2,
    'neutral':0,
    'bored': -1,
    'tired': -2,
    'sad': -3,
    'stressed': -3,
    'angry': -6,
    'anxious':-4,
    'frustrated':-5,
    'lonely':-2
}

def mood_to_score(user_mood: str) ->int:
    '''
    Conver the emotional words input by the user into corresponding.
    if the word is not in the dictionary, return 0(neutral)
    '''
    score = mood_score_map.get(user_mood.strip().lower(),0)

    return score

def score_to_mood(score: int) -> str:
    if score >= 5:
        return 'very happy 😊'

    elif score >= 2:
        return 'happy 🙂'
    
    elif score == 1 :
        return 'slightly positive 😌'
    
    elif score == 0 :
        return 'netural 😐'
    
    elif score >= -2:
        return 'a bit down 😕'

    elif score >= -5:
        return 'sad 😢'

    else:
        return 'very upset 😭'








