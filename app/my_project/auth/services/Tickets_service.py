from ..dao.Tickets_dao import TicketsDAO

class TicketsService:
    def __init__(self):
        self.dao = TicketsDAO()

    def get_tickets(self, conn):
        return self.dao.get_all_tickets(conn)

    def get_ticket(self, conn, ticket_id):
        return self.dao.get_ticket_by_id(conn, ticket_id)

    def create_ticket(self, conn, ticket_data):
        return self.dao.create_ticket(conn, ticket_data)

    def update_ticket(self, conn, ticket_id, ticket_data):
        self.dao.update_ticket(conn, ticket_id, ticket_data)

    def delete_ticket(self, conn, ticket_id):
        self.dao.delete_ticket(conn, ticket_id)
