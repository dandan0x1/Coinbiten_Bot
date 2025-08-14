import aiohttp
import asyncio
import random
import string
import time
import os
import json
from colorama import *

# 版权信息
def show_copyright():
    """展示版权信息"""
    copyright_info = f"""{Fore.CYAN}
    *****************************************************
    *           X:https://x.com/ariel_sands_dan         *
    *           Tg:https://t.me/sands0x1                *
    *           Copyright (c) 2025                      *
    *           All Rights Reserved                     *
    *****************************************************
    {Style.RESET_ALL}
    """
    print(copyright_info)
    print('=' * 50)
    print(f"{Fore.GREEN}申请key: https://661100.xyz/ {Style.RESET_ALL}")
    print(f"{Fore.RED}联系Dandan: \n QQ:712987787 QQ群:1036105927 \n 电报:sands0x1 电报群:https://t.me/+fjDjBiKrzOw2NmJl \n 微信: dandan0x1{Style.RESET_ALL}")
    print('=' * 50)

def read_random_line(filename):
    """从文件中随机读取一行"""
    filepath = os.path.join('config', filename)
    if not os.path.exists(filepath):
        print(f"警告: 文件 {filepath} 不存在，使用默认值")
        return None
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if lines:
                return random.choice(lines).strip()
            else:
                print(f"警告: 文件 {filepath} 为空")
                return None
    except Exception as e:
        print(f"读取文件 {filepath} 时出错: {e}")
        return None

def save_credentials(email, password):
    """保存注册成功的用户凭据到文件"""
    credentials_file = os.path.join("config", "registered_users.json")
    
    try:
        # 读取现有凭据
        existing_credentials = []
        if os.path.exists(credentials_file):
            with open(credentials_file, 'r', encoding='utf-8') as f:
                existing_credentials = json.load(f)
        
        # 检查是否已存在
        for cred in existing_credentials:
            if cred["email"] == email:
                print(f"用户 {email} 已存在，跳过保存")
                return
        
        # 添加新凭据
        new_credential = {
            "email": email,
            "password": password,
            "registered_at": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        existing_credentials.append(new_credential)
        
        # 保存到文件
        with open(credentials_file, 'w', encoding='utf-8') as f:
            json.dump(existing_credentials, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 用户凭据已保存: {email}")
        
    except Exception as e:
        print(f"保存用户凭据时出错: {e}")

def load_credentials():
    """从文件加载注册成功的用户凭据"""
    credentials_file = os.path.join("config", "registered_users.json")
    
    if not os.path.exists(credentials_file):
        print(f"警告: 文件 {credentials_file} 不存在，没有可用的登录凭据")
        return []
    
    try:
        with open(credentials_file, 'r', encoding='utf-8') as f:
            credentials = json.load(f)
        
        print(f"📁 从 {credentials_file} 加载了 {len(credentials)} 个用户凭据")
        return credentials
        
    except Exception as e:
        print(f"读取用户凭据文件时出错: {e}")
        return []

def get_random_proxy():
    """从proxy.txt中随机获取代理"""
    proxy = read_random_line('proxy.txt')
    if proxy:
        # 处理代理格式
        if proxy.startswith('http://') or proxy.startswith('https://'):
            return proxy
        else:
            return f"http://{proxy}"
    return None

def generate_random_string(length=10):
    # 只使用字母和数字，避免特殊字符导致的编码问题
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def get_all_emails_from_file(filename):
    """从文件中读取所有邮箱地址"""
    filepath = os.path.join('config', filename)
    if not os.path.exists(filepath):
        print(f"警告: 文件 {filepath} 不存在")
        return []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            emails = [line.strip() for line in f.readlines() if line.strip()]
        return emails
    except Exception as e:
        print(f"读取文件 {filepath} 时出错: {e}")
        return []

def generate_credentials(use_custom_domain=True, fixed_email=None, available_emails=None, email_index=None):
    if use_custom_domain:
        # 使用自定义域名模式（原有逻辑）
        random_username = generate_random_string(8).lower()
        
        # 读取自定义域名
        domain = read_random_line('domain.txt')
        if not domain:
            domain = 'gmail.com'  # 默认域名
        
        # 直接使用自定义域名
        final_domain = domain
        random_email = f"{random_username}@{final_domain}"
    else:
        # 使用固定邮箱模式
        if fixed_email:
            random_email = fixed_email
        else:
            # 从可用邮箱列表中按索引选择
            if available_emails and email_index is not None and email_index < len(available_emails):
                random_email = available_emails[email_index]
            else:
                random_email = "sandy@paydns.com"  # 默认固定邮箱
    
    # 验证邮箱格式
    if '@' not in random_email or random_email.count('@') > 1:
        print(f"⚠️ 警告: 邮箱格式不正确: {random_email}")
        random_email = "sandy@paydns.com"  # 使用默认邮箱
    
    # 生成安全的密码：只使用字母和数字，避免特殊字符
    random_password = generate_random_string(12)  # 12位字母数字组合
    
    # 从rf.txt中随机读取推荐码
    refer_by = read_random_line('rf.txt')
    if not refer_by:
        refer_by = "a4ce51ae25"  # 默认推荐码
    
    return {
        "email": random_email,
        "password": random_password,
        "confirmpass": random_password,
        "refer_by": refer_by
    }

# 注册请求的headers
register_headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://coinbiten.com",
    "Referer": "https://coinbiten.com/",
    "Sec-Ch-Ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
    "Sec-Ch-Ua-Mobile": "?1",
    "Sec-Ch-Ua-Platform": '"Android"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
}

# 登录请求的headers (基于curl请求)
login_headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryPBDTvZxPNUAOcX65",
    "Origin": "https://coinbiten.com",
    "Priority": "u=1, i",
    "Referer": "https://coinbiten.com/",
    "Sec-Ch-Ua": '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"macOS"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}

# Profile请求的headers
profile_headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryVuOC7aGYd362dWJA",
    "Origin": "https://coinbiten.com",
    "Priority": "u=1, i",
    "Referer": "https://coinbiten.com/",
    "Sec-Ch-Ua": '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"macOS"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}

# 挖矿请求的headers
mining_headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary1ArDaeBTCW9DGXBQ",
    "Origin": "https://coinbiten.com",
    "Priority": "u=1, i",
    "Referer": "https://coinbiten.com/",
    "Sec-Ch-Ua": '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"macOS"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}

async def send_register_request(session, url, data):
    try:
        # 获取随机代理
        proxy = get_random_proxy()
        
        # 确保数据是字符串格式
        encoded_data = {
            "email": str(data["email"]),
            "password": str(data["password"]),
            "confirmpass": str(data["confirmpass"]),
            "refer_by": str(data["refer_by"])
        }
        
        # 调试信息
        print(f"🔍 调试 - 发送数据: {encoded_data}")
        
        # 设置请求参数
        request_kwargs = {
            "data": encoded_data,
            "headers": register_headers
        }
        
        # 只有在有代理时才添加代理
        if proxy:
            request_kwargs["proxy"] = proxy
            print(f"🔍 调试 - 使用代理: {proxy}")
        
        async with session.post(url, **request_kwargs) as response:
            status = response.status
            content = await response.text()
            
            # 如果注册成功，保存凭据
            if status == 200:
                save_credentials(data["email"], data["password"])
            
            return {
                "email": data["email"],
                "password": data["password"],
                "status": status,
                "content": content
            }
    except Exception as e:
        return {
            "email": data["email"],
            "password": data["password"],
            "status": None,
            "content": f"Error: {str(e)}"
        }

async def send_mining_request(session, url, token):
    """提交挖矿请求"""
    try:
        # 获取随机代理
        proxy = get_random_proxy()
        
        # 使用简单的表单数据
        form_data = {
            'token': token
        }
        
        # 更新headers，使用application/x-www-form-urlencoded
        headers = mining_headers.copy()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        
        # 调试信息
        print(f"   🔍 调试 - 挖矿请求:")
        print(f"      URL: {url}")
        print(f"      Token: {token[:20]}...")
        print(f"      表单数据: {form_data}")
        
        # 设置请求参数
        request_kwargs = {
            "data": form_data,
            "headers": headers
        }
        
        # 只有在有代理时才添加代理
        if proxy:
            request_kwargs["proxy"] = proxy
            print(f"      🔍 调试 - 使用代理: {proxy}")
        
        async with session.post(url, **request_kwargs) as response:
            status = response.status
            content = await response.text()
            
            print(f"      🔍 调试 - 挖矿响应状态: {status}")
            print(f"      🔍 调试 - 挖矿响应内容: {content[:200]}...")
            
            return {
                "token": token,
                "status": status,
                "content": content
            }
    except Exception as e:
        print(f"      🔍 调试 - 挖矿异常: {type(e).__name__}: {str(e)}")
        return {
            "token": token,
            "status": None,
            "content": f"Error: {str(e)}"
        }

async def send_profile_request(session, url, token):
    """获取用户profile信息"""
    try:
        # 获取随机代理
        proxy = get_random_proxy()
        
        # 创建multipart/form-data
        data = aiohttp.FormData()
        data.add_field('token', token)
        
        # 设置请求参数
        request_kwargs = {
            "data": data,
            "headers": profile_headers
        }
        
        # 只有在有代理时才添加代理
        if proxy:
            request_kwargs["proxy"] = proxy
        
        async with session.post(url, **request_kwargs) as response:
            status = response.status
            content = await response.text()
            return {
                "token": token,
                "status": status,
                "content": content
            }
    except Exception as e:
        return {
            "token": token,
            "status": None,
            "content": f"Error: {str(e)}"
        }

async def send_login_request(session, url, email, password):
    try:
        # 获取随机代理
        proxy = get_random_proxy()
        
        # 尝试使用简单的表单数据
        form_data = {
            'email': email,
            'password': password
        }
        
        # 更新headers，使用application/x-www-form-urlencoded
        headers = login_headers.copy()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        
        # 调试信息
        print(f"🔍 调试 - 登录请求:")
        print(f"   URL: {url}")
        print(f"   邮箱: {email}")
        print(f"   密码: {password}")
        print(f"   表单数据: {form_data}")
        
        # 设置请求参数
        request_kwargs = {
            "data": form_data,
            "headers": headers
        }
        
        # 只有在有代理时才添加代理
        if proxy:
            request_kwargs["proxy"] = proxy
            print(f"   🔍 调试 - 使用代理: {proxy}")
        
        async with session.post(url, **request_kwargs) as response:
            status = response.status
            content = await response.text()
            
            print(f"   🔍 调试 - 响应状态: {status}")
            print(f"   🔍 调试 - 响应内容: {content[:200]}...")
            
            # 如果登录成功，尝试获取profile信息和提交挖矿请求
            token = None
            profile_info = None
            mining_result = None
            
            if status == 200:
                try:
                    response_data = json.loads(content)
                    if "token" in response_data:
                        token = response_data["token"]
                        print(f"   🔑 获取到Token: {token[:20]}...")
                        
                        # 获取profile信息
                        profile_url = "https://api.coinbiten.com/auth/profile"
                        profile_result = await send_profile_request(session, profile_url, token)
                        
                        if profile_result["status"] == 200:
                            try:
                                profile_data = json.loads(profile_result["content"])
                                profile_info = profile_data
                                print(f"   👤 用户信息: {profile_data.get('email', 'N/A')} | UID: {profile_data.get('uid', 'N/A')}")
                            except:
                                print(f"   ⚠️ 解析profile信息失败: {profile_result['content'][:100]}...")
                        else:
                            print(f"   ❌ 获取profile失败: {profile_result['status']}")
                        
                        # 提交挖矿请求
                        mining_url = "https://api.coinbiten.com/auth/miningstart"
                        mining_result = await send_mining_request(session, mining_url, token)
                        
                        if mining_result["status"] == 200:
                            try:
                                mining_data = json.loads(mining_result["content"])
                                print(f"   ⛏️ 挖矿启动成功: {mining_data}")
                            except:
                                print(f"   ⛏️ 挖矿启动成功: {mining_result['content'][:100]}...")
                        else:
                            print(f"   ❌ 挖矿启动失败: {mining_result['status']} - {mining_result['content'][:100]}...")
                            
                except json.JSONDecodeError:
                    print(f"   ⚠️ 解析登录响应失败: {content[:100]}...")
            elif status == 400:
                # 400错误通常是凭据问题
                print(f"   ❌ 登录失败 - 可能是邮箱或密码错误")
            elif status == 401:
                print(f"   ❌ 登录失败 - 认证失败")
            elif status == 403:
                print(f"   ❌ 登录失败 - 访问被拒绝")
            elif status == 429:
                print(f"   ❌ 登录失败 - 请求过于频繁")
            else:
                print(f"   ❌ 登录失败 - HTTP状态码: {status}")
            
            return {
                "email": email,
                "password": password,
                "status": status,
                "content": content,
                "token": token,
                "profile": profile_info,
                "mining": mining_result
            }
    except Exception as e:
        print(f"🔍 调试 - 异常: {type(e).__name__}: {str(e)}")
        return {
            "email": email,
            "password": password,
            "status": None,
            "content": f"Error: {str(e)}",
            "token": None,
            "profile": None,
            "mining": None
        }

async def send_register_batch(url, batch_size=200, use_custom_domain=True, fixed_email=None, available_emails=None, start_index=0):
    async with aiohttp.ClientSession() as session:
        tasks = []
        
        if use_custom_domain or fixed_email:
            # 自定义域名模式或单个固定邮箱模式
            for _ in range(batch_size):
                data = generate_credentials(use_custom_domain, fixed_email)
                tasks.append(send_register_request(session, url, data))
        else:
            # 固定邮箱列表模式
            if available_emails:
                # 计算实际可用的邮箱数量
                remaining_emails = len(available_emails) - start_index
                actual_batch_size = min(batch_size, remaining_emails)
                
                if actual_batch_size <= 0:
                    print("✅ 所有邮箱都已使用完毕")
                    return []
                
                print(f"📧 从第 {start_index + 1} 个邮箱开始，使用 {actual_batch_size} 个邮箱")
                
                for i in range(actual_batch_size):
                    email_index = start_index + i
                    data = generate_credentials(use_custom_domain, fixed_email, available_emails, email_index)
                    tasks.append(send_register_request(session, url, data))
            else:
                print("❌ 没有可用的邮箱地址")
                return []
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results

async def send_login_batch(url, credentials_list, batch_size=50):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(0, len(credentials_list), batch_size):
            batch = credentials_list[i:i+batch_size]
            for cred in batch:
                tasks.append(send_login_request(session, url, cred["email"], cred["password"]))
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results

async def register_main():
    url = "https://api.coinbiten.com/auth/register"
    batch_count = 0
    start_index = 0  # 添加起始索引

    # 检查必要的文件是否存在
    required_files = ['rf.txt', 'domain.txt', 'gmail.txt', 'proxy.txt']
    for file in required_files:
        filepath = os.path.join('config', file)
        if not os.path.exists(filepath):
            print(f"注意: 文件 {filepath} 不存在，将使用默认值")

    # 注册模式选择
    print("\n📝 请选择注册模式:")
    print("1. 🌐 使用自定义域名 (从domain.txt随机选择域名)")
    print("2. 📧 使用固定邮箱 (从gmail.txt随机选择完整邮箱)")
    print("3. 🔧 自定义固定邮箱")
    
    while True:
        try:
            mode_choice = input("请输入选项 (1-3): ").strip()
            
            if mode_choice == "1":
                use_custom_domain = True
                fixed_email = None
                available_emails = None
                print("✅ 已选择: 使用自定义域名模式")
                break
            elif mode_choice == "2":
                use_custom_domain = False
                fixed_email = None
                # 读取所有可用邮箱
                available_emails = get_all_emails_from_file('gmail.txt')
                if not available_emails:
                    print("❌ config/gmail.txt 文件中没有邮箱地址")
                    return
                print(f"✅ 已选择: 使用固定邮箱模式 (从gmail.txt选择，共{len(available_emails)}个邮箱)")
                break
            elif mode_choice == "3":
                use_custom_domain = False
                available_emails = None
                custom_email = input("请输入自定义邮箱地址: ").strip()
                if "@" in custom_email:
                    fixed_email = custom_email
                    print(f"✅ 已选择: 使用自定义邮箱 ({custom_email})")
                    break
                else:
                    print("❌ 邮箱格式不正确，请重新输入")
            else:
                print("❌ 无效选项，请输入 1-3 之间的数字")
        except KeyboardInterrupt:
            print("\n👋 用户取消操作")
            return

    # 设置注册参数
    while True:
        try:
            batch_size = int(input("请输入要注册的账户数量: ").strip())
            if batch_size > 0:
                break
            else:
                print("❌ 注册数量必须大于0")
        except ValueError:
            print("❌ 请输入有效的数字")
        except KeyboardInterrupt:
            print("\n👋 用户取消操作")
            return

    while True:
        try:
            wait_time = int(input("请输入每个账户注册后的等待时间(秒): ").strip())
            if wait_time >= 0:
                break
            else:
                print("❌ 等待时间不能为负数")
        except ValueError:
            print("❌ 请输入有效的数字")
        except KeyboardInterrupt:
            print("\n👋 用户取消操作")
            return

    print(f"🚀 开始注册 {batch_size} 个账户，每次注册后等待 {wait_time} 秒")

    while True:
        try:
            batch_count += 1
            print(f"\n[注册批次 {batch_count}] 发送 {batch_size} 个请求...")
            start_time = time.time()

            results = await send_register_batch(url, batch_size, use_custom_domain, fixed_email, available_emails, start_index)

            if not results:
                print("❌ 没有可用的邮箱地址，注册终止")
                break

            success_count = 0
            for result in results:
                status = result["status"]
                email = result["email"]
                password = result["password"]
                content = result["content"]
                if status == 200:
                    success_count += 1
                    print(f"✅ 注册成功 - 邮箱: {email}, 密码: {password}, 状态: {status}")
                else:
                    print(f"❌ 注册失败 - 邮箱: {email}, 密码: {password}, 状态: {status}, 响应: {content[:100]}...")

            print(f"[注册批次 {batch_count}] 完成: {success_count}/{len(results)} 成功, 耗时: {time.time() - start_time:.2f}秒")

            # 更新起始索引
            start_index += len(results)

            # 检查是否还有更多邮箱可用
            if not use_custom_domain and not fixed_email and available_emails:
                remaining_emails = len(available_emails) - start_index
                if remaining_emails <= 0:
                    print("✅ 所有可用邮箱都已注册完成")
                    break
                else:
                    print(f"📧 还有 {remaining_emails} 个邮箱可用")

            if wait_time > 0:
                print(f"等待 {wait_time} 秒后开始下一批次...")
                await asyncio.sleep(wait_time)
            else:
                print("继续下一批次...")

        except KeyboardInterrupt:
            print("\n用户停止 (Ctrl+C). 退出...")
            break
        except Exception as e:
            print(f"批次 {batch_count} 出错: {e}")
            print("10秒后重试...")
            await asyncio.sleep(10)

async def login_main():
    url = "https://api.coinbiten.com/auth/login"
    
    # 从文件加载注册成功的用户凭据
    credentials = load_credentials()
    
    if not credentials:
        print("❌ 没有可用的登录凭据，请先运行注册功能")
        return
    
    print(f"🔐 开始使用 {len(credentials)} 个用户凭据进行登录测试...")
    start_time = time.time()
    
    # 分批处理登录请求
    batch_size = 10  # 每批10个请求
    results = await send_login_batch(url, credentials, batch_size)
    
    success_count = 0
    failed_count = 0
    
    for result in results:
        status = result["status"]
        email = result["email"]
        password = result["password"]
        content = result["content"]
        token = result.get("token")
        profile = result.get("profile")
        mining = result.get("mining")
        
        if status == 200:
            success_count += 1
            print(f"✅ 登录成功 - 邮箱: {email}, 密码: {password}, 状态: {status}")
            
            # 显示token信息
            if token:
                print(f"   🔑 Token: {token[:30]}...")
            
            # 显示profile信息
            if profile:
                print(f"   👤 用户ID: {profile.get('uid', 'N/A')}")
                print(f"   📧 邮箱: {profile.get('email', 'N/A')}")
                print(f"   🏷️ 用户类型: {profile.get('usertype', 'N/A')}")

            # 显示挖矿结果
            if mining:
                if mining["status"] == 200:
                    try:
                        mining_data = json.loads(mining["content"])
                        print(f"   ⛏️ 挖矿启动成功: {mining_data}")
                    except:
                        print(f"   ⛏️ 挖矿启动成功: {mining['content'][:100]}...")
                else:
                    print(f"   ❌ 挖矿启动失败: {mining['status']} - {mining['content'][:100]}...")
        else:
            failed_count += 1
            print(f"❌ 登录失败 - 邮箱: {email}, 密码: {password}, 状态: {status}")
            if content:
                print(f"   响应: {content[:100]}...")
    
    print(f"\n📊 登录测试完成:")
    print(f"   成功: {success_count} 个")
    print(f"   失败: {failed_count} 个")
    print(f"   总计: {len(credentials)} 个")
    print(f"   耗时: {time.time() - start_time:.2f}秒")

if __name__ == "__main__":
    import sys
    
    def show_menu():
        show_copyright()
        time.sleep(5)
        print("🚀 Coinbiten 自动化工具")
        print("=" * 50)
        print("请选择要执行的操作:")
        print("1. 📝 批量注册用户")
        print("2. 🔐 批量登录测试")
        print("3. 📊 查看已注册用户")
        print("4. 🌐 管理代理IP")
        print("5. ❌ 退出程序")
        print("=" * 50)
    
    def show_registered_users():
        """显示已注册的用户信息"""
        credentials = load_credentials()
        if not credentials:
            print("❌ 还没有注册成功的用户")
            return
        
        print(f"\n📋 已注册用户列表 (共 {len(credentials)} 个):")
        print("-" * 80)
        print(f"{'序号':<4} {'邮箱':<30} {'密码':<20} {'注册时间':<20}")
        print("-" * 80)
        
        for i, cred in enumerate(credentials, 1):
            email = cred["email"]
            password = cred["password"]
            registered_at = cred.get("registered_at", "未知")
            print(f"{i:<4} {email:<30} {password:<20} {registered_at:<20}")
        
        print("-" * 80)
    
    def manage_proxies():
        """管理代理IP"""
        print("\n🌐 代理IP管理")
        print("1. 查看当前代理列表")
        print("2. 添加新代理")
        print("3. 删除代理")
        print("4. 返回主菜单")
        
        while True:
            try:
                choice = input("请选择操作 (1-4): ").strip()
                
                if choice == "1":
                    # 查看代理列表
                    filepath = os.path.join('config', 'proxy.txt')
                    if os.path.exists(filepath):
                        with open(filepath, 'r', encoding='utf-8') as f:
                            proxies = f.readlines()
                        print(f"\n📋 当前代理列表 (共 {len(proxies)} 个):")
                        for i, proxy in enumerate(proxies, 1):
                            print(f"{i}. {proxy.strip()}")
                    else:
                        print("❌ config/proxy.txt 文件不存在")
                    input("\n按回车键继续...")
                    
                elif choice == "2":
                    # 添加新代理
                    new_proxy = input("请输入新代理 (格式: ip:port 或 http://ip:port): ").strip()
                    if new_proxy:
                        if not new_proxy.startswith('http'):
                            new_proxy = f"http://{new_proxy}"
                        
                        filepath = os.path.join('config', 'proxy.txt')
                        with open(filepath, 'a', encoding='utf-8') as f:
                            f.write(f"{new_proxy}\n")
                        print(f"✅ 已添加代理: {new_proxy}")
                    else:
                        print("❌ 代理地址不能为空")
                    input("\n按回车键继续...")
                    
                elif choice == "3":
                    # 删除代理
                    filepath = os.path.join('config', 'proxy.txt')
                    if os.path.exists(filepath):
                        with open(filepath, 'r', encoding='utf-8') as f:
                            proxies = f.readlines()
                        
                        if proxies:
                            print(f"\n📋 当前代理列表:")
                            for i, proxy in enumerate(proxies, 1):
                                print(f"{i}. {proxy.strip()}")
                            
                            try:
                                index = int(input("请输入要删除的代理序号: ")) - 1
                                if 0 <= index < len(proxies):
                                    removed_proxy = proxies.pop(index)
                                    with open(filepath, 'w', encoding='utf-8') as f:
                                        f.writelines(proxies)
                                    print(f"✅ 已删除代理: {removed_proxy.strip()}")
                                else:
                                    print("❌ 无效的序号")
                            except ValueError:
                                print("❌ 请输入有效的数字")
                        else:
                            print("❌ 没有可用的代理")
                    else:
                        print("❌ proxy.txt 文件不存在")
                    input("\n按回车键继续...")
                    
                elif choice == "4":
                    break
                else:
                    print("❌ 无效选项，请输入 1-4 之间的数字")
                    
            except KeyboardInterrupt:
                print("\n👋 用户取消操作")
                break
            except Exception as e:
                print(f"❌ 发生错误: {e}")
                input("按回车键继续...")
    
    while True:
        show_menu()
        
        try:
            choice = input("请输入选项 (1-5): ").strip()
            
            if choice == "1":
                print("\n🚀 启动批量注册功能...")
                asyncio.run(register_main())
                
            elif choice == "2":
                print("\n🔐 启动批量登录功能...")
                asyncio.run(login_main())
                
            elif choice == "3":
                show_registered_users()
                input("\n按回车键返回主菜单...")
                
            elif choice == "4":
                manage_proxies()
                
            elif choice == "5":
                print("\n👋 感谢使用，再见！")
                break
                
            else:
                print("❌ 无效选项，请输入 1-5 之间的数字")
                input("按回车键继续...")
                
        except KeyboardInterrupt:
            print("\n\n👋 程序被用户中断，再见！")
            break
        except Exception as e:
            print(f"\n❌ 发生错误: {e}")
            input("按回车键继续...")
