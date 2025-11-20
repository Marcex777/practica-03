import csv

class Analizador:
    def __init__(self, ruta_csv):
        self.ruta_csv = ruta_csv
        try:
            self.datos = self._leer_csv()
            print(f"DEBUG: {len(self.datos)} filas cargadas correctamente.")
        except Exception as e:
            print(f"ERROR al inicializar el analizador: {e}")
            self.datos = []

    def _leer_csv(self):
        datos = []
        try:
            with open(self.ruta_csv, "r", encoding="utf-8") as archivo:
                lector = csv.DictReader(archivo, delimiter='|')
                for fila in lector:
                    datos.append(fila)
        except FileNotFoundError:
            print(f"ERROR: No se encontró el archivo: {self.ruta_csv}")
            return []
        return datos

    def ventas_totales_por_provincia(self):
        totales = {}
        for fila in self.datos:
            try:
                provincia = fila["PROVINCIA"].upper()
                total_venta = float(fila["TOTAL_VENTAS"])

                if provincia not in totales:
                    totales[provincia] = total_venta
                else:
                    totales[provincia] += total_venta
            except Exception:
                continue
        return totales

    def ventas_por_provincia(self, nombre):
        totales = self.ventas_totales_por_provincia()
        nombre = nombre.upper()

        if nombre not in totales:
            raise KeyError(f"La provincia '{nombre}' no existe en el dataset.")

        return totales[nombre]
