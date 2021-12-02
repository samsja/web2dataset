# web2dataset



web2dataset is a modulable library built to easily create image dataset from google image and other.
You can find the docs [here](https://samsja.github.io/web2dataset/)

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

```python
len(google_searcher.documents),len(donwloader.documents)
```




    (5, 5)



```python
!tree /tmp/my_search
```

    [01;34m/tmp/my_search[00m
    ├── [01;34mimages[00m
    │   ├── b63bc05c-5378-11ec-8284-645d865124e9
    │   ├── b63d6fb0-5378-11ec-8284-645d865124e9
    │   ├── b63ec2d4-5378-11ec-8284-645d865124e9
    │   ├── b6400d24-5378-11ec-8284-645d865124e9
    │   └── b6423dec-5378-11ec-8284-645d865124e9
    └── [01;34mmetadata[00m
        ├── b63bc05c-5378-11ec-8284-645d865124e9.json
        ├── b63d6fb0-5378-11ec-8284-645d865124e9.json
        ├── b63ec2d4-5378-11ec-8284-645d865124e9.json
        ├── b6400d24-5378-11ec-8284-645d865124e9.json
        └── b6423dec-5378-11ec-8284-645d865124e9.json
    
    2 directories, 10 files


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
