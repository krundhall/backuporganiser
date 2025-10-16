from backup_entry import BackupEntry

class DataCollection:
    """
    Collection of data with backups
    """
    def __init__(self, name, description, creation_date, last_modified_date, still_updated):
        self.name = name
        self.description = description
        self.creation_date = creation_date
        self.last_modified_date = last_modified_date
        self.still_updated = still_updated
        self.backups = []

    def add_backup(self, backup_name, backup_date, backup_location):
        """
        Add a new backup entry to the collection
        
        """
        new_backup = BackupEntry(backup_name, backup_date, backup_location)
        self.backups.append(new_backup)
        self.last_modified_date = backup_date

    def brief_str(self):
        """
        Gives a short summary of the collection (name, latest backup date or N/A)
        """
        latest = self.backups[-1].date if self.backups else "N/A"
        return [self.name, latest]
