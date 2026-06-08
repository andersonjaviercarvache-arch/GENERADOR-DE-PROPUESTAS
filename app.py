import streamlit as st
from fpdf import FPDF
import tempfile

# ==========================================
# CONFIGURACIÓN DE PÁGINA STREAMLIT
# ==========================================
st.set_page_config(page_title="Generador de Propuestas - Latitudsolar", layout="wide")
st.title("Generador de Propuestas Técnicas y Económicas")

# ==========================================
# CLASE FPDF PERSONALIZADA (PLANTILLA LATITUDSOLAR)
# ==========================================
class PDF(FPDF):
    def header(self):
        # Evitar encabezado en la portada
        if self.page_no() == 1:
            return
            
        # Membrete idéntico para páginas interiores
        self.set_font('helvetica', 'B', 14)
        self.set_text_color(0, 0, 0)
        self.cell(0, 6, 'LATITUDSOLAR C.LTDA.', border=0, ln=1, align='L')
        
        self.set_font('helvetica', '', 9)
        self.set_text_color(100, 100, 100)
        self.cell(0, 5, 'RUC 0993403111001', border=0, ln=1, align='L')
        self.cell(0, 5, 'TELEFONOS: 0969952794 - 0959032257', border=0, ln=1, align='L')
        self.set_draw_color(200, 200, 200)
        self.line(10, self.get_y(), 200, self.get_y()) # Línea divisoria
        self.ln(5)

    def footer(self):
        # Pie de página (Opcional, la propuesta original es limpia)
        pass

# ==========================================
# FUNCIÓN DE GENERACIÓN DEL DOCUMENTO
# ==========================================
def generar_pdf_identico():
    pdf = PDF()
    pdf.add_page()
    
    # ------------------------------------------
    # PÁGINA 1: PORTADA
    # ------------------------------------------
    pdf.set_font('helvetica', 'B', 24)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(20)
    pdf.cell(0, 10, 'Latitud Solar', ln=True, align='C')
    pdf.set_font('helvetica', '', 14)
    pdf.cell(0, 10, 'Renewable Energy', ln=True, align='C')
    pdf.ln(20)
    
    pdf.set_font('helvetica', 'B', 20)
    pdf.cell(0, 10, 'PROPUESTA TÉCNICA ECONÓMICA', ln=True, align='C')
    pdf.set_font('helvetica', 'B', 28)
    pdf.set_text_color(0, 102, 204) # Azul comercial
    pdf.cell(0, 15, '71,3KWP', ln=True, align='C')
    
    pdf.ln(30)
    pdf.set_font('helvetica', '', 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 6, 'LATITUDSOLAR C.LTDA.', ln=True, align='C')
    pdf.cell(0, 6, '0969952794', ln=True, align='C')
    pdf.cell(0, 6, 'ventas@latitudsolarecuador.com', ln=True, align='C')
    
    # Placeholder para el collage de fotos de la portada
    pdf.ln(10)
    pdf.set_fill_color(240, 240, 240)
    pdf.cell(0, 80, '[ESPACIO PARA COLLAGE DE FOTOS DRON/INSTALACIÓN]', border=1, ln=True, align='C', fill=True)
    
    # ------------------------------------------
    # PÁGINA 2: PROPUESTA DE AHORRO
    # ------------------------------------------
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 14)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, 'PROPUESTA DE AHORRO', ln=True, align='L')
    
    pdf.set_font('helvetica', '', 11)
    texto_intro = ("Propuesta técnica y económica para la implementación de una planta solar fotovoltaica "
                   "On-Grid, diseñada para optimizar los costos energéticos y promover la sostenibilidad "
                   "del Chifa Nueva Época.")
    pdf.multi_cell(0, 6, texto_intro)
    pdf.ln(10)
    
    # Tabla de Parámetros
    pdf.set_fill_color(200, 200, 200)
    pdf.set_font('helvetica', 'B', 10)
    pdf.cell(95, 8, 'Parámetro', border=1, fill=True)
    pdf.cell(95, 8, 'Unidades / Valor', border=1, ln=True, fill=True)
    
    pdf.set_font('helvetica', '', 10)
    parametros = [
        ("Potencia FV", "71,3 kWp"),
        ("Total de módulos", "115 unidades"),
        ("Área de los módulos", "314,75 m²"),
        ("Vida útil y producción de energía", "30 años"),
        ("Costo de planta solar", "50.013,90 USD"),
        ("Ahorro en vida útil", "355.131,00 USD"),
        ("Recuperación de inversión", "4 años")
    ]
    for param, valor in parametros:
        pdf.cell(95, 8, param, border=1)
        pdf.cell(95, 8, valor, border=1, ln=True)
        
    pdf.ln(10)
    pdf.set_font('helvetica', 'B', 12)
    pdf.cell(0, 10, 'COSTO UNITARIO DE PLANTA POR $701,45', ln=True, align='L')
    
    # ------------------------------------------
    # PÁGINA 3: ALCANCE DE SUMINISTRO
    # ------------------------------------------
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 14)
    pdf.cell(0, 10, 'ALCANCE DE SUMINISTRO Y COMPONENTES', ln=True, align='L')
    
    pdf.set_font('helvetica', 'B', 11)
    pdf.cell(0, 8, '1. ALCANCE DEL PROYECTO', ln=True)
    pdf.set_font('helvetica', '', 10)
    texto_alcance = ("El proyecto comprende la ejecución integral de un sistema de generación fotovoltaica de "
                     "71,3KWP bajo la modalidad \"llave en mano\", que incluye desde la ingeniería, suministro y "
                     "montaje, hasta la gestión administrativa necesaria para la puesta en marcha legal ante la "
                     "empresa eléctrica CNEL.")
    pdf.multi_cell(0, 6, texto_alcance)
    pdf.ln(8)
    
    pdf.set_font('helvetica', 'B', 11)
    pdf.cell(0, 8, '3. Tabla de Suministro y Componentes', ln=True)
    
    # Tabla de componentes
    pdf.set_font('helvetica', 'B', 9)
    pdf.cell(60, 8, 'Componente / Servicio', border=1, fill=True)
    pdf.cell(100, 8, 'Cantidad / Especificación', border=1, fill=True)
    pdf.cell(30, 8, 'Estado', border=1, ln=True, fill=True)
    
    pdf.set_font('helvetica', '', 9)
    componentes = [
        ("Paneles Solares", "115 unidades (Longi, Trina o Yingli) de 620Wp", "Incluido"),
        ("Inversores", "6 unidades Huawei SUN2000-10KTL-LCO (10 kW c/u)", "Incluido"),
        ("Estructura de Montaje", "Aluminio anodizado (mid/end clamps y tornillería)", "Incluido"),
        ("Protecciones Eléctricas", "Tableros de protección en DC y AC", "Incluido"),
        ("Canalización y Cableado", "Cableado fotovoltaico y tubería", "Incluido"),
        ("Sistema de Monitoreo", "Sistema de monitoreo remoto", "Incluido"),
        ("Gestión de Medidor", "Tramitación legal ante CNEL", "Incluido"),
        ("Instalación y Puesta en Marcha", "Mano de obra especializada", "Incluido"),
        ("Inducción y Capacitación", "Sesión técnica", "Incluido"),
        ("Mantenimiento", "Primer año de mantenimiento preventivo", "Gratis")
    ]
    for comp, esp, est in componentes:
        pdf.cell(60, 8, comp, border=1)
        pdf.cell(100, 8, esp, border=1)
        pdf.cell(30, 8, est, border=1, align='C', ln=True)

    # ------------------------------------------
    # PÁGINA 4: RESUMEN FINANCIERO Y TABLA 30 AÑOS
    # ------------------------------------------
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 14)
    pdf.cell(0, 10, 'PROPUESTA SOLAR - COMERCIAL', ln=True)
    
    # Datos de cabecera financiera
    pdf.set_font('helvetica', '', 10)
    pdf.cell(95, 6, 'DATOS DEL PROYECTO', ln=False)
    pdf.cell(95, 6, 'RESUMEN FINANCIERO DE RECUPERACIÓN', ln=True)
    
    pdf.cell(95, 5, 'Cliente: CHIFA NUEVA EPOCA', ln=False)
    pdf.cell(95, 5, 'Inversión Total: $50,013.90', ln=True)
    pdf.cell(95, 5, 'Proyecto: P0000000014', ln=False)
    pdf.cell(95, 5, 'Potencia Sugerida: 71.30 kWp', ln=True)
    pdf.cell(95, 5, 'Ciudad: Guayaquil', ln=False)
    pdf.cell(95, 5, 'Retorno Estimado Real: 1.40 años', ln=True)
    pdf.cell(95, 5, 'Costo kWh: $0.1223', ln=False)
    pdf.cell(95, 5, 'Esquema Beneficio: 50.00% por 2 año(s)', ln=True)
    pdf.ln(5)
    
    # Tabla de 30 años (Muestra representativa para el espacio)
    pdf.set_font('helvetica', 'B', 8)
    anchos = [15, 20, 25, 30, 30, 30]
    cabeceras = ['Año', 'Ind. Deg.', 'Prod. kWh', 'Ahorro En.', 'Ahorro Trib.', 'Acumulado']
    for i, cabecera in enumerate(cabeceras):
        pdf.cell(anchos[i], 6, cabecera, border=1, fill=True, align='C')
    pdf.ln()
    
    pdf.set_font('helvetica', '', 8)
    # Ejemplo de las primeras 5 filas (puedes poblar el resto iterando un dataframe)
    filas_ejemplo = [
        ("1", "-0.980", "88,380", "$10,805.03", "$25,006.95", "$35,811.98"),
        ("2", "-0.975", "87,894", "$10,745.60", "$25,006.95", "$71,564.53"),
        ("3", "-0.969", "87,410", "$10,686.50", "$0.00", "$82,251.04"),
        ("4", "-0.964", "86,930", "$10,627.73", "$0.00", "$92,878.76"),
        ("5", "-0.959", "86,451", "$10,569.27", "$0.00", "$103,448.04")
    ]
    for fila in filas_ejemplo:
        for i, dato in enumerate(fila):
            pdf.cell(anchos[i], 6, dato, border=1, align='C')
        pdf.ln()

    # ------------------------------------------
    # PÁGINA 5: ANÁLISIS DE RENTABILIDAD
    # ------------------------------------------
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 14)
    pdf.cell(0, 10, 'ANÁLISIS DE RENTABILIDAD', ln=True)
    
    pdf.set_font('helvetica', '', 10)
    texto_rent = ("La implementación de este sistema de 71.3 kWp representa una inversión estratégica de "
                  "$50,013.90. Mediante la aplicación de una depreciación acelerada del 50% anual, el "
                  "proyecto permite recuperar la totalidad del capital invertido en un plazo de 1.4 años. Al "
                  "concluir el segundo año, se habrá consolidado un beneficio acumulado de $71,576.26, lo "
                  "cual arroja un saldo a favor neto de $21,562.36. A partir de este punto, el activo genera "
                  "rentabilidad pura, asegurando beneficios económicos y ahorro energético continuo "
                  "durante el resto de su vida útil de 30 años.")
    pdf.multi_cell(0, 6, texto_rent)
    pdf.ln(10)
    
    # Tabla final de saldo
    pdf.set_font('helvetica', 'B', 10)
    pdf.cell(50, 8, 'Concepto', border=1, fill=True)
    pdf.cell(40, 8, 'Año 1', border=1, fill=True, align='C')
    pdf.cell(40, 8, 'Año 2', border=1, fill=True, align='C')
    pdf.cell(40, 8, 'Total (2 Años)', border=1, ln=True, fill=True, align='C')
    
    pdf.set_font('helvetica', '', 10)
    rentabilidad = [
        ("Ahorro Energético", "$10,810.91", "$10,751.45", "$21,562.36"),
        ("Ahorro Tributario", "$25,006.95", "$25,006.95", "$50,013.90"),
        ("Ahorro Total Acum.", "$35,817.86", "$35,758.40", "$71,576.26"),
        ("Inversión Inicial", "-", "-", "-$50,013.90")
    ]
    for c, a1, a2, tot in rentabilidad:
        pdf.cell(50, 8, c, border=1)
        pdf.cell(40, 8, a1, border=1, align='C')
        pdf.cell(40, 8, a2, border=1, align='C')
        pdf.cell(40, 8, tot, border=1, ln=True, align='C')
        
    pdf.set_font('helvetica', 'B', 10)
    pdf.cell(130, 8, 'Saldo a Favor Neto', border=1, align='R')
    pdf.cell(40, 8, '$21,562.36', border=1, ln=True, align='C')

    # Guardar archivo temporal
    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(temp.name)
    return temp.name

# ==========================================
# INTERFAZ DE USUARIO
# ==========================================
st.write("Generador formateado con la estructura comercial exacta.")

if st.button("Generar PDF Formateado"):
    ruta = generar_pdf_identico()
    with open(ruta, "rb") as file:
        btn = st.download_button(
            label="Descargar PDF",
            data=file,
            file_name="Propuesta_Tecnica_Economica_Identica.pdf",
            mime="application/pdf"
        )
