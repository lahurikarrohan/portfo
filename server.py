
from flask import Flask, render_template, request, url_for, redirect
import csv
import datetime
app = Flask(__name__)
today = datetime.date.today()
someday = datetime.date(2018, 12, 17)
diff =  today - someday 
exp_days=diff.days
exp_years=round(exp_days/365,2)

@app.route('/')
def hello_world(username = None):
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name,exp_years=exp_years)


def write_to_file(data):
	with open('database.txt', mode='a') as database:
		#print(my_file)
		email =data["email"]
		subject =data["subject"]
		message =data["message"]
		file = database.write(f'\n{email}\n{subject}\n{message}\n\n')
		
def write_to_csv(data):
	with open('database.csv', mode='a') as database2:
		#print(my_file)
		email =data["email"]
		subject =data["subject"]
		message =data["message"]
		csv_writer = csv.writer(database2, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])		


@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
	if request.method =='POST':
		data = request.form.to_dict()
		print(data)
		write_to_csv(data)
		return redirect('/thankyou.html')
	else:
		return 'Something went wrong'



