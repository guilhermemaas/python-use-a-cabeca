Python 3.7.5 (default, Nov 20 2019, 09:21:52) 
[GCC 9.2.1 20191008] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> import mysql-connector
SyntaxError: invalid syntax
>>> import mysql.connector
>>> dbconfig = { 'host': '127.0.0.1',
	     'user': 'vsearch',
	     'password': 'vsearchpasswd',
	     'database': 'vsearchlogDB', }
>>> 
>>> conn = mysql.connector.connect(**dbconfig)
>>> cursor = conn.cursor()
>>> _SQL = "
SyntaxError: EOL while scanning string literal
>>> _SQL = """insert into log
	(phrase, letters, ip, browser_string, results)
	values
	('hitch-hiker', 'aeiou', '127.0.0.1', 'FireFox', "{'e', 'i'}")"""
>>> cursor.execute(_SQL)
>>> conn.commit()
>>> _SQL = """insert into log
	(phrase, letters, ip, browse_string, results)
	values
	(%s, %s, %s, %s, %s)"""
>>> cursor.execute(_SQL, ('hitch-hiker', 'xyz', '127.0.0.1', 'Safari', 'set()'))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    cursor.execute(_SQL, ('hitch-hiker', 'xyz', '127.0.0.1', 'Safari', 'set()'))
  File "/usr/local/lib/python3.7/dist-packages/mysql/connector/cursor.py", line 569, in execute
    self._handle_result(self._connection.cmd_query(stmt))
  File "/usr/local/lib/python3.7/dist-packages/mysql/connector/connection.py", line 598, in cmd_query
    result = self._handle_result(self._send_cmd(ServerCmd.QUERY, query))
  File "/usr/local/lib/python3.7/dist-packages/mysql/connector/connection.py", line 486, in _handle_result
    raise errors.get_exception(packet)
mysql.connector.errors.ProgrammingError: 1054 (42S22): Unknown column 'browse_string' in 'field list'
>>> _SQL = """insert into log
	(phrase, letters, ip, browser_string, results)
	values
	(%s, %s, %s, %s, %s)"""
>>> cursor.execute(_SQL, ('hitch-hiker', 'xyz', '127.0.0.1', 'Safari', 'set()'))
>>> conn.comit()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    conn.comit()
AttributeError: 'MySQLConnection' object has no attribute 'comit'
>>> con.commit()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    con.commit()
NameError: name 'con' is not defined
>>> conn.commit()
>>> _SQL = """select * from log"""
>>> for row in cursor.fetchall():
	print(row)

	
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    for row in cursor.fetchall():
  File "/usr/local/lib/python3.7/dist-packages/mysql/connector/cursor.py", line 895, in fetchall
    raise errors.InterfaceError("No result set to fetch from.")
mysql.connector.errors.InterfaceError: No result set to fetch from.
>>> cursor.execute(_SQL)
>>> for row in cursor.fetchall():
	print(row)

	
(1, datetime.datetime(2020, 4, 13, 10, 39, 41), 'hitch-hiker', 'aeiou', '127.0.0.1', 'FireFox', "{'e', 'i'}")
(2, datetime.datetime(2020, 4, 13, 10, 46, 31), 'hitch-hiker', 'xyz', '127.0.0.1', 'Safari', 'set()')
>>> cursor.close() #fechar o cursor
True
>>> conn.close() #fechar a conexao com o banco
>>> 
