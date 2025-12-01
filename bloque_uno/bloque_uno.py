import streamlit as st
import math  

def check_answer_vector(correct_answer, user_answer, tolerance=0.01):
    """Verifica si la respuesta del usuario es correcta"""
    try:
        if abs(float(correct_answer) - float(user_answer)) <= tolerance:
            st.session_state.score_vector += 10
            st.session_state.exercises_completed_vector += 1
            st.success("🎉 ¡Correcto! +10 puntos")
            return True
        else:
            st.error("❌ Incorrecto. Intenta nuevamente.")
            return False
    except:
        st.error("❌ Formato inválido. Usa números.")
        return False

def app():
    st.title("📚 Ejercicios Interactivos - Unidad 1·")
    
    # Inicializar estado de la sesión
    if 'score_vector' not in st.session_state:
        st.session_state.score_vector = 0
    if 'exercises_completed_vector' not in st.session_state:
        st.session_state.exercises_completed_vector = 0

    # Menú de temas
    tema = st.sidebar.selectbox(
        "Selecciona un tema:",
        [
            "1.1 Topología de los espacios cartesianos",
            "1.2 Conceptos de funciones",
            "1.3 Dominio de una función real de un vector",
            "1.4 Límites de funciones reales de un vector",
            "1.5 Continuidad de funciones reales de un vector",
            "1.6 Graficación de funciones reales con CAS"
        ]
    )
    
    # Mostrar puntuación
    st.sidebar.markdown("---")
    st.sidebar.metric("🏆 Puntuación", st.session_state.score_vector)
    st.sidebar.metric("✅ Ejercicios Completados", st.session_state.exercises_completed_vector)
    
    if st.sidebar.button("🔄 Reiniciar Puntuación"):
        st.session_state.score_vector = 0
        st.session_state.exercises_completed_vector = 0
        st.rerun()

    # ========== 1.1 TOPOLOGÍA DE LOS ESPACIOS CARTESIANOS ==========
    if tema == "1.1 Topología de los espacios cartesianos":
        st.header("🔷 1.1 Topología de los Espacios Cartesianos")
        st.info("Practica conceptos de conjuntos abiertos, cerrados, frontera y conexidad")
        
        # Ejercicio 1 - Identificar y graficar conjuntos
        st.subheader("Ejercicio 1: Análisis Topológico de un Conjunto")
        st.write("Para el conjunto A = {(x, y) ∈ ℝ² | 1 < x² + y² ≤ 4}:")
        
        st.write("**Selecciona la opción correcta:**")
        
        pregunta1 = st.radio(
            "¿Qué tipo de conjunto es A?",
            ["Abierto", "Cerrado", "Ni abierto ni cerrado", "Tanto abierto como cerrado"],
            key="topo1"
        )
        
        pregunta2 = st.radio(
            "¿Es A un conjunto conexo?",
            ["Sí", "No"],
            key="topo2"
        )
        
        if st.button("Verificar Topología 1", key="check_topo1"):
            if pregunta1 == "Ni abierto ni cerrado" and pregunta2 == "Sí":
                st.session_state.score_vector += 10
                st.session_state.exercises_completed_vector += 1
                st.success("🎉 ¡Correcto! A es una corona circular que incluye la frontera exterior pero no la interior")
            else:
                st.error("❌ Incorrecto. Revisa las definiciones de conjuntos abiertos y cerrados")
        
        # Ejercicio 2 - Análisis topológico de una parábola
        st.subheader("Ejercicio 2: Conjunto de una Parábola")
        st.write("Para B = {(x, y) ∈ ℝ² | y = x²}:")
        
        pregunta3 = st.radio(
            "¿Es B un conjunto compacto?",
            ["Sí", "No"],
            key="topo3"
        )
        
        pregunta4 = st.radio(
            "¿Cuál es la frontera de B?",
            ["El mismo conjunto B", "Vacío", "Todo ℝ²", "El eje x"],
            key="topo4"
        )
        
        if st.button("Verificar Topología 2", key="check_topo2"):
            if pregunta3 == "No" and pregunta4 == "El mismo conjunto B":
                st.session_state.score_vector += 10
                st.session_state.exercises_completed_vector += 1
                st.success("🎉 ¡Correcto! B no es acotado (no compacto) y es igual a su frontera")
            else:
                st.error("❌ Incorrecto. Un conjunto es compacto si es cerrado y acotado")

    # ========== 1.2 CONCEPTOS DE FUNCIONES ==========
    elif tema == "1.2 Conceptos de funciones":
        st.header("🔷 1.2 Conceptos de Funciones")
        st.info("Practica funciones reales de vector, vectoriales de real y vectoriales de vector")
        
        # Ejercicio 1 - Función real de un vector y función vectorial de un real
        st.subheader("Ejercicio 1: Evaluación de Funciones")
        
        st.write("**Parte A:** f: ℝ³ → ℝ definida por f(x, y, z) = x² + 2y - cos(z)")
        user_f1 = st.number_input("f(1, -1, π) =", value=0.0, step=0.1, key="func1")
        
        st.write("**Parte B:** r: ℝ → ℝ³ definida por r(t) = (3cos(t), 3sin(t), t)")
        user_rx = st.number_input("r(π/2) componente x =", value=0.0, step=0.1, key="func2_x")
        user_rz = st.number_input("r(π/2) componente z =", value=0.0, step=0.1, key="func2_z")
        
        if st.button("Verificar Funciones", key="check_func"):
            correcto_f1 = check_answer_vector(2.0, user_f1)
            correcto_rx = check_answer_vector(0.0, user_rx)
            correcto_rz = check_answer_vector(math.pi/2, user_rz, 0.01)
            
            if correcto_f1 and correcto_rx and correcto_rz:
                st.session_state.score_vector += 5
        
        # Ejercicio 2 - Función vectorial de un vector
        st.subheader("Ejercicio 2: Función Vectorial de Vector")
        st.write("Para F: ℝ² → ℝ² definida por F(x, y) = (x² - y, eˣ sin(y))")
        
        user_F1 = st.number_input("F(0, π/2) primera componente =", value=0.0, step=0.1, key="func3_1")
        user_F2 = st.number_input("F(0, π/2) segunda componente =", value=0.0, step=0.1, key="func3_2")
        
        if st.button("Verificar Función Vectorial", key="check_func_vec"):
            correcto_F1 = check_answer_vector(-math.pi/2, user_F1, 0.01)
            correcto_F2 = check_answer_vector(1.0, user_F2)
            
            if correcto_F1 and correcto_F2:
                st.session_state.score_vector += 5

    # ========== 1.3 DOMINIO DE UNA FUNCIÓN REAL DE UN VECTOR ==========
    elif tema == "1.3 Dominio de una función real de un vector":
        st.header("🔷 1.3 Dominio de una Función Real de un Vector")
        st.info("Encuentra y representa gráficamente dominios de funciones multivariables")
        
        # Ejercicio 1 - Dominio y representación gráfica
        st.subheader("Ejercicio 1: Dominio en ℝ²")
        st.write("Para f(x, y) = √(4 - x² - y²) + ln(x² + y² - 1)")
        
        st.write("**Selecciona la descripción correcta del dominio:**")
        
        dominio1 = st.radio(
            "El dominio de f(x, y) es:",
            [
                "Una corona circular 1 ≤ x² + y² ≤ 4",
                "Una corona circular 1 < x² + y² ≤ 4", 
                "Una corona circular 1 < x² + y² < 4",
                "Todo el plano ℝ²"
            ],
            key="dom1"
        )
        
        if st.button("Verificar Dominio 1", key="check_dom1"):
            if dominio1 == "Una corona circular 1 < x² + y² ≤ 4":
                st.session_state.score_vector += 10
                st.session_state.exercises_completed_vector += 1
                st.success("🎉 ¡Correcto! La raíz requiere x² + y² ≤ 4 y el logaritmo requiere x² + y² > 1")
            else:
                st.error("❌ Incorrecto. Analiza las restricciones de la raíz cuadrada y el logaritmo")
        
        # Ejercicio 2 - Dominio en tres dimensiones
        st.subheader("Ejercicio 2: Dominio en ℝ³")
        st.write("Para g(x, y, z) = 1/√(9 - x² - y² - z²) + arcsin(z)")
        
        user_radio = st.number_input("Radio máximo de la esfera (sin incluir la frontera):", value=0.0, step=0.1, key="dom2")
        user_zmin = st.number_input("Valor mínimo de z:", value=-1.0, step=0.1, key="dom2_zmin")
        user_zmax = st.number_input("Valor máximo de z:", value=1.0, step=0.1, key="dom2_zmax")
        
        if st.button("Verificar Dominio 2", key="check_dom2"):
            correcto_radio = check_answer_vector(3.0, user_radio)
            correcto_zmin = check_answer_vector(-1.0, user_zmin)
            correcto_zmax = check_answer_vector(1.0, user_zmax)
            
            if correcto_radio and correcto_zmin and correcto_zmax:
                st.session_state.score_vector += 5

    # ========== 1.4 LÍMITES DE FUNCIONES REALES DE UN VECTOR ==========
    elif tema == "1.4 Límites de funciones reales de un vector":
        st.header("🔷 1.4 Límites de Funciones Reales de un Vector")
        st.info("Calcula límites multivariables y analiza existencia por diferentes caminos")
        
        # Ejercicio 1 - Cálculo directo y análisis por curvas
        st.subheader("Ejercicio 1: Límite por Diferentes Caminos")
        st.write("Calcula el límite: lim_{(x,y)→(0,0)} (x²y)/(x² + y²)")
        
        st.write("**Usa coordenadas polares o analiza por rectas y = mx**")
        
        user_lim1 = st.number_input("Valor del límite =", value=0.0, step=0.1, key="lim_vec1")
        
        if st.button("Verificar Límite 1", key="check_lim_vec1"):
            check_answer_vector(0.0, user_lim1)
        
        # Ejercicio 2 - Demostración de no existencia
        st.subheader("Ejercicio 2: Límite que No Existe")
        st.write("Para lim_{(x,y)→(0,0)} (xy)/(x² + y²):")
        
        st.write("**Selecciona la afirmación correcta:**")
        
        existencia = st.radio(
            "¿Qué puedes concluir sobre este límite?",
            [
                "El límite existe y vale 0",
                "El límite existe y vale 1/2",
                "El límite no existe porque depende del camino",
                "El límite existe pero no se puede calcular"
            ],
            key="lim_vec2"
        )
        
        if st.button("Verificar Existencia", key="check_exist"):
            if existencia == "El límite no existe porque depende del camino":
                st.session_state.score_vector += 10
                st.session_state.exercises_completed_vector += 1
                st.success("🎉 ¡Correcto! Por y = mx el límite da m/(1+m²), que varía con m")
            else:
                st.error("❌ Incorrecto. Prueba con diferentes rectas y = mx")

    # ========== 1.5 CONTINUIDAD DE FUNCIONES REALES DE UN VECTOR ==========
    elif tema == "1.5 Continuidad de funciones reales de un vector":
        st.header("🔷 1.5 Continuidad de Funciones Reales de un Vector")
        st.info("Analiza continuidad de funciones multivariables en diferentes puntos")
        
        # Ejercicio 1 - Estudio de continuidad en un punto
        st.subheader("Ejercicio 1: Continuidad en el Origen")
        st.write("Para f(x,y) = { x²y/(x² + y²) si (x,y) ≠ (0,0); 0 si (x,y) = (0,0) }")
        
        st.write("**¿Es f continua en (0,0)?**")
        
        continuidad = st.radio(
            "Selecciona la respuesta correcta:",
            ["Sí, es continua", "No, es discontinua", "No se puede determinar"],
            key="cont1"
        )
        
        if st.button("Verificar Continuidad 1", key="check_cont1"):
            if continuidad == "Sí, es continua":
                st.session_state.score_vector += 10
                st.session_state.exercises_completed_vector += 1
                st.success("🎉 ¡Correcto! El límite cuando (x,y)→(0,0) existe y coincide con f(0,0)")
            else:
                st.error("❌ Incorrecto. Revisa el ejercicio de límites anterior")
        
        # Ejercicio 2 - Clasificación de discontinuidades
        st.subheader("Ejercicio 2: Discontinuidades")
        st.write("Para g(x,y) = 1/(x - y):")
        
        st.write("**¿Cómo es el conjunto de discontinuidades?**")
        
        disco = st.radio(
            "Las discontinuidades forman:",
            ["Un punto aislado", "Una curva en el plano", "Varios puntos dispersos", "Todo el plano"],
            key="cont2"
        )
        
        if st.button("Verificar Discontinuidades", key="check_disco"):
            if disco == "Una curva en el plano":
                st.session_state.score_vector += 10
                st.session_state.exercises_completed_vector += 1
                st.success("🎉 ¡Correcto! g es discontinua en la recta y = x")
            else:
                st.error("❌ Incorrecto. La función no está definida cuando el denominador es cero")

    # ========== 1.6 GRAFICACIÓN DE FUNCIONES REALES CON CAS ==========
    elif tema == "1.6 Graficación de funciones reales con CAS":
        st.header("🔷 1.6 Graficación de Funciones Reales con CAS")
        st.info("Reconoce superficies y sus curvas de nivel a partir de ecuaciones")
        
        # Ejercicio 1 - Análisis y graficación de una superficie
        st.subheader("Ejercicio 1: Identificación de Superficies")
        st.write("Para z = f(x,y) = x² - y²:")
        
        st.write("**¿Qué tipo de superficie representa esta función?**")
        
        superficie = st.radio(
            "Selecciona la opción correcta:",
            [
                "Paraboloide elíptico",
                "Paraboloide hiperbólico (silla de montar)",
                "Plano inclinado", 
                "Esfera"
            ],
            key="graf1"
        )
        
        if st.button("Verificar Superficie", key="check_superf"):
            if superficie == "Paraboloide hiperbólico (silla de montar)":
                st.session_state.score_vector += 10
                st.session_state.exercises_completed_vector += 1
                st.success("🎉 ¡Correcto! Es un paraboloide hiperbólico, tiene forma de silla de montar")
            else:
                st.error("❌ Incorrecto. Observa los signos de x² e y²")
        
        # Ejercicio 2 - Visualización de un campo escalar
        st.subheader("Ejercicio 2: Curvas de Nivel")
        st.write("Para h(x,y) = e^(-(x² + y²)) que representa una 'montaña':")
        
        st.write("**¿Cómo son las curvas de nivel de esta función?**")
        
        curvas = st.radio(
            "Las curvas de nivel son:",
            [
                "Rectas paralelas",
                "Circunferencias concéntricas",
                "Elipses", 
                "Hipérbolas"
            ],
            key="graf2"
        )
        
        user_valor = st.number_input("Valor de h(0,0) en el pico de la montaña:", value=0.0, step=0.1, key="graf_valor")
        
        if st.button("Verificar Curvas de Nivel", key="check_curvas"):
            correcto_curvas = (curvas == "Circunferencias concéntricas")
            correcto_valor = check_answer_vector(1.0, user_valor)
            
            if correcto_curvas and correcto_valor:
                st.session_state.score_vector += 5

# Ejecutar la aplicación
if __name__ == "__main__":
    app()