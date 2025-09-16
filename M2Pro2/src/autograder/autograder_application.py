from .autograder_settings import AutograderSettings
from .autograder_instance_data import AutograderInstanceData
from typing import Any
import json

class Autograder:
    def __init__(self):
        self.settings: AutograderSettings = AutograderSettings()
        self.instanceData: AutograderInstanceData = AutograderInstanceData()

    def SetConfigurationFromDict(self, a_data: dict[str, Any]):
        self.settings.UpdateFromDict(a_data)
    
    def LoadConfiguration(self, a_path: str) -> None:
        try:
            with open(a_path, "r") as configurationFile:
                self.SetConfigurationFromDict(json.load(configurationFile))
        except FileNotFoundError as e:
            print(f"The file {e.filename} does not exist.")
    
    def SaveConfiguration(self, a_path: str) -> None:
        try:
            with open(a_path, "w") as configurationFile:
                json.dump(self.settings.ToDict(), configurationFile)
        except PermissionError as e:
            ...
        except IsADirectoryError as e:
            ...