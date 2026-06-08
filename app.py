import streamlit as st
from fpdf import FPDF
import pandas as pd
import tempfile

# 1. Configuración de la aplicación Streamlit
st.set_page_config(page_title="Generador de Propuestas - Latitudsolar", layout="wide")
st.title("Generador de Propuestas Comerciales Solares")

# 2. Formulario de ingreso de datos dinámicos
with st.sidebar:
    st.header("Datos del Proyecto")
    cliente = st.text_input("Nombre del Cliente", value="CHIFA NUEVA EPOCA")
    potencia_kwp = st.number_input("Potencia FV (kWp)", value=71.3)
    num_paneles = st.number_input("Total de Módulos", value=115)
    inversion_total = st.number_input("Costo de Inversión (USD)", value=50013.90)
    retorno_anios = st.number_input("Retorno Estimado (Años)", value=1.4)
    costo_kwh_actual = st.number_input("Costo kWh actual ($)", value=0.1223)

# 3. Clase FPDF Personalizada
class PDF(FPDF):
    def header(self):
        # Membrete de Latitudsolar
        self.set_font('helvetica', 'B', 15)
        self.cell(0, 10, 'LATITUDSOLAR C.LTDA.', border=0, ln=1, align='L')
        self.set_font('helvetica', '', 10)
        self.cell(0, 5, 'RUC 0993403111001 | Tel: 0969952794 - 0959032257', border=0, ln=1, align='L')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

# 4. Función de generación del PDF
def generar_pdf():
    pdf = PDF()
    pdf.add_page()
    
    # Título Principal
    pdf.set_font('helvetica', 'B', 16)
    pdf.cell(0, 10, 'PROPUESTA TÉCNICA ECONÓMICA', ln=True, align='C')
    pdf.cell(0, 10, f'{potencia_kwp} kWp', ln=True, align='C')
    pdf.ln(10)

    # Sección: Propuesta de Ahorro
    pdf.set_font('helvetica', 'B', 12)
    pdf.cell(0, 10, 'PROPUESTA DE AHORRO', ln=True)
    pdf.set_font('helvetica', '', 11)
    texto_intro = (f"Propuesta técnica y económica para la implementación de una planta solar fotovoltaica "
                   f"On-Grid, diseñada para optimizar los costos energéticos y promover la sostenibilidad de {cliente}.")
    pdf.multi_cell(0, 6, texto_intro)
    pdf.ln(5)

    # Tabla de Parámetros
    pdf.set_font('helvetica', 'B', 10)
    pdf.cell(90, 8, 'Parámetro', border=1)
    pdf.cell(90, 8, 'Unidades / Valor', border=1, ln=True)
    
    pdf.set_font('helvetica', '', 10)
    datos_tabla = [
        ("Potencia FV", f"{potencia_kwp} kWp"),
        ("Total de módulos", f"{num_paneles} unidades"),
        ("Vida útil y producción de energía", "30 años"),
        ("Costo de planta solar", f"$ {inversion_total:,.2f} USD"),
        ("Recuperación de inversión", f"{retorno_anios} años")
    ]
    for param, valor in datos_tabla:
        pdf.cell(90, 8, param, border=1)
        pdf.cell(90, 8, valor, border=1, ln=True)
    
    pdf.ln(10)

    # Alcance y Suministro
    pdf.set_font('helvetica', 'B', 12)
    pdf.cell(0, 10, 'ALCANCE DE SUMINISTRO Y COMPONENTES', ln=True)
    pdf.set_font('helvetica', '', 10)
    pdf.multi_cell(0, 6, "El proyecto comprende la ejecución integral bajo la modalidad 'llave en mano', "
                         "incluyendo ingeniería, suministro, montaje y gestión ante CNEL.")
    pdf.ln(5)

    # Análisis Financiero
    pdf.set_font('helvetica', 'B', 12)
    pdf.cell(0, 10, 'ANÁLISIS DE RENTABILIDAD', ln=True)
    pdf.set_font('helvetica', '', 10)
    texto_rentabilidad = (f"La implementación de este sistema representa una inversión estratégica de ${inversion_total:,.2f}. "
                          f"Mediante la aplicación de una depreciación acelerada del 50% anual, el proyecto permite "
                          f"recuperar la totalidad del capital invertido en un plazo de {retorno_anios} años.")
    pdf.multi_cell(0, 6, texto_rentabilidad)

    # Guardar en un archivo temporal para Streamlit
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(temp_file.name)
    return temp_file.name

# 5. Interfaz principal
st.write("Verifica los datos en la barra lateral y genera el documento.")

if st.button("Generar Propuesta en PDF"):
    ruta_pdf = generar_pdf()
    
    with open(ruta_pdf, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.success("¡PDF generado con éxito!")
    st.download_button(label="Descargar PDF",
                       data=PDFbyte,
                       file_name=f"Propuesta_Latitudsolar_{cliente}.pdf",
                       mime='application/octet-stream')
