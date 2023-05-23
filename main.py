from flask import Flask, send_file
from io import BytesIO
from barcode import EAN13
from barcode.writer import ImageWriter

app = Flask(__name__)


@app.route('/generate_barcode')
def generate_barcode():
    # Generate barcode and write to a BytesIO object (Write to a file-like object:)
    barcode_data = "100000902922"
    barcode_image = BytesIO()
    EAN13(barcode_data, writer=ImageWriter()).write(barcode_image)

    # Return the barcode image as a response
    barcode_image.seek(0)
    return send_file(barcode_image, mimetype='image/jpeg')


@app.route('/generate_barcode_file')
def generate_barcode_file():
    # Generate barcode and save it to a file(Write to an actual file)
    barcode_data = "100000011111"
    filename = "barcode.jpeg"
    EAN13(barcode_data, writer=ImageWriter()).write(filename)

    # Return the file as a response
    return send_file(filename, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run()