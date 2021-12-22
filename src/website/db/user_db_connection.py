class userAccountDbConnection:

    def connect_to_database(mysql):
        conn = mysql.connection.cursor()
        return conn

    def close_database_connection(conn):
        return conn.close()

    def create_user_table(conn):
        conn.execute(''' CREATE TABLE IF NOT EXISTS users (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                     name VARCHAR(100) NOT NULL,
                     email VARCHAR(100) NOT NULL,
                     password VARCHAR(1000) NOT NULL) ''')
        return conn

    def check_if_user_exists_in_db(conn, email):
        conn.execute('SELECT * FROM users WHERE email = % s ', (email,))
        user = conn.fetchone()
        return user


    def insert_new_user(conn, name, email, password):
        conn.execute('INSERT INTO users (name, email, password) VALUES (%s, %s, %s)', (name, email, password,))

    def commit_to_database(mysql):
        return mysql.connection.commit()
