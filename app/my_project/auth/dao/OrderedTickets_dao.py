class OrderedTicketsDAO:
    def __init__(self):
        pass

    def get_ordered_tickets_with_details(self, conn):
        """
        Отримати всі замовлення з квитками та їх кількістю.
        """
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute("""
                SELECT 
                    o.order_id, 
                    o.customer_name, 
                    o.order_date, 
                    t.ticket_id, 
                    t.price, 
                    t.type, 
                    ot.quantity
                FROM 
                    OrderedTickets ot
                JOIN 
                    Orders o ON ot.order_id = o.order_id
                JOIN 
                    Tickets t ON ot.ticket_id = t.ticket_id;
            """)
            result = cur.fetchall()
            cur.close()
            return result
        except Exception as e:
            print(f"Database error in get_ordered_tickets_with_details: {e}")
            raise
