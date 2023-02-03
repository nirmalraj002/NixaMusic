import glob
from pathlib import Path
from NixaMusic.utils import load_plugins
import logging
from NixaMusic import NixaMusic

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "NixaMusic/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
 
bsdk = "» sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴀʀᴛᴇᴅ ʙᴏᴛ 🎉🎉 !"
chumt = "» ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ !"   

print(bsdk)
print(chumt)

if __name__ == "__main__":
    NixaMusic.run_until_disconnected()
