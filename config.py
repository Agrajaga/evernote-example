import os
import dotenv


class Settings():
    EVERNOTE_CONSUMER_KEY = ""
    EVERNOTE_CONSUMER_SECRET = ""
    EVERNOTE_PERSONAL_TOKEN = ""

    JOURNAL_TEMPLATE_NOTE_GUID = ""
    JOURNAL_NOTEBOOK_GUID = ""

    INBOX_NOTEBOOK_GUID = ""
    
    def __init__(self):
        dotenv.load_dotenv()

        self.EVERNOTE_CONSUMER_KEY = os.getenv("EVERNOTE_CONSUMER_KEY")
        self.EVERNOTE_CONSUMER_SECRET = os.getenv("EVERNOTE_CONSUMER_SECRET")
        self.EVERNOTE_PERSONAL_TOKEN = os.getenv("EVERNOTE_PERSONAL_TOKEN")
        self.JOURNAL_TEMPLATE_NOTE_GUID = os.getenv("JOURNAL_TEMPLATE_NOTE_GUID")
        self.JOURNAL_NOTEBOOK_GUID = os.getenv("JOURNAL_NOTEBOOK_GUID")
        self.INBOX_NOTEBOOK_GUID = os.getenv("INBOX_NOTEBOOK_GUID")
