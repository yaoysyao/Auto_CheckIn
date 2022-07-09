# Auto_CheckIn

- 各大网站自动签到脚本，基于github actions
- 目前支持GLADOS，天翼云盘，后期会支持更多
- 支持多用户签到，多个Cookie之间采用`&@@&`手动分割
- 本项目包含Github Actions keep alive模块，可自动激活Github Actions
- 支持推送消息到pushplus平台(server酱和pushplus选择一个就好，也可以同时推送，如果不配置则不进行推送)
- 支持推送消息到server酱(server酱和pushplus选择一个就好，也可以同时推送，如果不配置则不进行推送)

## 使用教程

### 1. glados签到教程

#### 1.1 添加 GLADOS_COOKIE 至 Secrets

- 登陆[GLaDOS](https://glados.rocks/)后，F12打开开发者工具。
- 刷新网页，并在浏览器中提取复制`Cookie`值，注意不要把`Cookie:`前缀加入进来！！！！！
-

<p align="center">
  <img src="images/Step1.png" />
</p>

- 在项目页面，依次点击`Settings`-->`Secrets`-->`Actions`-->`New repository secret`

<p align="center">
  <img src="images/Step2.png" />
</p>

- 建立名为`GLADOS_COOKIE`的 secret，值为复制的`Cookie`内容，最后点击`Add secret`
- secret名字必须为`GLADOS_COOKIE`，大小写敏感
- 支持多用户签到，多个Cookie之间采用`&@@&`手动分割完成后填入`GLADOS_COOKIE`即可
- 为保护隐私，不在日志中输出任何Id信息，请自行分辨账号顺序

<p align="center">
  <img src="images/Step3.png" />
</p>

### 2 天翼云盘签到教程

#### 2.1 添加 天翼云盘cookie 至 Secrets

- 同方法1.1,首先需要登录天翼云盘获取cookie，然后建立名为`CLOUD189_COOKIE`的 secret，值为复制的`Cookie`内容，最后点击`Add secret`
- 支持多用户签到，多个Cookie之间采用`&@@&`手动分割完成后填入`CLOUD189_COOKIE`即可

### 3 消息推送配置教程(可选,不配置则不进行推送)

#### 3.1 添加 PUSHPLUS的token值 至 Secrets

- 建立名为`PUSHPLUS_TOKEN`的 secret，值为复制的`pushplus（推送加平台的token）`，最后点击`Add secret`
- 登陆[pushplus](http://www.pushplus.plus/)

<p align="center">
  <img src="images/pushplus_token.png" />
</p>

#### 3.2 如果使用[server酱](https://sct.ftqq.com/)，请添加 SERVER_TOKEN 至 Secrets,如果不想推送通知可以不填写此项

- 建立名为`SERVER_TOKEN`的 secret，值为复制的`server酱的token`，最后点击`Add secret`

### 请注意，如果两个推送平台均配置，则会同时推送至两个平台，建议只配置一个就好

### 推送消息时，所有的签到只推送一条通知，如下所示

<p align="center">
  <img src="images/checkin_info.png" />
</p>


