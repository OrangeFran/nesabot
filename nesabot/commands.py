from .creds import MY_CHAT_ID
from .const import HELP_MSG
from .scraper import fetch

# Check if it's actually me that issued the command
def wrong_user(update) -> bool:
    chat_id = update.effective_chat.id
    return chat_id != MY_CHAT_ID

# /help
# Display a help menu
def cmd_help(update, context):
    if wrong_user(update): return
    update.message.reply_text(text = HELP_MSG)

# /grades
# Reqeust the currently stored grades
def cmd_grades(update, context):
    if wrong_user(update): return
    update.message.reply_text(text = fetch(True))

# /fetch
# Explicitely look for new grades
def cmd_fetch(update, context):
    if wrong_user(update): return
    update.message.reply_text(text = fetch(False))
