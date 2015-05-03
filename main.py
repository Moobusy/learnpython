#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import create_app

if __name__ == '__main__':
	server_host = '192.168.31.110'
	server_port = 80
	app = create_app()
	app.run(host=server_host, port=server_port)