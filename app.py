from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>Chinese Subtitle App</h2>
    <p>Dán link YouTube video tiếng Trung:</p>
    <input style='width:90%' placeholder='https://youtu.be/...' />
    <br><br>
    <button>Tạo phụ đề</button>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
