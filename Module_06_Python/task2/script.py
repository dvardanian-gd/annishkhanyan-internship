"""
Full script for creating a SurveyMonkey survey from a JSON file
and adding recipients from a text file.
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


def load_recipients(path):
    """Load email addresses from a text file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            recipients = [line.strip() for line in f if line.strip()]
    except OSError as err:
        print(f"Error loading recipients file: {err}")
        sys.exit(1)

    if len(recipients) < 2:
        print("Error: At least 2 recipients required.")
        sys.exit(1)

    return recipients


def extract_survey_name(data):
    """Extract top-level survey name."""
    if not data:
        print("Error: JSON is empty")
        sys.exit(1)
    return list(data.keys())[0]

def create_survey(name):
    """Create a new survey in SurveyMonkey and return its id."""
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

    return response.json().get("id")


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

    return response.json().get("id")


def create_question(survey_id, page_id, question_name, question_data):
    """Create a single-choice question."""
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

    return response.json().get("id")


def create_collector(survey_id):
    """Create an email collector to send the survey."""
    url = f"{API_BASE}/surveys/{survey_id}/collectors"
    headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
    payload = {"type": "email"}

    response = requests.post(url, headers=headers, json=payload, timeout=10)
    if response.status_code not in (200, 201):
        print("Failed to create collector")
        print("Status:", response.status_code)
        print("Response:", response.text)
        sys.exit(1)

    return response.json().get("id")


def add_recipient(collector_id, email):
    """Add a single recipient to a collector."""
    url = f"{API_BASE}/collectors/{collector_id}/recipients"
    headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
    payload = {"email": email}

    response = requests.post(url, headers=headers, json=payload, timeout=10)
    if response.status_code not in (200, 201):
        print(f"Failed to add recipient: {email}")
        print("Status:", response.status_code)
        print("Response:", response.text)
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <questions.json> <emails.txt>")
        sys.exit(1)

    json_path = sys.argv[1]
    email_path = sys.argv[2]

    data = load_questions_json(json_path)
    recipients = load_recipients(email_path)

    survey_name = extract_survey_name(data)
    questions_dict = list(data[survey_name].values())[0]

    if len(questions_dict) < 3:
        print("Error: JSON must contain at least 3 questions.")
        sys.exit(1)

    survey_id = create_survey(survey_name)
    print(f"Survey '{survey_name}' created. ID: {survey_id}")

    page_name = list(data[survey_name].keys())[0]
    page_id = create_page(survey_id, page_name)
    print(f"Page '{page_name}' created. ID: {page_id}")

    for question_name, q_data in questions_dict.items():
        q_id = create_question(survey_id, page_id, question_name, q_data)
        print(f"Question '{question_name}' created. ID: {q_id}")

    collector_id = create_collector(survey_id)
    print(f"Collector created. ID: {collector_id}")

    for email in recipients:
        add_recipient(collector_id, email)
        print(f"Recipient added: {email}")

    print("Survey setup complete!")


if __name__ == "__main__":
    main()
