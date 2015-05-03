# -*- coding: utf-8 -*-
'''
	Docer - database
	~~~~~~
	A document viewing platform.

	:copyright: (c) 2015 by Docer.Org.
	:license: MIT, see LICENSE for more details.
'''

from sqlalchemy import create_engine

if __name__ == '__main__':
	engine = create_engine('mysql://55haitao:55haitao@192.168.1.81:3306/55shantao_v2?charset=utf8')