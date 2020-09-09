# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, health, room):
        self.name = name
        self.health = health
        self.room = room

    def __str__(self):
        return f"{self.name.capitalize()} has health {self.health} and is currently in room {self.room}"

    def __repr__(self):
        return f"Player(health: {self.health}, room: {self.room})"
