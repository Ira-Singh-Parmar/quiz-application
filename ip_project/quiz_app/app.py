from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import generate_charts

app = Flask(__name__)

# Route for Home Page
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    # Read questions from questions.csv
    questions = pd.read_csv('questions.csv')

    # Convert questions DataFrame to a list of dictionaries
    questions = questions.to_dict(orient='records')

    if request.method == 'POST':
        # Get the name of the user
        user_name = request.form['name']

        # Get the user's answers from the form
        answers = request.form.to_dict()

        # Calculate the score and total number of questions
        score, total_questions = calculate_score(answers)

        # Save the result to CSV (or a database in a real app)
        save_result(user_name, score)

        # Redirect to the result page
        return redirect(url_for('result', score=score, total_questions=total_questions, name=user_name))

    return render_template('quiz.html', questions=questions)


# Route for Result Page
@app.route('/result')
def result():
    score = request.args.get('score')
    name = request.args.get('name')
    total = request.args.get('total_questions')
    return render_template('result.html', score=score, name=name, total=total)

# Route for Performance Analysis Page (Graph)
@app.route('/analysis')
def analysis():
    # Generate the chart
    generate_charts.generate()

    # Render the analysis page with the graph
    return render_template('analysis.html')


def calculate_score(answers):
    # Correct answers should be based on questions in your CSV
    correct_answers = {
        "q1": "8",
        "q2": "all of the above",
        "q3": 'print("Hello World")',
        "q4": "**",
        "q5": "nan",
        "q6": "1variable",  # Invalid name
        "q7": "Returns the number of items in an object",
        "q8": "def",
        "q9": "7",
        "q10": "until"
    }

    score = 0
    total_questions = len(correct_answers)  # Total questions should be 10
    
    for question, correct_answer in correct_answers.items():
        if answers.get(question) == correct_answer:
            score += 1

    return score, total_questions  # Return both score and total questions


# Function to Save Results to CSV
def save_result(user_name, score):
    try:
        # Remove commas from name to avoid CSV format errors
        safe_name = user_name.replace(",", "")
        with open('results.csv', 'a') as f:
            f.write(f"{safe_name},{score}\n")
    except Exception as e:
        print(f"Error saving result: {e}")



if __name__ == '__main__':
    app.run(debug=True)
