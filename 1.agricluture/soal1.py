from abc import ABC, abstractmethod


class Plant(ABC):
    def __init__(self, name, water_needs, fertilizer_needs):
        self._name = name
        self._water_needs = water_needs
        self._fertilizer_needs = fertilizer_needs
        self._adjusted_water_needs = water_needs
        self._adjusted_fertilizer_needs = fertilizer_needs

    @abstractmethod
    def grow(self):
        pass

    def calculate_needs(self, rainfall, soil_moisture):
        print(f"Weather Report: Rainfall = {rainfall} mm, Soil Moisture = {soil_moisture}%")
        # Logika penyesuaian kebutuhan air
        if rainfall >= 8 and soil_moisture >= 60:
            self._adjusted_water_needs = int(self._water_needs * 0.75)  # pengurangan 25%
        else:
            self._adjusted_water_needs = self._water_needs

        # Logika penyesuaian pupuk (misal tidak berubah, atau bisa disesuaikan)
        if soil_moisture < 50:
            self._adjusted_fertilizer_needs = int(self._fertilizer_needs * 1.1)  # tambah 10%
        else:
            self._adjusted_fertilizer_needs = self._fertilizer_needs

    def show_needs(self):
        # Tambah indikator pengurangan karena hujan
        if self._adjusted_water_needs < self._water_needs:
            print(f"Adjusted Water Needs: {self._adjusted_water_needs} liters (reduced due to rain)")
        else:
            print(f"Adjusted Water Needs: {self._adjusted_water_needs} liters")

        print(f"Adjusted Fertilizer Needs: {self._adjusted_fertilizer_needs} kg\n")


class RicePlant(Plant):
    def __init__(self):
        super().__init__("Rice", 20, 5)

    def grow(self):
        print(f"{self._name} is growing in the paddy field")
        


class CornPlant(Plant):
    def __init__(self):
        super().__init__("Corn", 18, 7)


    def grow(self):
        print(f"{self._name} is growing in the farm")

rice1 = RicePlant()
corn1 = CornPlant()
rice1.grow()
rice1.calculate_needs(rainfall=10, soil_moisture=75)
rice1.show_needs()
corn1.grow()
corn1.calculate_needs(rainfall=2, soil_moisture=40)
corn1.show_needs()

