# -*- coding: utf8 -*-
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
* 摸鱼大赛第二名
## my Status
![Stats](https://github-readme-stats.vercel.app/api?username=uasier)
''')
        f.write(r'''
## Latest blog posts
''')
        r = requests.get("https://www.yuque.com/api/v2/repos/uasier/blog/docs",
        headers = {'X-Auth-Token': YUQUESECRET})
        i = 0
        for re in r.json()['data']:
            if i > 7:
                break
            i = i + 1
            timeArray = time.strptime(re['content_updated_at'], '%Y-%m-%dT%H:%M:%S.000Z')
            timestamp = time.mktime(timeArray)
            f.write('- [{}]({})\n'.format("【" + time.strftime("%Y-%m-%d", time.localtime(int(timestamp + 3600 * 8))) + "】" + re['title'], BASEURL + re['slug']))
        f.write('''
[>>> More blog posts](https://www.yuque.com/uasier/blog)
''')


if __name__ == "__main__":
    main_handler()
