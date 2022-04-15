# web2dataset



Web2dataset is a modulable library built to easily create image dataset from google image and other.
You can find the docs [here](https://samsja.github.io/web2dataset/)


* Easily create dataset from the web to train your own models for you own task
* Clean them 
* Modulable library that will allow sharing cleaners and downloaders

## Install

```shell
pip install web2dataset
```

or to get the latest update

```shell
pip install git+https://github.com/samsja/web2dataset.git@master
```

## How to use

let's perform a simple research on google image to search for 5 bike images

Example, how to scrap google image for image of red bike in 2 lines

from command line:

```bash
web2dataset scrap 16 'a red bike' /tmp/my_search 
```

or from python:


```python
from web2dataset.downloader import GoogleImageDownloader

downloader = GoogleImageDownloader("/tmp/my_search").download("a red bike", 16)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"></pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">
</pre>



let's load the downloaded image

```python
!tree "/tmp/my_search"
```

    [01;34m/tmp/my_search[0m
    ├── [00mdataset.bin[0m
    └── [01;34mimages[0m
        ├── [01;35m5752cec8-bcd2-11ec-97dc-645d865124e9.jpg[0m
        ├── [01;35m5755a1de-bcd2-11ec-97dc-645d865124e9.jpg[0m
        ├── [01;35m5756c3d4-bcd2-11ec-97dc-645d865124e9.jpg[0m
        ├── [01;35m5757e5f2-bcd2-11ec-97dc-645d865124e9.jpg[0m
        ├── [01;35m575900c2-bcd2-11ec-97dc-645d865124e9.jpg[0m
        ├── [01;35m575a13cc-bcd2-11ec-97dc-645d865124e9.jpg[0m
        ├── [01;35m575b29c4-bcd2-11ec-97dc-645d865124e9.jpg[0m
        ├── [01;35m575c46ec-bcd2-11ec-97dc-645d865124e9.jpg[0m
        ├── [01;35m575d6838-bcd2-11ec-97dc-645d865124e9.jpg[0m
        ├── [01;35m575e946a-bcd2-11ec-97dc-645d865124e9.jpg[0m
        ├── [01;35m575faf30-bcd2-11ec-97dc-645d865124e9.jpg[0m
        ├── [01;35m5760c4d8-bcd2-11ec-97dc-645d865124e9.jpg[0m
        ├── [01;35m5761dbac-bcd2-11ec-97dc-645d865124e9.jpg[0m
        ├── [01;35m5762eb28-bcd2-11ec-97dc-645d865124e9.jpg[0m
        ├── [01;35m5763f360-bcd2-11ec-97dc-645d865124e9.jpg[0m
        └── [01;35m57650890-bcd2-11ec-97dc-645d865124e9.jpg[0m
    
    1 directory, 17 files


```python
from docarray import DocumentArray

with open("/tmp/my_search/dataset.bin", "rb") as f:
    docs = DocumentArray.from_bytes(f.read())
```

```python
def load_img(d):
    d.uri = f"/tmp/my_search/{d.uri}"
    d.load_uri_to_image_tensor()
    return d


docs = docs.apply(load_img)
docs.plot_image_sprites()
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">
</pre>




    
![png](docs/images/output_13_2.png)
    


And you can parelellize in one additional line

```python
from web2dataset.downloader import GoogleImageDownloader
from web2dataset.paralel import ParalelDownload

paralel_downloader = ParalelDownload(
    "/tmp/my_search", GoogleImageDownloader, num_workers=2
)
paralel_downloader.download(["a red bike","a blue bike"], 8)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"></pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">
</pre>



or from command line:

```bash
web2dataset parallel 8 'a red bike' 'a blue bike' /tmp/my_search 2
```

```python
from docarray import DocumentArray

with open("/tmp/my_search/dataset.bin", "rb") as f:
    docs = DocumentArray.from_bytes(f.read())

docs = docs.apply(load_img)
docs.plot_image_sprites()
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">
</pre>




    
![png](docs/images/output_17_2.png)
    


## How to contribute

this project is built with [nbdev](https://github.com/fastai/nbdev)

first clone the repo

```bash 
git clone https://github.com/samsja/web2dataset
```

then install poetry
```bash
pip install poetry
```

then install the dev dependencies with poetry in a virtualenv

```bash 
poetry install
```

then activate the virtual env
```bash
poetry shell
```

 first install the git hooks
 ```bash
 nbdev_install_git_hooks
 ```

then launch jupyter and code :)
```bash
jupyter lab
```


test your code with
```bash
nbdev_test_nbs
```

finaly built the py files with nbdev and the docs 
```bash
nbdev_build_lib
```

```bash
nbdev_build_docs
```

you are goot to go and submit your PR :)
