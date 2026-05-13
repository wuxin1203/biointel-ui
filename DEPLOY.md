# BioIntelOS 页面部署流程

## 前置条件

- GitHub 账号：`wuxin1203`
- 仓库地址：https://github.com/wuxin1203/biointel-ui
- 本地仓库路径：`/Users/sushuxin/Desktop/wangyeUI/`
- GitHub CLI 路径：需要时重新下载（见下方）

---

## 方法一：快速部署（推荐）

适用于：已有 HTML 文件，直接上传到公网。

```bash
# 1. 进入仓库目录
cd /Users/sushuxin/Desktop/wangyeUI

# 2. 复制 HTML 文件到仓库（改一个简短的文件名）
cp /Users/sushuxin/Desktop/wangye/你的文件夹/index.html ./你的页面名.html

# 3. 提交并推送
git add 你的页面名.html
git commit -m "Add 你的页面名"
git push origin main

# 4. 等待 1-2 分钟，访问：
# https://wuxin1203.github.io/biointel-ui/你的页面名.html
```

---

## 方法二：用 Python 脚本生成后部署

适用于：需要从数据源动态生成 HTML。

```bash
# 1. 进入仓库目录
cd /Users/sushuxin/Desktop/wangyeUI

# 2. 运行生成脚本
python3 generate_saas_dashboard_v2.py

# 3. 提交并推送
git add .
git commit -m "Update dashboard"
git push origin main
```

---

## 如果 git push 失败（认证问题）

### 方案 A：重新下载 gh CLI 并配置

```bash
# 下载 gh CLI
curl -sL "https://github.com/cli/cli/releases/download/v2.67.0/gh_2.67.0_macOS_arm64.zip" -o /tmp/gh.zip
unzip -qo /tmp/gh.zip -d /tmp/gh_install
chmod +x /tmp/gh_install/gh_2.67.0_macOS_arm64/bin/gh

# 登录（会打开浏览器授权）
/tmp/gh_install/gh_2.67.0_macOS_arm64/bin/gh auth login --web --git-protocol https

# 配置 git 使用 gh 认证
/tmp/gh_install/gh_2.67.0_macOS_arm64/bin/gh auth setup-git

# 然后重新 push
git push origin main
```

### 方案 B：检查是否已登录

```bash
/tmp/gh_install/gh_2.67.0_macOS_arm64/bin/gh auth status
```

---

## 已部署的页面列表

| 页面 | 文件名 | 公网链接 |
|------|--------|----------|
| 数据看板 v1 | dashboard.html | https://wuxin1203.github.io/biointel-ui/dashboard.html |
| 数据看板 v2 | dashboard_v2.html | https://wuxin1203.github.io/biointel-ui/dashboard_v2.html |
| SaaS Dashboard v1 | biointel-saas-dashboard.html | https://wuxin1203.github.io/biointel-ui/biointel-saas-dashboard.html |
| SaaS Dashboard v2 | biointel-saas-dashboard-v2.html | https://wuxin1203.github.io/biointel-ui/biointel-saas-dashboard-v2.html |
| Dataset Workspace | dataset-workspace.html | https://wuxin1203.github.io/biointel-ui/dataset-workspace.html |
| Dataset AI | dataset-ai.html | https://wuxin1203.github.io/biointel-ui/dataset-ai.html |
| Dataset Dashboard 3 | dataset-dashboard-3.html | https://wuxin1203.github.io/biointel-ui/dataset-dashboard-3.html |

---

## 注意事项

1. **文件名不要有中文和空格**，用英文短横线连接
2. **推送后等 1-2 分钟** GitHub Pages 才会更新
3. **所有文件必须放在仓库根目录**（不要放子文件夹，否则路径会变）
4. **gh CLI 在 /tmp 下会被系统清理**，如果失效需要重新下载
