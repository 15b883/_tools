# -*- coding: utf-8 -*-
import os
import shutil
import sys

thunderPath = '/Applications/Thunder.app/Contents/PlugIns/'
CONFIGS = []

delList = {
    "advertising": [True, '广告'], 
    "featuredpage": [True, '主页'],
    "feedback": [True, '反馈'],
    "iOSThunder": [True, '手机迅雷'],
    "myvip": [True, '会员中心'],
    "softmanager": [True, '软件管家'],
    "viprenew": [True, '会员开通'],
    "viptips": [True, '会员提示'],
    "xlbrowser": [True, '内置浏览器'],
    "xlplayer": [True, '迅雷影音'],
    "webgame": [True, '应用-游戏'],
    "onethingcloud": [True, '应用-玩客云'],
    "activitycenter": [True, '应用-活动中心'],
    "downloadhistory": [True, '应用-下载记录（用户的下载记录 云端）'],
    "livestream": [True, '应用-美女直播'],
    "liveupdate": [True, "应用-美女直播"],
    "browserhelper": [True, '应用-浏览器支持'],
    "transfer": [True, '应用-备份与恢复'],
    "bbassistant": [True, '应用-迅雷快鸟'],
    "searchtask": [False, '搜索任务'],
    "diagnostic": [True, '网络诊断'],
    "cloudspace": [False, '云盘'], # 4.0 新增
    "userlogin": [False, '用户登录'], # 慎选，删除后无法登录
    "viptask": [False, '会员加速'], # 慎选，删除后无法使用加速
    "applications": [False, '应用'],  # 慎选，删除后无法进入设置
    "preferences": [False, '应用-设置'],  # 慎选，删除后无法进入设置
}
def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

for file in listdir_fullpath(thunderPath):
    if file[43:][:-9] in delList and delList.get(file[43:][:-9])[0]:
        CONFIGS.append(file)

for file in CONFIGS:
    try:
        shutil.rmtree(file)
        print("{} {} 删除成功！".format(file[43:], delList.get(file[43:][:-9])[1]))
    except:
        print(file)
        print("权限不足，精简失败！")
        sys.exit()
print("精简完成，请重启迅雷！")