class EventsDAO:
    def __init__(self):
        pass

    def get_all_events(self, conn):
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute("SELECT * FROM events")  # Отримуємо всі події
            events = cur.fetchall()
            cur.close()
            return events
        except Exception as e:
            print(f"Database error: {e}")
            raise

    def get_event_by_id(self, conn, event_id):
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute("SELECT * FROM events WHERE event_id = %s", (event_id,))  # Отримуємо подію за ID
            event = cur.fetchone()
            cur.close()
            return event
        except Exception as e:
            print(f"Database error: {e}")
            raise

    def create_event(self, conn, event_data):
        try:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO events (name, date, location, artist_id)
                VALUES (%s, %s, %s, %s)
            """, (event_data['name'], event_data['date'], event_data['location'], event_data['artist_id']))
            conn.commit()
            cur.close()
        except Exception as e:
            print(f"Database error: {e}")
            raise

    def update_event(self, conn, event_id, event_data):
        try:
            cur = conn.cursor()
            cur.execute("""
                UPDATE events SET name = %s, date = %s, location = %s, artist_id = %s
                WHERE event_id = %s
            """, (event_data['name'], event_data['date'], event_data['location'], event_data['artist_id'], event_id))
            conn.commit()
            cur.close()
        except Exception as e:
            print(f"Database error: {e}")
            raise

    def delete_event(self, conn, event_id):
        try:
            cur = conn.cursor()

            # Видаляємо записи з orderedtickets, пов'язані з подією
            cur.execute("""
                DELETE FROM orderedtickets 
                WHERE ticket_id IN (
                    SELECT ticket_id FROM tickets WHERE event_id = %s
                )
            """, (event_id,))

            # Видаляємо записи з tickets, пов'язані з подією
            cur.execute("DELETE FROM tickets WHERE event_id = %s", (event_id,))

            # Видаляємо саму подію
            cur.execute("DELETE FROM events WHERE event_id = %s", (event_id,))

            conn.commit()
            cur.close()
        except Exception as e:
            conn.rollback()
            print(f"Database error: {e}")
            raise

    def get_events_with_artists(self, conn):
        """
        Отримати список подій разом із відповідними артистами.
        """
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute("""
                SELECT 
                    e.event_id, 
                    e.name AS event_name, 
                    e.date, 
                    e.location, 
                    a.artist_id, 
                    a.name AS artist_name, 
                    a.genre
                FROM 
                    events e
                JOIN 
                    artists a
                ON 
                    e.artist_id = a.artist_id;
            """)
            result = cur.fetchall()
            cur.close()
            return result
        except Exception as e:
            print(f"Database error in get_events_with_artists: {e}")
            raise