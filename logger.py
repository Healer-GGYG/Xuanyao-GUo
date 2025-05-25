import csv
import os
from datetime import datetime

log_file = 'mood_log.csv'

def create_log_file():
    '''
    Create log file and write the title line (if the file does not exist)
    If the file not exist
    - create file
    - newline='': Prevent extra blank lines when writing to CSV
    - encoding='utf-8' : UTF-8 encoding is used, supporting Chinese characters and special characters
    - 
    '''
    if not os.path.exists(log_file): # If can't find the file
        with open(log_file, 'w', newline = '', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['timestamp', 'user_id','user_mood','mood_score'])
            

def log_mood(pet_name, pet,user_mood, mood_score):
    '''
    write a complete log
    '''
    create_log_file()
    #Combine the name of the current user with the type of pet to form a unique user ID
    user_id = f'{pet_name}||{pet}'
    today_str = datetime.now().strftime('%Y-%m-%d') # get today's date

    logs = read_logs() # return a dictionary
    updated_logs = [] # Used to temporarily store the records that will eventually be saved back (including old and new ones)
    has_today_record = False # initialize

    '''
    When traversing the log, if a record with the same username appears, 
    it indicates that this message was recorded today. 
    Then modify whether today is recorded as true. 
    If they are different, they will be stored in the temporary update_log.
    '''
    for row in logs:
        if row['user_id'] == user_id and row['timestamp'].startswith(today_str):
            has_today_record = True

        else:
            updated_logs.append(row)

    # When recording repeatedly, you can ask the user whether to overwrite the record    
    if has_today_record:
        choice = input('\nYou have already logged your mood today. Do you want to overwrite it? (y/n):').strip().lower()
        if choice != 'y':
            print('\n❌ No changes made to today\'s log.')
            return
    
    # Add a New Record (Overwrite first, then write)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    updated_logs.append({
        "timestamp": timestamp,
        "user_id": user_id,
        "user_mood": user_mood,
        "mood_score": str(mood_score),
    })

    # Rewrite the entire file
    with open(log_file,'w') as f:
        writer = csv.DictWriter(f, fieldnames=['timestamp', 'user_id', 'user_mood', 'mood_score'])
        writer.writeheader()
        for row in updated_logs:
            writer.writerow(row)
    
    print('\n✅ Today\'s mood has been recorded.')

            
def read_logs():
    '''
    return list of all user daata
    '''
    if not os.path.exists(log_file):
        return[]
    
    logs = []
    with open(log_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            logs.append(row)
        
    return logs

def read_logs_by_user(pet_name, pet_species):
    '''
    return a list of data with same user_id
    '''
    user_id = f'{pet_name}||{pet_species}'
    user_logs = []

    for row in read_logs():
        if row['user_id'] == user_id:
            user_logs.append(row)
    return user_logs








    
