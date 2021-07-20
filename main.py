# -*- coding: utf8 -*-
import datetime
import json
import time
import os

import requests

BASEURL="https://www.yuque.com/uasier/blog/"
YUQUESECRET = os.environ["YUQUESECRET"]

def main_handler():
    with open('README.md', 'w') as f:
        f.write(r'''
## That's me
* 1996
* C/C++ Bash/Python/PHP
## my Status
![Stats](https://github-readme-stats.vercel.app/api?username=uasier)
''')
        f.write(r'''
## Latest blog posts
''')
        r = requests.get("https://www.yuque.com/api/v2/repos/uasier/blog/docs",
        headers = {'X-Auth-Token': YUQUESECRET})
        for re in r.json()['data']:
            time_stamp = datetime.datetime.strptime(int(re['content_updated_at']) + 3600 * 8, '%Y-%m-%dT%H:%M:%S.000Z')
            f.write('- [{}]({})\n'.format(datetime.datetime.strftime(time_stamp, '%Y-%m-%d %H:%M:%S') + " >>> " + re['title'], BASEURL + re['slug']))
        f.write('''
[>>> More blog posts](https://www.yuque.com/uasier/blog)
''')


if __name__ == "__main__":
    main_handler()
