# This is a sample file used to update a repo based on a changeset saved in MongoDB

import os

network_repo_path = r"YOUR_REPO_PATH"


nuke_folder =  os.path.dirname(os.path.abspath(__file__))
local_repo_path = os.path.join(nuke_folder, "repo")
nuke.pluginAddPath(os.path.join(nuke_folder,"site-packages"))
import hglib, pymongo

if not os.path.exists(local_repo_path):
    hglib.clone( network_repo_path, local_repo_path)

repo = hglib.open(local_repo_path)
repo.pull()

client = pymongo.MongoClient(host = "YOUR_IP") # ex:192.168.1.100
db = client["fxphd"]
collection = db["repo"]
doc = collection.find_one({"name":"nuke"})
repo.update(doc["hash"],clean=True)

nuke.pluginAddPath("repo")
