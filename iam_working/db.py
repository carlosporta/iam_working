from sqlite3 import connect


def _get_connection():
    conn = connect('db.sqlite3')
    return conn


def _execute(query):
    conn = _get_connection()
    cursor = conn.cursor()
    resp = cursor.execute(query)
    conn.commit()
    return resp


def configure_db():
    query = '''
        CREATE TABLE IF NOT EXISTS Acitivity(date text, agent text, message text)
    '''
    _execute(query)


def insert(date, agent, message):
    query = f'INSERT INTO Acitivity VALUES("{date}", "{agent}", "{message}")'
    _execute(query)


def select_all():
    query = 'SELECT date, agent, message FROM Acitivity'
    resp = _execute(query)
    return [{'date': r[0], 'agent': r[1], 'message': r[2]} for r in resp]
