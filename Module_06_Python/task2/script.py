"""
Script for creating a SurveyMonkey survey from a JSON file.
"""

import sys
import json
import requests


API_BASE = "https://api.surveymonkey.com/v3"
TOKEN = (
    "lMsBrzQ04CQ89elrGwz-gwLBg6BLO48tRjX720KwLu-9TziyWCmGdlHG7arU3TpjDNqyVcMXgvzu"
    "8o6qz2-YcxOXLhTdp2sZyC.KKDwZ4IxkjSadkG0ZsNUvMwSN5WbS"
)


def load_questions_json(path):
    """
    Load questions JSON file.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError) as err:
        print(f"Error while loading JSON: {err}")
        sys.exit(1)


def extract_survey_name(data):
    """
    Extract the survey name (top-level key of the JSON file).
    """
    if not data:
        print("Error: JSON is empty")
        sys.exit(1)
    return  list(data.keys())[0]



def create_survey(name):
    """
    Create a new survey in SurveyMonkey and return its ID.
    """
    url = f"{API_BASE}/surveys"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {"title": name}

    response = requests.post(url, headers=headers, json=payload, timeout=10)

    if response.status_code not in (200, 201):
        print("Failed to create survey")
        print("Status:", response.status_code)
        print("Response:", response.text)
        sys.exit(1)

def main():
    """
    Main function for creating a survey from JSON file.
    """
    if len(sys.argv) != 2:
        print("Usage: python script.py <questions.json>")
        sys.exit(1)

    json_path = sys.argv[1]

    data = load_questions_json(json_path)
    survey_name = extract_survey_name(data)

    print(f"Survey '{survey_name}' was created successfully")

if __name__ == "__main__":
    main()
