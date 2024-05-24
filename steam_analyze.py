import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the CSV file
df = pd.read_csv("Sprint 2/steam-200k.csv", header=None, names=['user-id', 'game-title', 'behavior', 'value', '0'])

# Filter for purchase behavior
purchase_df = df[df['behavior'] == 'purchase']

def q_1():
    # Display the first few rows to verify the headers
    # print(df.head())

    # Count the number of purchases for each game
    purchase_counts = purchase_df['game-title'].value_counts().reset_index()
    purchase_counts.columns = ['game-title', 'purchase-count']

    # Filter for play behavior
    play_df = df[df['behavior'] == 'play']

    # Sum the playtime for each game
    play_time = play_df.groupby('game-title')['value'].sum().reset_index()
    play_time.columns = ['game-title', 'total-playtime']

    # Merge purchase counts and playtime
    popularity_df = pd.merge(purchase_counts, play_time, on='game-title', how='outer').fillna(0)

    # Sort by purchase counts and total playtime
    popular_by_purchase = popularity_df.sort_values(by='purchase-count', ascending=False)
    popular_by_playtime = popularity_df.sort_values(by='total-playtime', ascending=False)

    # Print the top 10 most purchased games
    print("Top 10 Most Purchased Games:")
    print(popular_by_purchase.head(10).to_string(index=False))

    # Plotting the top 10 most purchased games using pandas
    top_10_purchase = popular_by_purchase.head(10)
    # Create a bar plot for the top 10 most purchased games
    ax1 = top_10_purchase.plot(kind='bar', x='game-title', y='purchase-count', legend=False, color='skyblue', figsize=(10, 5))
    # Set the title of the plot
    ax1.set_title('Top 10 Most Purchased Games')
    # Set the label for the x-axis
    ax1.set_xlabel('Game Title')
    # Set the label for the y-axis
    ax1.set_ylabel('Purchase Count')
    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')
    # Adjust layout to ensure everything fits without overlapping
    plt.tight_layout()
    # Display the plot
    plt.show()

    # Print the top 10 most played games (by total playtime)
    print("\nTop 10 Most Played Games (by total playtime):")
    print(popular_by_playtime.head(10).to_string(index=False))

    # Plotting the top 10 most played games using pandas
    top_10_playtime = popular_by_playtime.head(10)
    # Create a bar plot for the top 10 most played games
    ax2 = top_10_playtime.plot(kind='bar', x='game-title', y='total-playtime', legend=False, color='lightgreen', figsize=(10, 5))
    # Set the title of the plot
    ax2.set_title('Top 10 Most Played Games (by Total Playtime)')
    # Set the label for the x-axis
    ax2.set_xlabel('Game Title')
    # Set the label for the y-axis
    ax2.set_ylabel('Total Playtime')
    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')
    # Adjust layout to ensure everything fits without overlapping
    plt.tight_layout()
    # Display the plot
    plt.show()

    return

def q_2():
    # Filter for play behavior
    play_df = df[df['behavior'] == 'play']

    # Group by game-title and user-id to get total playtime per user for each game
    user_playtime = play_df.groupby(['game-title', 'user-id'])['value'].sum().reset_index()

    # Calculate the average playtime per user for each game
    avg_playtime = user_playtime.groupby('game-title')['value'].mean().reset_index()
    avg_playtime.columns = ['game-title', 'average-playtime-per-user']

    # Sort by average playtime per user
    avg_playtime_sorted = avg_playtime.sort_values(by='average-playtime-per-user', ascending=False)

    # Print the top 10 games by average playtime per user
    print("\nTop 10 Games by Average Playtime per User:")
    print(avg_playtime_sorted.head(10).to_string(index=False))

    # Plotting the top 10 games by average playtime per user using pandas
    top_10_avg_playtime = avg_playtime_sorted.head(10)
    # Create a bar plot for the top 10 games by average playtime per user
    ax3 = top_10_avg_playtime.plot(kind='bar', x='game-title', y='average-playtime-per-user', legend=False, color='coral', figsize=(10, 5))
    # Set the title of the plot
    ax3.set_title('Top 10 Games by Average Playtime per User')
    # Set the label for the x-axis
    ax3.set_xlabel('Game Title')
    # Set the label for the y-axis
    ax3.set_ylabel('Average Playtime per User')
    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')
    # Adjust layout to ensure everything fits without overlapping
    plt.tight_layout()
    # Display the plot
    plt.show()

    return

# Introduction and user input section
print("This program uses pandas and matplotlib to answer two questions about a csv dataset.")
print("The data was collected from the game engine 'Steam' and had columns for games, playtime,")
print("and purchases. The two questions I wanted answered about the dataset were 1) What are the")
print("most popular games based on the number of purchases and playtime? and 2) What are the")
print("average playtimes per user for each game?")

# Ask the user which question they want answered
answer = input("Would you like the answer to question 1 or 2? ")
if answer == "1":
    q_1()
elif answer == "2":
    q_2()
else:
    print("Please enter either a 1 or a 2.")
