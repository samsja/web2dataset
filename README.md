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
!tree "/tmp/my_search"
```

    [01;34m/tmp/my_search[0m
    ├── [00mdataset.bin[0m
    └── [01;34mimages[0m
        ├── [01;35m7bc9a106-9ca6-11ec-ad14-645d865124e9.jpg[0m
        ├── [01;35m7bcbb3ec-9ca6-11ec-ad14-645d865124e9.jpg[0m
        ├── [01;35m7bcce988-9ca6-11ec-ad14-645d865124e9.jpg[0m
        ├── [01;35m7bcdfaee-9ca6-11ec-ad14-645d865124e9.jpg[0m
        ├── [01;35m7bcf16f4-9ca6-11ec-ad14-645d865124e9.jpg[0m
        ├── [01;35m7bd029fe-9ca6-11ec-ad14-645d865124e9.jpg[0m
        ├── [01;35m7bd132c2-9ca6-11ec-ad14-645d865124e9.jpg[0m
        ├── [01;35m7bd23fd2-9ca6-11ec-ad14-645d865124e9.jpg[0m
        ├── [01;35m7bd3401c-9ca6-11ec-ad14-645d865124e9.jpg[0m
        ├── [01;35m7bd453a8-9ca6-11ec-ad14-645d865124e9.jpg[0m
        ├── [01;35m7bd55bcc-9ca6-11ec-ad14-645d865124e9.jpg[0m
        ├── [01;35m7bd67d9a-9ca6-11ec-ad14-645d865124e9.jpg[0m
        ├── [01;35m7bd7b3a4-9ca6-11ec-ad14-645d865124e9.jpg[0m
        ├── [01;35m7bd8dd2e-9ca6-11ec-ad14-645d865124e9.jpg[0m
        ├── [01;35m7bda1bb2-9ca6-11ec-ad14-645d865124e9.jpg[0m
        └── [01;35m7bdb4e88-9ca6-11ec-ad14-645d865124e9.jpg[0m
    
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


    
![png](docs/images/output_11_0.png)
    


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
