# **ProCounter** 📊  

ProCounter est un **bot Discord** qui permet de compter de manière ordonnée dans un salon dédié. Il ajoute une réaction ✅ aux nombres valides et supprime uniquement les messages incorrects.

---

## **🚀 Fonctionnalités**  

✔️ Envoie automatiquement `1` au lancement.  
✔️ Vérifie uniquement le **dernier message envoyé** pour éviter les suppressions en chaîne.  
✔️ **Ajoute une réaction ✅** si le message correspond au nombre attendu.  
✔️ **Supprime uniquement** le dernier message incorrect.  

---

## **📦 Installation**  

1️⃣ **Clone le repo**  
```bash
git clone https://github.com/tonpseudo/ProCounter.git
cd ProCounter
```

2️⃣ **Installe les dépendances**  
```bash
pip install discord
```

3️⃣ **Configure ton bot**  
- Remplace **`TOKEN`** par ton **token de bot**  
- Mets l'**ID du salon** où le bot doit fonctionner  

---

## **▶️ Lancer le bot**  
```bash
python main.py
```

---

## **📜 Permissions requises**  
Assure-toi que le bot a les permissions suivantes :  
✅ Lire & Envoyer des messages  
✅ Ajouter des réactions  
✅ Supprimer des messages  

---

## **📌 Améliorations futures**  
- Ajouter une **commande pour reset** le compteur  
- Sauvegarder **l'état du compteur** en cas de redémarrage  
- Ajouter une **interface Web** pour configurer le bot  

---

## **🛠️ Développement**  
- **Python 3.10+**  
- **discord.py 2.3.2**  

