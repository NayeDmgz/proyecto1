from django.shortcuts import render
import json
import time

def cargar_urls_desde_archivo(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as file:
        contenido = file.read()

    urls_por_palabra = {}
    try:
        datos = json.loads(contenido)
        for item in datos:
            palabra = item.get("palabra")
            frecuencia_url = item.get("frecuencia_url", {})
            urls_por_palabra[palabra] = list(frecuencia_url.keys())
    except json.JSONDecodeError as e:
        print(f"Error al decodificar el archivo JSON: {e}")
        return {}  # Devuelve un diccionario vacío si hay un error en el formato JSON

    return urls_por_palabra

def obtener_resultados(query, ruta_archivo):
    urls_por_palabra = cargar_urls_desde_archivo(ruta_archivo)
    urls_encontradas = urls_por_palabra.get(query, [])

    # Elimina las líneas de impresión de debugging
    # print(f"Query: {query}")
    # print(f"Urls encontradas para la consulta '{query}': {urls_encontradas}")

    return urls_encontradas

def mostrar_resultados(request):
    if request.method == 'GET':
        query = request.GET.get('consulta', '')
        ruta_archivo = 'C:\\Users\misae\\Videos\\proyecto1\\minigoogle\\generales\\raiz\\raiz_ind_inv.txt'
        

        start_time = time.time()  # Registra el tiempo de inicio de la búsqueda

        resultados = obtener_resultados(query, ruta_archivo)

        elapsed_time = time.time() - start_time  # Calcula el tiempo transcurrido
        # print(f"Tiempo de búsqueda para '{query}': {elapsed_time} segundos")

        cantidad_resultados = len(resultados)
        
        contexto = {
            'resultados': resultados,
            'consulta': query,
            'cantidad_resultados': cantidad_resultados,
            'tiempo_busqueda': elapsed_time,
        }
        return render(request, 'resultado_busqueda.html', contexto)


def mostrar_formulario_busqueda(request):
    return render(request, 'formulario_busqueda.html')

def mi_vista_de_inicio(request):
    # Lógica para la vista de inicio
    return render(request, 'formulario_busqueda.html', {})  # Reemplaza 'template_inicio.html' con tu plantilla
