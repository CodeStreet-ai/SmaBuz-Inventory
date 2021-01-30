import os
from app import app, db
from models import *
import views
from flask_login import LoginManager


port = int(os.environ.get('PORT', 5000))
if __name__ == "__main__":
    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    app.run(host='0.0.0.0', port=5000, debug=True)
