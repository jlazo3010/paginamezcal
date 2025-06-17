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
    👈 Finaliza tu pedido aquí
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>

.titulo-principal {
    font-size: 10rem;
    color: #fcad00;
    text-shadow: 2px 2px 7px rgba(0,0,0,1);
    font-weight: bold;
    padding-bottom: 10px;
    border-bottom: 3px solid #fcad00;
    margin-bottom: 30px;
    text-align: left;
}

/* Resalta el botón de abrir el sidebar */
button[kind="header"] {
    background-color: #fcad00 !important;
    color: black !important;
    border: 2px solid black !important;
    font-weight: bold !important;
    animation: pulse 1.8s infinite;
    border-radius: 6px !important;
}

/* Animación para llamar la atención */
@keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(252, 173, 0, 0.7); }
    70% { box-shadow: 0 0 0 10px rgba(252, 173, 0, 0); }
    100% { box-shadow: 0 0 0 0 rgba(252, 173, 0, 0); }
}

/* Aviso fijo en pantalla para dirigir al sidebar */
.finaliza-sidebar {
    position: fixed;
    top: 50%;
    left: 5px;
    background-color: #fcad00;
    color: black;
    font-weight: bold;
    padding: 10px 15px;
    border-radius: 8px;
    transform: rotate(-90deg);
    transform-origin: left top;
    z-index: 9999;
    box-shadow: 0 4px 10px rgba(0,0,0,0.4);
}

/* Fuente base y ajustes generales */
html, body, .main, .block-container {
    font-family: 'Segoe UI', sans-serif;
    background-color: #871000 !important;
    padding: 0;
    margin: 70px;
    overflow-x: hidden !important;
    box-sizing: border-box;
}

/* Limitar ancho y centrar contenido */
.block-container {
    margin: auto !important;
    padding-top: 4rem;
    padding-left: 5rem;
    padding-right: 5rem;
}

/* Centrar imágenes */
img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    max-width: 100%;
}

/* Sidebar: fondo verde oscuro */
[data-testid="stSidebar"] {
    background-color: #105500;
}

img {
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}

/* Texto blanco en el sidebar */
[data-testid="stSidebar"] * {
    color: white !important;
}

/* Encabezados centrados */
h2, h3 {
    text-align: center;
}

/* Estilo para contenedores de mezcales */
.mezcal-container {
    background-color: #ffbc00 !important;
    padding: 15px !important;
    border-radius: 10px !important;
    margin: 10px 0 !important;
    color: black !important;
}

.mezcal-container * {
    color: black !important;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([5, 2])  # Ajusta proporción a tu gusto

with col1:
    st.markdown(
        "<h1 class='titulo-principal'>🔥 Mezcal Novena Entrada ⚾</h1>",
        unsafe_allow_html=True
    )

with col2:
    st.image("logo_mezcal.png", width=300)
    
st.subheader("Haz tu pedido directo por WhatsApp 📱")

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
        "precio": 850,
        "Tipo": "Para explorar lo mejor del agave silvestre.",
        "desc": "3 medios litros: Cuishe, Tobalá y Tepextate.",
        "ocasion": "Ideal para catas o para sorprender a alguien especial."
    },
    "Fiesta de Sabores": {
        "precio": 1000,
        "Tipo": "Un viaje por sabores únicos.",
        "desc": "1/2L de Espadín + 1/2L de Tobalá + 1/2L de Cuishe + 1/2L de Tepextate.",
        "ocasion": "Una noche larga, con música, mezcal y buena compañía."
    },
    "Ruta del Agave": {
        "precio": 700,
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

    has_items = False
    total = 0
    mensaje = "Hola! Quiero hacer el siguiente pedido de mezcal Novena Entrada:\n"

    # Procesar mezcales
    for i, nombre in enumerate(mezcales.keys()):
        l_key = nombre + "l"
        m_key = nombre + "m"

        l_val = st.session_state.get(l_key, 0)
        m_val = st.session_state.get(m_key, 0)

        if l_val > 0 or m_val > 0:
            has_items = True
            st.markdown(f"**{nombre}**")

        if l_val > 0:
            st.write(f"1L x {l_val} = ${mezcales[nombre]['litro'] * l_val:,.0f}")
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                if st.button("➖", key=f"menos_{l_key}"):
                    st.session_state[l_key] = max(0, l_val - 1)
            with col2:
                st.write(str(l_val))
            with col3:
                if st.button("➕", key=f"mas_{l_key}"):
                    st.session_state[l_key] = l_val + 1
            total += mezcales[nombre]["litro"] * l_val
            mensaje += f"- {l_val}L de {nombre} (${mezcales[nombre]['litro'] * l_val})\n"

        if m_val > 0:
            st.write(f"1/2L x {m_val} = ${mezcales[nombre]['medio'] * m_val:,.0f}")
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                if st.button("➖", key=f"menos_{m_key}"):
                    st.session_state[m_key] = max(0, m_val - 1)
            with col2:
                st.write(str(m_val))
            with col3:
                if st.button("➕", key=f"mas_{m_key}"):
                    st.session_state[m_key] = m_val + 1
            total += mezcales[nombre]["medio"] * m_val
            mensaje += f"- {m_val} x 1/2L de {nombre} (${mezcales[nombre]['medio'] * m_val})\n"

    # Procesar promociones
    for promo_nombre, promo_info in promos.items():
        promo_key = "promo" + promo_nombre
        p_val = st.session_state.get(promo_key, 0)
        if p_val > 0:
            has_items = True
            st.markdown(f"**{promo_nombre}**")
            st.write(f"{p_val} x ${promo_info['precio']} = ${promo_info['precio'] * p_val:,.0f}")
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                if st.button("➖", key=f"menos_{promo_key}"):
                    st.session_state[promo_key] = max(0, p_val - 1)
            with col2:
                st.write(str(p_val))
            with col3:
                if st.button("➕", key=f"mas_{promo_key}"):
                    st.session_state[promo_key] = p_val + 1
            total += promo_info["precio"] * p_val
            mensaje += f"- {p_val} x {promo_nombre} (${promo_info['precio'] * p_val})\n"

    if has_items:
        mensaje += f"\nTotal: ${total:,.0f}"
        st.markdown("---")
        st.markdown(f"**Total: ${total:,.0f}**")
        numero_wa = "5573876729"
        url_wa = f"https://wa.me/{numero_wa}?text={urllib.parse.quote(mensaje)}"
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
