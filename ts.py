from telegram import Update
from telegram.ext import ContextTypes
from utils.bin_lookup import buscar_bin

async def ts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        entrada = ' '.join(context.args).replace(" ", "")
        cc, mm, yy, cvv = entrada.split("|")
        bin_info = buscar_bin(cc[:6])

        if bin_info:
            mensaje = f""""
🔐 *Tsukiyomi – Braintree AVS*  
💳 `{bin_info['esquema']}`  
🏦 `{bin_info['banco']}`  
🌍 `{bin_info['pais']}`  
🧾 `{bin_info['tipo']}`

💬 AVS dice que sí, y yo digo que pasa como si tuviera padrino.
""""
        else:
            mensaje = "❌ Ese BIN es más raro que una bola gratis."

        await update.message.reply_text(mensaje, parse_mode="Markdown")
    except:
        await update.message.reply_text("❌ Usa: /ts 4000000000000000|12|26|123", parse_mode="Markdown")
