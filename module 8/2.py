import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Qwertyzmpq",
    database="flight_game",
    port="3300"
)
cursor = connection.cursor()
country_code = input("Enter the area code: ")
cursor.execute("""
    SELECT type, COUNT(*)
    FROM airport
    WHERE iso_country = %s
    GROUP BY type
    ORDER BY type
""", (country_code,))

results = cursor.fetchall()
if results:
    print("Airports in", country_code + ":")
    for row in results:
        airport_type = row[0]
        count = row[1]
        print(count, airport_type)
else:
    print("No airports found for that country code.")
connection.close()