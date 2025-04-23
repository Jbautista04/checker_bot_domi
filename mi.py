from telegram import Update
from telegram.ext import ContextTypes
from utils.bin_lookup import buscar_bin

async def mi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        entrada = ' '.join(context.args).replace(" ", "")
        cc, mm, yy, cvv = entrada.split("|")
        bin_info = buscar_bin(cc[:6])

        if bin_info:
            mensaje = f""""
🔐 *Mizuhame – Braintree*  
💳 `{bin_info['esquema']}`  
🏦 `{bin_info['banco']}`  
🌍 `{bin_info['pais']}`  
🧾 `{bin_info['tipo']}`

😎 Esa tarjeta pasa más fácil que motoconcho sin casco.
""""
        else:
            mensaje = "❌ No tengo info de ese BIN. Está como la luz: intermitente."

        await update.message.reply_text(mensaje, parse_mode="Markdown")
    except:
        await update.message.reply_text("❌ Usa: /mi 4000000000000000|12|26|123", parse_mode="Markdown")
