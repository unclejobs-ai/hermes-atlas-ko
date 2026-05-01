#!/usr/bin/env python3
"""Local static server that mimics Vercel cleanUrls for Hermes Atlas."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class CleanURLHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        raw = path.split('?', 1)[0].split('#', 1)[0]
        translated = Path(super().translate_path(path))
        if translated.exists():
            return str(translated)
        if not raw.endswith('/'):
            html_candidate = ROOT / raw.lstrip('/').replace('%20', ' ')
            html_candidate = html_candidate.with_suffix(html_candidate.suffix + '.html') if html_candidate.suffix else Path(str(html_candidate) + '.html')
            if html_candidate.exists():
                return str(html_candidate)
        index_candidate = ROOT / raw.lstrip('/') / 'index.html'
        if index_candidate.exists():
            return str(index_candidate)
        return str(translated)

if __name__ == '__main__':
    import os
    os.chdir(ROOT)
    port = 4173
    server = ThreadingHTTPServer(('127.0.0.1', port), CleanURLHandler)
    print(f'Serving Hermes Atlas KO at http://127.0.0.1:{port}')
    server.serve_forever()
