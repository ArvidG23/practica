""" Módulo que gestiona el libro diario para registrar transacciones
contables. """

from typing import List, Dict


class LibroDiario:
    """ Clase que gestiona las transacciones del libro diario contable. """

    def __init__(self):
        """ Inicializa el libro diario con una lista vacía de transacciones. """
        self.transacciones: List[Dict[str, str]] = []

    def agregar(self, fecha: str, descripcion: str, monto: float, tipo: str) -> None:
        """ Agrega una transacción al libro diario. """
        if tipo not in ["ingreso", "egreso"]:
            raise ValueError(
                "El tipo debe ser 'ingreso' o 'egreso'."
            )
        if monto <= 0:
            raise ValueError("El monto debe ser positivo.")
        self.transacciones.append({
            "fecha": fecha,
            "descripcion": descripcion,
            "monto": monto,
            "tipo": tipo
        })

    def resumen(self) -> Dict[str, float]:
        """ Devuelve un resumen de los ingresos y egresos. """
        ingresos = sum(
            t["monto"]
            for t in self.transacciones
            if t["tipo"] == "ingreso"
        )
        egresos = sum(
            t["monto"]
            for t in self.transacciones
            if t["tipo"] == "egreso"
        )

        return {
            "total_ingresos": ingresos,
            "total_egresos": egresos
        }
