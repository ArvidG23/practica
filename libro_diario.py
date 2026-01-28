class LibroDiario:
    """Clase que gestiona las transacciones del libro diario contable."""

    def __init__(self):
        """Inicializa el libro diario con una lista vacía de transacciones."""
        self.transacciones = []

    def agregar(self, fecha, descripcion, monto, tipo):
        """Agrega una transacción al libro diario."""
        self.transacciones.append({
            "fecha": fecha,
            "descripcion": descripcion,
            "monto": monto,
            "tipo": tipo
        })

    def resumen(self):
        """Devuelve un resumen de los ingresos y egresos."""
        ingresos = 0
        egresos = 0
        for t in self.transacciones:
            if t["tipo"] == "ingreso":
                ingresos += t["monto"]
            else:
                egresos += t["monto"]
        return "Total ingresos: " + str(ingresos) + " Total egresos: " + str(egresos)

