import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Qwertyzmpq",
    database="flight_game",
    port="3300"
)
cursor = connection.cursor()
icao_code = input("Enter the ICAO code of the airport: ")
cursor.execute("SELECT name, municipality FROM airport WHERE ident = %s", (icao_code,))
airport = cursor.fetchone()
if airport:
    print("Airport name:", airport[0])
    print("Town:", airport[1])
else:
    print("No airport found with that code.")

connection.close()