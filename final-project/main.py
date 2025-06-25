import discord
from discord.ext import commands
from config import TOKEN 

intents = discord.Intents.default()
intents.message_content = True  # Mesaj içeriğini okuyabilmesi için

bot = commands.Bot(command_prefix='!', intents=intents)

# BOT AÇILDIĞINDA MESAJ GÖSTER
@bot.event
async def on_ready():
    print(f'{bot.user} çalışıyor!')
user_input = input("Kullanıcı: ")

if user_input.lower() == "merhaba":
    print("Bot: Merhaba, iklim değişikliği hakkında bir sorun mu var?")

@bot.command()
async def iklim(ctx, *, soru):
    soru = soru.lower().strip()

    cevaplar = {
        "iklim değişikliği nedir": "İklim değişikliği, dünyanın sıcaklık ortalamalarının uzun vadede değişmesidir. Genellikle insanların çevreye verdiği zararlar bu durumu hızlandırır.",
        "bu sorun ne kadar ciddi? bizi ilgilendiriyor mu": "Evet, çok ciddi! Sel, kuraklık, yangınlar gibi afetler artıyor. Bu olaylar tarımı, sağlığı ve yaşam kalitemizi etkiliyor.",
        "iklim değişikliğini ne tetikler": "Fabrikalar, arabalar ve ormanların yok edilmesi gibi insan faaliyetleri; karbon salımını artırır ve bu da iklim değişikliğini tetikler.",
        "iklim değişikliğini nasıl engelleyebiliriz": "Enerji tasarrufu yapmak, geri dönüşüm, ağaç dikmek ve doğayı korumak bu sorunun yavaşlamasına yardım eder.",
        "karbondioksit nedir ve neden tehlikelidir": "Karbondioksit, havaya salınan bir gazdır. Fazlası atmosferde ısıyı hapseder ve dünyanın ısınmasına sebep olur.",
        "iklim değişikliğinin etkilerini günlük hayatımızda nasıl hissederiz": "Yazlar daha sıcak, kışlar daha az karlı olur. Kuraklık, su sıkıntısı ve artan fırtınalar da günlük hayatı etkiler.",

        # Yeni eklenenler:
        "sera etkisi nedir": "Sera etkisi, güneşten gelen ısının atmosferde hapsolmasıdır. Bu etki doğal olarak vardır ama fazla sera gazı bu etkiyi zararlı hâle getirir.",
        "en fazla sera gazı hangi kaynaktan çıkar": "Enerji üretimi (özellikle kömür ve petrol kullanımı) sera gazlarının en büyük kaynağıdır.",
        "bireysel olarak ne yapabilirim": "Toplu taşıma kullanmak, ışıkları boşa yakmamak, plastikten kaçınmak ve çevreye duyarlı olmak büyük fark yaratır!",
        "iklim değişikliği çocukları etkiler mi": "Evet, gelecek nesiller daha sıcak bir dünya, azalan kaynaklar ve daha fazla felaketle karşı karşıya kalabilir.",
        "okullarda bu konuda ne yapılabilir": "Geri dönüşüm kutuları konulabilir, enerji tasarrufu sağlanabilir, iklim kulüpleri kurulabilir ve farkındalık etkinlikleri yapılabilir.",
        "küresel ısınma ile iklim değişikliği aynı mı": "Hayır, küresel ısınma iklim değişikliğinin bir sonucudur. İklim değişikliği daha geniş kapsamlıdır.",
        "iklim krizinin sonucu ne olur": "Deniz seviyeleri yükselir, kuraklık artar, hayvan türleri yok olur, göçler başlar ve yaşam kalitesi düşer.",
        "iklim değişikliği neden hızlandı": "Sanayileşme, ormansızlaşma ve fosil yakıt tüketiminin artması iklim değişikliğini hızlandırmıştır."
    }

    if soru in cevaplar:
        await ctx.send(cevaplar[soru])
    else:
        await ctx.send("Üzgünüm, bu soruya henüz bir cevabım yok. Yeni şeyler öğrenmek için seni dinliyorum! 🌍✨")

    if soru in cevaplar:
        await ctx.send(cevaplar[soru])
    else:
        await ctx.send("Bu soruya henüz hazır değilim 😓")

# TEST VERİLERİ
def iklim_degisikligi_testi():
    return [
        {
            "soru": "İklim değişikliğinin temel nedeni nedir?",
            "secenekler": [
                "A) Güneş patlamaları",
                "B) Volkanik patlamalar",
                "C) Fosil yakıtların aşırı kullanımı",
                "D) Ay tutulmaları"
            ],
            "dogru": "C"
        },
        {
            "soru": "Aşağıdakilerden hangisi sera gazı değildir?",
            "secenekler": [
                "A) Karbondioksit",
                "B) Metan",
                "C) Azot",
                "D) Su buharı"
            ],
            "dogru": "C"
        },
        {
            "soru": "İklim değişikliği aşağıdakilerden hangisine yol açmaz?",
            "secenekler": [
                "A) Deniz seviyesinin yükselmesi",
                "B) Kuraklık ve su kıtlığı",
                "C) Ormanların çoğalması",
                "D) Aşırı hava olayları"
            ],
            "dogru": "C"
        },
        {
            "soru": "İklim değişikliğiyle mücadelede hangisi etkili bir bireysel davranış değildir?",
            "secenekler": [
                "A) Geri dönüşüm yapmak",
                "B) Toplu taşıma aracı kullanmak",
                "C) Enerji tasarruflu ürünler kullanmak",
                "D) Daha fazla fosil yakıt kullanmak"
            ],
            "dogru": "D"
        },
        {
            "soru": "Küresel ısınma hangi olayın bir sonucudur?",
            "secenekler": [
                "A) Sera etkisi",
                "B) Göktaşı çarpması",
                "C) Depremler",
                "D) Güneş tutulması"
            ],
            "dogru": "A"
        },
        {
            "soru": "En çok sera gazı yayan sektör hangisidir?",
            "secenekler": [
                "A) Tarım",
                "B) Ulaştırma",
                "C) Sanayi",
                "D) Enerji üretimi"
            ],
            "dogru": "D"
        },
        {
            "soru": "Aşağıdakilerden hangisi yenilenebilir enerji kaynağıdır?",
            "secenekler": [
                "A) Doğal gaz",
                "B) Güneş",
                "C) Kömür",
                "D) Petrol"
            ],
            "dogru": "B"
        },
        {
            "soru": "İklim değişikliğine karşı alınabilecek uluslararası önlem hangisidir?",
            "secenekler": [
                "A) Paris Anlaşması",
                "B) Tokyo Olimpiyatları",
                "C) G8 Zirvesi",
                "D) Avrupa Futbol Şampiyonası"
            ],
            "dogru": "A"
        },
        {
            "soru": "Ağaç dikmenin iklim değişikliğine etkisi nedir?",
            "secenekler": [
                "A) Sera gazlarını artırır",
                "B) İklimi daha sıcak yapar",
                "C) Karbondioksiti azaltır",
                "D) Hiçbir etkisi yoktur"
            ],
            "dogru": "C"
        },
        {
            "soru": "Kutuplardaki buzulların erimesi neye yol açar?",
            "secenekler": [
                "A) Yağmur miktarının artmasına",
                "B) Deniz seviyesinin yükselmesine",
                "C) Çölleşmeye",
                "D) Orman yangınlarına"
            ],
            "dogru": "B"
        },
        {
            "soru": "Sera gazlarının atmosferde birikmesi neye neden olur?",
            "secenekler": [
                "A) Atmosferin soğumasına",
                "B) Sıcaklığın düşmesine",
                "C) Küresel ısınmaya",
                "D) Yağmur ormanlarının artmasına"
            ],
            "dogru": "C"
        },
        {
            "soru": "Bireysel olarak karbon ayak izini azaltmak için ne yapılabilir?",
            "secenekler": [
                "A) Araba ile daha çok seyahat etmek",
                "B) Elektrikli aletleri açık bırakmak",
                "C) Geri dönüşüm yapmak",
                "D) Fosil yakıt kullanmak"
            ],
            "dogru": "C"
        },
        {
            "soru": "Aşağıdakilerden hangisi iklim değişikliğinin sağlık üzerindeki etkilerinden biridir?",
            "secenekler": [
                "A) Gıda bolluğu",
                "B) Yeni hastalıkların yayılması",
                "C) Spor etkinliklerinin artması",
                "D) Uyku düzeninin düzelmesi"
            ],
            "dogru": "B"
        },
        {
            "soru": "Orman yangınlarının artmasında iklim değişikliğinin rolü nedir?",
            "secenekler": [
                "A) Havanın soğuması",
                "B) Toprağın nemlenmesi",
                "C) Kuraklık ve sıcaklık artışı",
                "D) Rüzgarın durması"
            ],
            "dogru": "C"
        },
        {
            "soru": "Karbon salımını azaltmak neden önemlidir?",
            "secenekler": [
                "A) Teknolojik gelişmeleri durdurmak için",
                "B) Küresel ısınmayı yavaşlatmak için",
                "C) Sanayi üretimini azaltmak için",
                "D) Binaların yıkılmasını engellemek için"
            ],
            "dogru": "B"
        }
    ]


# TEST KOMUTU
@bot.command()
async def iklimtest(ctx):
    sorular = iklim_degisikligi_testi()
    for i, soru in enumerate(sorular, 1):
        mesaj = f"**{i}. {soru['soru']}**\n"
        for secenek in soru["secenekler"]:
            mesaj += f"{secenek}\n"
        await ctx.send(mesaj)


bot.run(TOKEN)
