import discord
from discord.ext import commands
from logic import quiz_questions
# Görev 7 - defaultdict komutunu içe aktarın
from config import token

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

user_responses = {}
# Görev 8 - Kullanıcı puanlarını kaydetmek için puan sözlüğünü oluşturun

@bot.command()
async def send_question(ctx_or_interaction, user_id):
    question = quiz_questions[user_responses[user_id]]
    buttons = question.gen_buttons()
    view = discord.ui.View()
    for button in buttons:
        view.add_item(button)

    if isinstance(ctx_or_interaction, commands.Context):
        await ctx_or_interaction.send(question.text, view=view)
    else:
        await ctx_or_interaction.followup.send(question.text, view=view)


@bot.event
async def on_ready():
    print(f'Yeni giriş: {bot.user}!')


@bot.event
async def on_interaction(interaction):
    user_id = interaction.user.id
    if user_id not in user_responses:
        await interaction.response.send_message("Lütfen !start komutunu yazarak testi başlatın")
        return

    custom_id = interaction.data["custom_id"]
    if custom_id.startswith("correct"):
        await interaction.response.send_message("Doğru cevap!")
        # Görev 9 - Doğru cevap için kullanıcıya puan ekleyin
    elif custom_id.startswith("wrong"):
        await interaction.response.send_message("Yanlış cevap!")

    # Görev 5 - soru sayacını ayarlayın
    # Görev 6 - kullanıcı tüm soruları yanıtladıysa sınav sonucuyla ilgili bir mesaj gönderin. Aksi takdirde, bir sonraki soruyu gönderin

@bot.command()
async def start(ctx):
    user_id = ctx.author.id
    if user_id not in user_responses:
        user_responses[user_id] = 0
        await send_question(ctx, user_id)

bot.run(token)

