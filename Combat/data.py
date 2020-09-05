""" Data Model for Discord Bot """
from os import getenv
from typing import List
from pymongo import MongoClient


class DataModel:

    def _connect(self):
        """ MongoDB Table Connection """
        db = MongoClient(
            f"mongodb+srv://{getenv('MONGODB_USER')}:{getenv('MONGODB_PASS')}"
            f"@{getenv('MONGODB_URI')}/test?retryWrites=true&w=majority"
        )
        return db.discord_bot.characters

    def push(self, character: dict):
        db = self._connect()
        db.insert_one(character)

    def load(self, query: dict) -> dict:
        db = self._connect()
        return db.find_one(query)

    def find(self, query: dict) -> List[dict]:
        db = self._connect()
        return list(db.find(query))

    def update(self, query: dict, character: dict):
        db = self._connect()
        db.replace_one(query, character, upsert=True)
