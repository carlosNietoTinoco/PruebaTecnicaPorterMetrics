from chalice import Chalice

from chalicelib.blueprint.user_controller import user_api

app = Chalice(app_name='prueba-tecnica')
app.register_blueprint(user_api, url_prefix='/v1')