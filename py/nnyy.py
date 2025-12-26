# -*- coding: utf-8 -*-
# @Author  : Doubebly
# @Time    : 2025/5/29 22:07

import sys
import time
import requests
import re
import html
import base64
from urllib.parse import quote, urljoin
sys.path.append('..')
from base.spider import Spider


class Spider(Spider):
    def getName(self):
        return "Nunuyy"

    def init(self, extend):
        self.home_url = 'https://nnyy.la/'
        self.ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        self.error_url = "https://sf1-cdn-tos.huoshanstatic.com/obj/media-fe/xgplayer_doc_video/mp4/xgplayer-demo-720p.mp4"
        
        # 分类映射
        self.cate_map = {
            '1': 'dianying',
            '2': 'dianshiju', 
            '3': 'zongyi',
            '4': 'dongman',
            '5': 'jilupian'
        }

    def getDependence(self):
        return []

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    def homeContent(self, filter):
        return {
            'class': [
                {'type_id': '0', 'type_name': '阿布影院'},
                {'type_id': '1', 'type_name': '电影'},
                {'type_id': '2', 'type_name': '电视剧'},
                {'type_id': '3', 'type_name': '综艺'},
                {'type_id': '4', 'type_name': '动漫'},
                {'type_id': '5', 'type_name': '纪录片'}
            ],
            'filters': {
                '1': [
                    {'key': 'class', 'name': '分类', 'value': [
                        {'n': '全部', 'v': ''}, {'n': '喜剧', 'v': '喜剧'}, {'n': '爱情', 'v': '爱情'},
                        {'n': '动作', 'v': '动作'}, {'n': '科幻', 'v': '科幻'}, {'n': '奇幻', 'v': '奇幻'},
                        {'n': '悬疑', 'v': '悬疑'}, {'n': '犯罪', 'v': '犯罪'}, {'n': '冒险', 'v': '冒险'},
                        {'n': '灾难', 'v': '灾难'}, {'n': '恐怖', 'v': '恐怖'}, {'n': '惊悚', 'v': '惊悚'},
                        {'n': '剧情', 'v': '剧情'}, {'n': '战争', 'v': '战争'}, {'n': '历史', 'v': '历史'},
                        {'n': '传记', 'v': '传记'}, {'n': '歌舞', 'v': '歌舞'}, {'n': '武侠', 'v': '武侠'},
                        {'n': '情色', 'v': '情色'}, {'n': '西部', 'v': '西部'}, {'n': '经典', 'v': '经典'},
                        {'n': '动画', 'v': '动画'}, {'n': '同性', 'v': '同性'}, {'n': '网络电影', 'v': '网络电影'}
                    ]},
                    {'key': 'area', 'name': '地区', 'value': [
                        {'n': '全部', 'v': ''}, {'n': '大陆', 'v': '大陆'}, {'n': '香港', 'v': '香港'},
                        {'n': '台湾', 'v': '台湾'}, {'n': '欧美', 'v': '欧美'}, {'n': '韩国', 'v': '韩国'},
                        {'n': '日本', 'v': '日本'}, {'n': '法国', 'v': '法国'}, {'n': '德国', 'v': '德国'},
                        {'n': '意大利', 'v': '意大利'}, {'n': '西班牙', 'v': '西班牙'}, {'n': '印度', 'v': '印度'},
                        {'n': '泰国', 'v': '泰国'}, {'n': '其它', 'v': '其它'}
                    ]},
                    {'key': 'year', 'name': '年代', 'value': [
                        {'n': '全部', 'v': ''}, {'n': '2020年代', 'v': '2020年代'}, {'n': '2025', 'v': '2025'},
                        {'n': '2024', 'v': '2024'}, {'n': '2023', 'v': '2023'}, {'n': '2022', 'v': '2022'},
                        {'n': '2021', 'v': '2021'}, {'n': '2020', 'v': '2020'}, {'n': '2019', 'v': '2019'},
                        {'n': '2010年代', 'v': '2010年代'}, {'n': '2000年代', 'v': '2000年代'}, {'n': '90年代', 'v': '90年代'},
                        {'n': '80年代', 'v': '80年代'}, {'n': '70年代', 'v': '70年代'}, {'n': '60年代', 'v': '60年代'},
                        {'n': '更早', 'v': '更早'}
                    ]},
                    {'key': 'by', 'name': '排序', 'value': [
                        {'n': '按时间排序', 'v': 'time'}, {'n': '按人气排序', 'v': 'hits'}, {'n': '按评分排序', 'v': 'score'}
                    ]}
                ],
                '2': [
                    {'key': 'class', 'name': '分类', 'value': [
                        {'n': '全部', 'v': ''}, {'n': '喜剧', 'v': '喜剧'}, {'n': '偶像', 'v': '偶像'},
                        {'n': '爱情', 'v': '爱情'}, {'n': '言情', 'v': '言情'}, {'n': '古装', 'v': '古装'},
                        {'n': '历史', 'v': '历史'}, {'n': '玄幻', 'v': '玄幻'}, {'n': '谍战', 'v': '谍战'},
                        {'n': '历险', 'v': '历险'}, {'n': '都市', 'v': '都市'}, {'n': '科幻', 'v': '科幻'},
                        {'n': '军旅', 'v': '军旅'}, {'n': '武侠', 'v': '武侠'}, {'n': '江湖', 'v': '江湖'},
                        {'n': '罪案', 'v': '罪案'}, {'n': '青春', 'v': '青春'}, {'n': '家庭', 'v': '家庭'},
                        {'n': '战争', 'v': '战争'}, {'n': '悬疑', 'v': '悬疑'}, {'n': '穿越', 'v': '穿越'},
                        {'n': '宫廷', 'v': '宫廷'}, {'n': '神话', 'v': '神话'}, {'n': '商战', 'v': '商战'},
                        {'n': '警匪', 'v': '警匪'}, {'n': '动作', 'v': '动作'}, {'n': '惊悚', 'v': '惊悚'},
                        {'n': '剧情', 'v': '剧情'}, {'n': '同性', 'v': '同性'}, {'n': '奇幻', 'v': '奇幻'},
                        {'n': '年代', 'v': '年代'}
                    ]},
                    {'key': 'area', 'name': '地区', 'value': [
                        {'n': '全部', 'v': ''}, {'n': '大陆', 'v': '大陆'}, {'n': '香港', 'v': '香港'},
                        {'n': '台湾', 'v': '台湾'}, {'n': '欧美', 'v': '欧美'}, {'n': '韩国', 'v': '韩国'},
                        {'n': '日本', 'v': '日本'}, {'n': '英国', 'v': '英国'}, {'n': '泰国', 'v': '泰国'},
                        {'n': '其它', 'v': '其它'}
                    ]},
                    {'key': 'year', 'name': '年代', 'value': [
                        {'n': '全部', 'v': ''}, {'n': '2025', 'v': '2025'}, {'n': '2024', 'v': '2024'},
                        {'n': '2023', 'v': '2023'}, {'n': '2022', 'v': '2022'}, {'n': '2021', 'v': '2021'},
                        {'n': '2020', 'v': '2020'}, {'n': '2019', 'v': '2019'}, {'n': '2020年代', 'v': '2020年代'},
                        {'n': '2010年代', 'v': '2010年代'}, {'n': '2000年代', 'v': '2000年代'}, {'n': '90年代', 'v': '90年代'},
                        {'n': '80年代', 'v': '80年代'}, {'n': '70年代', 'v': '70年代'}, {'n': '60年代', 'v': '60年代'},
                        {'n': '更早', 'v': '更早'}
                    ]},
                    {'key': 'by', 'name': '排序', 'value': [
                        {'n': '按时间排序', 'v': 'time'}, {'n': '按人气排序', 'v': 'hits'}, {'n': '按评分排序', 'v': 'score'}
                    ]}
                ]
            }
        }

    def homeVideoContent(self):
        video_list = []
        try:
            res = requests.get(f'{self.home_url}dianying/', headers={"User-Agent": self.ua})
            html_text = res.text
            
            # 使用555.py的稳定提取逻辑
            li_pattern = r'<li>\s*<a href="([^"]+)"[^>]*class="thumbnail"[^>]*>.*?<img[^>]*data-src="([^"]+)"[^>]*>.*?<div class="note"><span>([^<]+)</span>.*?<h2><a[^>]*>([^<]+)</a>'
            matches = re.findall(li_pattern, html_text, re.DOTALL)
            
            for match in matches:
                url, pic, remarks, name = match
                vod_id = url.split('/')[-1].replace('.html', '')
                
                video_list.append({
                    'vod_id': vod_id,
                    'vod_name': html.unescape(name.strip()),
                    'vod_pic': pic,
                    'vod_remarks': remarks.strip()
                })
                
                if len(video_list) >= 20:
                    break
                    
        except:
            pass
            
        return {
            'list': video_list,
            'parse': 0,
            'jx': 0
        }

    def categoryContent(self, cid, page, filter, ext):
        video_list = []
        
        # 获取分类名称
        cate_name = self.cate_map.get(cid, 'dianying')
        
        # 构建URL - 使用555.py的简单逻辑
        if page == 1:
            url = f'{self.home_url}{cate_name}/'
        else:
            url = f'{self.home_url}{cate_name}/?page={page}'
        
        # 如果有筛选条件，添加到URL中
        if ext:
            params = []
            for key, value in ext.items():
                if value:
                    params.append(f'{key}={quote(value)}')
            if params:
                url = f'{url}?{"&".join(params)}'
        
        try:
            res = requests.get(url, headers={"User-Agent": self.ua})
            html_text = res.text
            
            # 使用555.py的稳定提取逻辑
            li_pattern = r'<li>\s*<a href="([^"]+)"[^>]*class="thumbnail"[^>]*>.*?<img[^>]*data-src="([^"]+)"[^>]*>.*?<div class="note"><span>([^<]+)</span>.*?<div class="countrie">.*?<h2><a[^>]*>([^<]+)</a>'
            matches = re.findall(li_pattern, html_text, re.DOTALL)
            
            for match in matches:
                url, pic, remarks, name = match
                vod_id = url.split('/')[-1].replace('.html', '')
                
                # 尝试提取更多信息（年份、地区）
                year = ''
                area = ''
                try:
                    # 尝试从countrie中提取年份和地区
                    country_pattern = r'<div class="countrie">(.*?)</div>'
                    country_match = re.search(country_pattern, html_text[html_text.find(url):html_text.find(url)+500], re.DOTALL)
                    if country_match:
                        country_text = country_match.group(1)
                        # 提取年份和地区
                        span_matches = re.findall(r'<span[^>]*>([^<]+)</span>', country_text)
                        if len(span_matches) >= 2:
                            year = span_matches[0]
                            area = span_matches[1]
                        elif len(span_matches) == 1:
                            year = span_matches[0]
                except:
                    pass
                
                video_list.append({
                    'vod_id': vod_id,
                    'vod_name': html.unescape(name.strip()),
                    'vod_pic': pic,
                    'vod_remarks': remarks.strip(),
                    'vod_year': year,
                    'vod_area': area
                })
                
        except:
            pass
        
        return {'list': video_list, 'parse': 0, 'jx': 0}

    def detailContent(self, did):
        ids = did[0]
        video_list = []
        
        try:
            # 尝试从电影分类获取详情页
            detail_url = f'{self.home_url}dianying/{ids}.html'
            res = requests.get(detail_url, headers={"User-Agent": self.ua})
            
            if res.status_code != 200:
                # 如果电影分类没有，尝试其他分类
                for cate_name in ['dianshiju', 'zongyi', 'dongman', 'jilupian']:
                    detail_url = f'{self.home_url}{cate_name}/{ids}.html'
                    res = requests.get(detail_url, headers={"User-Agent": self.ua})
                    if res.status_code == 200:
                        break
            
            html_text = res.text
            
            # 提取基本信息
            # 标题
            title_match = re.search(r'<h2[^>]*>([^<]+)<span>', html_text)
            if not title_match:
                title_match = re.search(r'<h1[^>]*>([^<]+)<span>', html_text)
            
            vod_name = html.unescape(title_match.group(1).strip()) if title_match else ids
            
            # 提取年份
            year_match = re.search(r'<span>\((\d{4})\)</span>', html_text)
            vod_year = year_match.group(1) if year_match else ''
            
            # 图片
            pic_match = re.search(r'<img[^>]*data-src="([^"]+)"[^>]*alt="[^"]*"[^>]*>', html_text)
            vod_pic = pic_match.group(1) if pic_match else ''
            
            # 导演
            director_match = re.search(r'导演[：:]<span[^>]*>(.*?)</span>', html_text, re.DOTALL)
            if director_match:
                director_text = director_match.group(1)
                director_names = re.findall(r'>([^<]+)</a>', director_text)
                vod_director = ','.join(director_names) if director_names else ''
            else:
                vod_director = ''
            
            # 演员
            actor_match = re.search(r'主演[：:]<span[^>]*>(.*?)</span>', html_text, re.DOTALL)
            if actor_match:
                actor_text = actor_match.group(1)
                actor_names = re.findall(r'>([^<]+)</a>', actor_text)
                vod_actor = ','.join(actor_names) if actor_names else ''
            else:
                vod_actor = ''
            
            # 类型
            type_match = re.search(r'类型[：:]<span[^>]*>(.*?)</span>', html_text, re.DOTALL)
            if type_match:
                type_text = type_match.group(1)
                type_names = re.findall(r'>([^<]+)</a>', type_text)
                vod_type = ','.join(type_names) if type_names else ''
            else:
                vod_type = ''
            
            # 地区
            area_match = re.search(r'制片国家/地区[：:]<span[^>]*>(.*?)</span>', html_text, re.DOTALL)
            if area_match:
                area_text = area_match.group(1)
                area_names = re.findall(r'>([^<]+)</a>', area_text)
                vod_area = ','.join(area_names) if area_names else ''
            else:
                vod_area = ''
            
            # 简介
            desc_match = re.search(r'剧情简介[：:]<span[^>]*>([^<]+)</span>', html_text)
            vod_content = html.unescape(desc_match.group(1).strip()) if desc_match else ''
            
            # 评分
            rate_match = re.search(r'<span class="rate">([^<]+)</span>', html_text)
            vod_score = rate_match.group(1) if rate_match else ''
            
            # 播放源和剧集 - 关键优化：提取加密的播放地址
            # 提取所有播放源
            source_pattern = r'<dt data-sid="(\d+)"[^>]*>([^<]+)</dt>'
            source_matches = re.findall(source_pattern, html_text)
            
            # 提取加密的URL字典
            encrypted_dict = {}
            url_dict_pattern = r'urlDictionary\[(\d+)\]\[(\d+)\]\s*=\s*"([^"]+)"'
            url_dict_matches = re.findall(url_dict_pattern, html_text)
            
            for sid, nid, encrypted_url in url_dict_matches:
                if int(sid) not in encrypted_dict:
                    encrypted_dict[int(sid)] = {}
                encrypted_dict[int(sid)][int(nid)] = encrypted_url
            
            vod_play_from = []
            vod_play_url = []
            
            if source_matches:
                for sid_str, source_name in source_matches:
                    sid = int(sid_str)
                    
                    # 查找该源的所有剧集
                    episode_pattern = rf'data-sid="{sid}"[^>]*data-nid="(\d+)"[^>]*>.*?<a[^>]*>([^<]+)</a>'
                    episode_matches = re.findall(episode_pattern, html_text, re.DOTALL)
                    
                    if episode_matches:
                        vod_play_from.append(source_name)
                        episodes = []
                        for nid_str, episode_name in episode_matches:
                            nid = int(nid_str)
                            
                            # 构建播放ID：格式为 sid|nid|encrypted_url|detail_url
                            if sid in encrypted_dict and nid in encrypted_dict[sid]:
                                encrypted_url = encrypted_dict[sid][nid]
                                play_id = f"{sid}|{nid}|{encrypted_url}|{detail_url}"
                            else:
                                play_id = f"{sid}|{nid}|{detail_url}"
                            
                            episodes.append(f"{episode_name.strip()}${play_id}")
                        
                        if episodes:
                            vod_play_url.append('#'.join(episodes))
            
            # 如果没有提取到播放源，使用默认值
            if not vod_play_from:
                vod_play_from = ['阿布影院']
                vod_play_url = [f"小布丁线路${detail_url}"]
            
            # 构建视频信息
            video_info = {
                'type_name': vod_type,
                'vod_id': ids,
                'vod_name': vod_name,
                'vod_pic': vod_pic,
                'vod_year': vod_year,
                'vod_area': vod_area,
                'vod_remarks': f"评分:{vod_score}" if vod_score else '',
                'vod_actor': vod_actor,
                'vod_director': vod_director,
                'vod_content': f"阿布为你介绍🤩🤙{vod_content}",
                'vod_play_from': '$$$'.join(vod_play_from),
                'vod_play_url': '$$$'.join(vod_play_url)
            }
            
            video_list.append(video_info)
            
        except Exception as e:
            # 如果详情页解析失败，返回一个基本的视频信息
            print(f"解析详情页失败: {e}")
            pass
        
        return {"list": video_list, 'parse': 0, 'jx': 0}

    def searchContent(self, key, quick, page='1'):
        wd = key
        video_list = []
        
        try:
            search_url = f'{self.home_url}search?wd={quote(wd)}&page={page}'
            res = requests.get(search_url, headers={"User-Agent": self.ua})
            html_text = res.text
            
            # 使用555.py的稳定提取逻辑
            li_pattern = r'<li>\s*<a href="([^"]+)"[^>]*class="thumbnail"[^>]*>.*?<img[^>]*data-src="([^"]+)"[^>]*>.*?<div class="note"><span>([^<]+)</span>.*?<h2><a[^>]*>([^<]+)</a>'
            matches = re.findall(li_pattern, html_text, re.DOTALL)
            
            for match in matches:
                url, pic, remarks, name = match
                vod_id = url.split('/')[-1].replace('.html', '')
                
                video_list.append({
                    'vod_id': vod_id,
                    'vod_name': html.unescape(name.strip()),
                    'vod_pic': pic,
                    'vod_remarks': remarks.strip()
                })
                
        except:
            pass
        
        return {'list': video_list, 'parse': 0, 'jx': 0}

    def rc4_decrypt(self, encrypted_hex, key="i_love_you"):
        """RC4解密函数，与网页中的JavaScript实现一致"""
        try:
            # 将十六进制字符串转换为字节
            encrypted_bytes = bytes.fromhex(encrypted_hex)
            
            # RC4算法实现
            s = list(range(256))
            j = 0
            key_length = len(key)
            
            # KSA (Key-Scheduling Algorithm)
            for i in range(256):
                j = (j + s[i] + ord(key[i % key_length])) % 256
                s[i], s[j] = s[j], s[i]
            
            # PRGA (Pseudo-Random Generation Algorithm) 并解密
            i = j = 0
            decrypted_bytes = bytearray()
            
            for byte in encrypted_bytes:
                i = (i + 1) % 256
                j = (j + s[i]) % 256
                s[i], s[j] = s[j], s[i]
                key_byte = s[(s[i] + s[j]) % 256]
                decrypted_bytes.append(byte ^ key_byte)
            
            return decrypted_bytes.decode('utf-8', errors='ignore')
        except:
            return None

    def playerContent(self, flag, pid, vipFlags):
        play_url = self.error_url
        parse = 0  # 默认不解析，直接播放
        
        try:
            # 解析pid格式: sid|nid|encrypted_url|detail_url 或 sid|nid|detail_url
            parts = pid.split('|')
            
            if len(parts) >= 4:
                # 格式: sid|nid|encrypted_url|detail_url
                sid = parts[0]
                nid = parts[1]
                encrypted_url = parts[2]
                detail_url = parts[3]
                
                # 尝试使用RC4解密
                decrypted_url = self.rc4_decrypt(encrypted_url)
                
                if decrypted_url and decrypted_url.startswith('http'):
                    play_url = decrypted_url
                    parse = 0  # 直接播放解密后的URL
                else:
                    # 解密失败，返回详情页地址进行嗅探
                    play_url = detail_url
                    parse = 1  # 需要解析
                    
            elif len(parts) == 3:
                # 格式: sid|nid|detail_url
                detail_url = parts[2]
                play_url = detail_url
                parse = 1  # 需要解析
                
            else:
                # 不是标准格式，可能是直接的详情页URL
                if pid.startswith('http'):
                    play_url = pid
                    parse = 1  # 需要解析
                else:
                    # 可能是视频ID，尝试构建详情页URL
                    play_url = f'{self.home_url}dianying/{pid}.html'
                    parse = 1  # 需要解析
                    
        except Exception as e:
            print(f"播放地址解析失败: {e}")
            # 如果解析失败，尝试使用详情页地址
            if 'http' in pid:
                play_url = pid
                parse = 1
            else:
                play_url = self.error_url
                parse = 0
        
        h2 = {
            "User-Agent": self.ua,
            "Referer": self.home_url,
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }
        
        return {"url": play_url, "header": h2, "parse": parse, "jx": 0}

    def localProxy(self, params):
        pass

    def destroy(self):
        return '正在Destroy'

if __name__ == '__main__':
    pass