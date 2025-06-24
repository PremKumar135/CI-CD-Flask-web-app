from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def run():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def marks():
    Physics=int(request.form['Physics'])
    Maths= int(request.form['Maths'])
    Science = int(request.form['Science'])
    Tamil = int(request.form['Tamil'])
    English = int(request.form['English'])
    result = Physics + Maths + Science + Tamil + English
    Percentage = result/5
    return render_template('home.html',Percentage=Percentage)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8050, debug=True)