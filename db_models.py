from __future__ import annotations
from datetime import datetime
from extensions import db


class TimestampMixin:
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


class OLT(db.Model, TimestampMixin):
    __tablename__ = 'olts'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    ubicacion = db.Column(db.String(255), nullable=False)


class ODF(db.Model, TimestampMixin):
    __tablename__ = 'odfs'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    ubicacion = db.Column(db.String(255), nullable=False)


class Cable(db.Model, TimestampMixin):
    __tablename__ = 'cables'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    from_ubicacion = db.Column(db.String(255), nullable=False)
    to_ubicacion = db.Column(db.String(255), nullable=False)
    fibras = db.Column(db.Integer, nullable=False)


class Manga(db.Model, TimestampMixin):
    __tablename__ = 'mangas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    ubicacion = db.Column(db.String(255), nullable=False)


class Splitter(db.Model, TimestampMixin):
    __tablename__ = 'splitters'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    ratio = db.Column(db.String(16), nullable=False)
    ubicacion = db.Column(db.String(255), nullable=False)


class Fusion(db.Model, TimestampMixin):
    __tablename__ = 'fusiones'
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255), nullable=False)
    elemento_origen_tipo = db.Column(db.String(32), nullable=False)
    elemento_origen_id = db.Column(db.Integer, nullable=False)
    elemento_destino_tipo = db.Column(db.String(32), nullable=False)
    elemento_destino_id = db.Column(db.Integer, nullable=False)
    fibra_origen = db.Column(db.Integer)
    fibra_destino = db.Column(db.Integer)


class GeoFeature(db.Model, TimestampMixin):
    __tablename__ = 'geo_features'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(16), nullable=False)  # 'cable','manga','terminal','cabina'
    geometry = db.Column(db.Text, nullable=False)     # GeoJSON geometry as string
    properties = db.Column(db.JSON, default=dict)
