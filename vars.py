  import os

class vars(object):
    API_ID = int(os.environ.get("APP_ID", "23842900"))
    API_HASH = os.environ.get("API_HASH", "d21e95895cf2a5b83b0167fdd3b6e541")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5916376879:AAGOiLBT-WVOcEMoThxsP83N4t80hs8qNKw")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJ4BuwZjqRC7_yOHBcgEAynslI1t8tSINzBnzEw2_ldnYdQx1hIzX1LnqSfIOZXmQt_m42v75FUQVPqaxbqMz3hhB2xhyz7kjvOXwD7oz8Cxr-g-d-zwpV8a59m4AhKE2tVzelE3Dro5DDiDhgAVb0vXSMflsSN88Y6zSqFsDCHuPxDaO6_4AdSZWsxjadwUTq3erhte2mjcqAHPLd1-GYFvz7M3-2oJ_5BdgDCwGwFPWftJmq6wd54RvzkxtN4s82DRiKkWEjSOqNpScW3-NUT2L35RL9QhpvFC9z8beqrlXjsAM65GgtRaV0MeHNZy1ibpPxVbDDgsm_B7F2d0lOb-cqs=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "NixaMusicXBot")
    SUPPORT = os.environ.get("SUPPORT", "SankiWorldMF")
    CHANNEL = os.environ.get("CHANNEL", "NixaWorld")
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/3f47f71b0412f10fffe4c.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/3f47f71b0412f10fffe4c.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5470233619")) # required
