import discord
from discord.ext import commands
import time

date = time.strftime("%A %d %B %Y %H:%M:%S")


class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog Modération ok!')

    # ────────────────────clear────────────────────

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=99):
        await ctx.channel.purge(limit=amount + 1)
        embed = discord.Embed(title="Clear", description=f"{amount} messages ont été supprimés!", color=0xf5eded)
        embed.set_footer(text=date)
        await ctx.send(embed=embed, delete_after=5)

    # ────────────────────ban/kick/unban────────────────────

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed = discord.Embed(title="Ban", description=f"{member} a été banni!", color=0xfe0b00)
        embed.set_footer(text=f"BabelBot {date}")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(title="Kick", description=f"{member} a été kick !", color=0xfe0b00)
        embed.set_footer(text=f"BabelBot {date}")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users=await ctx.guild.bans()
        member_name, member_discriminator=member.split('#')

        for ban_entry in banned_users:
            user=ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(title="Unban", description=f"{user.name}#{user.discriminator} a été unban!", color=0xfe0b00)
                embed.set_footer(text=f"Babel | RP {date}")
                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Moderation(client))
