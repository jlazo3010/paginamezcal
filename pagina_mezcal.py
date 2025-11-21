import streamlit as st
import urllib.parse
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return encoded

img_data = get_base64_image("mezcal2.jpg")
img_m1 = get_base64_image("mezcal1.jpg")
img_m5 = get_base64_image("mezcal5.jpg")

st.set_page_config(page_title="Mezcal Novena Entrada ⚾🔥", page_icon="🌿", layout="wide")

st.markdown("""
<div class="finaliza-sidebar">
    Finaliza tu pedido aquí 👉 
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* Título principal en blanco */
.titulo-principal {
    font-size: 10rem;
    color: white !important;
    text-shadow: 2px 2px 7px rgba(0,0,0,1);
    font-weight: bold;
    padding-bottom: 10px;
    border-bottom: 3px solid white;
    margin-bottom: 30px;
    text-align: centered;
}

/* Texto blanco en el contenido principal */
html, body, .main, .block-container {
    font-family: 'Segoe UI', sans-serif;
    background-color: #871000 !important;
    color: white !important;
    padding: 0;
    margin: 70px;
    overflow-x: hidden !important;
    box-sizing: border-box;
}

/* Estilo para contenedores de mezcales */
.mezcal-container {
    background-color: #ffbc00 !important;
    padding: 15px !important;
    border-radius: 10px !important;
    margin: 10px 0 !important;
    color: white !important;
}

.block-container {
    margin: auto !important;
    padding-top: 4rem;
    padding-left: 5rem;
    padding-right: 5rem;
}            
            
/* Texto negro en elementos específicos dentro de contenedores de mezcal */
.mezcal-container * {
    color: black !important;
}

/* Aviso fijo en pantalla para dirigir al sidebar */
.finaliza-sidebar {
    position: fixed;
    top: 40%;
    left: 5px;
    background-color: #004d01;
    color: white;
    font-weight: bold;
    padding: 10px 15px;
    border-radius: 8px;
    transform: rotate(-90deg);
    transform-origin: left top;
    z-index: 9999;
    box-shadow: 0 4px 10px rgba(0,0,0,0.4);
}

/* Sidebar: fondo verde oscuro */
[data-testid="stSidebar"] {
    background-color: #105500;
}

/* Texto blanco en el sidebar */
[data-testid="stSidebar"] * {
    color: white !important;
}

/* Centrar imágenes */
img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    max-width: 100%;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}
            
label, .stNumberInput label {
    color: white !important;
}            

/* Encabezados centrados */
h2, h3 {
    text-align: center;
    color: white !important;
}
            
/* Estilo general del expander */
[data-testid="stExpander"] {
    background-color: #ffbc00 !important;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    color: black !important;
    transition: all 0.4s ease-in-out;
    overflow: hidden;
}

/* Estilo general del expander */
[data-testid="stExpander"] {
    background-color: #ffbc00 !important;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(255, 188, 0, 0.4);
    color: black !important;
    animation: glow 2s infinite ease-in-out;
    transition: all 0.4s ease-in-out;
    overflow: hidden;
}

/* Título del expander */
[data-testid="stExpander"] > div:first-child {
    background-color: #ffbc00 !important;
    color: black !important;
    font-size: 3rem;
    font-weight: bold;
    transition: background-color 0.3s ease;
}

/* Contenido del expander */
[data-testid="stExpander"] .streamlit-expanderContent {
    color: black !important;
    background-color: #fff3c2 !important;
    border-top: 1px solid rgba(0,0,0,0.2);
}

/* Animación de "glow" */
@keyframes glow {
    0% {
        box-shadow: 0 0 10px rgba(255, 188, 0, 0.3);
    }
    50% {
        box-shadow: 0 0 25px rgba(255, 188, 0, 0.8);
    }
    100% {
        box-shadow: 0 0 10px rgba(255, 188, 0, 0.3);
    }
}         
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([5, 2])  # Ajusta proporción a tu gusto

with col1:
    st.markdown(
        """
        <h1 class='titulo-principal'>🔥 Mezcal Novena Entrada ⚾</h1>
        <p style='color: white; font-size: 1.5rem; margin-top: 10px;'>
            Haz tu pedido directo por WhatsApp 📱
        </p>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.image("logo_mezcal.png", width=300)

mezcales = {
    "Espadín": {
        "litro": 450, "medio": 250,
        "desc": "Versátil y balanceado. Notas ahumadas suaves, hierbas y cítricos.",
        "coctel": "Ideal para un Mezcal Mule o Paloma de mezcal.",
        "maridaje": "Tacos al pastor, quesos semimaduros, frutas cítricas."
    },
    "Tobalá": {
        "litro": 600, "medio": 350,
        "desc": "Silvestre, elegante y floral. Dulzón, con fondo sutilmente ahumado.",
        "coctel": "Va increíble en un Negroni de mezcal o solo en copa.",
        "maridaje": "Ceviches, mariscos, queso de cabra."
    },
    "Cuishe": {
        "litro": 600, "medio": 350,
        "desc": "Herbal y seco, con perfil vegetal y especiado.",
        "coctel": "Perfecto en un Mezcal Sour con hierbabuena.",
        "maridaje": "Carnes asadas, hongos salteados, moles suaves."
    },
    "Tepextate": {
        "litro": 600, "medio": 350,
        "desc": "Notas intensas de espárrago, pimiento y especias. Complejo y exótico.",
        "coctel": "Maravilloso en un Martini ahumado o Old Fashioned de mezcal.",
        "maridaje": "Mole negro, chocolate amargo, cocina oaxaqueña."
    },
    "Jabalí": {
        "litro": 1000, "medio": 550,
        "desc": "Potente, raro y explosivo. Especias, fermento y dulzor profundo.",
        "coctel": "Prueba el 'Selva de Jabalí' con mango y chile ancho.",
        "maridaje": "Carnes curadas, platos con umami, postres con nuez."
    },
    "Guajolote y Frutos Amarillos": {
        "litro": 700, "medio": 400,
        "desc": "Infusionado con frutas tropicales. Jugoso, dulce y exótico.",
        "coctel": "Excelente en una Margarita tropical o con soda.",
        "maridaje": "Tostadas de atún, platos con curry, postres frutales."
    },
    "Abocado con Gusano de Maguey": {
        "litro": 700, "medio": 400,
        "desc": "Robusto y terroso. El gusano aporta carácter salado y ahumado.",
        "coctel": "Prueba el 'Fuego del Maguey' con naranja y chile.",
        "maridaje": "Chapulines, sal de gusano, tacos dorados."
    }
}

st.markdown("### 🛒 Elige tus mezcales")

st.markdown(
    "<hr style='border: 1px solid #fcad00;'>",
    unsafe_allow_html=True
)
 
pedido = []

cols = st.columns(2)
for i, (nombre, info) in enumerate(mezcales.items()):
    with cols[i % 2].container():
        st.markdown('<div class="mezcal-container">', unsafe_allow_html=True)
        st.markdown(f"#### 🌿 {nombre} 🔥")
        st.markdown(f"**Descripción:** {info['desc']}")
        st.markdown(f"**Coctel sugerido:** {info['coctel']}")
        st.markdown(f"**Maridaje recomendado:** {info['maridaje']}")
        
        # Mostrar imagen en un expander
        with st.expander("Recomendación de coctail 🥃🔥"):
            img_path = f"{i+1}.png"
            st.image(img_path, use_container_width=True)
        
        litro = st.number_input(f"**Precio 1L:** ${info['litro']:,.0f}", min_value=0, max_value=10, key=nombre + "l")
        medio = st.number_input(f"**Precio 1/2L:** ${info['medio']:,.0f}", min_value=0, max_value=10, key=nombre + "m")
        if litro > 0:
            pedido.append((f"{litro}L de {nombre}", info["litro"] * litro))
        if medio > 0:
            pedido.append((f"{medio} x 1/2L de {nombre}", info["medio"] * medio))
        st.markdown('</div>', unsafe_allow_html=True)
            
st.markdown(
    "<hr style='border: 1px solid #fcad00;'>",
    unsafe_allow_html=True
)

st.markdown(
            f"""
            <div style='text-align: center;'>
                <img src='data:image/jpeg;base64,{img_m1}' width='500'>
            </div>
            """,
            unsafe_allow_html=True
        )

            
st.markdown(
    "<hr style='border: 1px solid #fcad00;'>",
    unsafe_allow_html=True
)
            
# Promociones con descripción y ocasión
promos = {
    "Dúo de la Casa": {
        "precio": 500,
        "Tipo": "Un balance entre lo clásico y lo silvestre.",
        "desc": "1/2L de Espadín + 1/2L de Tobalá.",
        "ocasion": "Perfecto para regalar o una noche tranquila entre amigos."
    },
    "Bestia & Agave": {
        "precio": 700,
        "Tipo": "Fuerza salvaje con suavidad tradicional.",
        "desc": "1/2L de Jabalí + 1/2L de Espadín.",
        "ocasion": "Pensado para momentos intensos, comidas potentes o celebrar un logro."
    },
    "Trilogía Silvestre": {
        "precio": 950,
        "Tipo": "Para explorar lo mejor del agave silvestre.",
        "desc": "3 medios litros: Cuishe, Tobalá y Tepextate.",
        "ocasion": "Ideal para catas o para sorprender a alguien especial."
    },
    "Fiesta de Sabores": {
        "precio": 1100,
        "Tipo": "Un viaje por sabores únicos.",
        "desc": "1/2L de Espadín + 1/2L de Tobalá + 1/2L de Cuishe + 1/2L de Tepextate.",
        "ocasion": "Una noche larga, con música, mezcal y buena compañía."
    },
    "Ruta del Agave": {
        "precio": 900,
        "Tipo": "Del campo a la copa.",
        "desc": "1L de Guajolote y frutos amarillos + 1/2L de Abocado con gusano de maguey.",
        "ocasion": "Reunión informal o precopeo con personalidad."
    }
}

st.markdown("### 🎁 Promociones especiales")

promo_cols = st.columns(2)
for i, (promo_nombre, promo_info) in enumerate(promos.items()):
    with promo_cols[i % 2].container():
        st.markdown('<div class="mezcal-container">', unsafe_allow_html=True)
        st.markdown(f"#### 🎉 {promo_nombre}: {promo_info['Tipo']}")
        st.markdown(f"**Precio:** ${promo_info['precio']:,.0f}")
        st.markdown(f"**Contiene:** {promo_info['desc']}")
        st.markdown(f"**Ocasión recomendada:** {promo_info['ocasion']}")
        cantidad = st.number_input(f"Cantidad de '{promo_nombre}'", min_value=0, max_value=10, key="promo" + promo_nombre)
        if cantidad > 0:
            pedido.append((f"{cantidad} x {promo_nombre}", promo_info["precio"] * cantidad))
        st.markdown('</div>', unsafe_allow_html=True)
st.markdown(
    "<hr style='border: 1px solid #fcad00;'>",
    unsafe_allow_html=True
)

st.markdown(
            f"""
            <div style='text-align: center;'>
                <img src='data:image/jpeg;base64,{img_m5}' width='500'>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown(
    "<hr style='border: 1px solid #fcad00;'>",
    unsafe_allow_html=True
)

# Calcular total
with st.sidebar:
    st.markdown(
        "<h2 class='titulo-principal'>🧾 Resumen del pedido</h2>",
        unsafe_allow_html=True
    )
    

    if pedido:
        total = 0
        for desc, precio in pedido:
            st.write(f"- {desc}: ${precio:,.0f}")
            total += precio
        st.markdown(f"**Total: ${total:,.0f}**")

        # Mensaje para WhatsApp
        mensaje = "Hola! Quiero hacer el siguiente pedido de mezcal Novena Entrada:\n"
        for desc, precio in pedido:
            mensaje += f"- {desc} (${precio})\n"
        mensaje += f"\nTotal: ${total:,.0f}"

        # Enlace de WhatsApp
        numero_wa = "5573876729"  # Sustituye por tu número
        url_wa = f"https://wa.me/{numero_wa}?text={urllib.parse.quote(mensaje)}"

        st.markdown(
            "<hr style='border: 1px solid #fcad00;'>",
            unsafe_allow_html=True
        )
        st.markdown(f"[✅ Finaliza tu pedido por WhatsApp]({url_wa})", unsafe_allow_html=True)
        st.markdown(
            f"""
            <div style='text-align: center;'>
                <img src='data:image/jpeg;base64,{img_data}' width='200'>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        st.info("Agrega productos para ver el resumen aquí 👈")