from telegram import Update
from telegram.ext import ContextTypes
from utils.bin_lookup import buscar_bin

async def vbv(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        entrada = ' '.join(context.args).replace(" ", "")
        cc, mm, yy, cvv = entrada.split("|")
        bin_info = buscar_bin(cc[:6])

        if bin_info:
            mensaje = f""""
🔐 *VBV Checker – Braintree*  
💳 `{bin_info['esquema']}`  
🏦 `{bin_info['banco']}`  
🌍 `{bin_info['pais']}`  
🧾 `{bin_info['tipo']}`

🎉 E’ta tarjeta ta’ más nítida que un frío frío en el Malecón.
""""
        else:
            mensaje = "❌ Ese BIN ta’ más desaparecido que el internet de Altice."

        await update.message.reply_text(mensaje, parse_mode="Markdown")
    except:
        await update.message.reply_text("❌ Usa: /vbv 4000000000000000|12|26|123", parse_mode="Markdown")
