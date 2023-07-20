from flask import Flask, render_template, url_for, request,redirect
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')
  #  print(url_for('static', filename='nature.ico'))

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"] 
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv',newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"] 
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
  if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to the database'
  else:
    return 'something went wrong. Try again!'

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/works.html')
# def work():
#     return render_template('works.html')

# @app.route('/blog')
# def blog():
#     return 'these are my thoughts'

# @app.route('/blog/2022/mydogs')
# def blog2():
#     return 'these are my dogs'