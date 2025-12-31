# 🤖 GLaDOS 自动签到 (GitHub Actions 版)

这是一个基于 GitHub Actions 的 GLaDOS 自动签到脚本。
每日定时运行，支持 Telegram 通知，零成本、免服务器。

## 📂 项目结构

为了方便维护和理解，本项目结构如下：

```text
glados-auto-checkin/
├── .github/
│   └── workflows/
│       └── schedule.yml    # ⚙️ 核心配置：设定每天几点运行
├── checkin.py              # 🐍 核心逻辑：签到和发送通知的代码
├── requirements.txt        # 📦 依赖列表：告诉环境需要安装 requests 库
└── README.md               # 📖 说明文档：即你现在看到的这份说明

✨ 特性
- 🕒 每日自动签到：每天北京时间 10:00 自动执行。
- 📱 Telegram 通知：签到结果直接推送到手机（可选）。
- 🛡️ 安全隐私：所有敏感数据（Cookie、Token）存储在 GitHub Secrets 中，不会公开。
- 🧩 开源结构：逻辑代码与配置分离，易于查看和修改。

🚀 使用方法
1. Fork 本仓库
点击页面右上角的 Fork 按钮，将本项目克隆到你的 GitHub 账号下。

2. 配置 Secrets (环境变量)
进入你 Fork 后的仓库，点击上方导航栏的 Settings -> 左侧 Secrets and variables -> Actions -> New repository secret，依次添加以下变量：

变量名 (Name),必填,说明,获取方式
GLADOS_COOKIE,✅,GLaDOS 的 Cookie,网页 F12 -> Network -> checkin 请求 -> Request Headers -> cookie
TG_TOKEN,❌,Telegram 机器人 Token,找 @BotFather 申请 (/newbot)
TG_ID,❌,接收消息的 TG 用户 ID,找 @userinfobot 获取

提示：TG_TOKEN 和 TG_ID 如果不填，脚本会自动跳过通知步骤，只进行签到。

3. 启用 Actions
由于 GitHub 的安全策略，Fork 的项目默认可能禁用了 Actions。

点击仓库上方的 Actions 标签。

如果看到绿色按钮 I understand my workflows, go ahead and enable them，请点击它。

4. 测试运行
在 Actions 页面左侧点击 GLaDOS Checkin。

点击右侧的 Run workflow 按钮 -> 再次点击绿色的 Run workflow。

等待几秒后，检查运行日志或查看手机是否收到通知。

📅 定时说明
默认配置为每天 UTC 02:00 (即北京时间 10:00) 运行。

如果你需要修改运行时间，请编辑 .github/workflows/schedule.yml 文件中的 cron 表达式：

YAML

- cron: '0 2 * * *'  # 分 时 日 月 周 (UTC时间)
⚠️ 常见问题
Cookie 过期：如果收到“Cookie Error”通知，请重新提取 Cookie 并更新到 Secrets 中。

签到失败：请检查 Secrets 名字是否拼写正确（必须完全一致）。

📜 免责声明
本项目仅供学习交流使用，请勿用于商业用途。脚本运行完全基于 GitHub Actions 免费服务，不保证 100% 的可用性。
