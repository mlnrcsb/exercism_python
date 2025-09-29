class SpaceAge:
    def __init__(self, seconds):
        self.age = seconds/3600/24/365.25

    def on_earth(self):
        ORBITAL_PERIOD_IN_EARTH_YEARS = 1
        return round(self.age / ORBITAL_PERIOD_IN_EARTH_YEARS, 2)

    def on_mercury(self):
        ORBITAL_PERIOD_IN_EARTH_YEARS = 0.2408467
        return round(self.age / ORBITAL_PERIOD_IN_EARTH_YEARS, 2)

    def on_venus(self):
        ORBITAL_PERIOD_IN_EARTH_YEARS = 0.61519726
        return round(self.age / ORBITAL_PERIOD_IN_EARTH_YEARS, 2)

    def on_mars(self):
        ORBITAL_PERIOD_IN_EARTH_YEARS = 1.8808158
        return round(self.age / ORBITAL_PERIOD_IN_EARTH_YEARS, 2)

    def on_jupiter(self):
        ORBITAL_PERIOD_IN_EARTH_YEARS = 11.862615
        return round(self.age / ORBITAL_PERIOD_IN_EARTH_YEARS, 2)

    def on_saturn(self):
        ORBITAL_PERIOD_IN_EARTH_YEARS = 29.447498
        return round(self.age / ORBITAL_PERIOD_IN_EARTH_YEARS, 2)

    def on_uranus(self):
        ORBITAL_PERIOD_IN_EARTH_YEARS = 84.016846
        return round(self.age / ORBITAL_PERIOD_IN_EARTH_YEARS, 2)

    def on_neptune(self):
        ORBITAL_PERIOD_IN_EARTH_YEARS = 164.79132
        return round(self.age / ORBITAL_PERIOD_IN_EARTH_YEARS, 2)