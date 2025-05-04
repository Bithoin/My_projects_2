import mysql.connector

class DBConnection:
	def __init__(self, **db_config):
		self.db_config = db_config
		self.conn = None
		self.cur = None

	def __enter__(self):
		self.conn = mysql.connector.connect(**self.db_config)
		self.cur = self.conn.cursor()
		return self.conn, self.cur

	def __exit__(self, exc_type, exc_val, exc_tb):
		if self.cur:
			self.cur.close()
		if self.conn:
			if exc_type is not None:
				self.conn.rollback()
			else:
				self.conn.commit()
			self.conn.close()


DB_CONFIG = {
	"host": "localhost",
	"user": "root",
	"password": "",
	"database": "sakila"
}

with DBConnection(**DB_CONFIG) as (conn, cur):
	# query = "INSERT INTO actor (first_name, last_name) VALUES (%s, %s)"
	# values = ("John", "Doe")
	# cur.execute(query, values)
	query = "UPDATE actor SET first_name = %s WHERE actor_id = %s"
	values = ("MYLASTNAME", 201)
	cur.execute(query, values)
	# conn.commit()
	# cur.close()
	# conn.close()