from flask import Flask, request, render_template, send_from_directory

app = Flask(__name)

@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST' and 'image' in request.files:
        image = request.files['image']
        if image:
            # 이미지 업로드 처리 (이미지를 업로드 폴더에 저장)
            image.save("static/uploaded_image.jpg")

    return render_template('upload.html')

@app.route('/download')
def download_image():
    return send_from_directory('static', 'uploaded_image.jpg', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)