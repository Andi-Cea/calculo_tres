import streamlit as st
import math

def check_answer_int(correct_answer, user_answer, tolerance=0.01):
    """Verifica si la respuesta del usuario es correcta"""
    try:
        if abs(float(correct_answer) - float(user_answer)) <= tolerance:
            st.session_state.score_int += 10
            st.session_state.exercises_completed_int += 1
            st.success("🎉 ¡Correcto! +10 puntos")
            return True
        else:
            st.error("❌ Incorrecto. Intenta nuevamente.")
            return False
    except:
        st.error("❌ Formato inválido. Usa números.")
        return False

def app():
    st.title("📚 Ejercicios Interactivos - Cálculo Integral Multivariable")
    
    # Inicializar estado de la sesión
    if 'score_int' not in st.session_state:
        st.session_state.score_int = 0
    if 'exercises_completed_int' not in st.session_state:
        st.session_state.exercises_completed_int = 0

    # Menú de temas
    tema = st.sidebar.selectbox(
        "Selecciona un tema:",
        [
            "3.1 Integrales Dobles - Cambio de Orden",
            "3.2 Transformación de Coordenadas",
            "3.3 Integrales Dobles en Coordenadas Polares",
            "3.4 Integrales Triples",
            "3.5 Aplicaciones",
            "3.6 Graficación con CAS"
        ]
    )
    
    # Mostrar puntuación
    st.sidebar.markdown("---")
    st.sidebar.metric("🏆 Puntuación", st.session_state.score_int)
    st.sidebar.metric("✅ Ejercicios Completados", st.session_state.exercises_completed_int)
    
    if st.sidebar.button("🔄 Reiniciar Puntuación"):
        st.session_state.score_int = 0
        st.session_state.exercises_completed_int = 0
        st.rerun()

    # ========== 3.1 INTEGRALES DOBLES - CAMBIO DE ORDEN ==========
    if tema == "3.1 Integrales Dobles - Cambio de Orden":
        st.header("📐 3.1 Integrales Dobles - Cambio de Orden de Integración")
        st.info("Practica la evaluación de integrales dobles y cambio de orden de integración")
        
        # Ejercicio 1 - Cambio de orden básico
        st.subheader("Ejercicio 1: Cambio de Orden de Integración")
        st.write("Evalúa la integral iterada cambiando el orden de integración:")
        st.latex(r"\int_{0}^{1} \int_{y}^{1} e^{x^{2}}  dx  dy")
        st.write("**Pista:** La integral interna no es elemental en el orden dado")
        
        col1, col2 = st.columns([2, 1])
        with col1:
            user_result1 = st.number_input("Resultado =", value=0.0, step=0.1, key="int1")
        
        with col2:
            if st.button("Verificar ✅", key="check_int1"):
                # Resultado aproximado después del cambio de orden
                check_answer_int(0.859, user_result1, 0.01)
        
        # Explicación
        with st.expander("💡 Ver explicación"):
            st.write("""
            **Solución:**
            Cambiando el orden de integración:
            \[
            \int_{0}^{1} \int_{0}^{x} e^{x^{2}}  dy  dx = \int_{0}^{1} x e^{x^{2}}  dx
            \]
            Haciendo sustitución: \( u = x^2 \), \( du = 2x dx \)
            \[
            \frac{1}{2} \int_{0}^{1} e^{u}  du = \frac{1}{2}(e - 1) \approx 0.859
            \]
            """)
        
        # Ejercicio 2 - Determinación de límites
        st.subheader("Ejercicio 2: Determinación de Límites de Integración")
        st.write("Para la región acotada por y = x² y y = 2 - x:")
        st.write("Escribe los límites de integración en el orden dy dx para:")
        st.latex(r"\iint_{R} f(x,y)  dA")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            user_x_min = st.number_input("x mínimo =", value=0.0, step=0.1, key="xmin")
        with col2:
            user_x_max = st.number_input("x máximo =", value=0.0, step=0.1, key="xmax")
        with col3:
            user_y_func = st.text_input("y(x) =", value="x^2 a 2-x", key="yfunc")
        
        if st.button("Verificar Límites", key="check_lim"):
            if abs(user_x_min - (-1)) < 0.1 and abs(user_x_max - 2) < 0.1:
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("🎉 ¡Correcto! Límites bien determinados")
            else:
                st.error("❌ Revisa los puntos de intersección de las curvas")

    # ========== 3.2 TRANSFORMACIÓN DE COORDENADAS ==========
    elif tema == "3.2 Transformación de Coordenadas":
        st.header("🔄 3.2 Transformación de Coordenadas")
        st.info("Practica el uso del Jacobiano en cambios de variable")
        
        # Ejercicio 1 - Transformación lineal
        st.subheader("Ejercicio 1: Transformación Lineal")
        st.write("Para la integral doble en la región acotada por:")
        st.write("y = x, y = x - 2, y = -x, y = -x + 4")
        st.write("Usando u = x + y, v = y - x, calcula el Jacobiano:")
        st.latex(r"|J| = \left| \frac{\partial(x,y)}{\partial(u,v)} \right|")
        
        user_jacobian = st.number_input("|J| =", value=0.0, step=0.1, key="jac1")
        
        if st.button("Verificar Jacobiano", key="check_jac1"):
            check_answer_int(0.5, user_jacobian)
        
        # Ejercicio 2 - Transformación a región rectangular
        st.subheader("Ejercicio 2: Transformación de Paralelogramo")
        st.write("Para el paralelogramo con vértices (0,0), (4,1), (6,3), (2,2)")
        st.write("Usando u = y - x/2, v = y/2")
        st.write("¿Cuál es el área de la región transformada en el plano uv?")
        
        user_area_uv = st.number_input("Área en plano uv =", value=0.0, step=0.1, key="area_uv")
        
        if st.button("Verificar Área", key="check_area"):
            check_answer_int(4.0, user_area_uv)

    # ========== 3.3 INTEGRALES DOBLES EN COORDENADAS POLARES ==========
    elif tema == "3.3 Integrales Dobles en Coordenadas Polares":
        st.header("🎯 3.3 Integrales Dobles en Coordenadas Polares")
        st.info("Practica integración en regiones circulares usando coordenadas polares")
        
        # Ejercicio 1 - Volumen bajo paraboloide
        st.subheader("Ejercicio 1: Volumen Bajo Paraboloide")
        st.write("Calcula el volumen bajo z = 9 - x² - y² y sobre el plano xy")
        st.write("Expresa la integral en polares y calcula el volumen:")
        
        user_volume = st.number_input("Volumen =", value=0.0, step=1.0, key="vol1")
        
        if st.button("Verificar Volumen", key="check_vol1"):
            # Volumen = (81π)/2 ≈ 127.23
            check_answer_int(127.23, user_volume, 0.1)
        
        # Ejercicio 2 - Área entre curvas polares
        st.subheader("Ejercicio 2: Área entre Curvas Polares")
        st.write("Área en primer cuadrante entre r = 1 + cosθ y r = 1")
        st.write("Calcula el área usando integral doble en polares:")
        
        user_area_polar = st.number_input("Área =", value=0.0, step=0.1, key="area_polar")
        
        if st.button("Verificar Área Polar", key="check_area_polar"):
            # Área aproximada
            check_answer_int(0.785, user_area_polar, 0.01)

    # ========== 3.4 INTEGRALES TRIPLES ==========
    elif tema == "3.4 Integrales Triples":
        st.header("📦 3.4 Integrales Triples")
        st.info("Practica integración en 3D usando coordenadas rectangulares, cilíndricas y esféricas")
        
        # Ejercicio 1 - Masa con densidad variable
        st.subheader("Ejercicio 1: Masa con Densidad Variable")
        st.write("Para el cubo [0,1]×[0,1]×[0,1] con densidad ρ(x,y,z) = x eʸ z²")
        st.write("Calcula la masa total:")
        
        user_mass = st.number_input("Masa =", value=0.0, step=0.1, key="mass")
        
        if st.button("Verificar Masa", key="check_mass"):
            # Masa = (e-1)/2 ≈ 0.859
            check_answer_int(0.859, user_mass, 0.01)
        
        # Ejercicio 2 - Volumen de esfera
        st.subheader("Ejercicio 2: Volumen de Esfera")
        st.write("Para una esfera de radio R = 2:")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("Usando coordenadas cilíndricas:")
            user_vol_cil = st.number_input("Volumen cilíndricas =", value=0.0, step=1.0, key="vol_cil")
        with col2:
            st.write("Usando coordenadas esféricas:")
            user_vol_esf = st.number_input("Volumen esféricas =", value=0.0, step=1.0, key="vol_esf")
        
        if st.button("Verificar Volúmenes", key="check_vols"):
            vol_correcto = 33.51  # (4/3)π(2)³ ≈ 33.51
            correcto1 = check_answer_int(vol_correcto, user_vol_cil, 0.1)
            correcto2 = check_answer_int(vol_correcto, user_vol_esf, 0.1)
            if correcto1 and correcto2:
                st.session_state.score_int += 5

    # ========== 3.5 APLICACIONES ==========
    elif tema == "3.5 Aplicaciones":
        st.header("🏗️ 3.5 Aplicaciones de Integrales Múltiples")
        st.info("Aplica integrales múltiples a problemas físicos y geométricos")
        
        # Ejercicio 1 - Centro de masa
        st.subheader("Ejercicio 1: Centro de Masa")
        st.write("Sólido en primer octante acotado por x + y + z = 2")
        st.write("Con densidad ρ(x,y,z) = x")
        st.write("Calcula la coordenada x del centro de masa:")
        st.latex(r"\bar{x} = \frac{\iiint x \rho  dV}{\iiint \rho  dV}")
        
        user_x_centro = st.number_input("x̄ =", value=0.0, step=0.1, key="xcentro")
        
        if st.button("Verificar Centro de Masa", key="check_centro"):
            check_answer_int(1.2, user_x_centro, 0.1)
        
        # Ejercicio 2 - Momento de inercia
        st.subheader("Ejercicio 2: Momento de Inercia")
        st.write("Cilindro x² + y² ≤ 4, 0 ≤ z ≤ 3, densidad constante ρ₀ = 1")
        st.write("Momento de inercia respecto al eje z:")
        st.latex(r"I_z = \iiint (x^2 + y^2) \rho  dV")
        
        user_inercia = st.number_input("I_z =", value=0.0, step=1.0, key="inercia")
        
        if st.button("Verificar Inercia", key="check_inercia"):
            # I_z = 24π ≈ 75.4
            check_answer_int(75.4, user_inercia, 0.1)

    # ========== 3.6 GRAFICACIÓN CON CAS ==========
    elif tema == "3.6 Graficación con CAS":
        st.header("📊 3.6 Graficación de Funciones con CAS")
        st.info("Analiza y visualiza superficies en 3D")
        
        # Ejercicio 1 - Identificación de superficies
        st.subheader("Ejercicio 1: Identificación de Superficies")
        st.write("Para la superficie z = x² - y²:")
        
        pregunta_tipo = st.radio(
            "¿Qué tipo de superficie es?",
            ["Paraboloide elíptico", "Paraboloide hiperbólico", "Esfera", "Plano"],
            key="tipo_sup"
        )
        
        st.write("¿Cuántos puntos silla tiene?")
        user_puntos_silla = st.number_input("Puntos silla =", value=0, step=1, key="silla")
        
        if st.button("Verificar Superficie", key="check_sup"):
            if pregunta_tipo == "Paraboloide hiperbólico" and user_puntos_silla == 1:
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("🎉 ¡Correcto! Es una silla de montar con un punto silla en (0,0)")
            else:
                st.error("❌ Revisa la clasificación de superficies cuadráticas")
        
        # Ejercicio 2 - Intersección de superficies
        st.subheader("Ejercicio 2: Intersección de Superficies")
        st.write("Para el cono z = √(x² + y²) y la esfera x² + y² + z² = 1")
        st.write("¿Qué forma tiene la curva de intersección?")
        
        pregunta_interseccion = st.radio(
            "La curva de intersección es:",
            ["Una elipse", "Un círculo", "Una parábola", "Dos rectas"],
            key="interseccion"
        )
        
        st.write("¿A qué altura z ocurre la intersección?")
        user_z_int = st.number_input("z =", value=0.0, step=0.1, key="zint")
        
        if st.button("Verificar Intersección", key="check_int"):
            if pregunta_interseccion == "Un círculo" and abs(user_z_int - 0.707) < 0.01:
                st.session_state.score_int += 10
                st.session_state.exercises_completed_int += 1
                st.success("🎉 ¡Correcto! Intersección circular en z = √2/2")
            else:
                st.error("❌ Resuelve el sistema de ecuaciones")

# Ejecutar la aplicación
if __name__ == "__main__":
    app()