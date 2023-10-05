#!/bin/zsh

# Change to the project root (provided)
script_dir=$(dirname "$0")
cd "$script_dir/.."

# Run the summary_statistics.py script with the provided URI
poetry run pipelines/summary_statistics.py --uri "$2"

# Check if the script was successful
if [ $? -eq 0 ]; then
    # If successful, add changes, commit, and push to Git
    git add .
    git commit -m 'Updated summary statistics'
    git push
else
    echo "Script failed. Check the error message for details."
fi
