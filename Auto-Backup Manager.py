import os
from pathlib import Path
os.chdir(Path(__file__).resolve().parent)
from iro import *
from SETTINGS import *

def fofiNnoBackup():
    os.startfile(FFS_BATCH_FILE_NNO_PATH)

def fofiNnoNameOnlyNnoBackup():
    for pathToScan, outputTextFileNnoPath in LIST_OF_PATHS_TO_BE_SAVED_AS_FOFI_TREES:
        writeFofiTreeToTextFile(pathToScan, outputTextFileNnoPath)

if __name__ == "__main__":
    print(f"{BOLD}{GREEN}Attach the external SSD for backup.{RESET}")
    while True:
        input(f"Press Enter when ready.\n")
        if os.path.isfile(SSD_CHECKPOINT_NNO_PATH):
            break
        print(f"{BOLD}{RED}SSD Checkpoint File not found. Retry.\n{RESET}")
    #
    fofiNnoBackup()
    fofiNnoNameOnlyNnoBackup()
    #
    input(f"{BOLD}{GREEN}Finished successfully. Press enter to exit.{RESET}")
