from flask import Flask, request, Response

app = Flask(__name__)


@app.route("/headers")
def headers_processing():
    content_type = request.headers.get('Content-Type')

    if content_type == 'application/json':
        return {"currency": "USD", "rate": 41.5}  # Flask автоматично конвертує dict в JSON
    elif content_type == 'application/xml':
        xml_data = '<data><currency>USD</currency><rate>41.5</rate></data>'
        return Response(xml_data, mimetype='application/xml')
    else:
        return "USD - 41.5 (Plain Text)"


if __name__ == '__main__':
    app.run(port=8000)