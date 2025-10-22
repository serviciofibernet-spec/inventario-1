from flask import Flask, render_template
from extensions import db


def create_app():
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI="sqlite:///ftth.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    from views import bp as main_bp
    db.init_app(app)

    with app.app_context():
        # Crear tablas si no existen
        db.create_all()

    app.register_blueprint(main_bp)
    
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/healthz")
    def healthz():
        return {"status": "ok"}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
