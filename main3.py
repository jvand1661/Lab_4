from classes import Team, Driver
import csv

teams = {}

with open("f1_points.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        driver_name = row["Driver"]
        team_name = row["Team"]
        points = int(row["Points"])

        if team_name not in teams:
            teams[team_name] = Team(team_name)

        driver = Driver(driver_name, points)

        teams[team_name].add_driver(driver)

sorted_teams = sorted(teams.values())

if __name__ == "__main__":
    for team in sorted_teams:
        print(team)