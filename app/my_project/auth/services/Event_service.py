from ..dao.Event_dao import EventsDAO

class EventsService:
    def __init__(self):
        self.dao = EventsDAO()

    def get_events(self, conn):
        return self.dao.get_all_events(conn)  # Отримуємо всі події через DAO

    def get_event_by_id(self, conn, event_id):
        return self.dao.get_event_by_id(conn, event_id)  # Отримуємо подію за ID

    def create_event(self, conn, event_data):
        self.dao.create_event(conn, event_data)  # Створюємо нову подію

    def update_event(self, conn, event_id, event_data):
        self.dao.update_event(conn, event_id, event_data)  # Оновлюємо подію за ID

    def delete_event(self, conn, event_id):
        self.dao.delete_event(conn, event_id)  # Видаляємо подію за ID

    def get_events_with_artists(self, conn):
        """
        Викликає DAO для отримання подій із відповідними артистами.
        """
        return self.dao.get_events_with_artists(conn)

