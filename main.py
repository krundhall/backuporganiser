from collection_manager import CollectionManager
from restinterface import app

# Create manager
manager = CollectionManager()

# Temporary collections
manager.add_collection("Photos", "Family photos", "08/10-2025", "08/10-2025", True)
manager.add_collection("Documents", "Work files", "07/10-2025", "07/10-2025", True)

# Temporary backups
manager.collections[0].add_backup("Backup2", "09/10-25", "E:")
manager.collections[1].add_backup("BackupA", "07/10-25", "USB stick")

app.config["manager"] = manager

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
