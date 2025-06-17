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

/* Aviso fijo en pantalla para dirigir al sidebar */
.finaliza-sidebar {
    position: fixed;
    top: 30%;
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
# Inicializar session_state para el carrito si no existe
if 'carrito' not in st.session_state:
    st.session_state.carrito = {}

# Crear un diccionario temporal con los productos actuales del formulario
productos_formulario = {}
for desc, precio_total in pedido:
    # Parse del producto según su formato
    cantidad = 1
    desc_clean = desc
    key = ""
    precio_unit = precio_total

    if " x " in desc and "de" in desc:
        # Ejemplo: "2 x 1/2L de Espadín"
        cantidad = int(desc.split(" x ")[0])
        resto = desc.split(" x ")[1]
        if "1/2L de" in resto:
            nombre = resto.replace("1/2L de ", "").strip()
            key = f"medio_{nombre}"
            desc_clean = f"1/2L de {nombre}"
        elif "1L de" in resto:
            nombre = resto.replace("1L de ", "").strip()
            key = f"litro_{nombre}"
            desc_clean = f"1L de {nombre}"
        precio_unit = precio_total // cantidad

    elif "L de" in desc:
        # Ejemplo: "2L de Espadín" → cantidad: 2, nombre: Espadín
        cantidad_str, nombre = desc.split("L de")
        cantidad = int(cantidad_str.strip())
        nombre = nombre.strip()
        key = f"litro_{nombre}"
        desc_clean = f"1L de {nombre}"
        precio_unit = precio_total // cantidad

    elif " x " in desc:
        # Ejemplo: "2 x Trilogía Silvestre"
        cantidad = int(desc.split(" x ")[0])
        nombre = desc.split(" x ")[1].strip()
        key = f"promo_{nombre.replace(' ', '_')}"
        desc_clean = nombre
        precio_unit = precio_total // cantidad

    else:
        # Caso por defecto (por si acaso)
        cantidad = 1
        nombre = desc
        key = f"promo_{desc.replace(' ', '_')}"
        desc_clean = desc
        precio_unit = precio_total

    if key in productos_formulario:
        productos_formulario[key]['cantidad'] += cantidad
    else:
        productos_formulario[key] = {
            'descripcion': desc_clean,
            'precio_unitario': precio_unit,
            'cantidad': cantidad
        }

# Botón para actualizar el carrito manualmente
if st.button("🛒 Agregar al carrito"):
    for key, producto in productos_formulario.items():
        if producto['cantidad'] > 0:
            st.session_state.carrito[key] = producto

    # Remover del carrito productos que ya no están en el formulario
    keys_a_remover = [key for key in st.session_state.carrito if key not in productos_formulario]
    for key in keys_a_remover:
        del st.session_state.carrito[key]

# SIDEBAR
with st.sidebar:
    st.markdown(
        "<h2 style='color: #fcad00; text-align: center;'>🧾 Resumen del pedido</h2>",
        unsafe_allow_html=True
    )

    if st.session_state.carrito:
        total = 0
        st.markdown("### Edita tu pedido aquí:")

        productos_a_mostrar = list(st.session_state.carrito.items())

        for key, producto in productos_a_mostrar:
            desc = producto['descripcion']
            precio_unitario = producto['precio_unitario']
            cantidad = producto['cantidad']

            with st.container():
                st.markdown(f"**{desc}**")

                col1, col2, col3, col4 = st.columns([1, 2, 1, 1])

                with col1:
                    if st.button("➖", key=f"menos_{key}"):
                        if st.session_state.carrito[key]['cantidad'] > 1:
                            st.session_state.carrito[key]['cantidad'] -= 1
                        else:
                            del st.session_state.carrito[key]
                        st.rerun()

                with col2:
                    st.markdown(
                        f"<div style='text-align: center; padding: 8px; background-color: #fcad00; "
                        f"border-radius: 5px; color: black; font-weight: bold;'>{cantidad}</div>",
                        unsafe_allow_html=True
                    )

                with col3:
                    if st.button("➕", key=f"mas_{key}"):
                        st.session_state.carrito[key]['cantidad'] += 1
                        st.rerun()

                with col4:
                    if st.button("🗑️", key=f"del_{key}"):
                        del st.session_state.carrito[key]
                        st.rerun()

                precio_linea = precio_unitario * cantidad
                total += precio_linea
                st.write(f"💰 ${precio_linea:,.0f}")
                st.markdown("---")

        st.markdown(f"### **🔥 Total: ${total:,.0f}**")

        if st.button("🗑️ Vaciar carrito", type="secondary"):
            st.session_state.carrito = {}
            st.rerun()

        if st.session_state.carrito:
            mensaje = "¡Hola! Pedido de Mezcal Novena Entrada:\n\n"
            for key, producto in st.session_state.carrito.items():
                desc = producto['descripcion']
                cantidad = producto['cantidad']
                precio_linea = producto['precio_unitario'] * cantidad
                mensaje += f"• {cantidad}x {desc} - ${precio_linea:,.0f}\n"
            mensaje += f"\n🔥 TOTAL: ${total:,.0f}\n¡Gracias!"

            numero_wa = "5573876729"
            url_wa = f"https://wa.me/{numero_wa}?text={urllib.parse.quote(mensaje)}"

            st.markdown("<hr style='border: 2px solid #fcad00;'>", unsafe_allow_html=True)

            st.markdown(f"""
            <div style='text-align: center; margin: 20px 0;'>
                <a href='{url_wa}' target='_blank' style='
                    background-color: #25D366;
                    color: white;
                    padding: 15px 25px;
                    text-decoration: none;
                    border-radius: 10px;
                    font-weight: bold;
                    display: inline-block;
                '>✅ Finalizar por WhatsApp</a>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style='text-align: center;'>
                <img src='data:image/jpeg;base64,{img_data}' width='200' style='border-radius: 10px;'>
            </div>
            """, unsafe_allow_html=True)

    else:
        st.info("🌿 Agrega productos para ver el resumen")
        st.markdown(f"""
        <div style='text-align: center;'>
            <img src='data:image/jpeg;base64,{img_data}' width='200' style='border-radius: 10px;'>
        </div>
        """, unsafe_allow_html=True)