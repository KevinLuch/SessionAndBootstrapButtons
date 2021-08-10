from flask import Flask, render_template, request, session, redirect 

app = Flask(__name__)
app.secret_key = 'yeezy yeezy yeezy'

@app.route('/')
def index():

    if 'counter_1' not in session:
        session['counter_1'] = 0
    if 'counter_2' not in session:
        session['counter_2'] = 0
    if 'counter_3' not in session:
        session['counter_3'] = 0

    return render_template('index.html')

@app.route('/counter/<counter_id>')
def increment_counter(counter_id):

    session[f'counter_{counter_id}'] += 1

    return redirect('/')

@app.route('/reset_counters')
def reset_counter():
    session.clear()
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)