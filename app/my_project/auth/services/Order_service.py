from ..dao.Order_dao import OrdersDAO

class OrdersService:
    def __init__(self):
        self.dao = OrdersDAO()

    def get_orders(self, conn):
        return self.dao.get_all_orders(conn)  # Отримуємо всі замовлення через DAO

    def get_order_by_id(self, conn, order_id):
        return self.dao.get_order_by_id(conn, order_id)  # Отримуємо замовлення за ID

    def create_order(self, conn, order_data):
        self.dao.create_order(conn, order_data)  # Створюємо нове замовлення

    def update_order(self, conn, order_id, order_data):
        self.dao.update_order(conn, order_id, order_data)  # Оновлюємо замовлення за ID

    def delete_order(self, conn, order_id):
        self.dao.delete_order(conn, order_id)  # Видаляємо замовлення за ID
