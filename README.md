<h1 style="color:#2c3e50;">📱 Swifty Companion</h1>

<p>
  <b>Swifty Companion</b> est une application mobile développée avec 
  <span style="color:#e67e22;font-weight:bold;">Flutter</span> 
  qui permet de rechercher un étudiant de l'école 
  <b>42</b> et d’afficher son profil grâce à l’<b>API 42</b>.  
  L’application communique avec un 
  <span style="color:#27ae60;font-weight:bold;">serveur Flask</span> 
  qui gère l’authentification <b>OAuth2</b>.
</p>

<h2 style="color:#2c3e50;">🚀 Fonctionnalités</h2>
<ul>
  <li>🔍 Recherche d’un étudiant via son <b>login 42</b></li>
  <li>👤 Affichage du <b>profil complet</b> (login, email, niveau, wallet, photo…)</li>
  <li>📊 Visualisation des <b>compétences</b></li>
  <li>📂 Liste des <b>projets réussis et échoués</b></li>
  <li>⚠️ Gestion des erreurs (login introuvable, problème réseau, etc.)</li>
  <li>🔑 Authentification sécurisée via <b>OAuth2</b></li>
</ul>

<h2 style="color:#2c3e50;">🛠️ Technologies utilisées</h2>
<ul>
  <li><b>Frontend :</b> <span style="color:#e67e22;">Flutter (Dart)</span></li>
  <li><b>Backend :</b> <span style="color:#27ae60;">Flask (Python)</span>, OAuth2, 42 API</li>
  <li><b>Outils :</b> Android Studio, Git, <code>.env</code></li>
</ul>

<h2 style="color:#2c3e50;">📐 Architecture</h2>
<div style="margin:20px 0; padding:10px; border:1px solid #ddd; border-radius:6px; background:#fafafa; text-align:center;">
  <span style="background:#3498db; color:white; padding:8px 12px; border-radius:4px;">Mobile App (Flutter)</span>
  <span style="margin:0 10px; font-weight:bold;">⇆</span>
  <span style="background:#2ecc71; color:white; padding:8px 12px; border-radius:4px;">Backend (Flask)</span>
  <span style="margin:0 10px; font-weight:bold;">⇆</span>
  <span style="background:#9b59b6; color:white; padding:8px 12px; border-radius:4px;">42 API</span>
</div>

<h2 style="color:#2c3e50;">⚙️ Installation</h2>

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

⚠️ Ajoute un fichier <code>.env</code> dans le backend :
<pre><code>API_UID=your_42_api_uid
API_SECRET=your_42_api_secret
</code></pre>

<h2 style="color:#2c3e50;">✅ État du projet</h2>
<p>✔️ Projet fonctionnel – améliorations prévues (UI/UX)</p>

<h2 style="color:#2c3e50;">📄 Licence</h2>
<p>Projet réalisé dans le cadre de mon cursus à l’école <b>42</b>.</p>
