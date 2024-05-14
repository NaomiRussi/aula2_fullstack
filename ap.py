from flask import Flask, json, render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'teste'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'

mysql = MySQL(app)

@app.route('/')
def teste1():
    return render_template('aulamvc.html')

@app.route('/gravar', methods=['POST'])
def teste2():
    try:
        nomerec = request.form['nome']
        emailrec = request.form['email']
        senharec = request.form['senha']
        print("teste")
        print(nomerec)
        print(emailrec)
        print(senharec)
        
        if nomerec and emailrec and senharec:
            
            conn =  mysql.connect()
            cursor = conn.cursor()
            _hashed_password = senharec
            cursor.execute('insert into tbl_user (user_name, user_username, user_password) VALUES (%s, %s, %s)', (nomerec, emailrec, _hashed_password))
            conn.commit()
            
            return render_template('aulamvc.html')
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})
    except Exception as e:
        return json.dumps({'error':str(e)})
    # else:
        


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
