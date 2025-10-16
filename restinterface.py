from flask import Flask, request, jsonify, send_from_directory
from collection_manager import CollectionManager

app = Flask(__name__, static_folder='static')
manager = CollectionManager()

# Testing Collections
manager.add_collection("Photos", "Family photos", "08/10-2025", "08/10-2025", True)
manager.add_collection("Documents", "Work files", "07/10-2025", "07/10-2025", True)

"""
POST /api/Collection add a new collection DONE
GET /api/Overview get a JSON object with an overview of all data collections DONE
GET /api/List get a JSON object with a detailed list of all data collections DONE
GET /api/Info?name=data-collection-name get a JSON object with details for one specific data collection DONE
POST /api/Backup add a backup DONE
GET /api/Search?name=text DONE
POST /api/Edit DONE
POST /api/Unbackup DONE
DELETE /api/Delete?name=data-collection-name DONE
"""

@app.route("/")
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/api/Collection", methods=["POST"])
def add_collection():
    # request, flask object that represent the http request body
    data = request.get_json()
    manager.add_collection(
        data["name"],
        data["description"],
        data["creation_date"],
        data["modification_date"],
        data["still_updated"]
    )
    return jsonify({"message": f"Collection '{data['name']} added!"})

@app.route("/api/Overview", methods=["GET"])
def overview():
    summaries = manager.overview()

    return jsonify(summaries)

@app.route("/api/List", methods=["GET"])
def detailed_list():
    full_list = manager.detailed_overview()

    return jsonify(full_list)

@app.route("/api/Info", methods=["GET"])
def info():
    # get name from query parameter
    # method of getting the name
    # https://stackoverflow.com/a/11774434
    collection_name = request.args.get("name")
    collection = manager.get(collection_name)

    # build the json
    collection_info = {
        "name": collection.name,
        "description": collection.description,
        "creation_date": collection.creation_date,
        "last_modified_date": collection.last_modified_date,
        "still_updated": collection.still_updated,
        "backups": []
    }

    # add the backups
    # for-loop cause i dont understand list comprehensions : ^)
    for b in collection.backups:
        backup_info = {
            "name": b.name,
            "date": b.date,
            "location": b.location
        }
        collection_info["backups"].append(backup_info)
    
    return jsonify(collection_info)

@app.route("/api/Backup", methods=["POST"])
def add_backup():
    data = request.get_json()

    collection_name = data["name"]
    backup_name = data["backupname"]
    backup_date = data["date"]
    backup_location = data["location"]

    collection = manager.get(collection_name)
    collection.add_backup(backup_name, backup_date, backup_location)

    return jsonify({"message": "Backup Added"})

@app.route("/api/Edit", methods=["POST"])
def edit_collection():
    """
    Update "last modified date" and "still updated" in a collection
    """
    data = request.get_json()
    collection = manager.get(data["name"])

    collection.last_modified_date = data["modification_date"]
    collection.still_updated = data["still_updated"]

    return jsonify({"message": "Collection updated"})

@app.route("/api/Unbackup", methods=["POST"])
def unbackup():
    """
    Removes a backup entry
    Finds the backup using name provided by client
    """
    data = request.get_json()
    collection = manager.get(data["name"])

    # removing backup using enumarate/pop to practice more explicit programming
    for i, b in enumerate(collection.backups):
        if b.name == data["backupname"] and b.date == data["date"]:
            collection.backups.pop(i)
            break

    return jsonify({"message": "Backup removed"})

@app.route("/api/Search", methods=["GET"])
def search_collections():
    """
    Using name provided by client we search through all collections,
    take each match and append it (and last backupdate) to a list, then return the list.

    Collection name doesnt have to be complete, e.g searching for 'docu' will find the collection 'Documents'.
    """
    search_text = request.args.get("name")

    matches = []
    for c in manager.collections:
        if search_text.lower() in c.name.lower():
            matches.append(c.brief_str())
    
    return jsonify(matches)

@app.route("/api/Delete", methods=["DELETE"])
def delete_collection():
    collection_name = request.args.get("name")

    for i, c in enumerate(manager.collections):
        if c.name == collection_name:
            del manager.collections[i]
            break
    
    return jsonify({"message": f"Collection '{collection_name}' deleted"})
    