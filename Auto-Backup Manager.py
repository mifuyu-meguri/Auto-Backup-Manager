import os
from pathlib import Path
os.chdir(Path(__file__).resolve().parent)
from iro import *
from SETTINGS import *

if __name__ == "__main__":
    print(f"{BOLD}{GREEN}Attach the external SSD for backup.{RESET}")
    input(f"Press Enter when ready.\n")
    #
    while True:
        if os.path.isfile(SSD_CHECKPOINT_NNO_PATH):
             break
        print(f"{BOLD}{RED}SSD Checkpoint File not found. Retry.\n{RESET}")
    os.startfile(FFS_BATCH_FILE_NNO_PATH)
    #
    input("Finished successfully. Press enter to exit.")
