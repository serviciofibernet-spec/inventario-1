from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

# Nota: inicialmente usamos dataclasses para diseñar el modelo lógico.
# Luego migraremos a SQLAlchemy para persistencia.

@dataclass
class OLT:
    id: Optional[int]
    nombre: str
    ubicacion: str


@dataclass
class ODF:
    id: Optional[int]
    nombre: str
    ubicacion: str


@dataclass
class Cable:
    id: Optional[int]
    nombre: str
    from_ubicacion: str
    to_ubicacion: str
    fibras: int


@dataclass
class Manga:
    id: Optional[int]
    nombre: str
    ubicacion: str


@dataclass
class Splitter:
    id: Optional[int]
    nombre: str
    ratio: str  # p. ej. 1:8, 1:16
    ubicacion: str


@dataclass
class Fusion:
    id: Optional[int]
    descripcion: str
    elemento_origen_tipo: str  # 'cable','odf','olt','manga','splitter'
    elemento_origen_id: int
    elemento_destino_tipo: str
    elemento_destino_id: int
    fibra_origen: Optional[int] = None
    fibra_destino: Optional[int] = None
