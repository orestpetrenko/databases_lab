from flask import Flask
import mysql.connector
from ..auth.config import Config

# Створення об'єкта Flask
app = Flask(__name__)

# Завантаження конфігурації
app.config.from_object(Config)

# Функція для підключення до БД
def get_db_connection():
    return mysql.connector.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DB
    )

# Імпорт контролера вже після ініціалізації додатку
def create_app():
    from ..auth.controller.Event_controller import create_events_controller
    from ..auth.controller.Tickets_controller import create_tickets_controller
    from ..auth.controller.Order_controller import create_orders_controller

    # Підключення контролера
    events_controller = create_events_controller()
    app.register_blueprint(events_controller, url_prefix="/api")

    tickets_controller = create_tickets_controller()
    app.register_blueprint(tickets_controller, url_prefix="/api")

    orders_controller = create_orders_controller()
    app.register_blueprint(orders_controller, url_prefix="/api")




    return app

# Запуск додатку
if __name__ == '__main__':
    app = create_app()  # Тепер викликаємо create_app
    app.run(debug=True)
