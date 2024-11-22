from flask import Blueprint, jsonify, request
from ..services.Order_service import OrdersService
from ..app import get_db_connection  # Функція для отримання з'єднання з БД

def create_orders_controller():
    orders_controller = Blueprint('orders', __name__)
    service = OrdersService()

    @orders_controller.route('/orders', methods=['GET'])
    def get_orders():
        try:
            conn = get_db_connection()
            orders = service.get_orders(conn)  # Отримуємо всі замовлення
            conn.close()
            return jsonify(orders)  # Повертаємо список замовлень у форматі JSON
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @orders_controller.route('/orders/<int:order_id>', methods=['GET'])
    def get_order_by_id(order_id):
        try:
            conn = get_db_connection()
            order = service.get_order_by_id(conn, order_id)  # Отримуємо замовлення за ID
            conn.close()
            if order:
                return jsonify(order)
            else:
                return jsonify({"error": "Order not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @orders_controller.route('/orders', methods=['POST'])
    def create_order():
        try:
            order_data = request.get_json()  # Отримуємо дані замовлення з тіла запиту
            conn = get_db_connection()
            service.create_order(conn, order_data)  # Створюємо нове замовлення
            conn.close()
            return jsonify({"message": "Order created successfully"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @orders_controller.route('/orders/<int:order_id>', methods=['PUT'])
    def update_order(order_id):
        try:
            order_data = request.get_json()  # Отримуємо оновлені дані замовлення
            conn = get_db_connection()
            service.update_order(conn, order_id, order_data)  # Оновлюємо замовлення за ID
            conn.close()
            return jsonify({"message": "Order updated successfully"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @orders_controller.route('/orders/<int:order_id>', methods=['DELETE'])
    def delete_order(order_id):
        try:
            conn = get_db_connection()
            service.delete_order(conn, order_id)  # Видаляємо замовлення за ID
            conn.close()
            return jsonify({"message": "Order deleted successfully"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return orders_controller
