from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    # هذا السطر هو السحر اللي يخلي الموقع يقرأ ملفك الطويل من داخل مجلد templates
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
