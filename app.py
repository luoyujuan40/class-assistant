#导入flask对象
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from check_login import is_existed,exist_user,is_null
from flask import url_for
from flask import flash
from flask import Flask, render_template, redirect, url_for, request, flash


#使用flask对象创建一个app对象
app = Flask(__name__)
#路由

@app.route('/')
def index():
    #登录功能
    #return '需要实现登录的逻辑'
    return render_template('first.html')

@app.route('/first')
def first():
    #登录功能
    #return '需要实现登录的逻辑'
    return render_template('first.html')

@app.route('/login',methods=['GET','POST'])
def login():
        if request.method=='POST':
            username=request.form['username']
            password=request.form['password']
            teacher_is=request.form['teacher_is']
            if is_null(username,password):
                login_message="温馨提示：账号和密码都是必填"
                return render_template('login.html',message=login_message)
            elif is_existed(username,password,teacher_is):
                print(teacher_is)
                return render_template('my1.html',username=username)
            elif exist_user(username):
                login_message="温馨提示：密码错误，请输入正确密码"
                return render_template('login.html',message=login_message)
            else:
                login_message="温馨提示：不存在该用户,请先注册"
                return render_template('login.html',message=login_message)
        return render_template('login.html')

@app.route("/register",methods=["GET", 'POST'])
def register():
        return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)

