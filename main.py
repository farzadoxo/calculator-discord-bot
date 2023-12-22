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
      print(Fore.CYAN+"-->" ,Fore.GREEN+"Synced" , Fore.YELLOW+f"{len(synced)}" , Fore.GREEN+"Slash Commands")

   except Exception as e :
      print(e)
   print(Fore.CYAN+"-->" , Fore.BLUE+"Calculator bot is ready !")
   



#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________

# This command is responsible for performing 4 main actions 
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
   from embeds import computing_embed


      # conditions
   if operation.value == "+":
      computing_embed.add_field(name="**Resault :**",value=f"{num_1} + {num_2} = {num_1 + num_2}")
      await interaction.response.send_message(embed=computing_embed)
      computing_embed.remove_field(index=0)
   elif operation.value == "×":
      computing_embed.add_field(name="**Resault :**",value=f"{num_1} × {num_2} = {num_1 * num_2}")
      await interaction.response.send_message(embed=computing_embed)
      computing_embed.remove_field(index=0)
   elif operation.value == "-":
      computing_embed.add_field(name="**Resault :**",value=f"{num_1} - {num_2} = {num_1 - num_2}")
      await interaction.response.send_message(embed=computing_embed)
      computing_embed.remove_field(index=0)
   elif operation.value == "÷":
      computing_embed.add_field(name="**Resault :**",value=f"{num_1} ÷ {num_2} = {num_1 / num_2}")
      await interaction.response.send_message(embed=computing_embed)
      computing_embed.remove_field(index=0)

#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
       # compute area and premeter of circle
@bot.tree.command(
   name= "circle" , description= "Calculate the circumference and area of a circle ⭕"
)
@app_commands.describe(radius = "Enter radius of your circle")
@app_commands.choices(operation = [
   discord.app_commands.Choice(name="Area" , value="area"),
   discord.app_commands.Choice(name="Perimeter" , value= "perimeter")
])
async def circle(interaction:discord.Interaction , radius:int , operation:discord.app_commands.Choice[str]):
   from embeds import circle_embed

   pi = 3.14
   diameter = radius + radius
   
   if operation.value == "area":
      circle_embed.add_field(name="**Area :**",value=f"{radius} × {radius} × {pi} = {radius*radius * pi}")
      circle_embed.set_footer(text="The formula : (Radius × Radius) × π")
      await interaction.response.send_message(embed=circle_embed)
      circle_embed.remove_field(index=0)
      circle_embed.remove_footer()

   elif operation.value == "perimeter":
      circle_embed.add_field(name="**Perimeter :**",value=f"{diameter} × {pi} = {diameter*pi}")
      circle_embed.set_footer(text="The formula : Diameter * π")
      await interaction.response.send_message(embed=circle_embed)
      circle_embed.remove_field(index=0)
      circle_embed.remove_footer()

#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
         # compute area and premeter of square
@bot.tree.command(
   name= "square" , description= "Calculate the perimeter and area of the square 🔳"
)
@app_commands.describe(side = "Enter side of your square")
@app_commands.choices(operation = [
   discord.app_commands.Choice(name="Area" , value= "area"),
   discord.app_commands.Choice(name="Perimeter" , value= "perimeter")
])
async def square(interaction:discord.Interaction,side:int , operation:discord.app_commands.Choice[str]):
   from embeds import square_embed

   if operation.value == "area":
      square_embed.add_field(name="**Area :**",value=f"{side} × {side} = {side*side}")
      square_embed.set_footer(text="The formula : side × side")
      await interaction.response.send_message(embed=square_embed)
      square_embed.remove_field(index=0)
      square_embed.remove_footer()
   
   elif operation.value == "perimeter" :
      square_embed.add_field(name="**Perimeter :**",value=f"{side} × 4 = {side*4}")
      square_embed.set_footer(text="The formula : side × 4")
      await interaction.response.send_message(embed=square_embed)
      square_embed.remove_field(index=0)
      square_embed.remove_footer()
#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
         # compute area and premeter of rectangle
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
   from embeds import rectangle_embed


   if operation.value == "area" :
      rectangle_embed.add_field(name="**Area :**",value=f"{length} × {width} = {length*width}")
      rectangle_embed.set_footer(text="The formula : length × width")
      await interaction.response.send_message(embed=rectangle_embed)
      rectangle_embed.remove_field(index=0)
      rectangle_embed.remove_footer()
      
   elif operation.value == "perimeter" :
      resault = length + width * 2
      rectangle_embed.add_field(name="**Perimeter :**",value=f"({length} + {width}) = {resault}")
      rectangle_embed.set_footer(text="The formula : (length + width) × 2")
      await interaction.response.send_message(embed=rectangle_embed)
      rectangle_embed.remove_field(index=0)
      rectangle_embed.remove_footer()
#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
         # compute area and premeter of triangle
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
   from embeds import triangle_embed

   if operation.value == "area":
      resault = base * height / 2
      triangle_embed.add_field(name="**Area :**",value=f"{base} × {height} ÷ 2 = {resault}")
      triangle_embed.set_footer(text="The formula : (base × height) ÷ 2 ")
      await interactio.response.send_message(embed=triangle_embed)
      triangle_embed.remove_field(index=0)
      triangle_embed.remove_footer()
      
   elif operation.value == "perimeter" :
      triangle_embed.add_field(name="**Perimeter :**",value=f"{base} × 3 = {base * 3}")
      triangle_embed.set_footer(text="The formula : base × 3")
      await interactio.response.send_message(embed=triangle_embed)
      triangle_embed.remove_field(index=0)
      triangle_embed.remove_footer()
#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
      # send a multiplication table (picture)
@bot.tree.command(name='multiplication_table',description="Multiplication table 🧮")
async def multiplication_table(interaction:discord.Interaction):
   from embeds import multiplication_table_img
   await interaction.response.send_message(embed=multiplication_table_img)
#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________



bot.run(token)
