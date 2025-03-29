import random
import datetime
import os

def generate_commits():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = "activity_log.txt"
    num_commits = random.randint(1, 5)
    
    # Ensure the file exists initially
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write(f"Initial commit - {current_date}\n")
        os.system("git add .")
        os.system('git commit -m "Initial commit"')
    
    for i in range(num_commits):
        messages = [
            "Updated activity log",
            "Daily progress update",
            "Added new entry",
            "Modified log entry",
            "Routine update"
        ]
        commit_message = f"{random.choice(messages)} - {current_date} #{i+1}"
        
        with open(filename, "a") as f:
            f.write(f"{commit_message}\n")
        
        # Add debugging output
        print(f"Committing: {commit_message}")
        
        os.system("git add .")
        os.system(f'git commit -m "{commit_message}"')

if __name__ == "__main__":
    generate_commits()
