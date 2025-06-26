import discord
from discord.ext import commands
from config import TOKEN
import random

# Gerekli izinleri ayarlıyoruz
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} çalışıyor!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == "merhaba":
        await message.channel.send("Merhaba! İklim değişikliği hakkında soruların mı var?")
    elif message.content.lower() == "teşekkür ederim":
        await message.channel.send("Rica ederim, başka sorun olursa buradayım.")

    await bot.process_commands(message)

# Soru-cevap veritabanı (cevaplanabilir 45 soru)
cevaplar = {
    "iklim değişikliği nedir": "İklim değişikliği, dünyanın sıcaklık ortalamalarının uzun vadede değişmesidir. Genellikle insanların çevreye verdiği zararlar bu durumu hızlandırır.",
    "bu sorun ne kadar ciddi? bizi ilgilendiriyor mu": "Evet, çok ciddi! Sel, kuraklık, yangınlar gibi afetler artıyor. Bu olaylar tarımı, sağlığı ve yaşam kalitemizi etkiliyor.",
    "iklim değişikliğini ne tetikler": "Fabrikalar, arabalar ve ormanların yok edilmesi gibi insan faaliyetleri; karbon salımını artırır ve bu da iklim değişikliğini tetikler.",
    "iklim değişikliğini nasıl engelleyebiliriz": "Enerji tasarrufu yapmak, geri dönüşüm, ağaç dikmek ve doğayı korumak bu sorunun yavaşlamasına yardım eder.",
    "karbondioksit nedir ve neden tehlikelidir": "Karbondioksit, havaya salınan bir gazdır. Fazlası atmosferde ısıyı hapseder ve dünyanın ısınmasına sebep olur.",
    "iklim değişikliğinin etkilerini günlük hayatımızda nasıl hissederiz": "Yazlar daha sıcak, kışlar daha az karlı olur. Kuraklık, su sıkıntısı ve artan fırtınalar da günlük hayatı etkiler.",
    "sera etkisi nedir": "Sera etkisi, güneşten gelen ısının atmosferde hapsolmasıdır. Bu etki doğal olarak vardır ama fazla sera gazı bu etkiyi zararlı hâle getirir.",
    "en fazla sera gazı hangi kaynaktan çıkar": "Enerji üretimi (özellikle kömür ve petrol kullanımı) sera gazlarının en büyük kaynağıdır.",
    "bireysel olarak ne yapabilirim": "Toplu taşıma kullanmak, ışıkları boşa yakmamak, plastikten kaçınmak ve çevreye duyarlı olmak büyük fark yaratır!",
    "iklim değişikliği çocukları etkiler mi": "Evet, gelecek nesiller daha sıcak bir dünya, azalan kaynaklar ve daha fazla felaketle karşı karşıya kalabilir.",
    "okullarda bu konuda ne yapılabilir": "Geri dönüşüm kutuları konulabilir, enerji tasarrufu sağlanabilir, iklim kulüpleri kurulabilir ve farkındalık etkinlikleri yapılabilir.",
    "küresel ısınma ile iklim değişikliği aynı mı": "Hayır, küresel ısınma iklim değişikliğinin bir sonucudur. İklim değişikliği daha geniş kapsamlıdır.",
    "iklim krizinin sonucu ne olur": "Deniz seviyeleri yükselir, kuraklık artar, hayvan türleri yok olur, göçler başlar ve yaşam kalitesi düşer.",
    "iklim değişikliği neden hızlandı": "Sanayileşme, ormansızlaşma ve fosil yakıt tüketiminin artması iklim değişikliğini hızlandırmıştır.",
    "fosil yakıt nedir": "Fosil yakıtlar, milyonlarca yıl önce yaşamış organizmaların kalıntılarından oluşan enerji kaynaklarıdır (kömür, petrol, doğal gaz gibi).",
    "karbon ayak izi nedir": "Bir kişinin veya kurumun doğrudan ve dolaylı olarak atmosfere saldığı toplam karbon miktarına karbon ayak izi denir.",
    "yenilenebilir enerji kaynakları nelerdir": "Güneş, rüzgar, hidroelektrik, biyokütle ve jeotermal enerji yenilenebilir enerji kaynaklarıdır.",
    "küresel ısınma nedir": "Dünyanın ortalama sıcaklığının artmasıdır, genellikle sera gazlarının artışı nedeniyle oluşur.",
    "ormansızlaşmanın iklim değişikliğine etkisi nedir": "Ormanların yok edilmesi karbon tutma kapasitesini azaltır, böylece daha fazla karbon atmosfere salınır.",
    "sera gazları nelerdir": "Karbondioksit (CO2), metan (CH4), azot oksit (N2O) gibi gazlar sera gazlarıdır.",
    "iklim müzakereleri nedir": "Ülkelerin iklim değişikliğiyle mücadele için yaptıkları uluslararası görüşmelerdir.",
    "elektrikli araçlar neden önemli": "Fosil yakıt kullanan araçlara göre daha az sera gazı salarlar ve hava kirliliğini azaltırlar.",
    "biyoçeşitlilik neden önemlidir": "Canlı türlerinin çeşitliliği ekosistemlerin sağlığı ve istikrarı için gereklidir.",
    "iklim değişikliğinin ekonomik etkileri nelerdir": "Tarım, turizm, sağlık ve altyapı gibi sektörlerde büyük maliyetlere yol açar.",
    "iklim değişikliğiyle mücadelede uluslararası anlaşmalar hangileridir": "Kyoto Protokolü, Paris Anlaşması gibi anlaşmalar.",
    "iklim değişikliğinin sağlık üzerindeki etkileri nelerdir": "Sıcak hava dalgaları, hastalıkların yayılması ve kötü hava kalitesi sağlık sorunlarına yol açar.",
    "yenilenebilir enerjiye geçiş neden önemlidir": "Fosil yakıtların kullanımını azaltarak karbon emisyonlarını düşürür ve çevreyi korur.",
    "sera gazı emisyonlarını azaltmak için ne yapabiliriz": "Enerji verimliliği, yenilenebilir enerji kullanımı, ormanların korunması ve atık yönetimi.",
    "deniz seviyesinin yükselmesi neden tehlikelidir": "Kıyı bölgelerinde sel ve erozyona, insanların yer değiştirmesine neden olur.",
    "iklim değişikliği nasıl ölçülür": "Atmosfer ve okyanus sıcaklıkları, buzulların erimesi ve deniz seviyesi ölçümleriyle.",
    "iklim değişikliği ile ilgili farkındalık nasıl artırılır": "Eğitim, medya kampanyaları ve sosyal etkinliklerle.",
    "iklim değişikliğinin gençlere etkisi": "Gelecekleri tehdit altında, daha yaşanabilir bir dünya için mücadele ediyorlar.",
    "iklim değişikliği hangi sektörleri etkiler": "Tarım, balıkçılık, enerji, sağlık, turizm ve daha birçok sektörü.",
    "karbon ticareti nedir": "Karbon salınım haklarının alınıp satıldığı bir piyasa sistemi.",
    "iklim değişikliğine adaptasyon nedir": "Değişen iklim koşullarına uyum sağlama çabaları.",
    "iklim değişikliği nedeniyle hayvanlar ne yapar": "Yaşam alanlarını değiştirir veya yok olma riskiyle karşı karşıya kalır.",
    "yenilenebilir enerji projeleri örnekleri": "Güneş enerjisi çiftlikleri, rüzgar türbinleri.",
    "iklim değişikliğinin etkileri nerelerde daha belirgindir": "Kutuplar, deniz seviyesinin düşük olduğu bölgeler ve kurak alanlar.",
    "karbon salınımı nedir": "Atmosfere salınan karbondioksit miktarıdır.",
    "iklim değişikliği ile ilgili bireysel sorumluluklar nelerdir": "Enerji tasarrufu, geri dönüşüm, bilinçli tüketim.",
    "iklim değişikliği ne zaman başladı": "Sanayi Devrimiyle birlikte büyük ölçüde hızlandı.",
    "iklim değişikliğinin doğal nedenleri var mı": "Evet, volkanik faaliyetler ve güneş döngüleri gibi, ama insan etkisi daha baskın.",
    "iklim değişikliğine karşı teknolojik çözümler nelerdir": "Karbon yakalama, yenilenebilir enerji teknolojileri.",
    "iklim değişikliğinin gelecekteki etkileri": "Daha sık ve şiddetli hava olayları, ekosistemlerin zarar görmesi.",
    "iklim değişikliğine dikkat çekmek için neler yapılabilir": "Sanat, sosyal medya ve kampanyalar.",
    "iklim değişikliği ile ilgili en önemli uluslararası organizasyon": "Birleşmiş Milletler İklim Değişikliği Konferansı (COP)."
}

@bot.command()
async def iklim(ctx, *, soru: str):
    soru = soru.lower().strip()
    cevap = cevaplar.get(soru)
    if cevap:
        await ctx.send(cevap)
    else:
        await ctx.send("Üzgünüm, bu soruya henüz bir cevabım yok. Yeni şeyler öğrenmek için seni dinliyorum! 🌍✨")

@bot.command()
async def iklimpuanlıtest(ctx):
    def secenek_olustur(soru, cevap):
        yanlislar = [c for k, c in cevaplar.items() if k != soru]
        secenekler = random.sample(yanlislar, 3) + [cevap]
        random.shuffle(secenekler)
        harfler = ['A', 'B', 'C', 'D']
        dogru_harf = harfler[secenekler.index(cevap)]
        return [f"{harfler[i]}) {secenekler[i]}" for i in range(4)], dogru_harf

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    sorular = random.sample(list(cevaplar.items()), 10)
    puan = 0

    await ctx.send("🌱 **Puanlı İklim Testi** başlıyor! Her soruya A, B, C veya D şeklinde cevap ver.")

    for i, (soru, cevap) in enumerate(sorular, 1):
        secenekler, dogru = secenek_olustur(soru, cevap)
        mesaj = f"**{i}. {soru}?**\n" + "\n".join(secenekler)
        await ctx.send(mesaj)
        try:
            cevap_mesaj = await bot.wait_for("message", timeout=30.0, check=check)
            if cevap_mesaj.content.strip().upper() == dogru:
                await ctx.send("✅ Doğru!")
                puan += 1
            else:
                await ctx.send(f"❌ Yanlış. Doğru cevap: **{dogru}**")
        except:
            await ctx.send("⏱️ Süre doldu, sonraki soruya geçiyoruz!")

    await ctx.send(f"🎉 Test tamamlandı! Toplam puanın: **{puan} / 10** 🎓")

bot.run(TOKEN)
