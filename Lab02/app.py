from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher
app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template('index.html')

# Caesar Cipher page
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"<h3>Caesar Encryption</h3>Text: {text}<br/>Key: {key}<br/>Encrypted Text: {encrypted_text}<br/><a href='/caesar'>Back</a>"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"<h3>Caesar Decryption</h3>Text: {text}<br/>Key: {key}<br/>Decrypted Text: {decrypted_text}<br/><a href='/caesar'>Back</a>"

# Vigenere Cipher page
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/encrypt_vigenere", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.vigenere_encrypt(text, key)
    return f"<h3>Vigenère Encryption</h3>Text: {text}<br/>Key: {key}<br/>Encrypted Text: {encrypted_text}<br/><a href='/vigenere'>Back</a>"

@app.route("/decrypt_vigenere", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.vigenere_decrypt(text, key)
    return f"<h3>Vigenère Decryption</h3>Text: {text}<br/>Key: {key}<br/>Decrypted Text: {decrypted_text}<br/><a href='/vigenere'>Back</a>"

@app.route("/railfence")
def railfence():
    return render_template('railfence.html')
@app.route("/encrypt_railfence", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    RailFence = RailFenceCipher()
    encrypted_text = RailFence.rail_fence_encrypt(text, key)
    return f"<h3>Rail Fence Encryption</h3>Text: {text}<br/>Key: {key}<br/>Encrypted Text: {encrypted_text}<br/><a href='/railfence'>Back</a>"
@app.route("/decrypt_railfence", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    RailFence = RailFenceCipher()
    decrypted_text = RailFence.rail_fence_decrypt(text, key)
    return f"<h3>Rail Fence Decryption</h3>Text: {text}<br/>Key: {key}<br/>Decrypted Text: {decrypted_text}<br/><a href='/railfence'>Back</a>"

@app.route("/playfair")
def playfair():
    return render_template('playfair.html')
@app.route("/encrypt_playfair", methods=["POST"])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    Playfair = PlayfairCipher()
    matrix = Playfair.create_playfair_matrix(key)   # Tạo matrix từ key
    encrypted_text = Playfair.playfair_encrypt(text, matrix)
    # Trả về trang kết quả, bạn có thể render template hoặc trả html đơn giản
    return f"<h3>Playfair Encryption</h3>Plain Text: {text}<br>Key: {key}<br>Encrypted Text: {encrypted_text}<br><a href='/playfair'>Back</a>"



    return render_template('playfair.html', encrypted_text=encrypted_text, input_text=text, input_key=key)
    return f"<h3>Playfair Encryption</h3>Text: {text}<br/>Key: {key}<br/>Encrypted Text: {encrypted_text}<br/><a href='/playfair'>Back</a>"
@app.route("/create_matrix", methods=['POST'])
def create_playfair_matrix():
    key = request.form['inputKey']
    Playfair = PlayfairCipher()
    matrix = Playfair.create_playfair_matrix(key)
    # Trả về html hiển thị matrix
    matrix_html = "<h3>Playfair Matrix</h3><table border='1'>"
    for row in matrix:
        matrix_html += "<tr>" + "".join(f"<td>{letter}</td>" for letter in row) + "</tr>"
    matrix_html += "</table><br><a href='/playfair'>Back</a>"
    return matrix_html


@app.route("/decrypt_playfair", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    Playfair = PlayfairCipher()
    matrix = Playfair.create_playfair_matrix(key)  # Tạo matrix từ key
    decrypted_text = Playfair.playfair_decrypt(text, matrix)
    return f"<h3>Playfair Decryption</h3>Cipher Text: {text}<br>Key: {key}<br>Decrypted Text: {decrypted_text}<br><a href='/playfair'>Back</a>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
