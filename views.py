from flask import Blueprint, render_template, request, redirect, url_for, flash
from extensions import db
from db_models import OLT, ODF, Cable, Manga, Splitter, Fusion

bp = Blueprint('main', __name__)


@bp.route('/olts')
def list_olts():
    items = OLT.query.order_by(OLT.id.desc()).all()
    return render_template('list.html', title='OLTs', endpoint='create_olt', items=items, entity='OLT')


@bp.route('/olts/create', methods=['GET', 'POST'])
def create_olt():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        ubicacion = request.form.get('ubicacion', '').strip()
        if not nombre or not ubicacion:
            flash('Nombre y ubicación son obligatorios', 'danger')
        else:
            db.session.add(OLT(nombre=nombre, ubicacion=ubicacion))
            db.session.commit()
            flash('OLT creada', 'success')
            return redirect(url_for('main.list_olts'))
    return render_template('form_olt.html')


@bp.route('/odfs')
def list_odfs():
    items = ODF.query.order_by(ODF.id.desc()).all()
    return render_template('list.html', title='ODFs', endpoint='create_odf', items=items, entity='ODF')


@bp.route('/odfs/create', methods=['GET', 'POST'])
def create_odf():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        ubicacion = request.form.get('ubicacion', '').strip()
        if not nombre or not ubicacion:
            flash('Nombre y ubicación son obligatorios', 'danger')
        else:
            db.session.add(ODF(nombre=nombre, ubicacion=ubicacion))
            db.session.commit()
            flash('ODF creada', 'success')
            return redirect(url_for('main.list_odfs'))
    return render_template('form_odf.html')


@bp.route('/cables')
def list_cables():
    items = Cable.query.order_by(Cable.id.desc()).all()
    return render_template('list.html', title='Cables', endpoint='create_cable', items=items, entity='Cable')


@bp.route('/cables/create', methods=['GET', 'POST'])
def create_cable():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        from_ubicacion = request.form.get('from_ubicacion', '').strip()
        to_ubicacion = request.form.get('to_ubicacion', '').strip()
        fibras = request.form.get('fibras', '0').strip()
        try:
            fibras = int(fibras)
        except ValueError:
            fibras = 0
        if not nombre or not from_ubicacion or not to_ubicacion or fibras <= 0:
            flash('Todos los campos son obligatorios y fibras > 0', 'danger')
        else:
            db.session.add(Cable(nombre=nombre, from_ubicacion=from_ubicacion, to_ubicacion=to_ubicacion, fibras=fibras))
            db.session.commit()
            flash('Cable creado', 'success')
            return redirect(url_for('main.list_cables'))
    return render_template('form_cable.html')


@bp.route('/mangas')
def list_mangas():
    items = Manga.query.order_by(Manga.id.desc()).all()
    return render_template('list.html', title='Mangas', endpoint='create_manga', items=items, entity='Manga')


@bp.route('/mangas/create', methods=['GET', 'POST'])
def create_manga():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        ubicacion = request.form.get('ubicacion', '').strip()
        if not nombre or not ubicacion:
            flash('Nombre y ubicación son obligatorios', 'danger')
        else:
            db.session.add(Manga(nombre=nombre, ubicacion=ubicacion))
            db.session.commit()
            flash('Manga creada', 'success')
            return redirect(url_for('main.list_mangas'))
    return render_template('form_manga.html')


@bp.route('/splitters')
def list_splitters():
    items = Splitter.query.order_by(Splitter.id.desc()).all()
    return render_template('list.html', title='Splitters', endpoint='create_splitter', items=items, entity='Splitter')


@bp.route('/splitters/create', methods=['GET', 'POST'])
def create_splitter():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        ratio = request.form.get('ratio', '').strip()
        ubicacion = request.form.get('ubicacion', '').strip()
        if not nombre or not ratio or not ubicacion:
            flash('Todos los campos son obligatorios', 'danger')
        else:
            db.session.add(Splitter(nombre=nombre, ratio=ratio, ubicacion=ubicacion))
            db.session.commit()
            flash('Splitter creado', 'success')
            return redirect(url_for('main.list_splitters'))
    return render_template('form_splitter.html')


@bp.route('/fusiones')
def list_fusiones():
    items = Fusion.query.order_by(Fusion.id.desc()).all()
    return render_template('list_fusiones.html', items=items)


@bp.route('/fusiones/create', methods=['GET', 'POST'])
def create_fusion():
    if request.method == 'POST':
        descripcion = request.form.get('descripcion', '').strip()
        origen_tipo = request.form.get('elemento_origen_tipo', '').strip()
        origen_id = int(request.form.get('elemento_origen_id', '0'))
        destino_tipo = request.form.get('elemento_destino_tipo', '').strip()
        destino_id = int(request.form.get('elemento_destino_id', '0'))
        fibra_origen = request.form.get('fibra_origen')
        fibra_destino = request.form.get('fibra_destino')
        fibra_origen = int(fibra_origen) if fibra_origen else None
        fibra_destino = int(fibra_destino) if fibra_destino else None

        if not descripcion or not origen_tipo or not destino_tipo or origen_id <= 0 or destino_id <= 0:
            flash('Complete todos los campos requeridos', 'danger')
        else:
            db.session.add(Fusion(
                descripcion=descripcion,
                elemento_origen_tipo=origen_tipo,
                elemento_origen_id=origen_id,
                elemento_destino_tipo=destino_tipo,
                elemento_destino_id=destino_id,
                fibra_origen=fibra_origen,
                fibra_destino=fibra_destino,
            ))
            db.session.commit()
            flash('Fusión creada', 'success')
            return redirect(url_for('main.list_fusiones'))

    return render_template('form_fusion.html',
                           olts=OLT.query.all(), odfs=ODF.query.all(), cables=Cable.query.all(),
                           mangas=Manga.query.all(), splitters=Splitter.query.all())
