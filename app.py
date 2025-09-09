"""
Quickbox - Simple web-based file manager built with Flask
Version: 1.0.0
Author: Péricles Sávio
Repository: https://github.com/PericlesSavio/Quickbox
License: GPL-3.0
"""

from flask import Flask, request, redirect, url_for, render_template, send_from_directory, jsonify
import os
from datetime import datetime
from urllib.parse import quote, unquote
from config import Config
from languages import LANGUAGES


app = Flask(__name__)
app.config.from_object(Config)
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def full_upload_path(rel_path=''):
    return os.path.join(app.config['UPLOAD_FOLDER'], rel_path)


def get_items_list(current_path):
    full_path = full_upload_path(current_path)
    items = []

    for name in os.listdir(full_path):
        if not app.config.get('SHOW_HIDDEN_FILES', False) and name.startswith('.'):
            continue
        path = os.path.join(full_path, name)
        rel_path = os.path.join(current_path, name)
        mtime = datetime.fromtimestamp(os.path.getmtime(path)).strftime('%Y-%m-%d %H:%M:%S')
        if os.path.isdir(path):
            items.append({'name': name, 'is_dir': True, 'rel_path': rel_path, 'mtime': mtime})
        else:
            size = os.path.getsize(path)
            ext = os.path.splitext(name)[1][1:].lower() if '.' in name else ''
            items.append({'name': name, 'is_dir': False, 'rel_path': rel_path,
                          'size': f'{size / 1024:.2f} KB', 'ext': ext, 'mtime': mtime})

    return sorted(items, key=lambda x: (not x['is_dir'], x['name'].lower()))


def get_language():
    lang = app.config.get('DEFAULT_LANGUAGE', 'en')
    return LANGUAGES.get(lang, LANGUAGES['en'])


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    path = unquote(path)
    path = path.replace('\\','/').strip('/')
    parts = [p for p in path.split('/') if p]
    parent_path = '/'.join(parts[:-1]) if parts else ''

    items = get_items_list(path)
    texts = get_language()

    return render_template(
        'index.html',
        items=items,
        current_path=path,
        parent_path=parent_path,
        enable_drag_drop=app.config.get('ENABLE_DRAG_DROP', True),
        enable_create_folder=app.config.get('ENABLE_CREATE_FOLDER', True),
        default_theme=app.config.get('DEFAULT_THEME', 'dark'),
        t=texts
    )


@app.route('/upload', methods=['POST'])
def upload_file():
    current_path = request.form.get('current_path', '')
    files = request.files.getlist('file')
    if not files:
        return 'Nenhum arquivo enviado', 400

    for file in files:
        if not file.filename:
            continue
        save_path = os.path.join(full_upload_path(current_path), file.filename)
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        file.save(save_path)

    return redirect(url_for('index', path=current_path))


@app.route('/create_folder', methods=['POST'])
def create_folder():
    t = get_language()

    if not app.config.get('ENABLE_CREATE_FOLDER', True):
        return t['folder_creation_disabled'], 403

    current_path = request.form.get('current_path', '')
    folder_name = request.form.get('folder_name', '').strip()
    if not folder_name:
        return t['invalid_folder_name'], 400
    
    new_folder_path = os.path.join(full_upload_path(current_path), folder_name)
    try:
        os.makedirs(new_folder_path, exist_ok=True)
        return redirect(url_for('index', path=current_path))
    except OSError:
        return t['invalid_folder_name'], 400


@app.route('/uploads/<path:filename>')
def download_file(filename):
    safe_filename = quote(filename)
    return send_from_directory(app.config['UPLOAD_FOLDER'], safe_filename, as_attachment=True)


@app.route('/check_file', methods=['POST'])
def check_file():
    current_path = request.form.get('current_path', '')
    filename = request.form.get('filename', '')
    path = os.path.join(full_upload_path(current_path), filename)
    exists = os.path.exists(path)
    return jsonify({'exists': exists})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
