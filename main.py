# IMPORTS
import discord
from discord_components import *
import asyncpraw
from discord.ext import commands
import random
from random import choice, choices
import math
import json
import os
import requests

"----------------------------------------------------------------------------------------------------------------------"

# Searching for directory of SIDE_BOT...
os.chdir("C:\\Users\\Krrish\\PycharmProjects\\pythonProject9\\sidemen_bot")
"----------------------------------------------------------------------------------------------------------------------"

# Staring the bot
client = commands.Bot(command_prefix='>')
client.remove_command("help")
api_token = 'TOKEN'
"----------------------------------------------------------------------------------------------------------------------"
"""1. 
   2. 
   3. 
   4. 
   5. 
   6. 
   and more......."""
"----------------------------------------------------------------------------------------------------------------------"

# Settings of Tic Tac Toe
player1 = ""
player2 = ""
turn = ""
gameOver = True
"----------------------------------------------------------------------------------------------------------------------"

# Initializing board as list
board = []
"----------------------------------------------------------------------------------------------------------------------"

# Conditions to win tic tac toe...
winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]
"----------------------------------------------------------------------------------------------------------------------"

"""Event when bot starts:
   Changes status from None to 'Sidemen!! | use >'....."""


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Sidemen!! | use'>'"))
    print("bot is ready")
    DiscordComponents(client)


"----------------------------------------------------------------------------------------------------------------------"


# custom help command
@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title="HELP", description="Use >help <command> for info \n\n"
                                                 "**MINI GAMES:**\n\n\n"
                                                 "1. 8 Ball ------> [>8b/>8ball]<question> | 8ball answers your question\n\n"
                                                 "2. JUA    ------> >jua <amount> | Bet against the bot\n\n"
                                                 "3. RPS    ------> >rps <choice> | Play rock paper scissors v/s bot\n\n"
                                                 "4. DICE   ------> >roll | Bot rolls the dice for you\n\n"
                                                 "5. SLOTS  ------> >slots <amount> | Place bets on the slot machine\n\n"
                                                 "6.(A) TTT ------> >tictactoe <@player1> <@player2> | Play tictactoe\n\n"
                                                 "  (B) Place-----> >place <integer b/w 1 and 9> | Place X or O\n\n"
                                                 "7. TOSS   ------> >toss | Bot tosses a coin\n\n\n"
                                                 "**CURRENCY:**\n\n\n"
                                                 "1.BALANCE ------> >balance | Checks your account balance\n\n"
                                                 "2. BEG    ------> >beg | Beg from the sidemen\n\n"
                                                 "3.DEPOSIT ------> >deposit <amount> | Deposit from wallet to bank\n\n"
                                                 "4.WITHDRAW -----> >withdraw <amount> | Withdraw from bank\n\n"
                                                 "5. ROB    ------> >rob <member> | Try robbing your server members\n\n"
                                                 "6.SEND MONEY----> >sendmoney<member> | Send money to a mate\n\n\n"
                                                 "**SIDEMEN EXCLUSIVE:**\n\n\n"
                                                 "1. SIDEMEN -----> >sidemen <sideman name> | Gives their channel info\n\n"
                                                 "2. SDMN AVATAR--> >avatar | Which sideman are you??\n\n\n"
                                                 "**UTILITY:**\n\n\n"
                                                 "1. DELETE  -----> >clear <number of messages> | Clear up to 100 msgs\n\n"
                                                 "2. HELP    -----> >help | Shows this message\n\n"
                                                 "3. INFO  ------> >server | Returns server info\n\n\n"
                                                 "**EXTRAS:**\n\n\n"
                                                 "1. B.M.I   ------> >bmi <height(in cm)> <weight(Kg)> | Gives B.M.I\n\n"
                                                 "2. CALCULATOR ----> >calc <num1>(operator)<num2> | Computes result\n\n"
                                                 "3. GREET  -----> >hey | Waves Hi back (doesn't leave you hanging)\n\n"
                                                 "4. MEMES  -----> >meme | returns meme (pls be patient python takes time)\n\n"
                                                 "5. LATENCY ------> >ping | Shows latency\n\n"
                                                 "6. PP   ------> >pp | Your pp\n\n"
                                                 "7. QUOTE ------> >quotes | Returns a quote",
                       colour=discord.Colour.dark_red(),
                       timestamp=ctx.message.created_at)
    em.set_thumbnail(url="https://yt3.ggpht.com/ytc/"
                         "AKedOLSqViMyjHw5AiYTSTKnrmyCq-Bba5KS941AqfvpWw=s900-c-k-c0x00ffffff-no-rj")
    em.set_footer(text="HELP MENU")
    await ctx.send(embed=em)

"----------------------------------------------------------------------------------------------------------------------"
"""EVENT:
      greets members when the join"""


@client.event
async def on_member_join(member, ctx):
    embed = discord.Embed(description=f"Welcome {member.name}")
    await ctx.send(embed=embed)


"----------------------------------------------------------------------------------------------------------------------"


# Clear Messages
@client.command(name="clear", help=" --> clear up to 100 messages in one go")
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)


"----------------------------------------------------------------------------------------------------------------------"


# Returns a quote from Zenquotes.io
@client.command(name="quotes", help=" --> Gives a quote ...")
async def quotes(ctx):
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "\n\n--" + json_data[0]['a']
    embed = discord.Embed(title="**INSPIRATION**", description=quote,
                          color=discord.Colour.random(),
                          timestamp=ctx.message.created_at)
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/"
                            "images?q=tbn:ANd9GcQWEXerr2qK3ee-9S3Fu8r7AO2EUAm3WMbfTQ&usqp=CAU")
    embed.set_footer(text=f"{ctx.author.display_name}'s quote")
    await ctx.send(embed=embed)


"----------------------------------------------------------------------------------------------------------------------"


# Returns latency
@client.command(name='ping', help=' --> Check latency')
async def ping(ctx):
    pong = client.latency * 1000
    embed = discord.Embed(title="Ping", description=f"**Latency**: {pong}ms", color=discord.Color.random())
    await ctx.send(embed=embed)


"----------------------------------------------------------------------------------------------------------------------"

"""EVENT:
    When there is an error in command,
    it returns an error message"""


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Please Check whether you have entered the correct command...")


"----------------------------------------------------------------------------------------------------------------------"


# Returns a greeting personally to author of message
@client.command(name="hey", help=" --> Cause not everyone says Hello")
async def hey(ctx):
    auth = ctx.author
    embed = discord.Embed(name="Hello", description=f":wave:**Hey** {auth.name}, good to see you",
                          color=discord.Colour.random())
    embed.set_thumbnail(url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


"----------------------------------------------------------------------------------------------------------------------"

"""MINI_GAME: TIC TAC TOE ,
   play with other members in discord server"""


@client.command(name="tictactoe", help=" --> Play tictactoe with a friend!")
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")


"----------------------------------------------------------------------------------------------------------------------"

# Place X or O when it is your turn
"""PARAMETERS: ctx, position of x or o,
    VARIABLES: turn 1, turn 2, place, board, count, game over"""


@client.command(name="place", help=" --> Place X or O")
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the !tictactoe command.")


"----------------------------------------------------------------------------------------------------------------------"


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True


"----------------------------------------------------------------------------------------------------------------------"


# error check for game board
@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")


"----------------------------------------------------------------------------------------------------------------------"


# error check while placing X or O
@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")


"----------------------------------------------------------------------------------------------------------------------"


# use of replication of string
@client.command()
async def pp(ctx):
    stringing = "="
    embed = discord.Embed(title=f"{ctx.author.display_name}'s pp", description=f" 8{stringing * random.randint(1, 10)}D"
                          , colour=discord.Colour.random())
    embed.set_thumbnail(url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


"----------------------------------------------------------------------------------------------------------------------"

"""SERVER INFO:-->
   1. Name-
   2. Owner-
   3. I.D-
   4. Group Icon-
   5. Region-"""


@client.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    member_count = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color.random()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=member_count, inline=True)

    await ctx.send(embed=embed)


"----------------------------------------------------------------------------------------------------------------------"

# Rock paper scissors
"""PARAMETERS: ctx, (spaces), guess-
   uses random for bot choice..."""


@client.command(name="rps", help=" --> Play rock Paper scissors")
async def rps(ctx, *, guess):
    ch1 = ["rock", "paper", "scissors"]
    bot_answer = choice(ch1)
    if guess not in ch1:
        embed = discord.Embed(title="**Rock Paper Scissors**", description="**ERROR** :interrobang:", color=0xF85252)
        await ctx.send(embed=embed)
    else:
        if bot_answer == guess:
            embed = discord.Embed(title="**Rock Paper Scissors**",
                                  description=f"**DRAW**, we both picked **{bot_answer}**",
                                  color=discord.Colour.random())
            embed.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/"
                    "images?q=tbn:ANd9GcRAGr0w5G_Z_UgIR6Q0207lSwmQrHo7seRt2g&usqp=CAU")
            await ctx.send(embed=embed)
        if bot_answer == "rock":
            if guess == "paper":
                embed = discord.Embed(title="**Rock Paper Scissors**",
                                      description=f"**You win** , i picked **{bot_answer}** and you chose **{guess}**",
                                      color=discord.Color.random())
                embed.set_thumbnail(url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
        if bot_answer == "rock":
            if guess == "scissors":
                embed = discord.Embed(title="**Rock Paper Scissors**",
                                      description=f"**You Lose** , i picked **{bot_answer}** and you chose **{guess}**",
                                      color=discord.Color.random())
                embed.set_thumbnail(url="https://i.redd.it/f3iy7etf3ur41.jpg")
                await ctx.send(embed=embed)
        if bot_answer == "paper":
            if guess == "scissors":
                embed = discord.Embed(title="**Rock Paper Scissors**",
                                      description=f"**You win** , i picked **{bot_answer}** and you chose **{guess}**",
                                      color=discord.Colour.random())
                embed.set_thumbnail(url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
        if bot_answer == "paper":
            if guess == "rock":
                embed = discord.Embed(title="**Rock Paper Scissors**",
                                      description=f"**You Lose** , i picked **{bot_answer}** and you chose **{guess}**",
                                      color=discord.Colour.random())
                embed.set_thumbnail(url="https://i.redd.it/f3iy7etf3ur41.jpg")
                await ctx.send(embed=embed)
        if bot_answer == "scissors":
            if guess == "paper":
                embed = discord.Embed(title="**Rock Paper Scissors**",
                                      description=f"**You Lose** , i picked **{bot_answer}** and you chose **{guess}**",
                                      color=discord.Colour.random())
                embed.set_thumbnail(url="https://i.redd.it/f3iy7etf3ur41.jpg")
                await ctx.send(embed=embed)
        if bot_answer == "scissors":
            if guess == "rock":
                embed = discord.Embed(title="**Rock Paper Scissors**",
                                      description=f"**You Win** , i picked **{bot_answer}** and you chose **{guess}**",
                                      color=discord.Colour.random())
                embed.set_thumbnail(url=ctx.author.avatar_url)
                await ctx.send(embed=embed)


"----------------------------------------------------------------------------------------------------------------------"

"""PARAMETERS: ctx, __SPACE__, QUESTION"""


# 8-ball mini game
@client.command(aliases=["8b", "8ball"], help=" --> Get Answers to your questions")
async def _8ball(ctx, *, question):
    responses = ("It is certain",
                 "Without a doubt",
                 "Yes definitely",
                 "You may rely on it",
                 "It is decidedly so",
                 "As I see it, yes",
                 "Most likely",
                 "Yes",
                 "Outlook good",
                 "Signs point to yes",
                 "Reply hazy try again",
                 "Better not tell you now",
                 "Ask again later",
                 "Cannot predict now",
                 "Concentrate and ask again",
                 "Don’t count on it",
                 "Outlook not so good",
                 "My sources say no",
                 "Very doubtful",
                 "My reply is no",
                 "F....you wouldn't like what i have to say")

    em = discord.Embed(title="**8BALL**",
                       description=f":8ball: Question:{question}\n:8ball: Answer: {choices(responses)}",
                       colour=discord.Colour.random(),
                       timestamp=ctx.message.created_at)
    em.set_footer(text=f"{ctx.author.display_name}'s answer")
    em.set_thumbnail(url="https://i.pinimg.com/236x/36/d8/a3/36d8a3cb3cacd453cc1b08e562fc2608.jpg")

    await ctx.send(embed=em)


"----------------------------------------------------------------------------------------------------------------------"

"""PARAMETERS: ctx, float, float , operator
   OPERATORS --> +, -, *, /, ^, sqrt"""


# calculator
@client.command()
async def calc(ctx, num1: float, res: str, num2: float):
    operators = ["+", "-", "*", "/", "^", "sqrt"]
    if res in operators:
        if res == "+":
            em = discord.Embed(title="**ADDITION**", description=f"Result: {num1 + num2}",
                               colour=discord.Colour.random(),
                               timestamp=ctx.message.created_at)
            await ctx.send(embed=em)
        if res == "-":
            em = discord.Embed(title="**SUBTRACTION**", description=f"Result: {num1 - num2}",
                               colour=discord.Colour.random(),
                               timestamp=ctx.message.created_at)
            await ctx.send(embed=em)
        if res == "*":
            em = discord.Embed(title="**MULTIPLICATION**", description=f"Result: {num1 * num2}",
                               colour=discord.Colour.random(),
                               timestamp=ctx.message.created_at)
            await ctx.send(embed=em)
        if res == "/":
            em = discord.Embed(title="**DIVISION**", description=f"Result: {num1 / num2}",
                               colour=discord.Colour.random(),
                               timestamp=ctx.message.created_at)
            await ctx.send(embed=em)
        if res == "^":
            em = discord.Embed(title="**EXPONENT**", description=f"Result: {num1 ** num2}",
                               colour=discord.Colour.random(),
                               timestamp=ctx.message.created_at)
            await ctx.send(embed=em)
        if res == "sqrt":
            em = discord.Embed(title="**SQUARE ROOT**", description=f"Result: first: {math.sqrt(num1)}, \n"
                                                                    f"second: {math.sqrt(num2)}",
                               colour=discord.Colour.random(),
                               timestamp=ctx.message.created_at)
            await ctx.send(embed=em)

    else:
        embed = discord.Embed(title="ERROR", description="THE INPUT COMMAND DOESN'T EXIST",
                              colour=discord.Colour.dark_red())
        await ctx.send(embed=embed)


"----------------------------------------------------------------------------------------------------------------------"

"""PARAMETERS: ctx, sideman name"""


# links to channels of the sidemen
@client.command()
async def sidemen(ctx, side: str):
    responses = ["sidemen", "ksi", "JJ", "w2s", "behz", "zerkaa", "tbjzl", "TBJZL", "VIKK", "vikk", "miniminter",
                 "simon"]
    if side in responses:
        if side == "sidemen":
            em = discord.Embed(title="**SIDEMEN**",
                               description="Sidemen XIX: https://www.youtube.com/channel/UCDogdKl7t7NHzQ95aEwkdMw \n\n"
                                           "MoreSidemen: https://www.youtube.com/channel/UCh5mLn90vUaB1PbRRx_AiaA \n\n"
                                           "SidemenReacts: https://www.youtube.com/channel/UCjRkTl_HP4zOh3UFaThgRZw",
                               colour=discord.Colour.random(),
                               timestamp=ctx.message.created_at)
            em.set_thumbnail(
                url="https://yt3.ggpht.com/ytc/"
                    "AKedOLSqViMyjHw5AiYTSTKnrmyCq-Bba5KS941AqfvpWw=s900-c-k-c0x00ffffff-no-rj")
            await ctx.send(embed=em)
        if side == "ksi" or side == "JJ":
            em = discord.Embed(title="**FATNEEK**",
                               description="KSI:https://www.youtube.com/channel/UCVtFOytbRpEvzLjvqGG5gxQ"
                                           "\n\n JJ:https://www.youtube.com/user/KSIOlajidebtHD",
                               colour=discord.Colour.random(),
                               timestamp=ctx.message.created_at)
            em.set_thumbnail(
                url="https://static.wikia.nocookie.net/ksi/images/b/b8/Baldski.png"
                    "/revision/latest/top-crop/width/360/height/450?cb=20201223000429")
            await ctx.send(embed=em)
        if side == "w2s":
            em = discord.Embed(title="**HAROLDINHO**",
                               description="W2S:https://www.youtube.com/user/wroetoshaw \n\n"
                                           "W2S plays:https://www.youtube.com/user/BlueJumperGaming",
                               colour=discord.Colour.random(),
                               timestamp=ctx.message.created_at)
            em.set_thumbnail(
                url="https://i.redd.it/czqkza30v4661.jpg")
            await ctx.send(embed=em)
        if side == "behz":
            em = discord.Embed(title="**BIG BEHZ**", description="BEHZ: https://www.youtube.com/user/Behzinga \n\n"
                                                                 "BEH2INGA: https://www.youtube.com/user/Beh2inga",
                               colour=discord.Colour.random(),
                               timestamp=ctx.message.created_at)
            em.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/"
                    "images?q=tbn:ANd9GcThsV3bCJpDVLP8yWbDd7iribV8S0GAsDAYmw&usqp=CAU")
            await ctx.send(embed=em)
        if side == "zerkaa":
            em = discord.Embed(title="**BIG JOSHER**",
                               description="ZERKAA:https://www.youtube.com/user/ZerkaaHD \n\n"
                                           "ZERKAAPLAYS:https://www.youtube.com/user/ZerkaaPlays",
                               colour=discord.Colour.random(),
                               timestamp=ctx.message.created_at)
            em.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/"
                    "images?q=tbn:ANd9GcSgLKCyE1U0b60plvLg06RiM86MueQoH-d3NQ&usqp=CAU")
            await ctx.send(embed=em)
        if side == "tbjzl" or side == "TBJZL":
            em = discord.Embed(title="**TBJZL**", description="TBJZL:https://www.youtube.com/user/TBJZL \n\n"
                                                              "TBJZLplays:https://www.youtube.com/user/EDITinGAMING",
                               colour=discord.Colour.random(),
                               timestamp=ctx.message.created_at)
            em.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/"
                    "images?q=tbn:ANd9GcRsT0F5C10Tw_QQSdfKDz59ZJ08b6DOOYqm2g&usqp=CAU")
            await ctx.send(embed=em)
        if side == "vikk" or side == "VIKK":
            em = discord.Embed(title="**VIKK**", description="Vikkstar123:https://www.youtube.com/user/Vikkstar123 \n\n"
                                                             "Vikkstar123HD:https://www.youtube.com/user/Vikkstar123HD",
                               colour=discord.Colour.random(),
                               timestamp=ctx.message.created_at)
            em.set_thumbnail(
                url="https://encrypted-tbn0.gstatic.com/"
                    "images?q=tbn:ANd9GcRzXimWIdYQGBHYJsZqF33y5uDf9FDloIOidw&usqp=CAU")
            await ctx.send(embed=em)
        if side == "miniminter" or side == "simon":
            em = discord.Embed(title="**MINIMINTER**",
                               description="Miniminter:https://www.youtube.com/user/miniminter \n\n"
                                           "MM7Games:https://www.youtube.com/user/MM7Games",
                               colour=discord.Colour.random(),
                               timestamp=ctx.message.created_at)
            em.set_thumbnail(
                url="https://www.famousbirthdays.com/faces/miniminter-image.jpg")
            await ctx.send(embed=em)

    else:
        em = discord.Embed(description="ERROR....that's not a sideman", colour=discord.Colour.random())
        await ctx.send(embed=em)


"----------------------------------------------------------------------------------------------------------------------"


# what's your sideman avatar
@client.command()
async def avatar(ctx):
    sdmn = ["Harry", "JJ", "Josh", "Ethan", "Tobi", "Vikk", "Simon"]
    ch = choice(sdmn)
    if ch in sdmn:
        if ch == "Harry":
            em = discord.Embed(title="YOU ARE HARRY!!",
                               description="Channel name : W2S(15M)| W2Splays(3M) \n\n"
                                           "Age: 24 years \n\n"
                                           "Qualities: More ket and alcohol plzz",
                               colour=discord.Colour.random())
            em.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/"
                                 "images?q=tbn:ANd9GcRRpkxJTIqVefKruIvPB4wFXQABBYay5GjrEw&usqp=CAU")
            await ctx.send(embed=em)
        if ch == "JJ":
            em = discord.Embed(title="YOU ARE JJ!!",
                               description="Channel name : KSI(22M)| JJOlatunji(13M) \n\n"
                                           "Age: 28 years \n\n"
                                           "Qualities: The G.O.A.T",
                               colour=discord.Colour.random())
            em.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/"
                                 "images?q=tbn:ANd9GcSm3ZrH5myR33MJdS2CO8ckQgaLTCoc4j7oBw&usqp=CAU")
            await ctx.send(embed=em)
        if ch == "Josh":
            em = discord.Embed(title="YOU ARE JOSH!!",
                               description="Channel name : Zerkaa(4M)| ZerkaaPlays(1M) \n\n"
                                           "Age: 28 years \n\n"
                                           "Qualities: The Old Man--> Backbone of the sidemen",
                               colour=discord.Colour.random())
            em.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/"
                                 "images?q=tbn:ANd9GcSgLKCyE1U0b60plvLg06RiM86MueQoH-d3NQ&usqp=CAU")
            await ctx.send(embed=em)
        if ch == "Ethan":
            em = discord.Embed(title="YOU ARE ETHAN!!",
                               description="Channel name : Behzinga(4M)| Beh2inga(2M) \n\n"
                                           "Age: 25 years \n\n"
                                           "Qualities: The Gym Lad",
                               colour=discord.Colour.random())
            em.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/"
                                 "images?q=tbn:ANd9GcThsV3bCJpDVLP8yWbDd7iribV8S0GAsDAYmw&usqp=CAU")
            await ctx.send(embed=em)
        if ch == "Tobi":
            em = discord.Embed(title="YOU ARE TOBI!!",
                               description="Channel name : TBJZL(4M)| TBJZLPlays(1M) \n\n"
                                           "Age: 28 years \n\n"
                                           "Qualities: The G.M.F",
                               colour=discord.Colour.random())
            em.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/"
                                 "images?q=tbn:ANd9GcTh4-HaA34qWQ85VVXI5nTK_b7748BUl18gag&usqp=CAU")
            await ctx.send(embed=em)
        if ch == "Vikk":
            em = discord.Embed(title="YOU ARE VIKK!!",
                               description="Channel name : VikkStar123(7M)| VikkStar123HD(3M) \n\n"
                                           "Age: 25 years \n\n"
                                           "Qualities: One of Two from Folabi and Punjabi",
                               colour=discord.Colour.random())
            em.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/"
                                 "images?q=tbn:ANd9GcQ37J3WsbNzjZPQ4cC95P6M3GbosP9C0Ivyvw&usqp=CAU")
            await ctx.send(embed=em)
        if ch == "Simon":
            em = discord.Embed(title="YOU ARE SIMON!!",
                               description="Channel name : Miniminter(9M)| MM7Games(4M) \n\n"
                                           "Age: 28 years \n\n"
                                           "Qualities: The Wedgeman",
                               colour=discord.Colour.random())
            em.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/"
                                 "images?q=tbn:ANd9GcQ9vxglO9ElRRs8Db8QrH0e8nk1YFJfAJ4oxA&usqp=CAU")
            await ctx.send(embed=em)
    else:
        ctx.send("Error something went wrong....")


"----------------------------------------------------------------------------------------------------------------------"

"""using async-praw:
   This is used instead of praw as we are using it in an 
   asynchronous environment...."""


# To access subreddit r/memes
@client.command()
async def meme(ctx, sub_red="memes"):
    reddit = asyncpraw.Reddit(
        client_id="h8w9HZKqxL7EUA",
        client_secret="aToowM93kqa29C6OzynlAAzyaj1NfA",
        username="Aatti_13",
        password="Aattreya@1309",
        user_agent="<console:Dard:1.0>")

    subreddit = await reddit.subreddit(sub_red)
    all_subs = []
    top = subreddit.top(limit=350)  # searches among top 350 posts

    async for submission in top:
        all_subs.append(submission)

    random_sub = choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title=name, colour=discord.Colour.random(), timestamp=ctx.message.created_at, url=url)

    em.set_image(url=url)
    em.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    em.set_footer(text="Here's your meme...")
    await ctx.send(embed=em)


"______________________________________________________________________________________________________________________"
"""Thumbnails represent what had been 
rolled by the dice......"""


# roll the dice mini-game
@client.command(name="roll", help=" --> Roll the dice")
async def roll(ctx):
    comp = random.randint(1, 6)
    if comp == 1:
        embed = discord.Embed(name="Rolling Dice",
                              description=f"rolled a {comp}:game_die:",
                              color=discord.Colour.random(),
                              timestamp=ctx.message.created_at)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/2/2c/Alea_1.png")
        await ctx.send(embed=embed)
    if comp == 2:
        embed = discord.Embed(name="Rolling Dice",
                              description=f"rolled a {comp}:game_die:",
                              color=discord.Colour.random(),
                              timestamp=ctx.message.created_at)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/b/b8/Alea_2.png")
        await ctx.send(embed=embed)
    if comp == 3:
        embed = discord.Embed(name="Rolling Dice",
                              description=f"rolled a {comp}:game_die:",
                              color=discord.Colour.random(),
                              timestamp=ctx.message.created_at)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/2/2f/Alea_3.png")
        await ctx.send(embed=embed)
    if comp == 4:
        embed = discord.Embed(name="Rolling Dice",
                              description=f"rolled a {comp}:game_die:",
                              color=discord.Colour.random(),
                              timestamp=ctx.message.created_at)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/8/8d/Alea_4.png")
        await ctx.send(embed=embed)
    if comp == 5:
        embed = discord.Embed(name="Rolling Dice",
                              description=f"rolled a {comp}:game_die:",
                              color=discord.Colour.random(),
                              timestamp=ctx.message.created_at)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/5/55/Alea_5.png")
        await ctx.send(embed=embed)
    if comp == 6:
        embed = discord.Embed(name="Rolling Dice",
                              description=f"rolled a {comp}:game_die:",
                              color=discord.Colour.random(),
                              timestamp=ctx.message.created_at)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/f/f4/Alea_6.png")
        await ctx.send(embed=embed)


"----------------------------------------------------------------------------------------------------------------------"


@client.command(name="toss", help=" --> Toss the coin")
async def toss(ctx):
    outcome = ["Heads", "Tails"]
    ran = choice(outcome)
    if ran == "Heads":
        embed = discord.Embed(title="**TOSS**", description="HEADS IT IS",
                              colour=discord.Colour.random(),
                              timestamp=ctx.message.created_at)
        embed.set_thumbnail(url="https://media.istockphoto.com/vectors/"
                                "silhouette-of-a-head-vector-id515660465?k="
                                "6&m=515660465&s=612x612&w=0&h=iNHBd4s9amVrjg7eCpQDSzPAZbzYxFujpmMNPd71wOc=")
        await ctx.send(embed=embed)

    if ran == "Tails":
        embed = discord.Embed(title="**TOSS**", description="TAILS IT IS",
                              colour=discord.Colour.random(),
                              timestamp=ctx.message.created_at)
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/"
                                "images?q=tbn:ANd9GcTfG9bmP4x-AYcryCsFfROgD_9U2Iz7D6hn9Q&usqp=CAU")
        await ctx.send(embed=embed)


"----------------------------------------------------------------------------------------------------------------------"


@client.command()
async def balance(ctx):
    await open_account(ctx.author)
    us = ctx.author
    u = await get_bank_data()

    wallet_amt = u[str(us.id)]["wallet"]
    bank_amt = u[str(us.id)]["bank"]

    em = discord.Embed(title=f"{ctx.author.display_name}'s balance",
                       colour=discord.Colour.random(),
                       timestamp=ctx.message.created_at)
    em.add_field(name="Wallet balance", value=wallet_amt)
    em.add_field(name="Bank balance", value=bank_amt)
    em.set_thumbnail(url=ctx.author.avatar_url)
    await ctx.send(embed=em)


"----------------------------------------------------------------------------------------------------------------------"


@client.command()
async def beg(ctx):
    await open_account(ctx.author)

    u = await get_bank_data()

    us = ctx.author

    earnings = random.randrange(501)
    rand = ["JJ", "Harry", "Ethan", "Josh", "Tobi", "Simon", "Vikk"]

    await ctx.send(f"{choice(rand)} gave you {earnings} coins")

    u[str(us.id)]["wallet"] += earnings

    with open("mainbank.json", "w") as f:
        json.dump(u, f)


"----------------------------------------------------------------------------------------------------------------------"


@client.command()
async def withdraw(ctx, amount=None):
    await open_account(ctx.author)
    if amount is None:
        await ctx.send("Please Enter an amount")
        return

    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount > bal[1]:
        await ctx.send("Insufficient Funds")
        return
    if amount < 0:
        await ctx.send("Amount must be positive")
        return

    await update_bank(ctx.author, amount)
    await update_bank(ctx.author, -1 * amount, "bank")

    await ctx.send(f"You withdrew {amount}")


"----------------------------------------------------------------------------------------------------------------------"


@client.command()
async def deposit(ctx, amount=None):
    await open_account(ctx.author)
    if amount is None:
        await ctx.send("Please Enter an amount")
        return

    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount > bal[0]:
        await ctx.send("Insufficient Funds")
        return
    if amount < 0:
        await ctx.send("Amount must be positive")
        return

    await update_bank(ctx.author, -1 * amount)
    await update_bank(ctx.author, amount, "bank")

    await ctx.send(f"You deposited {amount}")


"----------------------------------------------------------------------------------------------------------------------"


@client.command()
async def sendmoney(ctx, member: discord.Member, amount=None):
    await open_account(ctx.author)
    await open_account(member)

    if amount is None:
        await ctx.send("Please Enter an amount")
        return

    bal = await update_bank(ctx.author)
    if amount == "all":
        amount = bal[0]
    amount = int(amount)
    if amount > bal[1]:
        await ctx.send("Insufficient Funds")
        return
    if amount < 0:
        await ctx.send("Amount must be positive")
        return

    await update_bank(ctx.author, -1 * amount, "bank")
    await update_bank(member, amount, "bank")

    await ctx.send(f"You deposited {amount}")


"----------------------------------------------------------------------------------------------------------------------"


@client.command()
async def rob(ctx):
    await ctx.send(" :rage: Sike There's no robbery here :rage:")


"----------------------------------------------------------------------------------------------------------------------"


@client.command()
async def jua(ctx, amount=None):
    await open_account(ctx.author)
    if amount is None:
        await ctx.send("Please Enter an amount")
        return

    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount > bal[0]:
        await ctx.send("Insufficient Funds")
        return
    if amount < 0:
        await ctx.send("Amount must be positive")
        return

    a = random.randint(1, 6)
    b = random.randint(1, 6)

    if a > b:
        await update_bank(ctx.author, 2 * amount)
        embed = discord.Embed(title="SHAKUNI JUA", description="You Win!!!", colour=discord.Colour.random())

        embed.add_field(name="**YOU BET**", value=str(a))
        embed.add_field(name="**SIDE_BOT BET**", value=str(b))
        embed.set_thumbnail(url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    if a == b:
        await update_bank(ctx.author, 0)
        embed = discord.Embed(title="SHAKUNI JUA", description="Draw!!!", colour=discord.Colour.random())

        embed.add_field(name="**YOU BET**", value=str(a))
        embed.add_field(name="**SIDE_BOT BET**", value=str(b))
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/"
                                "images?q=tbn:ANd9GcRAGr0w5G_Z_UgIR6Q0207lSwmQrHo7seRt2g&usqp=CAU")

        await ctx.send(embed=embed)

    if a < b:
        await update_bank(ctx.author, -1 * amount)
        embed = discord.Embed(title="SHAKUNI JUA", description="You Lose!!!", colour=discord.Colour.random())

        embed.add_field(name="**YOU BET**", value=str(a))
        embed.add_field(name="**SIDE_BOT BET**", value=str(b))
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/"
                                "images?q=tbn:ANd9GcSo-w0ysf-1ojTqzb4mY0UajgiUqDTG5mwFiA&usqp=CAU")

        await ctx.send(embed=embed)


"----------------------------------------------------------------------------------------------------------------------"


@client.command()
async def slots(ctx, amount=None):
    await open_account(ctx.author)
    if amount is None:
        await ctx.send("Please Enter an amount")
        return

    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount > bal[0]:
        await ctx.send("Insufficient Funds")
        return
    if amount < 0:
        await ctx.send("Amount must be positive")
        return
    final = []
    for i in range(3):
        a = random.choice(["X", "O", "Q"])

        final.append(a)

    if final[0] == final[1] == final[2]:
        await update_bank(ctx.author, 2 * amount)

        em = discord.Embed(title="**SLOT MACHINE**", description=f"{str(final)} \n\n MEGA WIN!!!",
                           colour=discord.Colour.random())
        await ctx.send(embed=em)

    if final[0] == final[1] or final[0] == final[2] or final[1] == final[2]:
        await update_bank(ctx.author, amount)

        em = discord.Embed(title="**SLOT MACHINE**", description=f"{str(final)} \n\n WIN!!!",
                           colour=discord.Colour.random())
        await ctx.send(embed=em)
    else:
        await update_bank(ctx.author, -1 * amount)

        em = discord.Embed(title="**SLOT MACHINE**", description=f"{str(final)} \n\n YOU LOSE!!!",
                           colour=discord.Colour.random())

        await ctx.send(embed=em)


"----------------------------------------------------------------------------------------------------------------------"


async def open_account(us):
    u = await get_bank_data()

    if str(us.id) in u:
        return False
    else:
        u[str(us.id)] = {}
        u[str(us.id)]["wallet"] = 0
        u[str(us.id)]["bank"] = 0

    with open("mainbank.json", "w") as f:
        json.dump(u, f)
    return True


"----------------------------------------------------------------------------------------------------------------------"


async def get_bank_data():
    with open("mainbank.json", "r") as f:
        u = json.load(f)

    return u


"----------------------------------------------------------------------------------------------------------------------"


async def update_bank(us, change=0, mode="wallet"):
    u = await get_bank_data()

    u[str(us.id)][mode] += change

    with open("mainbank.json", "w") as f:
        json.dump(u, f)

    bal = [u[str(us.id)]["wallet"], u[str(us.id)]["bank"]]
    return bal


"----------------------------------------------------------------------------------------------------------------------"


@client.command()
async def bmi(ctx, height: float, weight: float):
    height /= 100
    w = height ** 2
    body_mass = weight / w
    if 25 > body_mass >= 19:
        em = discord.Embed(title="BODY MASS INDEX", description=f"Your B.M.I is: {body_mass}\n\n"
                                                                f">**STATUS**: Normal B.M.I",
                           colour=discord.Colour.random(),
                           timestamp=ctx.message.created_at)
        em.set_author(name=ctx.author.display_name)
        await ctx.send(embed=em)
    elif body_mass > 30:
        em = discord.Embed(title="BODY MASS INDEX", description=f"Your B.M.I is: {body_mass}\n\n"
                                                                f">**STATUS**: Obese",
                           colour=discord.Colour.random(),
                           timestamp=ctx.message.created_at)
        em.set_author(name=ctx.author.display_name)
        await ctx.send(embed=em)
    elif 30 >= body_mass >= 25:
        em = discord.Embed(title="BODY MASS INDEX", description=f"Your B.M.I is: {body_mass}\n\n"
                                                                f">**STATUS**: Overweight",
                           colour=discord.Colour.random(),
                           timestamp=ctx.message.created_at)
        em.set_author(name=ctx.author.display_name)
        await ctx.send(embed=em)
    else:
        em = discord.Embed(title="BODY MASS INDEX", description=f"Your B.M.I is: {body_mass}\n\n"
                                                                f">**STATUS**: Underweight",
                           colour=discord.Colour.random(),
                           timestamp=ctx.message.created_at)
        em.set_author(name=ctx.author)
        await ctx.send(embed=em)


"----------------------------------------------------------------------------------------------------------------------"

client.run(api_token)
"**********************************************************************************************************************"

# This program can be copied or added for their respective discord bots...

# Took 2 days to make

# Pls check requirements from respective file

# YouTube has multiple solutios and tutorials in case you don't understand any part

# There are no intentional errors 

# May not be the most efficient code
