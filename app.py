from flask import Flask, request, render_template
import qrcode
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    data = request.form['data']
    
    # Generate QR code
    img = qrcode.make(data)
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    
    # Encode the image in base64 to display in the template
    img_data = base64.b64encode(img_io.getvalue()).decode('utf-8')
    base64_img = f'data:image/png;base64,{img_data}'
    
    return render_template('index.html', qr_code_url=base64_img)

if __name__ == '__main__':
    app.run(debug=True)
