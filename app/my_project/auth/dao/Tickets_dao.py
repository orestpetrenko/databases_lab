class TicketsDAO:
    def __init__(self):
        pass

    def get_all_tickets(self, conn):
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute("SELECT * FROM tickets")
            tickets = cur.fetchall()
            cur.close()
            return tickets
        except Exception as e:
            print(f"Database error: {e}")
            raise

    def get_ticket_by_id(self, conn, ticket_id):
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute("SELECT * FROM tickets WHERE ticket_id = %s", (ticket_id,))
            ticket = cur.fetchone()
            cur.close()
            return ticket
        except Exception as e:
            print(f"Database error: {e}")
            raise

    def create_ticket(self, conn, ticket_data):
        try:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO tickets (event_id, seat_id, price, type) VALUES (%s, %s, %s, %s)
            """, (ticket_data['event_id'], ticket_data['seat_id'], ticket_data['price'], ticket_data['type']))
            conn.commit()
            ticket_id = cur.lastrowid
            cur.close()
            return ticket_id
        except Exception as e:
            print(f"Database error: {e}")
            raise

    def update_ticket(self, conn, ticket_id, ticket_data):
        try:
            cur = conn.cursor()
            cur.execute("""
                UPDATE tickets SET event_id = %s, seat_id = %s, price = %s, type = %s WHERE ticket_id = %s
            """, (ticket_data['event_id'], ticket_data['seat_id'], ticket_data['price'], ticket_data['type'], ticket_id))
            conn.commit()
            cur.close()
        except Exception as e:
            print(f"Database error: {e}")
            raise

    def delete_ticket(self, conn, ticket_id):
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM tickets WHERE ticket_id = %s", (ticket_id,))
            conn.commit()
            cur.close()
        except Exception as e:
            print(f"Database error: {e}")
            raise
