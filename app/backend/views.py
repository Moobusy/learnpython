# -*- coding: utf-8 -*-
'''
	Docer - backend - views
	~~~~~~
	A document viewing platform.

	:copyright: (c) 2015 by Docer.Org.
	:license: MIT, see LICENSE for more details.
'''

from . import backend
from flask import request, session, g, redirect, url_for, abort, render_template, flash

@backend.route('/')
def hello_world():
	return "Hello admin!"
    
@backend.route('/user')
def user():
	return 'Userpage'

@backend.route('/user/reg')
def reg():
	return render_template('admin/reg.html')
	
@backend.route('/user/do_reg', methods=['POST'])
def do_reg():
	from app.models import Users
	_uname = request.form['username'].strip()
	_pwd = request.form['password'].strip()
#	检验数据
	if len(_uname)>20 or len(_uname)<5:
		return '用户名要求长度5-20'
	elif len(_pwd)>20 or len(_pwd)<8:
		return '密码要求长度8-20'
	else:
		exists_users = Users.objects.filter(username = request.form['username'])
		if exists_users.count()>0:
			return '帐号已存在'
#	执行注册	
	new_user = Users(
		username = _uname,
		password = _pwd
	)
	new_user.save()	
	return '注册成功'
