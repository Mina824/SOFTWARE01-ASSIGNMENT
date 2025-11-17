
import json
import mysql.connector
from flask import Flask, Response

app = Flask(__name__)
app.json.sort_keys = False

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database= 'flight_game',
    user='root',
    password='nadith',
    autocommit=True
)


@app.route("/airport/<icao>")
def airport(icao):

    sql = "SELECT ident, name, municipality FROM airport WHERE ident = %s"
    cursor = connection.cursor()
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()

    if result:
        response = {
            "ICAO": result[0],
            "Name": result[1],
            "Location": result[2]
        }
        json_response = json.dumps(response)
        return Response(response=json_response, status=200, mimetype="application/json")

    response = {"message": "Airport not found"}
    json_response = json.dumps(response)
    return Response(response=json_response, status=404, mimetype="application/json")


if __name__ == "__main__":
    app.run(debug=True)
