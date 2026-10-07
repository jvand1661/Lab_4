
class Driver:

    def __init__(self, name: str, points: int):
        self.name = name
        self.points = points

    def __repr__(self) -> str:      
        return f"{self.name} ({self.points} pts)"


class Team:

    def __init__(self, name: str):
        self.name = name
        self.drivers = []
    
    def add_driver(self, driver: Driver) -> None:
        self.drivers.append(driver)

    def get_total_points(self) -> int:
        total = 0

        for driver in self.drivers:
            total += driver.points

        return total

    def __repr__(self) -> str:
        driver_names = []

        for driver in self.drivers:
            driver_names.append(driver.name)

        return f"{self.name} with drivers {', '.join(driver_names)}. Total pts: {self.get_total_points()}"

    def __lt__(self, other) -> bool:
        return self.get_total_points() < other.get_total_points()
