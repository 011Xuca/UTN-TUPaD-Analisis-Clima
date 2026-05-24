# Analisis de Temperatura Global

## Integrante
Facundo Emanuel Yramain (Comision 3)

## Escenario
Analisis de Datos Climaticos - Temperatura Global

## Descripción
Este proyecto analiza datos historicos de temperatura global para identificar 
tendencias en el cambio climatico. Se calculan indicadores como temperatura 
promedio, maxima, minima y se genera una visualización de la evolución temporal.

## Dataset
- Fuente: DataHub - Global Temperature
- Archivo: monthly.csv
- Periodo: Datos historicos globales

## Indicadores Calculados
- Temperatura promedio global
- Temperatura maxima
- Temperatura minima
- Desviación estandar

## Instrucciones para ejecutar
1. Asegúrate de tener Python instalado
2. Instala las librerias necesarias: `pip3 install pandas matplotlib`
3. Ejecuta el script: `scripts/analisis_temperatura.py`
4. Los graficos se guardaran en la carpeta `/resultados`

## Archivos principales
- `scripts/analisis_temperatura.py` - Script principal de analisis
- `datos/monthly.csv` - Dataset de temperatura
- `resultados/` - Graficos generados