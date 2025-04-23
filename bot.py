from gates import email
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

# Token de BotFather (¡Recuerda mantenerlo privado en producción!)
BOT_TOKEN = '7729657771:AAFayfD_M5hmTINJWql0-w5m7hnZ51qnXJg'

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = (
        "👋🏽 *Bienvenido al CheckerBotRD 🇩🇴*\n\n"
        "Aquí verificamos tarjetas con estilo dominicano.\n"
        "Usa el comando:\n"
        "`/vbv 4000000000000000|12|26|123`\n"
        "Y te digo si esa tarjeta sirve pa’ pasar en el colmado. 🏪💳"
    )
    await update.message.reply_text(mensaje, parse_mode="Markdown")

# Comando /vbv
async def vbv(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        entrada = ' '.join(context.args).replace(" ", "")
        cc, mm, yy, cvv = entrada.split("|")

        if not cc.isdigit() or len(cc) < 6:
            raise ValueError("Número de tarjeta inválido")

        bin_code = cc[:6]
        url = f"https://lookup.binlist.net/{bin_code}"
        res = requests.get(url)

        if res.status_code == 200:
            data = res.json()
            banco = data.get("bank", {}).get("name", "Banco desconocido")
            pais = data.get("country", {}).get("name", "Desconocido")
            esquema = data.get("scheme", "???").upper()
            tipo = data.get("type", "???").capitalize()

            respuesta = f"""
✅ *Tarjeta válida detectada*
💳 Esquema: `{esquema}`
🏦 Banco: `{banco}`
🌍 País: `{pais}`
🧾 Tipo: `{tipo}`

🎉 _E’ta tarjeta ta’ más nítida que una cena en Boca Chica, manito._
"""
        else:
            respuesta = "❌ Ese BIN no aparece ni en Google, loco. Revisa eso."

        await update.message.reply_text(respuesta, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text("❌ *Formato inválido.*\n\nUsa: `/vbv 4000000000000000|12|26|123`", parse_mode="Markdown")

# Crear aplicación del bot
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("vbv", vbv))
app.add_handler(CommandHandler("email", email.email))

# Iniciar bot
print("🚀 Bot dominicano corriendo... pásame una tarjeta pa' chequearla.")
app.run_polling()
