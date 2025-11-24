from rasa_sdk import Action
import mysql.connector
import os

class ActionGuardarReserva(Action):

    def name(self):
        return "action_guardar_reserva"

    def run(self, dispatcher, tracker, domain):
        personas = tracker.get_slot("personas")
        fecha = tracker.get_slot("fecha")
        hora = tracker.get_slot("hora")

        db = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO reservas (personas, fecha, hora) VALUES (%s, %s, %s)",
            (personas, fecha, hora)
        )
        db.commit()
        cursor.close()
        db.close()

        dispatcher.utter_message("Tu reserva fue guardada correctamente.")

        return []
