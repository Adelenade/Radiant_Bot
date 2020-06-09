import discord
from discord.ext import commands
import time
import random
import mysql.connector

random.seed(2)

dbusers = mysql.connector.connect(
    host='localhost',
    user='Ade',
    password='soligaleo5',
    database='userslevels',
    auth_plugin='mysql_native_password'
)

date = time.strftime("%A %d %B %Y %H:%M:%S")


class Levels(commands.Cog):

    def __init__(self, client):
        self.client = client

    @staticmethod
    def generateXP():
        return random.randint(1, 10)

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog Levels ok!')
        print(dbusers)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        else:
            xp = Levels.generateXP()
            print(message.author.name + " A reçu " + str(xp) + " xp!")
            cursor = dbusers.cursor()
            cursor.execute("SELECT user_xp FROM users WHERE client_id =" + str(message.author.id))
            result = cursor.fetchall()

            if len(result) == 0:
                print("Utilisateur non présent dans la base de données... Ajout de l'utilisateur...")
                cursor.execute("INSERT INTO users VALUES(" + str(message.author.id) + "," + str(xp) + ")")
                dbusers.commit()
                print("Utilisateur ajouté.")
                print(result)

            else:
                newXP = result[0][0] + xp
                print("Xp total de l'utilisateur après ajout de l'xp: " + str(newXP))
                cursor.execute("UPDATE users SET user_xp = " + str(newXP) + " WHERE client_id = " + str(message.author.id))
                dbusers.commit()
                print("Database mise a jour.")

        if newXP >= 1500:
            cursor.execute("SELECT user_level FROM users WHERE client_id =" + str(message.author.id))
            lvlresult = cursor.fetchall()
            newLevel = lvlresult[0][0] + 1
            print(message.author.name + "Est monté d'un niveau! il est maintenant niveau " + str(newLevel))
            cursor.execute("UPDATE users SET user_level = " + str(newLevel) + " WHERE client_id = " + str(message.author.id))
            cursor.execute("UPDATE users SET user_xp = 0 WHERE client_id = " + str(message.author.id))
            dbusers.commit()
            print("Database mise a jour.")


def setup(client):
    client.add_cog(Levels(client))
