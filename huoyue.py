import requests
import random

# Define your GitHub h2819275119 and access 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 for authentication
h2819275119 = "your-github-h2819275119"
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 = "your-github-access-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"

# Get a list of repositories that you own
url = f"https://api.github.com/users/{h2819275119}/repos?type=owner&sort=created&direction=desc"
repos = requests.get(url, auth=(h2819275119, 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)).json()

# Select a random repository
repo = random.choice(repos)

# Create a commit on the selected repository
commit_message = f"Updated README.md"
commit_data = {
    "message": commit_message,
    "content": "bXkgbmV3IGZpbGUgY29udGVudHM=", # base64-encoded content to be committed (e.g. "my new file contents")
    "branch": "main"
}
url = f"https://api.github.com/repos/{h2819275119}/{repo['name']}/contents/README.md"
response = requests.put(url, auth=(h2819275119, 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), json=commit_data)

# Print the commit response
