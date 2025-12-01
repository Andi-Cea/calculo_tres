import streamlit as st
import numpy as np
import math
import sympy as sp

def check_answer_multivar(correct_answer, user_answer, tolerance=0.01):
    """Verifica si la respuesta del usuario es correcta"""
    try:
        if abs(float(correct_answer) - float(user_answer)) <= tolerance:
            st.session_state.score_multivar += 10
            st.session_state.exercises_completed_multivar += 1
            st.success("🎉 ¡Correcto! +10 puntos")
            return True
        else:
            st.error("❌ Incorrecto. Intenta nuevamente.")
            return False
    except:
        st.error("❌ Formato inválido. Usa números.")
        return False

def app():
    st.title("📚 Ejercicios Interactivos - Unidad 2")
    
    # Inicializar estado de la sesión
    if 'score_multivar' not in st.session_state:
        st.session_state.score_multivar = 0
    if 'exercises_completed_multivar' not in st.session_state:
        st.session_state.exercises_completed_multivar = 0

    # Menú de temas
    tema = st.sidebar.selectbox(
        "Selecciona un tema:",
        [
            "2.1 Derivadas parciales: definición, notación y cálculo",
            "2.2 Derivadas de orden superior",
            "2.3 Diferenciabilidad de funciones",
            "2.4 Regla de la cadena",
            "2.5 Derivada direccional y gradiente",
            "2.6 Aplicación de la derivada direccional y gradiente",
            "2.7 Máximos y mínimos sin restricciones",
            "2.8 Máximos y mínimos con restricciones",
            "2.9 Serie de Taylor en dos variables",
            "2.10 Graficación de funciones en R³"
        ]
    )
    
    # Mostrar puntuación
    st.sidebar.markdown("---")
    st.sidebar.metric("🏆 Puntuación", st.session_state.score_multivar)
    st.sidebar.metric("✅ Ejercicios Completados", st.session_state.exercises_completed_multivar)
    
    if st.sidebar.button("🔄 Reiniciar Puntuación"):
        st.session_state.score_multivar = 0
        st.session_state.exercises_completed_multivar = 0
        st.rerun()

    # ========== 2.1 DERIVADAS PARCIALES ==========
    if tema == "2.1 Derivadas parciales: definición, notación y cálculo":
        st.header("📐 2.1 Derivadas Parciales: Definición, Notación y Cálculo")
        st.info("Practica el cálculo de derivadas parciales de funciones multivariables")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Cálculo básico de derivadas parciales")
        st.write("Para la función \( f(x, y) = 3x^2y + \sin(xy) \), calcula:")
        
        col1, col2 = st.columns(2)
        with col1:
            user_fx = st.number_input("\( f_x(0, \pi) \) =", value=0.0, step=0.1, key="fx1")
        with col2:
            user_fy = st.number_input("\( f_y(0, \pi) \) =", value=0.0, step=0.1, key="fy1")
        
        if st.button("Verificar Derivadas Parciales", key="check_partial1"):
            correct_fx = 3 * math.pi
            correct_fy = 0.0
            
            check1 = check_answer_multivar(correct_fx, user_fx)
            check2 = check_answer_multivar(correct_fy, user_fy)
            
            if check1 and check2:
                st.session_state.score_multivar += 5
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Definición por límite")
        st.write("Para \( f(x, y) = x^2 + 2xy + y^2 \), usa la definición por límite:")
        st.latex(r"f_x(1,2) = \lim_{h \to 0} \frac{f(1+h,2) - f(1,2)}{h}")
        
        user_lim_def = st.number_input("\( f_x(1,2) \) por definición =", value=0.0, step=0.1, key="lim_def")
        
        if st.button("Verificar por Definición", key="check_lim_def"):
            check_answer_multivar(6.0, user_lim_def)

    # ========== 2.2 DERIVADAS DE ORDEN SUPERIOR ==========
    elif tema == "2.2 Derivadas de orden superior":
        st.header("📈 2.2 Derivadas de Orden Superior")
        st.info("Practica el cálculo de derivadas parciales de segundo orden")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Derivadas de segundo orden")
        st.write("Para \( f(x, y) = e^{x^2y} \), calcula en el punto (1,0):")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            user_fxx = st.number_input("\( f_{xx}(1,0) \) =", value=0.0, step=0.1, key="fxx")
        with col2:
            user_fyy = st.number_input("\( f_{yy}(1,0) \) =", value=0.0, step=0.1, key="fyy")
        with col3:
            user_fxy = st.number_input("\( f_{xy}(1,0) \) =", value=0.0, step=0.1, key="fxy")
        
        if st.button("Verificar Segundas Derivadas", key="check_second"):
            correct_fxx = 2.0
            correct_fyy = 1.0
            correct_fxy = 2.0
            
            check1 = check_answer_multivar(correct_fxx, user_fxx)
            check2 = check_answer_multivar(correct_fyy, user_fyy)
            check3 = check_answer_multivar(correct_fxy, user_fxy)
            
            if check1 and check2 and check3:
                st.session_state.score_multivar += 10
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Teorema de Clairaut")
        st.write("Para \( f(x, y) = x^3y + xy^3 \), verifica que \( f_{xy} = f_{yx} \)")
        
        user_fxy2 = st.number_input("\( f_{xy}(1,1) \) =", value=0.0, step=0.1, key="fxy2")
        user_fyx2 = st.number_input("\( f_{yx}(1,1) \) =", value=0.0, step=0.1, key="fyx2")
        
        if st.button("Verificar Clairaut", key="check_clairaut"):
            correct_value = 4.0
            if abs(user_fxy2 - correct_value) <= 0.01 and abs(user_fyx2 - correct_value) <= 0.01:
                st.session_state.score_multivar += 10
                st.session_state.exercises_completed_multivar += 1
                st.success("🎉 ¡Correcto! Se verifica el Teorema de Clairaut")
            else:
                st.error("❌ Incorrecto. Las derivadas cruzadas deben ser iguales")

    # ========== 2.3 DIFERENCIABILIDAD ==========
    elif tema == "2.3 Diferenciabilidad de funciones":
        st.header("🔍 2.3 Diferenciabilidad de Funciones")
        st.info("Analiza la diferenciabilidad de funciones multivariables")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Verificación de diferenciabilidad")
        st.write("Para \( f(x, y) = \\begin{cases} \\frac{xy}{\sqrt{x^2 + y^2}}, & (x,y) \\neq (0,0) \\\\ 0, & (x,y) = (0,0) \\end{cases} \\)")
        
        pregunta = st.radio(
            "¿Es f diferenciable en (0,0)?",
            ["Sí, es diferenciable", "No, no es diferenciable"],
            key="diff1"
        )
        
        if st.button("Verificar Diferenciabilidad", key="check_diff1"):
            if pregunta == "Sí, es diferenciable":
                st.session_state.score_multivar += 10
                st.session_state.exercises_completed_multivar += 1
                st.success("🎉 ¡Correcto! La función es diferenciable en (0,0)")
            else:
                st.error("❌ Incorrecto. Las derivadas parciales existen y son continuas")
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Continuidad vs Diferenciabilidad")
        st.write("Selecciona la afirmación CORRECTA sobre funciones multivariables:")
        
        afirmacion = st.radio(
            "Sobre diferenciabilidad:",
            [
                "Si las derivadas parciales existen, la función es diferenciable",
                "Diferenciabilidad implica continuidad",
                "Continuidad implica diferenciabilidad",
                "La existencia de derivadas direccionales garantiza diferenciabilidad"
            ],
            key="cont_diff_multi"
        )
        
        if st.button("Verificar Concepto", key="check_concept"):
            if afirmacion == "Diferenciabilidad implica continuidad":
                st.session_state.score_multivar += 10
                st.session_state.exercises_completed_multivar += 1
                st.success("🎉 ¡Correcto! Diferenciabilidad es una condición más fuerte que continuidad")
            else:
                st.error("❌ Incorrecto. Revisa las relaciones entre continuidad y diferenciabilidad")

    # ========== 2.4 REGLA DE LA CADENA ==========
    elif tema == "2.4 Regla de la cadena":
        st.header("🔗 2.4 Regla de la Cadena")
        st.info("Practica la aplicación de la regla de la cadena en múltiples variables")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Una variable independiente")
        st.write("Si \( z = x^2 \ln(y) \), con \( x = \sin(t) \), \( y = e^t \), calcula \( \\frac{dz}{dt} \) en \( t = 0 \)")
        
        user_dzdt = st.number_input("\( \\frac{dz}{dt}(0) \) =", value=0.0, step=0.1, key="dzdt")
        
        if st.button("Verificar Regla Cadena 1", key="check_chain1"):
            check_answer_multivar(0.0, user_dzdt)
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Dos variables independientes")
        st.write("Si \( w = \arctan(xyz) \), con \( x = s + t \), \( y = s - t \), \( z = st^2 \)")
        st.write("Calcula \( \\frac{\partial w}{\partial s} \) en \( s=1, t=1 \)")
        
        user_dwds = st.number_input("\( \\frac{\partial w}{\partial s}(1,1) \) =", value=0.0, step=0.1, key="dwds")
        
        if st.button("Verificar Regla Cadena 2", key="check_chain2"):
            check_answer_multivar(0.5, user_dwds, 0.1)

    # ========== 2.5 DERIVADA DIRECCIONAL Y GRADIENTE ==========
    elif tema == "2.5 Derivada direccional y gradiente":
        st.header("🧭 2.5 Derivada Direccional y Gradiente")
        st.info("Calcula derivadas direccionales y vectores gradiente")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Cálculo del gradiente")
        st.write("Para \( f(x, y, z) = x^2y + y^2z + z^2x \), en el punto P(1, 2, -1)")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            user_grad_x = st.number_input("\( \\nabla f_x \) =", value=0.0, step=0.1, key="grad_x")
        with col2:
            user_grad_y = st.number_input("\( \\nabla f_y \) =", value=0.0, step=0.1, key="grad_y")
        with col3:
            user_grad_z = st.number_input("\( \\nabla f_z \) =", value=0.0, step=0.1, key="grad_z")
        
        if st.button("Verificar Gradiente", key="check_grad"):
            correct_x = 0.0
            correct_y = -3.0
            correct_z = 5.0
            
            check1 = check_answer_multivar(correct_x, user_grad_x)
            check2 = check_answer_multivar(correct_y, user_grad_y)
            check3 = check_answer_multivar(correct_z, user_grad_z)
            
            if check1 and check2 and check3:
                st.session_state.score_multivar += 10
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Derivada direccional")
        st.write("Para la misma función, dirección \( \vec{v} = (2, 1, -2) \), calcula \( D_{\vec{u}}f(1,2,-1) \)")
        
        user_dir_deriv = st.number_input("Derivada direccional =", value=0.0, step=0.1, key="dir_deriv")
        
        if st.button("Verificar Direccional", key="check_dir"):
            check_answer_multivar(13/3, user_dir_deriv, 0.1)

    # ========== 2.6 APLICACIÓN DERIVADA DIRECCIONAL ==========
    elif tema == "2.6 Aplicación de la derivada direccional y gradiente":
        st.header("📊 2.6 Aplicación de la Derivada Direccional y Gradiente")
        st.info("Aplica conceptos de gradiente a problemas prácticos")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Tasa de cambio de temperatura")
        st.write("Temperatura: \( T(x, y) = 50 - x^2 - 2y^2 \), insecto en (3,2) moviéndose hacia (4,-1)")
        
        user_temp_rate = st.number_input("Tasa de cambio de temperatura =", value=0.0, step=0.1, key="temp_rate")
        
        if st.button("Verificar Tasa Cambio", key="check_temp"):
            check_answer_multivar(-38/math.sqrt(10), user_temp_rate, 0.1)
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Dirección de máximo enfriamiento")
        st.write("Para la misma función temperatura en (3,2):")
        
        col1, col2 = st.columns(2)
        with col1:
            user_dir_x = st.number_input("Componente x dirección =", value=0.0, step=0.1, key="dir_x")
        with col2:
            user_dir_y = st.number_input("Componente y dirección =", value=0.0, step=0.1, key="dir_y")
        
        if st.button("Verificar Dirección Óptima", key="check_opt_dir"):
            correct_x = 6/math.sqrt(52)
            correct_y = 8/math.sqrt(52)
            
            check1 = check_answer_multivar(correct_x, user_dir_x, 0.1)
            check2 = check_answer_multivar(correct_y, user_dir_y, 0.1)
            
            if check1 and check2:
                st.session_state.score_multivar += 5

    # ========== 2.7 MÁXIMOS Y MÍNIMOS SIN RESTRICCIONES ==========
    elif tema == "2.7 Máximos y mínimos sin restricciones":
        st.header("📈 2.7 Máximos y Mínimos Sin Restricciones")
        st.info("Encuentra y clasifica puntos críticos de funciones")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Puntos críticos")
        st.write("Para \( f(x, y) = x^3 + y^3 - 3xy \), encuentra los puntos críticos")
        
        st.write("Coordenada x del punto crítico (distinto del origen):")
        user_crit_x = st.number_input("x =", value=0.0, step=0.1, key="crit_x")
        user_crit_y = st.number_input("y =", value=0.0, step=0.1, key="crit_y")
        
        if st.button("Verificar Punto Crítico", key="check_crit"):
            if abs(user_crit_x - 1.0) <= 0.01 and abs(user_crit_y - 1.0) <= 0.01:
                st.session_state.score_multivar += 10
                st.session_state.exercises_completed_multivar += 1
                st.success("🎉 ¡Correcto! Punto crítico en (1,1)")
            else:
                st.error("❌ Incorrecto. Resuelve el sistema \( f_x = 0, f_y = 0 \)")
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Clasificación de puntos críticos")
        st.write("Para el punto (1,1) de la función anterior, ¿qué tipo de punto crítico es?")
        
        tipo_punto = st.radio(
            "Clasificación:",
            ["Máximo local", "Mínimo local", "Punto silla", "Punto de inflexión"],
            key="tipo_crit"
        )
        
        if st.button("Verificar Clasificación", key="check_class"):
            if tipo_punto == "Punto silla":
                st.session_state.score_multivar += 10
                st.session_state.exercises_completed_multivar += 1
                st.success("🎉 ¡Correcto! Es un punto silla")
            else:
                st.error("❌ Incorrecto. Calcula el determinante hessiano")

    # ========== 2.8 MÁXIMOS Y MÍNIMOS CON RESTRICCIONES ==========
    elif tema == "2.8 Máximos y mínimos con restricciones":
        st.header("⛓️ 2.8 Máximos y Mínimos Con Restricciones")
        st.info("Aplica multiplicadores de Lagrange para optimización con restricciones")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Multiplicadores de Lagrange")
        st.write("Optimiza \( f(x, y) = xy \) sujeta a \( \\frac{x^2}{8} + \\frac{y^2}{2} = 1 \)")
        
        st.write("Valor MÁXIMO de la función:")
        user_max_val = st.number_input("Valor máximo =", value=0.0, step=0.1, key="max_val")
        
        if st.button("Verificar Valor Máximo", key="check_max"):
            check_answer_multivar(2.0, user_max_val)
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Dos restricciones")
        st.write("En la intersección de \( x + y + z = 1 \) y \( x^2 + y^2 + z^2 = 1 \)")
        st.write("Distancia MÍNIMA al origen:")
        
        user_min_dist = st.number_input("Distancia mínima =", value=0.0, step=0.1, key="min_dist")
        
        if st.button("Verificar Distancia Mínima", key="check_min_dist"):
            check_answer_multivar(math.sqrt(1/3), user_min_dist, 0.01)

    # ========== 2.9 SERIE DE TAYLOR ==========
    elif tema == "2.9 Serie de Taylor en dos variables":
        st.header("🎯 2.9 Serie de Taylor en Dos Variables")
        st.info("Aproxima funciones usando polinomios de Taylor")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Polinomio de Taylor de segundo orden")
        st.write("Para \( f(x, y) = e^x \cos(y) \) alrededor de (0,0)")
        
        st.write("Coeficiente del término \( x^2 \):")
        user_coef_x2 = st.number_input("Coeficiente \( x^2 \) =", value=0.0, step=0.1, key="coef_x2")
        
        if st.button("Verificar Coeficiente", key="check_coef"):
            check_answer_multivar(0.5, user_coef_x2)
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Aproximación lineal")
        st.write("Para \( f(x, y) = \sqrt{xy} \) en (1,4), aproximación lineal en (1.1, 4.1):")
        
        user_approx = st.number_input("Aproximación lineal =", value=0.0, step=0.1, key="lin_approx")
        
        if st.button("Verificar Aproximación", key="check_approx"):
            correct_approx = 2.0 + 1.0*0.1 + 0.25*0.1
            check_answer_multivar(correct_approx, user_approx, 0.01)

    # ========== 2.10 GRAFICACIÓN EN R³ ==========
    elif tema == "2.10 Graficación de funciones en R³":
        st.header("🎨 2.10 Graficación de Funciones en R³")
        st.info("Visualiza superficies y puntos críticos")
        
        # Ejercicio 1
        st.subheader("Ejercicio 1: Identificación de puntos críticos")
        st.write("Para \( f(x, y) = x^3 - 3xy^2 \) (Silla de Mono)")
        
        pregunta_punto = st.radio(
            "¿Qué tipo de punto crítico tiene en (0,0)?",
            ["Máximo local", "Mínimo local", "Punto silla", "No tiene punto crítico"],
            key="punto_silla"
        )
        
        if st.button("Verificar Tipo de Punto", key="check_silla"):
            if pregunta_punto == "Punto silla":
                st.session_state.score_multivar += 10
                st.session_state.exercises_completed_multivar += 1
                st.success("🎉 ¡Correcto! Es un punto silla (punto de silla de mono)")
            else:
                st.error("❌ Incorrecto. La función tiene un punto silla en el origen")
        
        # Ejercicio 2
        st.subheader("Ejercicio 2: Interpretación gráfica")
        st.write("Para una función con mapa de contorno que muestra curvas cerradas concéntricas:")
        
        pregunta_contorno = st.radio(
            "¿Qué indica este patrón de curvas de nivel?",
            [
                "Un punto silla",
                "Un máximo o mínimo local", 
                "Una línea de puntos críticos",
                "Una discontinuidad"
            ],
            key="contorno"
        )
        
        if st.button("Verificar Interpretación", key="check_contorno"):
            if pregunta_contorno == "Un máximo o mínimo local":
                st.session_state.score_multivar += 10
                st.session_state.exercises_completed_multivar += 1
                st.success("🎉 ¡Correcto! Las curvas cerradas concéntricas indican un extremo local")
            else:
                st.error("❌ Incorrecto. Las curvas cerradas alrededor de un punto sugieren un extremo")

# Ejecutar la aplicación
if __name__ == "__main__":
    app()
    