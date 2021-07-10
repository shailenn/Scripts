import logging
import os
import traceback
from random import choice
from time import sleep

import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox, FirefoxProfile
from selenium.webdriver.firefox.options import Options

logger = logging.getLogger(__name__)

import socket

proxies = {}
proxy_supplier = []

socket.setdefaulttimeout(120)


logging.basicConfig(filename="email.txt", level=logging.INFO)


def load_proxy():
	proxylist = os.scandir('proxies/')
	for i in proxylist:
		proxies[i.name] = False


def load_proxy_supply():
	if os.path.exists('proxysupply.txt'):
		with open('proxysupply.txt', encoding='utf-8') as f:
			for line in f:
				if line.strip():
					proxy_supplier.append(line.strip())


def get(url, proxy=None):
	if proxy is not None:
		ip, port, protocol = proxy.split(',')
		proxy = {
			'https': f'socks{protocol}://{ip}:{port}',
			'http': f'socks{protocol}://{ip}:{port}',
		}

	r = requests.get(
		url,
		proxies=proxy,
		headers={
			'User-Agent':
				'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
		})

	return r


def test_proxy(proxy):
	if not proxy:
		return
	# r = get('https://www.google.com/', proxy)
	ip, port, version = proxy.split(',')
	print(f'Checking proxy {ip}:{port}')
	options = Options()
	options.headless = True
	profile = FirefoxProfile()
	profile.set_preference('network.proxy.type', 1)
	profile.set_preference("network.proxy.socks", ip)
	profile.set_preference("network.proxy.socks_port", int(port))
	profile.set_preference("network.proxy.socks_version", int(version))
	profile.update_preferences()
	browser = Firefox(executable_path=r"./geckodriver",firefox_profile=profile, options=options)
	try:
		browser.get('https://showip.net/')
		soup = BeautifulSoup(browser.page_source, 'html.parser')
		return soup.select_one('#checkip').get('value').strip() == proxy.split(
			',')[0].strip()
	except KeyboardInterrupt:
		raise KeyboardInterrupt('Abort')
	except:
		logging.error(traceback.format_exc())
	finally:
		browser.quit()


def _get_sock_proxy_net(driver):
	'''Get proxy from https://www.socks-proxy.net/'''
	driver.get('https://www.socks-proxy.net/')
	soup = BeautifulSoup(driver.page_source, 'html.parser')
	count = 0
	while count < 5:
		row = choice(
			[x for x in soup.select('#proxylisttable_wrapper tbody tr')])
		ip, port, _, _, protocol, _, _, _ = [
			x.text.strip() for x in row.select('td')
		]
		r = f"{ip},{port},{protocol.lower().replace('socks', '')}"
		if r in proxies:
			count += 1
		else:
			return r


def _get_premproxy_com(driver):
	'''Get proxy from https://premproxy.com/socks-list/'''
	driver.get('https://premproxy.com/socks-list/')
	soup = BeautifulSoup(driver.page_source, 'html.parser')
	count = 0
	while count < 5:
		row = choice([x for x in soup.select('#proxylistt tbody tr')])
		ip_port, protocol, _, _, _, _ = [
			x.text.strip() for x in row.select('td')
		]
		ip, port = [x.strip() for x in ip_port.split(':')]
		r = f"{ip},{port},{protocol.lower().replace('socks', '')}"
		if r in proxies:
			count += 1
		else:
			return r


def _get_sockslist_net(driver):
	'''Get proxy from https://sockslist.net/list/proxy-socks-5-list/'''
	driver.get('https://sockslist.net/list/proxy-socks-5-list/')
	soup = BeautifulSoup(driver.page_source, 'html.parser')
	count = 0
	while count < 5:
		row = choice([x for x in soup.select('.proxytbl tbody tr')])
		ip, port, _, protocol, _, _ = [
			x.text.strip() for x in row.select('td')
		]
		port = port.split('\n')[-1].strip()
		r = f"{ip},{port},{protocol.lower().replace('socks', '')}"
		if r in proxies:
			count += 1
		else:
			return r


def _get_my_proxy_com():
	'''Get proxy from https://www.my-proxy.com/free-socks-5-proxy.html'''
	r = get('https://www.my-proxy.com/free-socks-5-proxy.html')
	soup = BeautifulSoup(r.text, 'html.parser')
	count = 0
	while count < 5:
		row = choice([
			x.strip()
			for x in soup.select_one('div.list').text.strip().split('\n')
		])
		ip, port = row.split('#')[0].split(':')
		if f"{ip},{port},5" in proxies:
			count += 1
		else:
			return f"{ip},{port},5"


def get_random_proxy(supplier, driver):
	print(f'Getting random proxy from {supplier}')
	if 'socks-proxy.net' in supplier:
		return _get_sock_proxy_net(driver)
	elif 'premproxy.com/socks-list' in supplier:
		return _get_premproxy_com(driver)
	elif 'my-proxy.com' in supplier:
		return _get_my_proxy_com()
	elif 'sockslist.net' in supplier:
		return _get_sockslist_net(driver)


def main():
	options = Options()
	options.headless = True
	driver = Firefox(executable_path=r"./geckodriver",options=options)
	sleep(3)
	load_proxy()
	load_proxy_supply()
	# Run every 3 minutes
	while True:
		try:
			ok_proxies_count = sum([1 for x in proxies.values() if x])
			if ok_proxies_count >= 10:
				driver.quit()
				return
			not_checked_proxies = [x for x in proxies.keys() if not proxies[x]]
			if not_checked_proxies:
				proxy = not_checked_proxies[0]
			else:
				supplier = choice(proxy_supplier)
				proxy = get_random_proxy(supplier, driver)

			if test_proxy(proxy):
				print(f'{proxy}: OK')
				proxies[proxy] = True
				print("%s is working" % (proxy))
				ip, port, version = proxy.split(',')
				with open('proxies/' + str(ip) + "," +  str(port) + "," + str(version), 'w', encoding='utf-8') as f:
					f.write('\n')
			else:
				print(f'{proxy} is not working, removing it!')
				if os.path.exists("proxies/" + proxy):
					os.remove("proxies/" + proxy)
				proxies.pop(proxy, None)

			sleep(1)
		except KeyboardInterrupt:
			break
		except:
			sleep(1)
			logging.error(traceback.format_exc())
	driver.quit()
	# with open('proxy.txt', 'w', encoding='utf-8') as f:
	#     f.write('\n'.join(proxies.keys()))


if __name__ == "__main__":
	main()
