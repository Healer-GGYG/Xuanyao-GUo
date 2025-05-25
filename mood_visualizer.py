import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from logger import read_logs_by_user
from datetime import datetime, timedelta


def plot_mood_bar_chart(pet_name, species, period):
    # loading the data(Log)
    logs = read_logs_by_user(pet_name, species)
    if not logs:
        print("No mood data available.")
        return
    # Determine the time period
    days_map = {
        "last 7": 7,
        "last 14": 14,
        "last 21": 21,
        "last 30": 30
    }

    if period not in days_map:
        print("Invalid period.")
        return

    today = datetime.today().date() # Get today's date
    date_range = [today - timedelta(days=i) for i in reversed(range(days_map[period]))] #This line generates a list of dates, including all the dates from N days ago to today
    date_strs = [d.strftime("%Y-%m-%d") for d in date_range] #Convert the date type to the string format yyyy-mm-dd
    score_map = {d: [] for d in date_strs} # Create a dictionary with the key being the date (string) of each day.

    #Read the log and extract the mood scores whose dates fall within the range
    for row in logs:
        try:
            ts = datetime.strptime(row["timestamp"], "%Y-%m-%d %H:%M:%S") #Parse the timestamp string into a datetime object
            date_str = ts.strftime("%Y-%m-%d") #Extract its date part again and convert it to yyyy-mm-dd
            if date_str in score_map:
                score_map[date_str].append(int(row["mood_score"]))
        except:
            continue

    # Correspond the scores to the dates. If there is no value, return none
    x = date_strs
    y = []
    for d in x:
        if score_map[d]:
            y.append(score_map[d][-1])  
        else:
            y.append(None)


    plt.figure(figsize=(12, 5))
    # bar chart, none-->0(for y),
    bars = plt.bar(x, [s if s is not None else 0 for s in y], color='skyblue')

    #Display the position of the numerical value
    for i, score in enumerate(y):
        if score is None:
            plt.text(i, 0.2, "No data", ha='center', va='bottom', fontsize=8, color='gray')
        else:
            plt.text(i, score + 0.6, str(score), ha='center', va='bottom', fontsize=9)

    plt.title(f"Mood Log - {period.replace('_', ' ').title()}")
    plt.xlabel("Date")
    plt.ylabel("Mood Score")
    plt.xticks(rotation=45) #Rotate the date text on the horizontal coordinate by 45 degrees for better reading
    plt.ylim(-10, 10) #Set the range of the Y-axis from -10 to 10 (emotion score range)

    # Modify the Y-axis scale
    ax = plt.gca() #Obtain the coordinate axes of the current graph (ax = axis）
    ax.yaxis.set_major_locator(MaxNLocator(integer=True)) #Force the Y-axis to display integer scales

    plt.tight_layout() # Automatically adjust the graphic layout to prevent text from overlapping or squeezing out boundaries
    plt.grid(axis='y', linestyle='--', alpha=0.3) # Add a horizontal dotted grid (for convenient alignment of Y values)
    plt.show()

