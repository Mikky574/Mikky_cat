# Mikky_cat
本项目主要是用python写了一个qq群聊机器人，项目是基于mirai项目的http-api-v2插件，目标是让所有会python语言的都能搭建一个用python开发的qq机器人。也做得蛮多东西了得，把凯露的代码发出来。具体整理得不太好，感觉还是有点乱，最后干脆摆了，反正也没啥人关注，就把ReadMe写得详细点就行了。

具体而言就是绑定一个qq机器人号，向机器人账号发送信息mirai可以收到信息，并通过http-api插件把信息传到自己写的python脚本上，python处理相关信息后将得到应该回复的消息，再将消息通过mirai发送出去。

本项目主要包含的功能是：
1、抽卡小游戏（响应特定关键词，然后发送回一段文字描述以及一张抽卡结果的图片）
2、定时任务（每天8点以及21点向发送过消息的群聊，发送一首诗词作为问候）
3、chatgpt聊天api（实现了私聊以及群聊两种方式，为每个用户设立单独的存储列表，用来存用户的历史记录，进而实现持续的聊天）
4、网页截屏（响应用户发送的消息内携带网址的片段，使用爬虫访问对应网址并截屏）
~~5、AI绘画（之前是实现了的，但作者太懒，没更新模型，后面就舍弃了。有需要作者再考虑少打几把LOL来加回去）~~
~~6、原本还有写数据库的，若干个版本后懒惰了，就没这块内容了，也是懒得，同时也是没啥用户使用，有需求的话，我再加回去。~~

## Mirai安装
先安装mirai以及http-v2的插件，这里不对mirai如何安装使用进行说明，因为没啥人看，有需要的话作者会更新。

这里放点链接以及群聊

[mirai论坛](https://mirai.mamoe.net/)

有个别人建的mirai的qq讨论群群：780594692

本人是使用mcl的，用core也行，反正是用的http-api开发的：

[mirai-mcl](https://github.com/iTXTech/mirai-console-loader)

配置号mirai,可以运行后，下载并将http-v2的插件放到plugins文件夹下，重新启动mirai即可自动完成安装：

[http-api插件](https://github.com/project-mirai/mirai-api-http/releases)

具体内容关注这个，也可以不看，因为我都封装到even类里面，处理好了的：

[http-v2插件的官方文档说明](https://docs.mirai.mamoe.net/mirai-api-http/api/API.html#%E8%8E%B7%E5%8F%96%E7%BE%A4%E6%88%90%E5%91%98%E5%88%97%E8%A1%A8)

## python3使用到的相关的库汇总

