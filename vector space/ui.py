import cos_sim_calc
from flask import Flask, redirect, url_for, request
import main


app = Flask(__name__)


@app.route('/success/<query>')
def success(query):
    if query == 'Error Empty query':
        return "<h1>Error Empty query<h1>"
    cos_sim = "Cos sim : "
    main.create_files(10,'files')
    result = dict(sorted(cos_sim_calc.calc_result(query,main.get_file_names()).items(),key=lambda x:x[1], reverse=True))
    # print(main.get_file_names())
    for i in result:
        cos_sim +="<br>"+ i + " : " + str(result[i]) + "\n"
    
    # print(result[1])
    return "<h1>{0}<h1>".format(cos_sim)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        query = request.form['query']
        return redirect(url_for('success', query=query))
    elif request.method == 'GET':
        with open("home.html") as file:
            return file.read()


app.debug = True
app.run()
