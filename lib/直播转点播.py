import sys

sys.path.append('..')
from base.spider import Spider

class Spider(Spider):
    def getName(self):
        return "赞赏视频点播转直播"

    def init(self, extend):
        pass

    def homeContent(self, filter):
        result = {}
        classes = []
        videos = []

        try:
            # 读取txt文件
            with open('zansang2.txt', 'r', encoding='utf-8') as f:
                lines = f.readlines()

            current_genre = ""
            for line in lines:
                line = line.strip()
                if not line:
                    continue

                if line.endswith("#genre#"):
                    # 分类行
                    current_genre = line.replace("#genre#", "").strip()
                    if current_genre:
                        classes.append({
                            'type_name': current_genre,
                            'type_id': current_genre
                        })
                else:
                    # 视频行
                    if ',' in line:
                        title, url = line.split(',', 1)
                        if current_genre:
                            # 作为直播频道格式
                            videos.append({
                                'vod_name': title.strip(),
                                'vod_id': url.strip(),
                                'vod_pic': 'https://img.alicdn.com/imgextra/i1/6000000003098/O1CN01pO8Btj1PT2XgLcu4w_!!6000000001835-2-tps-400-400.png',  # 默认图片
                                'vod_remarks': current_genre,
                                'vod_tag': '直播'
                            })

        except Exception as e:
            print(f"读取文件失败: {e}")

        result['class'] = classes
        if videos:
            result['list'] = videos  # 首页直接显示所有视频

        return result

    def homeVideoContent(self):
        return {}

    def categoryContent(self, tid, pg, filter, extend):
        # 由于我们只有一页，直接返回空或首页数据
        return self.homeContent(filter) if pg == 1 else {'list': []}

    def detailContent(self, array):
        result = {}
        if not array or not array[0]:
            return result

        vod_id = array[0]
        vod_name = "赞赏视频"

        # 直接从vod_id获取播放地址（vod_id就是直链）
        vod = {
            'vod_id': vod_id,
            'vod_name': vod_name,
            'vod_pic': 'https://img.alicdn.com/imgextra/i1/6000000003098/O1CN01pO8Btj1PT2XgLcu4w_!!6000000001835-2-tps-400-400.png',
            'vod_content': '感谢您的赞赏支持',
            'vod_play_from': '直连播放',
            'vod_play_url': f'播放${vod_id}'  # 用$分隔播放列表，这里是单个直链
        }

        result['list'] = [vod]
        return result

    def playerContent(self, flag, id, vipFlags):
        result = {}
        if not id:
            return result

        # id就是直链地址
        result["parse"] = 0  # 0表示不解析，直接播放
        result["playUrl"] = ''
        result["url"] = id
        result["header"] = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        return result

    def searchContent(self, key, quick, page='1'):
        return {}

    def isVideoFormat(self, url):
        return '.mp4' in url or '.m3u8' in url or '.flv' in url

    def manualVideoCheck(self):
        return False

    def localProxy(self, param):
        return {}
