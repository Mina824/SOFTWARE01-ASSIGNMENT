from geopy.distance import geodesic
import mysql.connector
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database = "flight_game",
    user = "root",
    password = "nadith",
    autocommit = True,

)

def airport_coordinates(icao):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s;"
    cursor = connection.cursor()
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    return result if result else None

def distance_between_airports(icao1, icao2):
    coords1 = airport_coordinates(icao1)
    coords2 = airport_coordinates(icao2)
    if coords1 and coords2:
        dist = geodesic(coords1, coords2).kilometers
        print(f"Distance between {icao1} and {icao2}: {dist:.2f} km")
    else:
        print("One or both ICAO codes not found.")

icao1 = input("Enter first ICAO code: ")
icao2 = input("Enter second ICAO code: ")
distance_between_airports(icao1, icao2)
