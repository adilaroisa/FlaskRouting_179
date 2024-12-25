from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route untuk halaman sukses (sambutan)
@app.route('/success/<name>')
def success(name):
    return render_template('success.html', name=name)

# Route untuk halaman login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['nm']  # Mengambil data nama dari form
        return redirect(url_for('success', name=name))  # Redirect ke halaman sukses
    return render_template('index.html')  # Menampilkan form login (index.html)

if __name__ == '__main__':
    app.run(debug=True)
