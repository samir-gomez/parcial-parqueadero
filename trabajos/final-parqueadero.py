from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

# -------------------------------
# ABSTRACCIÓN
# -------------------------------
class Vehiculo(ABC):
    def __init__(self, placa: str, subtipo: str, hora_entrada: datetime, hora_salida: datetime):
        self.__placa = placa
        self.__subtipo = subtipo
        self.__hora_entrada = hora_entrada
        self.__hora_salida = hora_salida

    # Encapsulamiento: getters y setters
    def get_placa(self) -> str:
        return self.__placa

    def set_placa(self, placa: str) -> None:
        self.__placa = placa

    def get_subtipo(self) -> str:
        return self.__subtipo

    def set_subtipo(self, subtipo: str) -> None:
        self.__subtipo = subtipo

    def get_hora_entrada(self) -> datetime:
        return self.__hora_entrada

    def set_hora_entrada(self, hora: datetime) -> None:
        self.__hora_entrada = hora

    def get_hora_salida(self) -> datetime:
        return self.__hora_salida

    def set_hora_salida(self, hora: datetime) -> None:
        self.__hora_salida = hora

    # Métodos abstractos → polimorfismo
    @abstractmethod
    def calcular_precio(self) -> float:
        pass

    @abstractmethod
    def obtener_tipo(self) -> str:
        pass

    def __str__(self) -> str:
        return (f"\nVehículo: {self.obtener_tipo()} - {self.__subtipo}\n"
                f"Placa: {self.__placa}\n"
                f"Entrada: {self.__hora_entrada.strftime('%H:%M')}\n"
                f"Salida: {self.__hora_salida.strftime('%H:%M')}\n"
                f"Total a pagar: ${self.calcular_precio():.0f}\n")


# -------------------------------
# HERENCIA + POLIMORFISMO
# -------------------------------
class Moto(Vehiculo):
    def calcular_precio(self) -> float:
        horas = (self.get_hora_salida() - self.get_hora_entrada()).seconds / 3600
        return horas * 2000  # tarifa moto

    def obtener_tipo(self) -> str:
        return "Moto"


class Carro(Vehiculo):
    def calcular_precio(self) -> float:
        horas = (self.get_hora_salida() - self.get_hora_entrada()).seconds / 3600
        return horas * 4000  # tarifa carro

    def obtener_tipo(self) -> str:
        return "Carro"


class Bicicleta(Vehiculo):
    def calcular_precio(self) -> float:
        horas = (self.get_hora_salida() - self.get_hora_entrada()).seconds / 3600
        return horas * 1000  # tarifa bici

    def obtener_tipo(self) -> str:
        return "Bicicleta"


# -------------------------------
# CLASE PARQUEADERO
# -------------------------------
class Parqueadero:
    def __init__(self):
        self.__vehiculos: List[Vehiculo] = []

    def registrar_vehiculo(self, vehiculo: Vehiculo) -> None:
        self.__vehiculos.append(vehiculo)
        print(f"\n✅ Vehículo {vehiculo.get_placa()} registrado con éxito.")

    def mostrar_facturas(self) -> None:
        print("\n📋 FACTURAS DEL PARQUEADERO:")
        for i, v in enumerate(self.__vehiculos, 1):
            print(f"{i}. {v}")


# -------------------------------
# INTERACTIVIDAD
# -------------------------------
if __name__ == "__main__":
    parqueadero = Parqueadero()

    print("🚗 Bienvenido al Parqueadero 🚙\n")
    while True:
        print("Tipos de vehículo disponibles:")
        print("1. Moto")
        print("2. Carro")
        print("3. Bicicleta")
        print("4. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "4":
            break

        subtipo = input("Ingrese el subtipo (ejemplo: camioneta, scooter, montañera): ")
        placa = input("Ingrese la placa del vehículo: ")
        entrada_str = input("Ingrese la hora de entrada (HH:MM): ")
        salida_str = input("Ingrese la hora de salida (HH:MM): ")

        hora_entrada = datetime.strptime(entrada_str, "%H:%M")
        hora_salida = datetime.strptime(salida_str, "%H:%M")

        # Crear objeto según el tipo
        if opcion == "1":
            vehiculo = Moto(placa, subtipo, hora_entrada, hora_salida)
        elif opcion == "2":
            vehiculo = Carro(placa, subtipo, hora_entrada, hora_salida)
        elif opcion == "3":
            vehiculo = Bicicleta(placa, subtipo, hora_entrada, hora_salida)
        else:
            print("❌ Opción inválida.")
            continue

        parqueadero.registrar_vehiculo(vehiculo)

    # Mostrar facturas finales
    parqueadero.mostrar_facturas()
