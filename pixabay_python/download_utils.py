from pathlib import Path
from typing import List, Union

import requests


def download(url: str,
             outputDir: Union[str, Path],
             connectTimeout: float = 10,
             readTimeout: float = 20,
             streamToFile: bool = False,
             chunkSize: int = 128,
             overwriteExisting: bool = False):
    outputDirPath = Path(outputDir)
    outputDirPath.mkdir(parents=True, exist_ok=True)
    assert url.startswith("https://")
    fileName = url.split(sep="/")[-1]
    outputFilePath = outputDirPath.joinpath(fileName)
    if not overwriteExisting:
        if outputFilePath.exists():
            print(f"this file, {fileName}, already exists and is not overwritten\n")

    print(f"--downloading\nFROM {url}\nTO {outputFilePath.resolve()}\n")
    try:
        resp = requests.get(url=url, verify=True, timeout=(connectTimeout, readTimeout))
        if streamToFile:
            with open(file=outputFilePath, mode="wb") as file:
                for chunk in resp.iter_content(chunk_size=chunkSize):
                    file.write(chunk)
        else:
            if resp.status_code == 200:
                with open(file=outputFilePath, mode="wb") as file:
                    file.write(resp.content)

    except requests.ConnectTimeout as error:
        raise error

    except requests.ReadTimeout as error:
        raise error


def downloadList(urlList: List[str],
                 outputDir: Union[str, Path],
                 connectTimeout: float = 10,
                 readTimeout: float = 20,
                 streamToFile: bool = False,
                 chunkSize: int = 128,
                 overwriteExisting: bool = False):
    outputDirPath = Path(outputDir)
    outputDirPath.mkdir(parents=True, exist_ok=True)
    urlCount = len(urlList)
    for index, url in enumerate(urlList):
        assert url.startswith("https://")
        fileName = url.split(sep="/")[-1]
        outputFilePath = outputDirPath.joinpath(fileName)
        if not overwriteExisting:
            if outputFilePath.exists():
                print(f"url {index + 1} / {urlCount} | this file already exists and is not overwritten\n")
                continue

        print(f"url {index + 1} / {urlCount} --downloading\nFROM {url}\nTO {outputFilePath.resolve()}\n")
        try:
            resp = requests.get(url=url, verify=True, timeout=(connectTimeout, readTimeout))
            if streamToFile:
                with open(file=outputFilePath, mode="wb") as file:
                    for chunk in resp.iter_content(chunk_size=chunkSize):
                        file.write(chunk)
            else:
                if resp.status_code == 200:
                    with open(file=outputFilePath, mode="wb") as file:
                        file.write(resp.content)

        except requests.ConnectTimeout as error:
            raise error

        except requests.ReadTimeout as error:
            raise error


if __name__ == '__main__':
    files = ["https://pngimg.com/uploads/apple/apple_PNG12489.png"]
    downloadList(files, outputDir="./apple", overwriteExisting=True, streamToFile=True)
