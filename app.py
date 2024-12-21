from flask import Flask, render_template, jsonify

app = Flask(__name__)

# List of questions, each with four options and the correct option index
questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['Berlin', 'Madrid', 'Paris', 'Rome'],
        'answer': 2  # Correct answer index (0-based)
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
        'answer': 1
    },
    {
        'question': 'Who wrote "Hamlet"?',
        'options': ['Shakespeare', 'Dickens', 'Austen', 'Hemingway'],
        'answer': 0
    }
]

# Index of the current question
question_index = 0

@app.route('/')
def index():
    global question_index
    question = questions[question_index]
    return render_template('index.html', question=question)

@app.route('/next', methods=['POST'])
def next_question():
    global question_index
    # Check if it's the last question, then reset to 0
    if question_index < len(questions) - 1:
        question_index += 1
    else:
        question_index = 0  # Reset to the first question
    return jsonify({'question': questions[question_index]})

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)

