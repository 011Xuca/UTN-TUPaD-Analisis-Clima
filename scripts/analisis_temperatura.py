import pandas
import matplotlib.pyplot

matplotlib.pyplot.switch_backend("agg")

print("=== ANALISIS DE TEMPERATURA GLOBAL ===\n")

# - CARGAR Y LIMPIAR DATOS
datos = pandas.read_csv("datos/monthly_csv.csv")
datos_limpios = datos.dropna()

# - INDICADORES
temp_promedio = datos_limpios["Mean"].mean()
temp_max = datos_limpios["Mean"].max()
temp_min = datos_limpios["Mean"].min()
temp_std = datos_limpios["Mean"].std()
cantidad_registros = len(datos_limpios)
año_inicio = datos_limpios["Year"].min()
año_fin = datos_limpios["Year"].max()

# - MOSTRAR RESULTADOS CLAROS
print("INFORMACION DEL DATASET")
print(f"Registros analizados: {cantidad_registros}")
print(f"Periodo: {año_inicio} - {año_fin}")

print("\nINDICADORES PRINCIPALES")
print(f"Temperatura promedio: {temp_promedio:+.2f}°C")
print(f"Temperatura maxima: {temp_max:+.2f}°C")
print(f"Temperatura minima: {temp_min:+.2f}°C")
print(f"Desviacion estandar: {temp_std:.2f}°C")

# - ANALISIS ADICIONAL
print("\nANALISIS ADICIONAL")
temp_positivas = (datos_limpios["Mean"] > 0).sum()
temp_negativas = (datos_limpios["Mean"] < 0).sum()
porcentaje_positivas = (temp_positivas / cantidad_registros) * 100

print(f"Registros con temperatura positiva: {temp_positivas} ({porcentaje_positivas:.1f}%)")
print(f"Registros con temperatura negativa: {temp_negativas} ({100 - porcentaje_positivas:.1f}%)")

# ---

# - GRAFICO 1
RUTA_PREDETERMINADA = "resultados/"

print("\nGENERANDO GRAFICOS")
matplotlib.pyplot.figure(figsize=(14, 6))
matplotlib.pyplot.plot(datos_limpios.index, datos_limpios["Mean"], linewidth = 1.5, color = "#d62728", alpha = 0.8)
matplotlib.pyplot.fill_between(datos_limpios.index, datos_limpios["Mean"], alpha = 0.2, color = "#d62728")
matplotlib.pyplot.axhline(y = 0, color = "black", linestyle = "-", linewidth = 0.8, alpha = 0.5)
matplotlib.pyplot.axhline(y = temp_promedio, color = "blue", linestyle = "--", linewidth = 2, label = f"Promedio: {temp_promedio:+.2f}°C", alpha = 0.7)
matplotlib.pyplot.title("Evolucion de la Temperatura Global (1850 - Actualidad)", fontsize = 14, fontweight = "bold")
matplotlib.pyplot.xlabel("Tiempo (registros mensuales)", fontsize = 12)
matplotlib.pyplot.ylabel("Anomalía de Temperatura (°C)", fontsize = 12)
matplotlib.pyplot.legend(fontsize = 11)
matplotlib.pyplot.grid(True, alpha = 0.3)
matplotlib.pyplot.tight_layout()
matplotlib.pyplot.savefig(f"{RUTA_PREDETERMINADA}evolucion_temperatura.png", dpi = 300, bbox_inches="tight")
print("Grafico 1: evolucion_temperatura.png")

# - GRAFICO 2
matplotlib.pyplot.figure(figsize=(10, 6))
matplotlib.pyplot.hist(datos_limpios["Mean"], bins=50, color="#1f77b4", edgecolor="black", alpha=0.7)
matplotlib.pyplot.axvline(temp_promedio, color = "red", linestyle = "--", linewidth = 2.5, label = f"Promedio: {temp_promedio:+.2f}°C")
matplotlib.pyplot.axvline(0, color = "black", linestyle = "-", linewidth = 1, alpha = 0.5, label = "Línea base (0°C)")
matplotlib.pyplot.title("Distribucion de Temperaturas", fontsize = 14, fontweight = "bold")
matplotlib.pyplot.xlabel("Temperatura (°C)", fontsize = 12)
matplotlib.pyplot.ylabel("Frecuencia", fontsize = 12)
matplotlib.pyplot.legend(fontsize = 11)
matplotlib.pyplot.grid(True, alpha = 0.3, axis = "y")
matplotlib.pyplot.tight_layout()
matplotlib.pyplot.savefig(f"{RUTA_PREDETERMINADA}distribucion_temperatura.png", dpi = 300, bbox_inches = "tight")
print("Grafico 2: distribucion_temperatura.png")

matplotlib.pyplot.close("all")