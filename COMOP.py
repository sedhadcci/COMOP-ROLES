import streamlit as st
import random

# Liste des participants
participants = [
    "Rania AMORIM", "Sana AZIAR", "Mérouane BEGHDADI", "Rosanna CHADOIN",
    "Arthur CHEN", "Doriane CRISPIN", "Seddik HADJI", "Nathan HATTE",
    "Jean Sé HILBERT", "Patrick HUET", "Justine JOLLY", "Berengère KALASZ",
    "Laetitia MINIEN", "Vincent PERLIN", "Oumou SANOGO", "Hélène SAUZEAU"
]

# Rôles à attribuer
roles = ["Roadmaper", "Scrib", "Time keeper", "Pousse décision", "Meta"]

# Application Streamlit
st.title("Attribution des rôles pour la réunion COMOP")

# Case à cocher pour chaque participant
selected_participants = []
for participant in participants:
    if st.checkbox(participant, key=participant):
        selected_participants.append(participant)

# Bouton pour attribuer les rôles
if st.button("Attribuer les rôles"):
    if len(selected_participants) >= len(roles):
        # Attribution aléatoire des rôles
        assigned_roles = random.sample(selected_participants, len(roles))
        # Affichage des rôles attribués
        for i, role in enumerate(roles):
            st.write(f"{role}: {assigned_roles[i]}")
    else:
        st.error("Pas assez de participants sélectionnés pour tous les rôles.")
