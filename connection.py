from configparser import ConfigParser
import psycopg2

def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

class connection():
    def __init__(self):
        self.conn = None
        self.cur = None

    def whileConnected(self):
        pass

    def connect(self):
        try:
            params = config()
            self.conn = psycopg2.connect(**params)
            self.cur = self.conn.cursor()

            self.whileConnected()
            print('success')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()
                print('Database connection closed.')

class exampleConnection(connection):
    def whileConnected(self):
        self.cur.execute('SELECT name FROM rawcards LIMIT 5;')
        names = self.cur.fetchall()
        print('Names:', names)

if __name__ == '__main__':
    conn = exampleConnection()
    conn.connect()