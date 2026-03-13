import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Qwertyzmpq",
    database="flight_game",
    port="3300"
)

cursor = connection.cursor()
first_airport = input("Enter the ICAO code of the first airport: ")
second_airport = input("Enter the ICAO code of the second airport: ")
cursor.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s", (first_airport,))
coords1 = cursor.fetchone()
cursor.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s", (second_airport,))
coords2 = cursor.fetchone()
if coords1 and coords2:
    distance = geodesic(coords1, coords2).kilometers
    print("Distance between the two airports:", round(distance, 1), "km")
else:
    print("One or both airports were not found in the database.")
connection.close()