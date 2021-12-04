# web2dataset



Web2dataset is a modulable library built to easily create image dataset from google image and other.
You can find the docs [here](https://samsja.github.io/web2dataset/)

Web2datast it's:

* Easily create dataset from the web to train your own models for you own task
* Clean them with the SOTA etich techniques
* Modulable library that will allow sharing of cleaner and searcher
* working in pair with Hugging face datasets, fasti ai, pytorch dataset and others 

The core value of Web2dataset are:
 * Ethic
 * Community based
 * fast and scalable

## Install

```shell
pip install git+https://github.com/samsja/web2dataset.git@master
```

## How to use

let's perform a simple research on google image to search for 5 bike images

```python
import json

import jsons

from web2dataset.cleaner import DuplicateCleaner
from web2dataset.downloader import BasicDownloader
from web2dataset.searcher import GoogleImageSearcher

google_searcher = GoogleImageSearcher(
    "bike race", n_item=5, cleaners=[DuplicateCleaner()]
)
google_searcher.search()
google_searcher.clean()
google_searcher.save("/tmp/my_search")

donwloader = BasicDownloader("/tmp/my_search")
donwloader.download()
```

and here you are with two folder containing the images and the metadata

```python
!tree /tmp/my_search
```

    [01;34m/tmp/my_search[00m
    ├── [01;34mimages[00m
    │   ├── 41a07628-54f6-11ec-b278-645d865124e9
    │   ├── 41a0795c-54f6-11ec-b278-645d865124e9
    │   ├── 41a07b3c-54f6-11ec-b278-645d865124e9
    │   ├── 41a07cc2-54f6-11ec-b278-645d865124e9
    │   ├── 41a07e3e-54f6-11ec-b278-645d865124e9
    │   ├── 97cce43c-54f6-11ec-b2e3-645d865124e9
    │   ├── 97d25fa2-54f6-11ec-b2e3-645d865124e9
    │   ├── 97dc6d6c-54f6-11ec-b2e3-645d865124e9
    │   ├── 97df7d54-54f6-11ec-b2e3-645d865124e9
    │   └── 97e2be2e-54f6-11ec-b2e3-645d865124e9
    └── [01;34mmetadata[00m
        ├── 41a07628-54f6-11ec-b278-645d865124e9.json
        ├── 41a0795c-54f6-11ec-b278-645d865124e9.json
        ├── 41a07b3c-54f6-11ec-b278-645d865124e9.json
        ├── 41a07cc2-54f6-11ec-b278-645d865124e9.json
        ├── 41a07e3e-54f6-11ec-b278-645d865124e9.json
        ├── 97cce43c-54f6-11ec-b2e3-645d865124e9.json
        ├── 97d25fa2-54f6-11ec-b2e3-645d865124e9.json
        ├── 97dc6d6c-54f6-11ec-b2e3-645d865124e9.json
        ├── 97df7d54-54f6-11ec-b2e3-645d865124e9.json
        └── 97e2be2e-54f6-11ec-b2e3-645d865124e9.json
    
    2 directories, 20 files


Web scraping is so important for data science. Indeed most of the data, either image or text that Ml models are trained on come from the web. (cite crawl dataset). It allows small research teams, startups and people doing personal projects to finetune models on their own scrap data for their own needs. As an example, let's say that I want to create a dog versus cat classifier. It seems a "fairly simple" task, deep learning models, cnn or transformers, are good to perform classification and thanks to pretrain models and transfer learning (cc fastai/Hugging face) you don't have an enormous amount of data to train your models. But you still need some images, at least a couple hundreds of images. Even if such an amount is small from a deep learning perspective, it is still a huge amount for humans. Without web scraping you may have to ask all your friends for a photo of their cats/dogs (and I hope you have enough friends). But with web scraping you can do it within seconds. Amazing.

In the ML field, there are plenty of open source libraries to train and fitune your NN easily, you can even use the SOTA models (HF) out of the box without being a research engineer and implement every paper from scratch. You spawn a GPU instance within minutes without having to configure anything, find hyperparameters automatically etc ...
But you don't have the tools to create a dataset easily. And you can use the last and biggest transformers based vision models if you don't have enough quality data you won't get anything. Of course you can use one of the thousands of dataset from hugging face ! But you have to wait for someone to prepare the right dataset for your case. What if you could do it yourself with some web scraping without being a selenium or javascript expert ?
That's the first goal of Web2dataset (the name is still definitive yet open to suggestion), create a dataset in minutes for your needs.

Web2dataset is thought to be modulable, add every kind of image source you want as a Searcher, add any kind of Cleaner, i.e way of deleting bad samples from your dataset.

Web2datast has a second, maybe even more important, goal : clean your dataset and include ethic way of creating a dataset. Indeed, let's be honest, internet is sometime full of crap. You won't let your child only from scrolling on internet would you ? Well it should be the same with yours models. How to scrap only "good" and "ethic" data ? That's an open question, with a lot of researchers working on it (cc Tournesol). Web2datase is built from its core around this idea of scraping "ethics" data and it will (someday) incorporate state of the art cleaning technique to keep a dataset ethic and safe.



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

# TODO (not exhaustive)

- [ ] use proper logging
