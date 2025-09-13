import mysql.connector
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database = "flight_game",
    user = "root",
    password = "nadith",
)
def airport_by_code(area_code):
    sql = f"select type  from airport where iso_country = '{area_code}';"

    cursor = connection.cursor()
    cursor.execute(sql)
    database_data = cursor.fetchall()
    if len(database_data) > 0:
        print(f"Airports in {area_code}:")
        for data in database_data:
            print(f" Airport type: {data[0]}, count: {data[1]}")
    else:
        print("No airports found")



user_input = input("Enter area code: ")
airport_by_code(user_input)




