"""Genera index.html (la app lista para usar) a partir de src/app.src.html y las fotos de src/img/.

Uso:  python3 build.py
"""
import base64, pathlib

RAIZ = pathlib.Path(__file__).parent
FOTOS = {
    '__FOTO1__': 'foto1_ensamble_perfil.jpg', '__FOTO2__': 'foto2_ensamble_frente.jpg',
    '__FOTO3__': 'foto3_calidad_amarillo.jpg', '__FOTO4__': 'foto4_estacion_verde.jpg',
    '__FOTO5__': 'foto5_bodega_carga.jpg', '__FOTO6__': 'foto6_portada.jpg',
    '__MUESTRA_PERFIL__': 'muestra_perfil.jpg', '__MUESTRA_FRENTE__': 'muestra_frente.jpg',
    '__MUESTRA_DETALLE__': 'muestra_detalle.jpg',
}
HEAD = ('<!doctype html><html lang="es"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="description" content="APLOMO. Evaluación ergonómica de puestos de trabajo con el método RULA: fotos, ángulos, puntaje y resultados.">'
        '<meta name="theme-color" content="#0B0B0C"></head><body>')

app = (RAIZ / 'src' / 'app.src.html').read_text(encoding='utf-8')
for marca, archivo in FOTOS.items():
    assert marca in app, f'falta {marca} en app.src.html'
    datos = base64.b64encode((RAIZ / 'src' / 'img' / archivo).read_bytes()).decode()
    app = app.replace(marca, 'data:image/jpeg;base64,' + datos)
(RAIZ / 'index.html').write_text(HEAD + app + '</body></html>', encoding='utf-8')
print('index.html listo:', round(len(app) / 1e6, 1), 'MB')
