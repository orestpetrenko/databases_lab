from flask import Blueprint, jsonify, request
from ..services.Event_service import EventsService
from ..app import get_db_connection  # Імпортуємо функцію для отримання з'єднання
from ..dao.OrderedTickets_dao import OrderedTicketsDAO

def create_events_controller():
    events_controller = Blueprint('events', __name__)
    service = EventsService()

    # Отримати всі події
    @events_controller.route('/events', methods=['GET'])
    def get_events():
        try:
            conn = get_db_connection()
            events = service.get_events(conn)
            conn.close()
            return jsonify(events), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # Отримати подію за ID
    @events_controller.route('/events/<int:event_id>', methods=['GET'])
    def get_event_by_id(event_id):
        try:
            conn = get_db_connection()
            event = service.get_event_by_id(conn, event_id)
            conn.close()
            if event:
                return jsonify(event), 200
            else:
                return jsonify({"error": "Event not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # Створити нову подію
    @events_controller.route('/events', methods=['POST'])
    def create_event():
        try:
            event_data = request.get_json()
            conn = get_db_connection()
            service.create_event(conn, event_data)
            conn.close()
            return jsonify({"message": "Event created successfully"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # Оновити подію
    @events_controller.route('/events/<int:event_id>', methods=['PUT'])
    def update_event(event_id):
        try:
            event_data = request.get_json()
            conn = get_db_connection()
            service.update_event(conn, event_id, event_data)
            conn.close()
            return jsonify({"message": "Event updated successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # Видалити подію
    @events_controller.route('/events/<int:event_id>', methods=['DELETE'])
    def delete_event(event_id):
        try:
            conn = get_db_connection()
            service.delete_event(conn, event_id)
            conn.close()
            return jsonify({"message": "Event deleted successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # Отримати події разом із відповідними артистами
    @events_controller.route('/events/artists', methods=['GET'])
    def get_events_with_artists():
        """
        Повертає список подій разом із інформацією про артистів.
        """
        try:
            conn = get_db_connection()
            events_with_artists = service.get_events_with_artists(conn)
            conn.close()
            return jsonify(events_with_artists), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @events_controller.route('/orders/tickets', methods=['GET'])
    def get_ordered_tickets():
        try:
            conn = get_db_connection()
            ordered_tickets = OrderedTicketsDAO().get_ordered_tickets_with_details(conn)
            conn.close()
            return jsonify(ordered_tickets), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return events_controller




