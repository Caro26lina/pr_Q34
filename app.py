from flask import Flask, request, render_template_string
app=Flask(__name__)
tasks=[]
@app.route('/')
def home():
    html= """
        <h2>TO-DO List</h2>
        <form method='post' action='/add'>
            <input type="text" name="task" placeholder="Enter A task"> <br>
            <button type="submit">Add</button>
        </form>
        <ul>
            {% for t in task%}
                <li>{{t}}</li>
            {%endfor%}
        </ul>
    """
    return render_template_string(html,task=tasks)
@app.route('/add', methods=['post'])
def add_task():
    task=request.form['task']
    tasks.append(task)
    return "<h2>Task Added sucessfuly <br> <a href='/'> Go Back</a>"
if __name__=='__main__':
    app.run(debug=True)

