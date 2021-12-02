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
from web2dataset.searcher import GoogleImageSearcher


google_searcher = GoogleImageSearcher(
    "bike race",
    n_item=5,
    cleaners = [DuplicateCleaner()]
)
google_searcher.search()
google_searcher.clean()

google_searcher.save("/tmp/my_search")
```

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
