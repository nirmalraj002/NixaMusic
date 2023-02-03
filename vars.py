import os

class vars(object):
    API_ID = int(os.environ.get("APP_ID", "15523618"))
    API_HASH = os.environ.get("API_HASH", "8979514968543c31a37a3ed8a0726d83")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5985275666:AAH6rGSsF63dt2SzKf1gWig9Lu1HcXJRx3w")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJ4Bux66T7uXdYWZa7iHoRgSyWZNRDQS0H-Um8w0WWdmyg5LvRw91yNf8IYvSjOIiaH9sEekgFyyedj42UtFHRawIuyRVR0vPV5qdFRxOeoATrnUDxIlta45E6L7MGIMK2lg9WnMkMBowrrwZJB55u06Wtk8C2qn4ZftTPJtcdSiR_DwZ_DhIvov6dxq6oBuyFeja_UVmGcb8_9i3jDwEPPqXm-AXqWxsc6EktG9T2cqc-qSDSS5ghvRsWCKFRWRTV338f6AmFxg6KMp4WMXhtgkHbrRraCsM4FA5-Gvzu1lM3GnllHSFV5w26yQRgmSotQAACOzrd5bxiLnr0NMnE6WcPk=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "NixaMusicXBot")
    SUPPORT = os.environ.get("SUPPORT", "SankiWorldMF")
    CHANNEL = os.environ.get("CHANNEL", "NixaWorld")
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/3f47f71b0412f10fffe4c.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/3f47f71b0412f10fffe4c.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5470233619")) # required
