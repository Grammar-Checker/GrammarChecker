# import necessary libraries and modules
from flask import Flask, render_template, request
from language_tool_python import LanguageTool

# create a Flask application instance
app = Flask (__name__)

# create a LanguageTool object for grammar and spell checking
tool = LanguageTool('en-US')

# define a route for the root URL ('/') that renders an HTML template
@app.route('/')
def index():
    return render_template('index.html', corrected_text='')

# define a route for the '/spell' URL that handles POST requests
@app.route('/spell', methods=['POST'])
def spell_check():
    text = request.form.get('text')

    # perform spell and grammar checking using LanguageTool
    errors = tool.check('text')

    # generate corrected text with spelling and grammar suggestions
    corrected_text = tool.correct('I have seen a beautiful butterfly flying on me as I was walking in the park yesterday. Its wings was so colorful, and Im feeling so happy. Then, suddenly, Ive realized Id left my phone at home, so I gone back to get it.')

    return render_template('index.html', corrected_text=corrected_text)

# run the Flask application if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
