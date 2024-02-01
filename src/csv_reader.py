import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Pokemon dataset
url = "../data/Pokemon.csv"
pokemon_data = pd.read_csv(url)

# Display the first few rows of the dataset
#print(pokemon_data.head())


# Plot the amount of Pokemon for each type
def amount_type():
    # Combine 'Type 1' and 'Type 2' columns into a new DataFrame. Melt will account for duplicates.
    types_df = pd.melt(pokemon_data[['Type 1', 'Type 2']], value_vars=['Type 1', 'Type 2'], var_name='Type')
    plt.figure(figsize=(12, 6))
    sns.countplot(x='value', data=types_df, order=types_df['value'].value_counts().index, palette='viridis')
    plt.title('Number of Pokemon for Each Type (including Type 2)')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.show()
    return None


# Plot the count of Pokemon sharing stats like HP, or the total
def share_stat_total(stat):
    plt.figure(figsize=(12, 6))
    sns.countplot(x=stat, data=pokemon_data, palette='coolwarm')
    plt.title('Count of Pokemon Sharing Base Stat Totals')
    sns.histplot(x=stat, data=pokemon_data, bins=738, kde=True, color='skyblue')
    plt.title('Distribution of stat: ' + stat)
    plt.xlabel('Stat: ' + stat)
    plt.ylabel('Count')
    plt.show()
    return None


# Display a list of Pokemon in descending order of any attribute, like base stat total
def create_pokemon_list(attribute, generation = None, legendary = None):
    sorted_pokemon = pokemon_data[['Name', attribute]].sort_values(by=attribute, ascending=False)
    print(sorted_pokemon[['Name', attribute]])
    # Save the sorted Pokemon data to a text file (CSV)
    sorted_pokemon.to_csv('../results/sorted_pokemon_data.txt', index=False, sep='\t')  # '\t' for tab-separated values
