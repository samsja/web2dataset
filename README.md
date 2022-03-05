# web2dataset



Web2dataset is a modulable library built to easily create image dataset from google image and other.
You can find the docs [here](https://samsja.github.io/web2dataset/)

Web2datast it's:

* Easily create dataset from the web to train your own models for you own task
* Clean them 
* Modulable library that will allow sharing of cleaner and downloader

## Install

```shell
pip install git+https://github.com/samsja/web2dataset.git@master
```

## How to use

let's perform a simple research on google image to search for 5 bike images

Example, how to scrap google image for image of red bike in 2 lines

```python
from web2dataset.downloader import GoogleImageDownloader
downloader = GoogleImageDownloader("/tmp/my_search").download("a red bike",16)
```

let's load the downloaded image

```python
from docarray import DocumentArray

with open("/tmp/my_search/dataset.bin", "rb") as f:
    docs = DocumentArray.from_bytes(f.read())
```

```python
docs = docs.apply(lambda d : d.load_uri_to_image_tensor())
docs.plot_image_sprites()
```


    
![png](docs/images/output_10_0.png)
    


## How to contribute

this project is built with [nbdev](https://github.com/fastai/nbdev)

first clone the repo
> ```git clone https://github.com/samsja/web2dataset```

then install poetry
> ```pip install poetry```

then install the dev dependencies with poetry in a virtualenv

> ```poetry install```

then activate the virtual env
> ```poetry shell```

 first install the git hooks
 > ```nbdev_install_git_hooks```

then launch jupyter and code :)
> ```jupyter lab```


test your code with
> nbdev_test_nbs

finaly built the py files with nbdev and the docs
>```nbdev_build_lib```

> ```nbdev_build_docs```

you are goot to go and submit your PR :)
