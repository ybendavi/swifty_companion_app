<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Swifty Companion - README</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      max-width: 900px;
      margin: auto;
      padding: 20px;
      color: #333;
    }
    h1, h2, h3 {
      color: #2c3e50;
    }
    code, pre {
      background: #f4f4f4;
      padding: 6px 10px;
      border-radius: 4px;
      font-size: 0.9em;
    }
    .archi {
      margin: 30px 0;
      padding: 20px;
      border: 1px solid #ddd;
      border-radius: 8px;
      background: #fafafa;
      text-align: center;
    }
    .archi span {
      display: inline-block;
      margin: 0 15px;
      padding: 10px 15px;
      background: #3498db;
      color: white;
      border-radius: 6px;
    }
    .arrow {
      font-weight: bold;
      margin: 0 10px;
      color: #2c3e50;
    }
  </style>
</head>
<body>

  <h1>📱 Swifty Companion</h1>

  <p>
    <b>Swifty Companion</b> est une application mobile développée avec <b>Flutter</b> qui permet de rechercher un étudiant de l'école <b>42</b> et d’afficher son profil grâce à l’<b>API 42</b>.  
    L’application communique avec un <b>serveur Flask</b> qui gère l’authentification <b>OAuth2</b> et les requêtes à l’API.
  </p>

  <h2>🚀 Fonctionnalités</h2>
  <ul>
    <li>🔍 Recherche d’un étudiant via son <b>login 42</b></li>
    <li>👤 Affichage du <b>profil complet</b> : login, email, niveau, wallet, évaluations, photo, etc.</li>
    <li>📊 Visualisation des <b>compétences</b> avec niveaux et pourcentages</li>
    <li>📂 Liste des <b>projets réalisés et échoués</b></li>
    <li>⚠️ Gestion des erreurs (login introuvable, problème réseau, etc.)</li>
    <li>📱 Interface responsive adaptée à différentes tailles d’écrans</li>
    <li>🔑 Authentification sécurisée via <b>OAuth2</b> (avec rafraîchissement de token)</li>
  </ul>

  <h2>🛠️ Technologies utilisées</h2>
  <ul>
    <li><b>Frontend :</b> Flutter (Dart)</li>
    <li><b>Backend :</b> Flask (Python), OAuth2, 42 API</li>
    <li><b>Outils :</b> Android Studio, Git, fichiers .env</li>
  </ul>

  <h2>📐 Architecture</h2>
  <div class="archi">
    <span>Mobile App (Flutter)</span>
    <span class="arrow">⇆</span>
    <span>Backend (Flask)</span>
    <span class="arrow">⇆</span>
    <span>42 API</span>
  </div>

  <h2>⚙️ Installation</h2>

  <h3>Backend (Flask)</h3>
  <pre><code>git clone https://github.com/ton-compte/swifty-companion.git
cd backend
pip install -r requirements.txt
flask run
</code></pre>

  <h3>Frontend (Flutter)</h3>
  <pre><code>cd frontend
flutter pub get
flutter run
</code></pre>

  <p>⚠️ Crée un fichier <code>.env</code> dans le backend avec tes identifiants API 42 :</p>
  <pre><code>API_UID=your_42_api_uid
API_SECRET=your_42_api_secret
</code></pre>

  <h2>✅ État du projet</h2>
  <p>✔️ Projet fonctionnel – en cours d’amélioration avec de nouvelles fonctionnalités (UI/UX, gestion avancée des tokens, etc.)</p>

  <h2>📄 Licence</h2>
  <p>Projet réalisé dans le cadre de l’école <b>42</b>. Libre pour usage personnel et académique.</p>

</body>
</html>
