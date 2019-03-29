from flask import Flask

app = Flask(__name__)


@app.route('/<int:count>/hi/<name>')
def foo(count, name):
    str1 = 'hello'
    for i in range(0, count):
        str1 += '%s ' % name
    return str1


@app.route('/mypath/<float:weight>/<path:goal>')
def bar(goal, weight):
    str2 = 'float=%f, string=%s' % (weight,goal)
    return str2


app.run(port=5552, host='0.0.0.0', debug=True)
