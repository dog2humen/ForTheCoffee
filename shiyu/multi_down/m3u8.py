import os
import re
import sys
import functools
from urllib import parse
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

import urllib3
import requests
from tqdm import tqdm
from faker import Faker
from pathlib import Path


urllib3.disable_warnings()

def file_sort(x, y):
    x_num = int(re.findall(r'\d+', x)[0])
    y_num = int(re.findall(r'\d+', y)[0])
    if x_num < y_num:
        return -1
    elif x_num == y_num:
        return 0
    else:
        return 1

class Downloader():
    def __init__(self, url, dst=None, filename=None):
        """
        :param url: m3u8 文件下载地址
        :param dst: 指定下载视频文件输出目录，不指定则为当前目录
        :param filename: 下载视频文件名
        """
        self.url = url
        self.dst = dst or os.getcwd()
        self.filename = filename or "output"
        self.filename = self.filename + ".mp4"

        # ts 文件缓存目录
        self.tmp_folder = "down_temp_" + filename

        self.session = requests.Session()
        self.session.headers.update({'User-Agent': Faker().user_agent()})
        self.session.verify = False
        self.session.timeout = 6
        self.session.proxies = {
            "http": "http://agent.baidu.com:8188",
            "https": "http://agent.baidu.com:8188",
        }

    def parse_m3u8_url(self):
        """
        获取m3u8文件 并解析文件获取ts视频文件地址
        :return: ts文件下载地址
        """
        text = self.session.get(self.url).text

        return [parse.urljoin(self.url, row.strip()) for row in text.split('\n') if len(row) > 1 and (".ts" in row or ".m3u8" in row) and not row.startswith('#')]

    def check_save_folder(self):
        """
        检测视频输出目录是否正确，并创建temp目录用于临时存储ts文件
        :return: ts文件保存目录 (Path对象)
        """
        dst_folder = Path(self.dst)
        if not dst_folder.is_dir():
            raise Exception(f'{self.dst} is not a dir!')

        # 如果temp目录不存在便创建
        save_folder = Path(self.tmp_folder)
        if not save_folder.exists():
            save_folder.mkdir()

        return save_folder

    def download(self, key, ts_url, save_folder, pbar):
        """
        根据ts文件地址下载视频文件并保存到指定目录
        * 当前处理递归下载！！！
        :param ts_url: ts文件下载地址
        :param save_folder: ts文件保存目录
        :return: ts文件保存路径
        """
        # ts_url 可能有参数
        #filename = parse.urlparse(ts_url).path.split('/')[-1]
        filename = str(key) + ".ts"

        filepath = save_folder / filename
        if filepath.exists():
            # 文件已存在 跳过
            pbar.update(1)
            return True

        down_i = 0
        while True:
            if down_i > 8:
                break
            else:
                down_i += 1

            try:
                res = self.session.get(ts_url)
            except Exception as e:
                print_exc(e)
                continue

            if not (200 <= res.status_code < 400):
                print(f'{ts_url}, status_code: {res.status_code}')
                continue

            with filepath.open('wb') as fp:
                fp.write(res.content)

        pbar.update(1)
        return True

    def merge(self):
        """
        ts文件合成
        ffmpeg -i "concat:file01.ts|file02.ts|file03.ts" -acodec copy -vcodec copy output.mp4
        ffmpeg -f concat -safe 0 -i filelist.txt -c copy output.mp4
        :return:
        """

        filenames = []
        save_folder = self.check_save_folder()
        for root, dirs, files in os.walk(save_folder):
            for name in files:
                try:
                    filenames.append(name)
                except Exception as e:
                    print(e)
                    continue

        new_filenames = sorted(filenames, key=functools.cmp_to_key(file_sort))
        txt_content = '\n'.join([f'file {row}' for row in new_filenames])

        txt_filename = "concat_ts.txt"
        txt_filepath = Path(self.tmp_folder) / txt_filename
        with txt_filepath.open('w+') as fp:
            fp.write(txt_content)

        # 拼接ts文件
        command = f'ffmpeg -f concat -safe 0 -i {self.tmp_folder}/{txt_filename} -c copy {self.filename}'
        os.system(command)

    def remove_ts_file(self):
        save_folder = self.check_save_folder()
        for root, dirs, files in os.walk(save_folder):
            for name in files:
                try:
                    os.remove(os.path.join(root, name))
                except Exception as e:
                    print(e)
                    continue

        os.remove("./" + str(save_folder))

    def run(self, max_workers=4):
        """
        任务主函数
        :param max_workers: 线程池最大线程数
        """
        #获取ts文件地址列表
        ts_urls = self.parse_m3u8_url()
        if len(ts_urls) == 1:
            self.url = ts_urls[0]
            ts_urls = self.parse_m3u8_url()


        # 初始化进度条
        pbar = tqdm(total=len(ts_urls), initial=0, unit=' file', unit_scale=True, desc=self.filename, unit_divisor=1)

        # 获取ts文件保存目录
        save_folder = self.check_save_folder()

        tasks = []
        # 创建线程池，将ts文件下载任务推入线程池
        pool = ThreadPoolExecutor(max_workers=max_workers)
        tasks = [pool.submit(self.download, key, url, save_folder, pbar) for key,url in enumerate(ts_urls)]
        #阻塞至下载完毕
        wait(tasks, return_when=ALL_COMPLETED)

        # 关闭进度条
        pbar.close()

        # 合并ts文件
        self.merge()

        # 删除临时目录
        self.remove_ts_file()


if __name__ == '__main__':
    # How to use it in your work!
    url = "http://video.twimg.com/ext_tw_video/1204327308938506240/pu/pl/432x240/m2wY9Q9LPuFDXEr0.m3u8"
    name = "六万4"
    Downloader(url, filename=name).run(max_workers=128)
