import discord
import colorama
from discord.ext import commands
from discord.ui import Button , View , Select
from discord import app_commands
from colorama import Fore , init
init(convert=True)



token = "Your token"


intents = discord.Intents.all()
bot = commands.Bot(command_prefix= "CL!",
                   intents= intents ,
                status = discord.Status.online ,
                activity = discord.Activity(type = discord.ActivityType.competing , name= "Numbers"))


@bot.event
async def on_ready():
   try:
      synced = await bot.tree.sync()
      print(Fore.CYAN+"-->" ,Fore.GREEN+"Synced" , Fore.YELLOW+f"{len(synced)}" , Fore.GREEN+"Slash Command")

   except Exception as e :
      print(e)
   print(Fore.CYAN+"-->" , Fore.BLUE+"Calculator bot is ready !")
   



#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
@bot.tree.command(
   name= "computing" , description= "Calculation of 4 main mathematical operations ➖➕➗"
)
@app_commands.describe(num_1 = "Enter first number")
@app_commands.choices(operation = [
   discord.app_commands.Choice(name= "+" , value= "+"),
   discord.app_commands.Choice(name= "×" , value= "×"),
   discord.app_commands.Choice(name= "-" , value= "-"),
   discord.app_commands.Choice(name= "÷" , value= "÷")
])
@app_commands.describe(num_2 = "Enter second number")
async def computing(interaction:discord.Interaction , num_1:int , operation:discord.app_commands.Choice[str] , num_2:int):

   if operation.value == "+":
      await interaction.response.send_message(f"""```{num_1} + {num_2} = {num_1+num_2}```""")
   elif operation.value == "×":
      await interaction.response.send_message(f"""```{num_1} × {num_2} = {num_1*num_2}```""")
   elif operation.value == "-":
      await interaction.response.send_message(f"""```{num_1} - {num_2} = {num_1-num_2}```""")
   elif operation.value == "÷":
      await interaction.response.send_message(f"""```{num_1} ÷ {num_2} = {num_1/num_2}```""")

#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
@bot.tree.command(
   name= "circle" , description= "Calculate the circumference and area of a circle ⭕"
)
@app_commands.describe(radius = "Enter radius of your circle")
@app_commands.choices(operation = [
   discord.app_commands.Choice(name="Area" , value="area"),
   discord.app_commands.Choice(name="Perimeter" , value= "perimeter")
])
async def circle(interaction:discord.Interaction , radius:int , operation:discord.app_commands.Choice[str]):

   pi = 3.14
   diameter = radius + radius
   
   if operation.value == "area":
      await interaction.response.send_message(f"""```
π = 3.14
The formula : (Radius × Radius) × π
------------------------------------------
Solution : {radius} × {radius} × {pi} = {radius * radius * pi}```""")
   elif operation.value == "perimeter":
      await interaction.response.send_message(f"""```
π = 3.14
Diameter = Radius + Radius
The formula : Diameter * π
------------------------------------------
Solution : {diameter} × {pi} = {diameter * pi}```""")
#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
@bot.tree.command(
   name= "square" , description= "Calculate the perimeter and area of the square 🔳"
)
@app_commands.describe(side = "Enter side of your square")
@app_commands.choices(operation = [
   discord.app_commands.Choice(name="Area" , value= "area"),
   discord.app_commands.Choice(name="Perimeter" , value= "perimeter")
])
async def square(interaction:discord.Interaction,side:int , operation:discord.app_commands.Choice[str]):
   if operation.value == "area":
      await interaction.response.send_message(f"""```
The formula : side × side
------------------------------
Solution : {side} × {side} = {side*side}```""")
   
   elif operation.value == "perimeter" :
      await interaction.response.send_message(f"""```
The formula : side × 4
-------------------------
Solution : {side} × 4 = {side*4}```""")
#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
@bot.tree.command(
   name= "rectangle" ,description="Calculate the perimeter and area of the rectangle 🔲"
)
@app_commands.describe(length = "Enter the length of your rectangle")
@app_commands.describe(width = "Enter widthof your rectangle")
@app_commands.choices(operation = [
   discord.app_commands.Choice(name="Area" , value= "area"),
   discord.app_commands.Choice(name="Perimeter" , value= "perimeter")
])
async def rectangle(interaction:discord.Interaction , length:int , width:int,operation:discord.app_commands.Choice[str]):
   if operation.value == "area" :
      await interaction.response.send_message(f"""```
The formula : length × width
--------------------------------
Solution : {length} × {width} = {length*width}```""")
      
   elif operation.value == "perimeter" :
      first = length + width
      second = first * 2
      await interaction.response.send_message(f"""```
The formula : (length + width) × 2
----------------------------------------
Solution : {length} + {width} × 2 = {second}```""")
#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
@bot.tree.command(
   name= "triangle" , description= "Calculate the perimeter and area of the triangle 🔺"
)
@app_commands.describe(base = "Enter the base of your triangle")
@app_commands.describe(height = "Enter the height of your triangle")
@app_commands.choices(operation = [
   discord.app_commands.Choice(name="Area" , value= "area"),
   discord.app_commands.Choice(name="Perimeter" , value= "perimeter")
])
async def triangle(interactio:discord.Interaction, base:int , height:int , operation:discord.app_commands.Choice[str]):
   if operation.value == "area":
      first = base * height
      second = first / 2
      await interactio.response.send_message(f"""```
The formula : (base × height) ÷ 2 
----------------------------------------
Solution : {base} × {height} ÷ 2 = {second}```""")
      
   elif operation.value == "perimeter" :
      await interactio.response.send_message(f"""```
The formula : base × 3
--------------------------------------
Solution : {base} × 3 = {base *3}```""")
#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________


bot.run(token)
