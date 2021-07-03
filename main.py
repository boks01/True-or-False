import requests
import html
from checking import Checking

response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()
data = response.json()
question_data = data['results']
question_bank = [html.unescape(question["question"]) for question in question_data]
answer_bank = [question["correct_answer"] for question in question_data]
testing = Checking(question_bank, answer_bank)
question = testing.give_question()