[https://google.com](https://uuboyscy.dev)

# Vibe coding

i am writing a web page to show employee information.
i am using Flask
Following is a router I need you to implement
```python
# GET /show_employee?name=Marry
@app.route("/show_employee")
def show_employee():
    # Extract arguments from user
    # Call function for employee dataframe
    # Send employee data to template
    # Return the rendered HTML, using flask render_template
    pass
```

I will also need a template HTML
and a MySQL connection function for the router
following is how I connect to MySQL
```python
# 連接資料庫
import pymysql

host = 'localhost'
port = 3307  # if you are using docker, you must use 3307, or reserve 3306
user = 'root'
passwd = '1qaz@WSX'
db = 'TESTDB'
charset = 'utf8mb4'

conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
print('Successfully connected!')

cursor = conn.cursor()
```

Columns for your reference:
ID, Name, DeptId, Age, Gender, Salary, recordDt