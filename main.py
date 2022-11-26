import requests
#alizhan
#saken
#aidynlox
from flask import Flask, render_template, request, url_for, flash, redirect


'''email = input("Please enter your email: ")
email = email.strip()
email = email.lower()
import requests
response = ["https://2ip.ru/?area=ajaxHaveIBeenPwned&query=", "https://api.snusbase.com/combo/antipublic/"]
response[0] = requests.get(f"{response[0]}"f"{email}")
print(response[0])


'''

import json


app = Flask(__name__)
app.config['SECRET_KEY'] = '7b09add526e0f9d38f575bca8c20a1fac116122d136b3d5d'
messages = []

@app.route("/mail")
def hello():
    return "Hello World!"

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

#
@app.route('/create/', methods=('GET', 'POST'))
def create():
    response = []
    messages.clear()
    if request.method == 'POST':
        content = request.form['content']
        content = content.strip()
        emaill = request.form['content']
        response.append(requests.get(f'https://2ip.ru/?area=ajaxHaveIBeenPwned&query={content}'))
        response.append(requests.get(f'https://api.snusbase.com/combo/antipublic/{content}'))
        if not content:
            flash('Content is required!')
        else:
            messages.clear()
            for x in response:
                parsed = x.json()
                content = parsed
                messages.append({'title': emaill, 'content': content})
            response.clear()
            return redirect(url_for('index'))

    return render_template('create.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)







'''import json
dict1={}

json_object = json.dumps(response, indent=4)


out_file = open("myfile.json", "w")
json.dumps(response, out_file, indent=2)'''