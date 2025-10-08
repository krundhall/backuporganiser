

class DataCollection:
    def __init__(self, name, description, creation_date, last_modified_date, still_updated):
        self.name = name
        self.description = description
        self.creation_date = creation_date
        self.last_modified_date = last_modified_date
        self.still_updated = still_updated
        self.backups = []
    
    def add_backup(self, backup_name, backup_date, backup_location):
        new_backup = BackupEntry(backup_name, backup_date, backup_location)
        self.backups.append(new_backup)
        self.last_modified_date = backup_date

    def brief_str(self):
        # Returns a brief summary of name and latest backup date
        latest = self.backups[-1].date if self.backups else "N/A"
        return [self.name, latest]

### Creates the backup
class BackupEntry:
    def __init__(self, name, date, location):
        self.name = name
        self.date = date
        self.location = location

### Stores my collections
class CollectionManager:
    def __init__(self):
        self.collections = []

    def add_collection(self, name, description, creation_date, last_modified_date, still_updated):
        new_collection = DataCollection(name, description, creation_date, last_modified_date, still_updated)
        self.collections.append(new_collection)

    def overview(self):
        summaries = []

        for col in self.collections:
            summary = col.brief_str()
            summaries.append(summary)
        return summaries
    def detailed_overview(self):
        pass

photo_entry = DataCollection(
    name="Photos",
    description="Family photos and events",
    creation_date="08/10-2025",
    last_modified_date="08/10-2025",
    still_updated=True
)
photo_entry.add_backup("Backup1", "08/10-25", "D:")

manager = CollectionManager()
manager.add_collection("Bilder", "Familjebilder", "Idag", "Idag", True)

print(manager.collections[0].name)