"""
Script for creating a SurveyMonkey survey from a JSON file.
"""

import sys
import json
import requests
from dotenv import load_dotenv
import os

API_BASE = "https://api.surveymonkey.com/v3"

load_dotenv()
TOKEN = os.getenv("ACCESS_TOKEN")


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

    return list(data.keys())[0]


def create_survey(name):
    """
    Create a new survey in SurveyMonkey and return its ID.
    """
    if not TOKEN:
        print("ERROR: ACCESS_TOKEN is missing. Add it to your .env file.")
        sys.exit(1)

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

    # Return the survey ID from the response
    return response.json().get("id")


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

    survey_id = create_survey(survey_name)

    print(f"Survey '{survey_name}' was created successfully!")
    print(f"Survey ID: {survey_id}")


if __name__ == "__main__":
    main()