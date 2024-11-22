from flask import Blueprint, jsonify, request
from ..services.Tickets_service import TicketsService
from ..app import get_db_connection

def create_tickets_controller():
    tickets_controller = Blueprint('tickets', __name__)
    service = TicketsService()

    @tickets_controller.route('/tickets', methods=['GET'])
    def get_tickets():
        try:
            conn = get_db_connection()
            tickets = service.get_tickets(conn)
            conn.close()
            return jsonify(tickets)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @tickets_controller.route('/tickets/<int:ticket_id>', methods=['GET'])
    def get_ticket(ticket_id):
        try:
            conn = get_db_connection()
            ticket = service.get_ticket(conn, ticket_id)
            conn.close()
            if ticket:
                return jsonify(ticket)
            else:
                return jsonify({"error": "Ticket not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @tickets_controller.route('/tickets', methods=['POST'])
    def create_ticket():
        try:
            ticket_data = request.get_json()
            conn = get_db_connection()
            ticket_id = service.create_ticket(conn, ticket_data)
            conn.close()
            return jsonify({"ticket_id": ticket_id}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @tickets_controller.route('/tickets/<int:ticket_id>', methods=['PUT'])
    def update_ticket(ticket_id):
        try:
            ticket_data = request.get_json()
            conn = get_db_connection()
            service.update_ticket(conn, ticket_id, ticket_data)
            conn.close()
            return jsonify({"message": "Ticket updated successfully"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @tickets_controller.route('/tickets/<int:ticket_id>', methods=['DELETE'])
    def delete_ticket(ticket_id):
        try:
            conn = get_db_connection()
            service.delete_ticket(conn, ticket_id)
            conn.close()
            return jsonify({"message": "Ticket deleted successfully"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return tickets_controller
