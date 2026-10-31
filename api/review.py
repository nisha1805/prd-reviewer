import json, os, sys, pathlib, hmac
from http.server import BaseHTTPRequestHandler

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from src.review import review, clean, norm  # noqa: E402

MAX_CHARS = 60000


class handler(BaseHTTPRequestHandler):
    def _send(self, status, payload):
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", 0))
            if length > 200000:
                return self._send(413, {"error": "Request too large."})
            data = json.loads(self.rfile.read(length) or b"{}")
        except Exception:
            return self._send(400, {"error": "Invalid request."})

        expected = os.environ.get("ACCESS_CODE", "")
        given = str(data.get("code", ""))
        if not expected or not hmac.compare_digest(given.encode(), expected.encode()):
            return self._send(401, {"error": "Wrong or missing access code."})

        text = clean(str(data.get("text", "")))
        if len(text.strip()) < 200:
            return self._send(400, {"error": "Please paste a full PRD (at least 200 characters)."})
        if len(text) > MAX_CHARS:
            return self._send(400, {"error": "Document too long (max %d characters)." % MAX_CHARS})

        try:
            findings, usage = review(text)
        except Exception:
            return self._send(502, {"error": "The review failed. Please try again."})

        for f in findings:
            ev = f.get("evidence", "")
            f["quote_ok"] = ev == "" or norm(ev) in norm(text)
        self._send(200, {"findings": findings,
                         "tokens_in": usage.input_tokens,
                         "tokens_out": usage.output_tokens})
