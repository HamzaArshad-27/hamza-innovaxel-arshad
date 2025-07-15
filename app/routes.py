from flask import Blueprint, request, jsonify
from . import db
from .models import URL
from .utils import generate_shortcode

bp = Blueprint('api', __name__, url_prefix='/')

@bp.route('/shorten', methods=['POST'])
def create_short_url():
    data = request.json
    original_url = data.get('url')
    if not original_url:
        return jsonify({'error': 'URL is required'}), 400

    short_code = generate_shortcode()
    new_url = URL(url=original_url, short_code=short_code)
    db.session.add(new_url)
    db.session.commit()

    return jsonify({
        'id': new_url.id,
        'url': new_url.url,
        'shortCode': new_url.short_code,
        'createdAt': new_url.created_at.isoformat(),
        'updatedAt': new_url.updated_at.isoformat()
    }), 201

@bp.route('/shorten/<string:short_code>', methods=['GET'])
def get_original_url(short_code):
    url_obj = URL.query.filter_by(short_code=short_code).first()
    if not url_obj:
        return jsonify({'error': 'Short URL not found'}), 404

    url_obj.access_count += 1
    db.session.commit()

    return jsonify({
        'id': url_obj.id,
        'url': url_obj.url,
        'shortCode': url_obj.short_code,
        'createdAt': url_obj.created_at.isoformat(),
        'updatedAt': url_obj.updated_at.isoformat()
    })

@bp.route('/shorten/<string:short_code>', methods=['PUT'])
def update_url(short_code):
    data = request.json
    updated_url = data.get('url')
    url_obj = URL.query.filter_by(short_code=short_code).first()

    if not url_obj:
        return jsonify({'error': 'Short URL not found'}), 404

    if not updated_url:
        return jsonify({'error': 'URL is required'}), 400

    url_obj.url = updated_url
    db.session.commit()

    return jsonify({
        'id': url_obj.id,
        'url': url_obj.url,
        'shortCode': url_obj.short_code,
        'createdAt': url_obj.created_at.isoformat(),
        'updatedAt': url_obj.updated_at.isoformat()
    })

@bp.route('/shorten/<string:short_code>', methods=['DELETE'])
def delete_url(short_code):
    url_obj = URL.query.filter_by(short_code=short_code).first()
    if not url_obj:
        return '', 404
    db.session.delete(url_obj)
    db.session.commit()
    return '', 204

@bp.route('/shorten/<string:short_code>/stats', methods=['GET'])
def url_stats(short_code):
    url_obj = URL.query.filter_by(short_code=short_code).first()
    if not url_obj:
        return jsonify({'error': 'Short URL not found'}), 404

    return jsonify({
        'id': url_obj.id,
        'url': url_obj.url,
        'shortCode': url_obj.short_code,
        'createdAt': url_obj.created_at.isoformat(),
        'updatedAt': url_obj.updated_at.isoformat(),
        'accessCount': url_obj.access_count
    })
from flask import render_template, redirect, url_for

@bp.route("/", methods=["GET", "POST"])
def home():
    short_url = None
    error = None
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            short_code = generate_shortcode()
            new_url = URL(url=url, short_code=short_code)
            db.session.add(new_url)
            db.session.commit()
            short_url = request.host_url + 'shorten/' + short_code
        else:
            error = "URL is required"

    return render_template("index.html", short_url=short_url, error=error)
