import streamlit as st
import random

# Liste des participants avec le nom mis à jour
participants = [
    "Rania AMORIM", "Sana AZIAR", "Mérouane BEGHDADI", "Rosanna CHADOIN",
    "Arthur CHEN", "Doriane CRISPIN", "Seddik HADJI", "Nathan HATTE",
    "Jean Sébastien HILBERT", "Patrick HUET", "Justine JOLLY", "Berengère KALASZ",
    "MOUTON Benoit", "Vincent PERLIN", "Oumou SANOGO", "Hélène SAUZEAU" , "CIROTTEAU Axel"
]

# Rôles à attribuer
roles = ["Roadmaper", "Scrib", "Time keeper", "Pousse décision"]

# Application Streamlit
st.title("Attribution des rôles pour la réunion COMOP")

# Case à cocher pour chaque participant, cochée par défaut
selected_participants = {participant: st.checkbox(participant, key=participant, value=True) for participant in participants}

# Logique personnalisée d'attribution des rôles
def assign_roles(participants, roles):
    # Gérer le rôle 'Meta'
    if "Nathan HATTE" in participants and random.random() < 0.99:
        meta_role = "Nathan HATTE"
    else:
        meta_candidates = [p for p in ["MOUTON Benoit", "Arthur CHEN"] if p in participants]
        meta_role = random.choice(meta_candidates) if meta_candidates else None

    # Exclure le participant du rôle 'Meta' et 'Seddik HADJI' pour les autres rôles
    remaining_participants = [p for p in participants if p != meta_role and p != "Seddik HADJI"]

    # Réduire la probabilité que Seddik HADJI soit sélectionné
    if "Seddik HADJI" in participants:
        if random.random() < 0.2:  # 20% de chance d'inclure Seddik HADJI dans le tirage
            remaining_participants.append("Seddik HADJI")

    # Attribuer les rôles restants
    assigned_roles = random.sample(remaining_participants, len(roles))
    return assigned_roles, meta_role

# Bouton pour attribuer les rôles
if st.button("Attribuer les rôles"):
    present_participants = [p for p, present in selected_participants.items() if present]
    if len(present_participants) >= len(roles):
        assigned_roles, meta_role = assign_roles(present_participants, roles)
        # Afficher les rôles attribués
        for role, participant in zip(roles, assigned_roles):
            st.write(f"{role}: {participant}")
        if meta_role:
            st.write(f"Meta: {meta_role}")
    else:
        st.error("Pas assez de participants sélectionnés pour tous les rôles.")
