# Pixabay_Python
This is a Python library for interacting with *[Pixabay](https://pixabay.com/)* api. 

# Requirements
Requirements can be installed by this line:

```
$ python -m pip install pixabay_python
```

# Usage
You need to first sign up to Pixabay and get an api key from *[here](https://pixabay.com/service/about/api/)*. 
Then you can use your api key to access Pixabay like the 
following examples

### example 1
```
import pixabay_python as pxb

client = pxb.PixabayClient(apiKey="your_api_key") 
searchResult = client.searchImage(q="tree")
hitsList = list(searchResult.hits)
pxb.download(url=hitsList[0].largeImageURL, outputDir="./anOutDir")
```

### example 2
```
import pixabay_python as pxb

client = pxb.PixabayClient(apiKey="your_api_key") 
searchResult = client.searchImage(q="tree")
hitsList = list(searchResult.hits)
someSelectedURLs = [hit.largeImageURL for hit in hitsList[:5]]
pxb.downloadList(urlList=someSelectedURLs, outputDir="./anOutDir")
```

# License
Pixabay_Python is licensed under Apache 2.0 License.

# Credits
+ Developed by Farzad Shayanfar