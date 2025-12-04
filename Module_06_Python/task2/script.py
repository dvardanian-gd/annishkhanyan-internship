"""
Full script for creating a SurveyMonkey survey from a JSON file.
"""

import sys
import json
import os
import requests
from dotenv import load_dotenv

API_BASE = "https://api.surveymonkey.com/v3"

load_dotenv()
TOKEN = os.getenv("ACCESS_TOKEN")

def load_questions_json(path):
    """Load the questions JSON file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError) as err:
        print(f"Error while loading JSON: {err}")
        sys.exit(1)


def extract_survey_name(data):
    """Extract survey name."""
    if not data:
        print("Error: JSON is empty")
        sys.exit(1)
    return list(data.keys())[0]


def create_survey(name):
    """Create a new SurveyMonkey survey and return its ID."""
    if not TOKEN:
        print("ERROR: ACCESS_TOKEN is missing. Add it to your .env file.")
        sys.exit(1)

    url = f"{API_BASE}/surveys"
    headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
    payload = {"title": name}

    response = requests.post(url, headers=headers, json=payload, timeout=10)
    if response.status_code not in (200, 201):
        print("Failed to create survey")
        print("Status:", response.status_code)
        print("Response:", response.text)
        sys.exit(1)

    return response.json()["id"]


def create_page(survey_id, page_name):
    """Create a page inside the survey."""
    url = f"{API_BASE}/surveys/{survey_id}/pages"
    headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
    payload = {"title": page_name}

    response = requests.post(url, headers=headers, json=payload, timeout=10)
    if response.status_code not in (200, 201):
        print("Failed to create page")
        print("Status:", response.status_code)
        print("Response:", response.text)
        sys.exit(1)

    return response.json()["id"]


def create_question(survey_id, page_id, question_name, question_data):
    """Create a single-choice question with vertical layout."""
    if "Answers" not in question_data or not question_data["Answers"]:
        print(f"Error: Question '{question_name}' has no Answers list in JSON.")
        sys.exit(1)

    url = f"{API_BASE}/surveys/{survey_id}/pages/{page_id}/questions"
    headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

    payload = {
        "headings": [{"heading": question_name}],
        "family": "single_choice",
        "subtype": "vertical",
        "answers": {
            "choices": [{"text": ans} for ans in question_data["Answers"]]
        },
    }

    response = requests.post(url, headers=headers, json=payload, timeout=10)
    if response.status_code not in (200, 201):
        print(f"Failed to create question: {question_name}")
        print("Status:", response.status_code)
        print("Response:", response.text)
        sys.exit(1)

    return response.json()["id"]


def main():
    """
    Main orchestration of the program
    """
    if len(sys.argv) != 2:
        print("Usage: python script.py <questions.json>")
        sys.exit(1)

    json_path = sys.argv[1]

    # Load questions
    data = load_questions_json(json_path)

    survey_name = extract_survey_name(data)
    page_name = list(data[survey_name].keys())[0]
    questions_dict = data[survey_name][page_name]

    if len(questions_dict) < 3:
        print("Error: JSON must contain at least 3 questions.")
        sys.exit(1)

    # Create survey
    survey_id = create_survey(survey_name)
    print(f"Survey '{survey_name}' created. ID: {survey_id}")

    # Create page
    page_id = create_page(survey_id, page_name)
    print(f"Page '{page_name}' created. ID: {page_id}")

    # Create questions
    for q_name, q_data in questions_dict.items():
        q_id = create_question(survey_id, page_id, q_name, q_data)
        print(f"Question '{q_name}' created. ID: {q_id}")

    print("Survey setup complete!")


if __name__ == "__main__":
    main()
