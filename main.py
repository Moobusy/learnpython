#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import create_app

if __name__ == '__main__':
#	本地测试环境
	local_host = '192.168.31.110'
	local_port = 80
#	公开测试环境
	test_host = '127.0.0.1'
	test_port = 5000
	
	app = create_app()
	app.run(host=test_host, port=test_port)