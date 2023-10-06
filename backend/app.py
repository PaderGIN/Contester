from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, render_template, request

import subprocess, os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

class CodeForm(FlaskForm):
    code = TextAreaField('Code', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/submit', methods=['POST'])
def submit():
    form = CodeForm()
    result = None
    if form.validate_on_submit():
        code = form.code.data
        result = execute_code(code)
    return render_template('index.html', form=form, result=result)

def execute_code(code):
    try:
        result = subprocess.check_output(['python', '-c', code], stderr=subprocess.STDOUT)
        result = result.decode('utf-8')
    except subprocess.CalledProcessError as e:
        result = e.output.decode('utf-8')
    return result

if __name__ == '__main__':
    app.run(debug=True)