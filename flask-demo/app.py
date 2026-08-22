from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello Flask!</h1>"

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

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
