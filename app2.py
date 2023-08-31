import streamlit as st
import folium
from geopy.geocoders import Nominatim
from streamlit_folium import folium_static



st.title("Localisateur de Ville")

    # Saisie du nom de la ville
ville = st.text_input("Entrez le nom de la ville :")

col1, col2 = st.columns([1, 2])

with col1:
    if ville:
        # Obtenir les coordonnées de la ville à partir de son nom
        geolocalisation = Nominatim(user_agent="city_locator")
        location = geolocalisation.geocode(ville)

        if location:
            st.write(f"localisation de **{ville}**:")
            #st.write(f"Latitude: {location.latitude}, Longitude: {location.longitude}")


            carte = folium.Map(location=[location.latitude, location.longitude], zoom_start=10)
            folium.Marker([location.latitude, location.longitude], popup=ville).add_to(carte)

            # Afficher la carte
            folium_static(carte)
        else:
            st.write("Impossible de trouver la ville.")

with col2 :
    st.markdown('**74**')


    KPI = [
                ("indic 1", "1"),
                ("indic 2", "2"),
                ("indic 3", "3"),
                # Ajoutez d'autres KPI ici
            ]
    for valeur in KPI:
                st.markdown(
                    f"{valeur}"
                )
