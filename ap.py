from flask import Flask, render_template, request, json
from flask_mysqldb import MySQL

app = Flask (__name__)

app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "impacta2024"
app.config['MYSQL_DB'] = "teste"
app.config['MYSQL_HOST'] = "localhost"
mysql = MySQL(app)

@app.route('/')
def main ():
    return render_template('aulamvc.html')


# @app.route('/showSignUp')
# def showSignUp():
#     return render_template('signup.html')



@app.route('/gravar', methods=['POST'])
def gravar ():
    try:
        nomerec= request.form['nome']
        emailrec = request.form['email']
        senharec = request.form['senha']
        print(nomerec)
        print(emailrec)
        print(senharec)

        if nomerec and emailrec and senharec:

            conn = mysql.connection
            cursor = conn.cursor()
            _hashed_password = senharec
            cursor.execute('insert into tbl_user (user_name, user_username, user_password) VALUES (%s, %s, %s)', ( nomerec,emailrec,_hashed_password))
            conn.commit()


            return render_template('aulamvc.html')
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        # cursor.close()
        # conn.close()
        print('ops')

if __name__ == "__main__":
    # port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=5000)