# web2dataset



## Install

```shell
pip install git+https://github.com/samsja/web2dataset.git@master
```

## How to use

let's perform a simple research on google image to search for 5 bike images

```python
from web2dataset.searcher import GoogleImageSearcher
import jsons
import json

google_searcher = GoogleImageSearcher(
    "https://www.google.fr/search?q=bike&hl=fr&tbm=isch&sxsrf=AOaemvJcg1mx6w-ERS3fiG7QS7DORk9IOw%3A1638274784048&source=hp&biw=1920&bih=971&ei=4BamYaFU_p2Muw_43YuoCg&iflsig=ALs-wAMAAAAAYaYk8KzfwTYwqaWeGpaKIQxMxICkwyh2&ved=0ahUKEwihxK6UicD0AhX-DmMBHfjuAqUQ4dUDCAU&uact=5&oq=bike&gs_lcp=CgNpbWcQAzIHCCMQ7wMQJzIHCCMQ7wMQJzIICAAQgAQQsQMyCAgAEIAEELEDMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgoIIxDvAxDqAhAnOggIABCxAxCDAToLCAAQgAQQsQMQgwFQvxhYwSVgriZoBXAAeACAAUeIAfADkgEBOJgBAKABAaoBC2d3cy13aXotaW1nsAEK&sclient=img",
    n_item=5,
)
google_searcher.search()
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
