from flask import Flask, render_template, request

from db import get_employee_df

app = Flask(__name__, static_url_path="/static", static_folder="./static")

@app.route("/")
def hello():
    return "<h1>Hello Flask!</h1>"

# GET /api/employee/<dep_id:str>/<emp_id:str>
@app.route("/api/employee/<dep_id>/<emp_id>")
def get_employee(dep_id, emp_id):
    sql = f"""
        select
            emp_name,
            emp_id,
            dep_id,
            email
        from staff
        where dep_id = '{dep_id}' and emp_id = '{emp_id}'
    """
    # result = execute_sql(sql)
    return {
        "emp_name": "Allen",
        "emp_id": emp_id,
        "dep_id": dep_id,
        "email": "aaa@example.com"
    }

# GET /hello?username=Allen&age=22
@app.route("/hello")
def hello_user():
    username = request.args.get("username")
    age = request.args.get("age")
    if not username:
        return "Who are you?"
    if not age:
        return f"Hello {username}."
    return f"Hello {username}, you are {age} years old."

@app.route("/hello_post", methods=["GET", "POST"])
def hello_post():
    result_html = """
    <html>
    <form action="/hello_post" method="POST">
        <label>What is your name?</label>
        <br>
        <input type="textbox" name="username">
        <button type="submit">Submit</button>
    </form>
    <div>
    %s
    </div>
    </html>
    """
    if request.method == "GET":
        return result_html % ("")

    username = request.form.get("username")
    return result_html % ("Hello %s" % (username))

@app.route("/hello_post2", methods=["GET", "POST"])
def hello_post2():
    return render_template(
        "hello_post.html",
        username=request.form.get("username"),
        request_method=request.method,
    )

# GET /show_employee?name=Marry
@app.route("/show_employee")
def show_employee():
    # Extract arguments from user
    # Call function for employee dataframe
    # Send employee data to template
    # Return the rendered HTML
    pass

@app.route("/show_employee")
def show_employee():
    # Extract arguments from user
    name = request.args.get("name", default=None, type=str)
    
    # Call function for employee dataframe
    df = get_employee_df(name=name)
    
    # Send employee data to template
    employee_records = df.to_dict(orient="records")
    
    # Return the rendered HTML, using flask render_template
    return render_template(
        "show_employee.html", 
        employees=employee_records, 
        searched_name=name
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
