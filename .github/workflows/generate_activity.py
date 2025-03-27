import random
import datetime
import os

def generate_commits():
    # Get current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Create or update a file
    filename = "activity_log.txt"
    
    # Number of commits for today (random between 1 and 5)
    num_commits = random.randint(1, 5)
    
    for i in range(num_commits):
        # Generate a random message
        messages = [
            "Updated activity log",
            "Daily progress update",
            "Added new entry",
            "Modified log entry",
            "Routine update"
        ]
        commit_message = f"{random.choice(messages)} - {current_date} #{i+1}"
        
        # Write to file
        with open(filename, "a") as f:
            f.write(f"{commit_message}\n")
        
        # Git commands to commit
        os.system("git add .")
        os.system(f'git commit -m "{commit_message}"')

if __name__ == "__main__":
    generate_commits()
