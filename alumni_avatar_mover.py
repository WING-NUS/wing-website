import os
import re
from glob import glob

pattern = r"alumni"
authors = [os.path.basename(path) for path in glob("content/authors/*")]

print("Avatar moved for the following alumni:")
for aut in authors:
    with open("content/authors/"+aut+"/_index.md", "r") as f:
        content = f.read()
        if re.search(pattern, content, re.IGNORECASE):
            try:
                ext = glob("content/authors/"+aut+"/avatar.*")[0].split(".")[-1]
                os.rename("content/authors/"+aut+"/avatar."+ext, "content/alumni_avatars/"+aut+"."+ext)
                print(aut)
            except:
                pass