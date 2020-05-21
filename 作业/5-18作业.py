# 1.匹配出所有的阿拉伯和汉字数字
# string = "药品58和五十八号都已经受理，药品166和一百六十六号都已经受理，"
# 匹配结果：58, 五十八, 166, 一百六十六
#
import re
string = "药品58和五十八号都已经受理，药品166和一百六十六号都已经受理，"
ret = re.findall("\d+|[一-十 百千万]",string)
print(ret)
#
# 2提取网址中的图片地址
# content = '<img class="BDE_Image" src="http://tiebapic.baidu.com/forum/w%3D580/sign=e8708b64df95d143da76e42b43f18296/3242314e251f95ca7b1ff5d1de177f3e660952b3.jpg" size="37141" width="360" height="780" src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589802905449&di=857542ce04ab10b28403b7ba5faa6a07&imgtype=0&src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2F9095dbb30dfad766a38bb7f8.jpg" style="cursor: url(&quot;//tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur&quot;), pointer;">'
content = '<img class="BDE_Image" src="http://tiebapic.baidu.com/forum/w%3D580/sign=e8708b64df95d143da76e42b43f18296/3242314e251f95ca7b1ff5d1de177f3e660952b3.jpg" size="37141" width="360" height="780" src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589802905449&di=857542ce04ab10b28403b7ba5faa6a07&imgtype=0&src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2F9095dbb30dfad766a38bb7f8.jpg" style="cursor: url(&quot;//tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur&quot;), pointer;">'
ret = re.findall(r"src=(.*?\.jpg)",content)
print(ret)