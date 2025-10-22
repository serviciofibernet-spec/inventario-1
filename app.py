from flask import Flask, render_template
from extensions import db
from sqlalchemy import text


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
        # Asegurar columnas nuevas en SQLite (migraciones simples)
        try:
            def table_has_column(table: str, column: str) -> bool:
                rows = db.session.execute(text(f"PRAGMA table_info({table});")).mappings().all()
                return any(r['name'] == column for r in rows)

            if not table_has_column('cables', 'manga_id'):
                db.session.execute(text('ALTER TABLE cables ADD COLUMN manga_id INTEGER'))
            if not table_has_column('splitters', 'manga_id'):
                db.session.execute(text('ALTER TABLE splitters ADD COLUMN manga_id INTEGER'))
            db.session.commit()
        except Exception:
            db.session.rollback()

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
