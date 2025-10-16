from data_collection import DataCollection
class CollectionManager:
    """
    Manages multiple collections of data
    """
    def __init__(self):
        """
        Starting with an empty list
        """
        self.collections = []

    def add_collection(self, name, description, creation_date, last_modified_date, still_updated):
        """
        Add a new collection
        """
        new_collection = DataCollection(name, description, creation_date, last_modified_date, still_updated)
        self.collections.append(new_collection)

    def overview(self):
        """
        Short summary of all collections (name, latest backup date)
        """
        summaries = []
        for col in self.collections:
            summaries.append(col.brief_str())
        return summaries

    def detailed_overview(self):
        """
        Return full info for all collections.
        """
        details = []

        for col in self.collections:
            # Build a dictionary with collection info
            col_info = {
                "name": col.name,
                "description": col.description,
                "creation_date": col.creation_date,
                "last_modified_date": col.last_modified_date,
                "still_updated": col.still_updated,
                "backups": []  # will fill in backups next
            }

            # Add all backups for this collection
            for backup in col.backups:
                backup_info = {
                    "name": backup.name,
                    "date": backup.date,
                    "location": backup.location
                }
                col_info["backups"].append(backup_info)

            # Add this collection info to the list
            details.append(col_info)

        return details

    def get(self, collection_name):
        """
        Return the datacollection object, or none if nothing is found
        """
        for col in self.collections:
            if col.name == collection_name:
                return col
        return None