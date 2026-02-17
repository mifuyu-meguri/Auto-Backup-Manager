import os
from pathlib import Path
from natsort import natsort_keygen, ns
from typing import Iterator

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"

def xPrint(text:str="", properties:str="", end:str="\n") -> None:
    print(properties + text + "\033[0m", end=end)

def xInput(text:str="", inputProperties:str="", outputProperties:str="") -> str:
    i = input(inputProperties + text + "\033[0m" + outputProperties)
    print("\033[0m", end="")
    return i

def writeFofiTreeToTextFile(
        pathToScan:str, outputTextFileNnoPath:str, 
        startText:str="", finishText:str="", 
        startTextProperties:str="", finishTextProperties:str=""
    ) -> bool:
    """
    DEPENDENCIES:
        import os
        from pathlib import Path
        from natsort import natsort_keygen, ns
        from typing import Iterator

        #iropy
        from terminalFormatting_iro import *
            BOLD
            RED
            xPrint()
    """
    #
    SORTING_FUNCTION = natsort_keygen(alg=ns.IGNORECASE)
    #
    def listPath(pathToScan:Path) -> tuple[list, int]:
        try:
            fofis = list(os.scandir(pathToScan))
        except PermissionError:
            return [], 1
        except FileNotFoundError:
            return [], 2
        except Exception:
            return [], 3
        fofis.sort(
            key=lambda fofi: (
                not fofi.is_dir(follow_symlinks=False),
                SORTING_FUNCTION(fofi.name),
            )
        )
        return fofis, 0
    #
    def walkPath(pathToScan:Path, prefix:str="") -> Iterator[str]:
        fofis, ifError = listPath(pathToScan)
        if ifError:
            if ifError == 1:
                yield prefix + "└── <Permission Error>"
            elif ifError == 2:
                yield prefix + "└── <File Not Found Error>"
            else:
                yield prefix + "└── <Some Error Occurred>"
            return
        if not fofis:
            yield prefix + "└── <Empty Folder>"
            return
        for index, fofi in enumerate(fofis):
            isLast = (1 + index == len(fofis))
            thisLineNnoId = "└── " if isLast else "├── "
            appendToPrefix = "    " if isLast else "│   "
            yield prefix + thisLineNnoId + fofi.name
            if fofi.is_dir(follow_symlinks=False):
                yield from walkPath(Path(fofi.path), prefix + appendToPrefix)
    #
    xPrint(startText, startTextProperties, end="")
    pathToScan = Path(pathToScan).expanduser()
    outputTextFileNnoPath = Path(outputTextFileNnoPath).expanduser()
    if not pathToScan.exists():
        xPrint(f"{pathToScan} doesn't exist.", BOLD + RED)
        return False
    if not outputTextFileNnoPath.parent.exists():
        xPrint(f"{outputTextFileNnoPath.parent} doesn't exist.", BOLD + RED)
        return False
    linesToWrite = []
    if pathToScan.is_file():
        linesToWrite.append(pathToScan.name)
    else:
        linesToWrite.append(pathToScan.name or str(pathToScan))
        linesToWrite.extend(walkPath(pathToScan, ""))
    outputTextFileNnoPath.write_text("\n".join(linesToWrite), encoding="utf-8")
    xPrint(finishText, finishTextProperties, end="")
    return True
