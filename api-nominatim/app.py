from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    try:
        conn = sqlite3.connect("clients.db")
        conn.row_factory = sqlite3.Row
        rows = conn.execute("SELECT * FROM clients").fetchall()
        clients = [dict(row) for row in rows]
    except Exception as e:
        print("❌ Erreur lors de la lecture de la base :", e)
        clients = []
    finally:
        conn.close()

    return render_template("map.html", clients=clients)


if __name__ == "__main__":
    app.run(debug=True)
