"""Rebuild the homepage from real, locally present editions. No network or publishing."""
from datetime import date
from html import escape
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
editions = json.loads((DOCS / 'ediciones.json').read_text())
assert editions, 'Añade al menos una edición real.'
seen = set()
for edition in editions:
    date.fromisoformat(edition['date'])
    assert edition['date'] not in seen, 'Fecha duplicada.'
    seen.add(edition['date'])
    file = edition['file']
    assert file.startswith('ediciones/') and '..' not in file and file.endswith('.html')
    assert (DOCS / file).is_file(), f'No existe {file}'
editions.sort(key=lambda e: e['date'], reverse=True)
latest = editions[0]
months = ['', 'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

def display_date(iso):
    d = date.fromisoformat(iso)
    return f'{d.day} de {months[d.month]} de {d.year}'

cards = '\n'.join(f'''<li class="edition"><div><p class="eyebrow">Día {int(e['day'])} · <time datetime="{e['date']}">{display_date(e['date'])}</time></p><h3><a href="{escape(e['file'], quote=True)}">{escape(e['title'])} <span aria-hidden="true">↗</span></a></h3><p>{escape(e['description'])}</p></div><span class="duration">{escape(e['minutes'])} min</span></li>''' for e in editions)
page = f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"><meta name="color-scheme" content="dark"><meta name="theme-color" content="#0b1220"><meta name="description" content="Tu biblioteca de clases interactivas para entender la NFL: reglas, jugadores, formaciones y práctica a tu ritmo."><title>NFL Academy · Tu campo de aprendizaje</title><link rel="icon" href="assets/icon.svg" type="image/svg+xml"><link rel="stylesheet" href="assets/home.css"></head>
<body><a class="skip" href="#contenido">Saltar al contenido</a><div class="page"><header class="masthead"><a class="brand" href="index.html" aria-label="NFL Academy, inicio"><span class="brand-icon" aria-hidden="true">A</span><span>NFL <b>ACADEMY</b></span></a><a class="archive-link" href="#ediciones">Ver ediciones <span aria-hidden="true">↓</span></a></header>
<main id="contenido"><section class="hero" aria-labelledby="hero-title"><div class="hero-copy"><p class="eyebrow">Aprende · Observa · Practica</p><h1 id="hero-title">Entiende el juego.<br><span>Disfruta cada jugada.</span></h1><p class="intro">Tu academia de NFL, a tu ritmo. Reglas claras, caras conocidas y ejercicios para leer lo que pasa en el campo.</p><a class="button" href="{escape(latest['file'], quote=True)}">Abrir la última clase <span aria-hidden="true">→</span></a><p class="latest">Última edición disponible: <time datetime="{latest['date']}">{display_date(latest['date'])}</time> · Día {int(latest['day'])}</p></div><div class="field" aria-hidden="true"><div class="field-caption">TU PRÓXIMA JUGADA<br><strong>Aprender algo nuevo.</strong></div><svg viewBox="0 0 360 280" xmlns="http://www.w3.org/2000/svg"><g fill="none" stroke="#355a78"><path d="M30 25V265M90 25V265M150 25V265M210 25V265M270 25V265M330 25V265"/><path d="M20 70H340M20 140H340M20 210H340" stroke-dasharray="4 12"/></g><path d="M70 240V170Q70 140 110 140H255" fill="none" stroke="#ffd680" stroke-width="5" stroke-linecap="round"/><path d="m240 125 17 15-17 15" fill="none" stroke="#ffd680" stroke-width="5" stroke-linecap="round"/><g fill="#142c45" stroke="#80caff" stroke-width="3"><circle cx="70" cy="240" r="12"/><circle cx="135" cy="240" r="12"/><circle cx="200" cy="240" r="12"/><circle cx="265" cy="240" r="12"/></g><g stroke="#8bd7b2" stroke-width="3" stroke-linecap="round"><path d="m58 91 18 18m0-18-18 18m75-18 18 18m0-18-18 18m75-18 18 18m0-18-18 18m75-18 18 18m0-18-18 18"/></g></svg></div></section>
<section class="features" aria-label="Cómo es la academia"><p><span aria-hidden="true">01</span> Explicaciones en español</p><p><span aria-hidden="true">02</span> Simuladores y práctica</p><p><span aria-hidden="true">03</span> Exámenes con corrección</p></section>
<section id="ediciones" class="library" aria-labelledby="library-title"><div class="section-heading"><div><p class="eyebrow">Tu biblioteca</p><h2 id="library-title">Entra al campo.</h2></div><span class="count">{len(editions)} {'edición' if len(editions)==1 else 'ediciones'}</span></div><ul class="editions">{cards}</ul><p class="archive-note">Cada clase conserva su fecha. Sus horarios, noticias y estadísticas corresponden a esa edición.</p></section>
<section class="how" aria-labelledby="how-title"><h2 id="how-title">Un enlace. Tu academia.</h2><p>Abre una clase, prueba los controles y completa el examen cuando estés listo. Las fotos tienen un enlace para verlas en grande.</p><details><summary>Guárdala en tu iPhone o iPad</summary><p>Abre esta página en Safari. En el menú <strong>Compartir</strong>, elige <strong>Añadir a pantalla de inicio</strong> o guárdala en favoritos. Necesitas internet para abrir las clases y cargar las fotografías.</p></details><details><summary>¿Dónde se guardan mis respuestas?</summary><p>El examen se corrige en tu navegador. Pulsa <strong>Copiar resultado</strong> y pégalo en tu chat de estudio si quieres registrar tu avance. Este sitio no envía tus respuestas ni las sincroniza entre dispositivos.</p></details></section>
</main><footer><p><b>NFL Academy</b> · Aprende a tu ritmo.</p><p>Proyecto educativo independiente, sin afiliación con la NFL. Fotografías y marcas pertenecen a sus titulares.</p></footer></div></body></html>'''
(DOCS / 'index.html').write_text(page)
(DOCS / '.nojekyll').touch()
print(f'Portada actualizada: {len(editions)} edición(es); última {latest["date"]}.')
