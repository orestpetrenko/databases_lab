class OrdersDAO:
    def __init__(self):
        pass

    def get_all_orders(self, conn):
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute("SELECT * FROM orders")  # Отримуємо всі замовлення
            orders = cur.fetchall()
            cur.close()
            return orders
        except Exception as e:
            print(f"Database error: {e}")
            raise

    def get_order_by_id(self, conn, order_id):
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute("SELECT * FROM orders WHERE order_id = %s", (order_id,))  # Отримуємо замовлення за ID
            order = cur.fetchone()
            cur.close()
            return order
        except Exception as e:
            print(f"Database error: {e}")
            raise

    def create_order(self, conn, order_data):
        try:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO orders (customer_name, order_date, delivery_option_id, payment_status)
                VALUES (%s, %s, %s, %s)
            """, (order_data['customer_name'], order_data['order_date'], order_data['delivery_option_id'], order_data['payment_status']))
            conn.commit()
            cur.close()
        except Exception as e:
            print(f"Database error: {e}")
            raise

    def update_order(self, conn, order_id, order_data):
        try:
            cur = conn.cursor()
            cur.execute("""
                UPDATE orders SET customer_name = %s, order_date = %s, delivery_option_id = %s, payment_status = %s
                WHERE order_id = %s
            """, (order_data['customer_name'], order_data['order_date'], order_data['delivery_option_id'], order_data['payment_status'], order_id))
            conn.commit()
            cur.close()
        except Exception as e:
            print(f"Database error: {e}")
            raise

    def delete_order(self, conn, order_id):
        try:
            cur = conn.cursor()

            # Видаляємо записи з transporttickets, пов'язані із замовленням
            cur.execute("""
                DELETE FROM transporttickets WHERE order_id = %s
            """, (order_id,))

            # Видаляємо записи з payments, пов'язані із замовленням
            cur.execute("""
                DELETE FROM payments WHERE order_id = %s
            """, (order_id,))

            # Видаляємо саме замовлення
            cur.execute("""
                DELETE FROM orders WHERE order_id = %s
            """, (order_id,))

            conn.commit()
            cur.close()
        except Exception as e:
            conn.rollback()
            print(f"Database error: {e}")
            raise


