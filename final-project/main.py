import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Mesajları okuyabilmesi için gerekli
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} çalışıyor!')

@bot.command()
async def iklim(ctx, *, soru):
    soru = soru.lower().strip()

    cevaplar = {
        "iklim değişikliği nedir": "İklim değişikliği, dünyanın sıcaklık ortalamalarının uzun vadede değişmesidir. Genellikle insanların çevreye verdiği zararlar bu durumu hızlandırır.",
        "bu sorun ne kadar ciddi? bizi ilgilendiriyor mu": "Evet, çok ciddi! Sel, kuraklık, yangınlar gibi afetler artıyor. Bu olaylar tarımı, sağlığı ve yaşam kalitemizi etkiliyor.",
        "iklim değişikliğini ne tetikler": "Fabrikalar, arabalar ve ormanların yok edilmesi gibi insan faaliyetleri; karbon salımını artırır ve bu da iklim değişikliğini tetikler.",
        "iklim değişikliğini nasıl engelleyebiliriz": "Enerji tasarrufu yapmak, geri dönüşüm, ağaç dikmek ve doğayı korumak bu sorunun yavaşlamasına yardım eder.",
        "karbondioksit nedir ve neden tehlikelidir": "Karbondioksit, havaya salınan bir gazdır. Fazlası atmosferde ısıyı hapseder ve dünyanın ısınmasına sebep olur.",
        "iklim değişikliğinin etkilerini günlük hayatımızda nasıl hissederiz": "Yazlar daha sıcak, kışlar daha az karlı olur. Kuraklık, su sıkıntısı ve artan fırtınalar da günlük hayatı etkiler."
    }

    if soru in cevaplar:
        await ctx.send(cevaplar[soru])
    else:
        await ctx.send("Bu soruya henüz hazır değilim ")
