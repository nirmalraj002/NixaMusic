import os

class vars(object):
    API_ID = int(os.environ.get("APP_ID", "15523618"))
    API_HASH = os.environ.get("API_HASH", "8979514968543c31a37a3ed8a0726d83")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5840649503:AAEgRn1ogjgHcJtEKjaAeWdnz7oH_hLKOU0")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOMUBu36GtbH4dQrPrfkq3UotGP_TzVFDBDZ0BjKSoNTGa3II1LwRYX3FEqit2UTZ4NyHMdt4riIx6hv_pX30xtDDFc6O2Do2KaU3twtlM36FjiDwFe9s_UmG3_haPG_k-_ltt_vZVekfwqFX0xvb1cJlY_vqMxlBXlmfA2f5efwPv4Ze18SwTknHMPFXz93hMhSmpQyPzgso6RUM06Zr_Su6v1IQboP4trafUH_LzKpB1hlYvjxpHpTNX_3r2yhg3jXVBPG7GJNT-y_qTT1BIV8bmL-3ecBekjbfD9kmIZ9aWYKAk7r4HWMkuy3fcCkJuKfXgaqdxF91Oyjkm0tnSF9_D3E=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "NisthaMusicBot")
    SUPPORT = os.environ.get("SUPPORT", "TeleBotsSupport")
    CHANNEL = os.environ.get("CHANNEL", "Fake_Peoples")
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/535a7db55e251a316b807.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/5b5e408cfd6a6ee9e4bd7.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5881219743")) # required
