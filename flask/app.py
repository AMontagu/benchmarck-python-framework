import time, os, flask, sqlite3, logging

app = flask.Flask('benchmark')

log = logging.getLogger('werkzeug')
log.disabled = True

@app.route('/char')
def char():
    return "t"

@app.route('/dbinsert')
def dbinsert():
    dt = int(time.time())
    conn.execute("""INSERT INTO data VALUES (?, ?)""", (dt, "hello"))
    return "done"

@app.route('/dbsearch')
def dbsearch():
    res = conn.execute("""SELECT * FROM data WHERE  t liKE "hello" """)
    s = ""
    for r in res:
        s += f"{r[0]}<br>"
    return s

@app.route('/data2')
def data2():
    return flask.Response(y2, headers={'Content-Type': "application/octet-stream"})

@app.route('/data10')
def data10():
    return flask.Response(y10, headers={'Content-Type': "application/octet-stream"})

conn = sqlite3.connect(':memory:', check_same_thread=False)
conn.execute("CREATE TABLE data(datetime INTEGER, t TEXT);")
y2 = os.urandom(2_000_000)
y10 = os.urandom(10_000_000)

app.run()
