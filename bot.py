
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from PIL import Image, ImageDraw, ImageFont

TOKEN = "ضع التوكن هنا"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أرسل الرقم حتى أضيفه على الصورة!")

async def handle_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    number = update.message.text.strip()

    img = Image.open("template.jpg")
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("arial.ttf", 80)

    x, y = 120, 90
    draw.text((x, y), number, font=font, fill=(0, 0, 0))

    output_path = "output.jpg"
    img.save(output_path)

    await update.message.reply_photo(photo=open(output_path, "rb"))

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_number))

print("البوت يعمل...")
app.run_polling()
