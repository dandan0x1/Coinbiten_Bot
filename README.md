# Coinbiten_Bot
# 🚀 Coinbiten 自动化工具

一个功能强大的Coinbiten平台自动化工具，支持批量注册、登录、挖矿等功能。

注册rf: https://coinbiten.com/?ref=493fd1a054

## 📋 功能特性

- 🔐 **批量注册**：支持多种邮箱模式，自动保存成功注册的用户
- 🔑 **批量登录**：自动获取token和用户信息
- ⛏️ **自动挖矿**：登录成功后自动启动挖矿
- 🌐 **代理支持**：支持随机代理IP，提高成功率
- 📊 **用户管理**：查看和管理已注册用户
- 🎨 **彩色界面**：美观的命令行界面

## 🛠️ 安装要求

### 系统要求
- Python 3.7+
- macOS/Linux/Windows

### 依赖包
```bash
pip install aiohttp colorama
```

## 📦 安装步骤

1. **克隆项目**
```bash
git clone https://github.com/your-username/coinbiten-automation.git
cd coinbiten-automation
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **创建配置文件目录**
```bash
mkdir config
```

## ⚙️ 配置文件设置

在 `config/` 目录中创建以下配置文件：

### 1. `config/domain.txt` - 域名列表
```
gmail.com
yahoo.com
hotmail.com
outlook.com
```

### 2. `config/gmail.txt` - 完整邮箱地址列表
```
user1@gmail.com
user2@yahoo.com
user3@hotmail.com
```

### 3. `config/proxy.txt` - 代理IP列表
```
http://127.0.0.1:7890
http://proxy1.example.com:8080
http://proxy2.example.com:8080
```

### 4. `config/rf.txt` - 推荐码列表
```
a4ce51ae25
b5df62bf36
c6eg73cg47
```

## 🚀 运行程序

```bash
python bot.py
```

## 📋 功能说明

### 主菜单选项

```
==================================================
🚀 Coinbiten 自动化工具
==================================================
请选择要执行的操作:
1. 📝 批量注册用户
2. 🔐 批量登录测试
3. 📊 查看已注册用户
4. 🌐 管理代理IP
5. ❌ 退出程序
==================================================
```

### 1. 📝 批量注册用户

#### 注册模式选择
- **选项1**：使用自定义域名 (从domain.txt随机选择域名)
- **选项2**：使用固定邮箱 (从gmail.txt随机选择完整邮箱)
- **选项3**：自定义固定邮箱

#### 参数设置
- 注册账户数量
- 每次注册后的等待时间

#### 功能特点
- 自动生成随机用户名和密码
- 成功注册的用户自动保存到 `config/registered_users.json`
- 支持代理IP轮换
- 避免重复注册相同邮箱

### 2. 🔐 批量登录测试

#### 功能流程
1. 从 `config/registered_users.json` 读取用户凭据
2. 批量登录测试
3. 自动获取用户token
4. 获取用户profile信息
5. **自动启动挖矿**

#### 输出信息
- 登录状态和结果
- 用户token信息
- 用户profile信息
- 挖矿启动结果

### 3. 📊 查看已注册用户

显示所有已注册用户的详细信息：
- 邮箱地址
- 密码
- 注册时间

### 4. 🌐 管理代理IP

#### 代理管理功能
- **查看代理列表**：显示当前所有代理IP
- **添加新代理**：支持多种格式 (ip:port 或 http://ip:port)
- **删除代理**：按序号删除指定代理

## 📁 项目结构

```
coinbiten-automation/
├── reg.py                          # 主程序文件
├── requirements.txt                 # 依赖包列表
├── README.md                       # 说明文档
└── config/                         # 配置文件目录
    ├── domain.txt                  # 域名列表
    ├── gmail.txt                   # 邮箱地址列表
    ├── proxy.txt                   # 代理IP列表
    ├── rf.txt                      # 推荐码列表
    └── registered_users.json       # 注册成功的用户凭据
```

## 🔧 配置说明

### 域名配置 (`config/domain.txt`)
- 每行一个域名
- 用于选项1的自定义域名模式
- 程序会随机选择域名生成邮箱

### 邮箱配置 (`config/gmail.txt`)
- 每行一个完整的邮箱地址
- 用于选项2的固定邮箱模式
- 程序会按顺序使用这些邮箱

### 代理配置 (`config/proxy.txt`)
- 每行一个代理地址
- 支持格式：`ip:port` 或 `http://ip:port`
- 程序会随机选择代理发送请求

### 推荐码配置 (`config/rf.txt`)
- 每行一个推荐码
- 用于注册时的推荐人字段
- 程序会随机选择推荐码

## ⚠️ 注意事项

1. **代理设置**：确保代理IP可用，否则请求可能失败
2. **邮箱格式**：确保邮箱地址格式正确
3. **请求频率**：建议设置适当的等待时间，避免请求过于频繁
4. **文件权限**：确保程序有读写配置文件的权限

## 🐛 故障排除

### 常见问题

1. **注册失败**
   - 检查网络连接
   - 验证代理IP是否可用
   - 确认邮箱格式正确

2. **登录失败**
   - 确认用户已成功注册
   - 检查邮箱和密码是否正确
   - 验证token获取是否成功

3. **挖矿启动失败**
   - 确认登录成功
   - 检查token是否有效
   - 验证用户权限

## 📞 技术支持

- **X (Twitter)**: https://x.com/ariel_sands_dan
- **Telegram**: https://t.me/sands0x1
- **QQ**: 712987787
- **QQ群**: 1036105927
- **电报群**: https://t.me/+fjDjBiKrzOw2NmJl
- **微信**: dandan0x1

## 📄 许可证

Copyright (c) 2025 All Rights Reserved

## 🔗 相关链接

- **申请key**: https://661100.xyz/
---

**免责声明**: 本工具仅供学习和研究使用，请遵守相关法律法规和平台规则。

