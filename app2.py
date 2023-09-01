import streamlit as st
import folium
from geopy.geocoders import Nominatim
from streamlit_folium import folium_static
import req_api as api

#create the page of the web app
st.set_page_config(page_title = "Weather",
                   layout = "wide", 
                   )

st.title("Localisateur de Ville")

    # Saisie du nom de la ville
ville = st.text_input("Entrez le nom de la ville :",value= "Paris")

col1, col2 = st.columns(2)

with col1:
    metric = st.selectbox("Choose unit metric", options= ["degrée Celsius", "degrée Farhneit", "Kelvin"])
    if metric == "degrée Celsius" :
        unit = "metric"
        unit_sign = "°C"
    elif metric == "degrée Farhneit" :
        unit = "imperial"
        unit_sign = "°F"
    elif metric == "Kelvin" :
        unit = ""
        unit_sign = "K"
        
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
    data = api.weather(ville, unit)
    temp = data["Temperature"].values[0] 
    st.header(f"{temp} {unit_sign}" )
    st.write(data["Description"].values[0])
    icon = data["icon"].values[0]
    st.image(f"https://openweathermap.org/img/wn/{icon}@2x.png")
    st.metric(label="Feels Like", value=data["Feels Like"])
    st.metric(label="Min Temperature", value=data["Min Temperature"])
    st.metric(label="Max Temperature", value=data["Max Temperature"])
    st.metric(label="Humidity", value=data["Humidity"])
   
    

