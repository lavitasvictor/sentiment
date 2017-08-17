from flask import Flask, render_template, session, request, url_for, redirect
import random, os

app = Flask(__name__)
app.secret_key = os.urandom(48)

@app.route('/', methods = ['GET', 'POST'])
def form():
    guess = random.randrange(1,6)
    if request.method == 'POST':
        session['your_answer'] = request.form['your_answer']
        session['guess']=guess

        check = lambda x,y: 10 if x==y else -1
        if 'points' not in session:
            session['points']=check(int(session['your_answer']), guess)
        else:
            session['points'] += check(int(session['your_answer']), guess)

        if "computer_number_log" not in session:
            session['computer_number_log']=str(guess)
        else:
            session['computer_number_log']+=", "+str(guess)
        if "your_number_log" not in session:
            session["your_number_log"] = session["your_answer"]
        else:
            session["your_number_log"]+=", "+session["your_answer"]
        return redirect(url_for('answer'))
        
    return render_template('form.html')

@app.route('/answer')
def answer():
    if session:
        return render_template("answer.html", number_log = session["computer_number_log"], points=session["points"],check_it = int(session["your_answer"]) == session["guess"], guess= session['guess'], your_number_log=session["your_number_log"])
    else:
        return render_template('answer.html', number_log = None, points= None,check_it = False, guess = None, your_number_log=None)
        
@app.route('/null')
def null_the_score():
    session['points']=0
    session['number_log']="0"
    return render_template('form.html')


app.run(debug = True, host = '0.0.0.0', port = 8080)

