import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load election data from a CSV file."""
    return pd.read_csv(file_path)

def analyze_results(df):
    """Analyze election results and return vote counts, percentages, and winner."""
    total_votes = len(df)
    results = df['Candidate'].value_counts().reset_index()
    results.columns = ['Candidate', 'Votes']
    results['Percentage'] = (results['Votes'] / total_votes) * 100
    winner = results.iloc[0]['Candidate']
    return results, winner

def plot_results(results):
    """Plot the election results."""
    plt.figure(figsize=(8, 5))
    plt.bar(results['Candidate'], results['Votes'], color=['blue', 'red', 'green', 'purple'])
    plt.xlabel("Candidates")
    plt.ylabel("Votes")
    plt.title("Election Results")
    plt.xticks(rotation=45)
    plt.show()

def main():
    file_path = "election_data.csv"  # Change this to your actual file path
    df = load_data(file_path)
    results, winner = analyze_results(df)
    print("Election Results:")
    print(results)
    print(f"Winner: {winner}")
    plot_results(results)

if __name__ == "__main__":
    main()
