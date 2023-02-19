#该程序只能推送消息至企业微信

#引入库
import requests
import json
import time

# 请在此处填写您的企业微信机器人的WEBHOOK，这样消息才可以推送到企业微信。
def send(content, webhook_url="WEBHOOK"):
    data = {"msgtype": "markdown", "markdown": {"content": content}}
    r = requests.post(url=webhook_url, data=json.dumps(
        data, ensure_ascii=False).encode('utf-8'), verify=False)
    return r.text, r.status_code
info = ""
ok = True
# 请在中括号内填写需检测的网站，如：["beesu.cn","pan.beesu.cn"]
site = ["网址"]
for i in site:
    info += f">{i} 网站运行"
    try:
        r = requests.get(i)
        if (r.ok):
            info += f"<font color=\"info\">正常</font>\n"
        else:
            ok = False
            info += f"<font color=\"warning\">异常</font>\n    返回码: <font color=\"warning\">{r.status_code}</font>\n"
    except Exception as e:
        ok = False
        info += f"<font color=\"warning\">异常</font>\n    异常信息: <font color=\"warning\">{e}</font>\n"
if (ok):
    info = f"网站总体运行<font color=\"info\">正常</font>,请相关同事注意!\n"+info
else:
    # 请在这里填写需要@的人,例如<@蜜蜂云>，可以多个填写，例如<@蜜蜂云><@duyuxuan><@wyc>
    info = f"网站运行<font color=\"warning\">异常</font>,请相关同事注意!\n<@jingteng>\n"+info
info = f'现在是{time.strftime("%Y年%m月%d日 %H时%M分",time.localtime())}\n' + info
send(info)
 # 版权归蜜蜂云所有
