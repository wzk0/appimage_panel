import os
import getpass
import json

data_json='/home/%s/.appimage_py.json'%getpass.getuser()
right_name=['appimage','Appimage','AppImage','APPimage','APPImage']

def check(path=''):
	os.system('touch '+data_json) if not os.path.exists(data_json) else print('\n当前库中应用: \033[1;32m%s\033[0m个\n'%len(read_from_json()))
	appimage_path_not_clear=[]
	for root, dirs, files in os.walk('/' if path=='' else path):
		[appimage_path_not_clear.append(os.path.join(root,name)) for name in files if name.split('.')[-1] in right_name]
		[appimage_path_not_clear.append(os.path.join(root,name)) for name in dirs if name.split('.')[-1] in right_name]
	appimage_path=[]
	[appimage_path.append(appimage) for appimage in appimage_path_not_clear if appimage not in appimage_path]
	os.system('clear')
	print('共\033[1;32m%s\033[0m个扫描结果, 如下(<\033[1;32m路径\033[0m> │ [\033[1;34m应用\033[0m]):\n'%len(appimage_path))
	[print('<\033[1;32m'+'/'.join(appimage.split('/')[:-1])+'\033[0m> │ [\033[1;34m'+'.'.join(appimage.split('/')[-1].split('.')[:-1])+'\033[0m]') for appimage in appimage_path]
	write_in_json(appimage_path) if input('\n是/否(y/n)保存此结果:')=='y' else print('\nOK')
	os.system('clear')
	return appimage_path

def write_in_json(appimage_path):
	appimage_data=[]
	[appimage_data.append({'short_name':'.'.join(appimage.split('/')[-1].split('.')[:-1]),'path':appimage}) for appimage in appimage_path]
	with open(data_json,'w')as f:
		f.write(json.dumps(appimage_data,ensure_ascii=False))

def read_from_json():
	with open(data_json,'r')as f:
		return json.loads(f.read())

def start_from_json(appimage_path):
	print('\n当前库中应用(蓝色为可用, 红色为不存在的文件): \033[1;32m%s\033[0m个\n'%len(read_from_json()))
	for appimage in appimage_path:
		if os.path.exists(appimage['path']):
			print('\033[1;32m%s\033[0m. \033[1;34m'%appimage_path.index(appimage)+appimage['short_name']+'\033[0m') 
		else:
			print('\033[1;32m%s\033[0m. \033[1;31m'%appimage_path.index(appimage)+appimage['short_name']+'\033[0m')
	path=appimage_path[int(input('\n请输入序号:'))]['path']
	other=input('请输入参数(没有请回车):')
	print('应用完整路径: \033[1;32m%s\033[0m - [将在3秒后启动]'%path)
	os.system('sleep 3 && %s %s'%(path,other))
	os.system('chmod +x %s && %s'%(path,path)) if input('若启动失败, 可能是文件或其软链接失效或没有执行权限, 是/否(y/n)给予权限并重试[成功运行请忽略]:')=='y' else print('\nOK')

def remove_from_json(appimage_path):
	print('\n当前库中应用: \033[1;32m%s\033[0m个\n'%len(read_from_json()))
	[print('\033[1;32m%s\033[0m. \033[1;34m'%appimage_path.index(appimage)+appimage['short_name']+'\033[0m') for appimage in appimage_path]
	remove_path=[]
	[remove_path.append(appimage_path[int(path_id)]) for path_id in input('\n请输入要移除的应用序号, 多个序号可用空格分开:').split(' ')]
	[appimage_path.remove(re) for re in remove_path]
	print('\n新列表如下, 共\033[1;32m%s\033[0m个应用\n'%len(appimage_path))
	[print('\033[1;32m%s\033[0m. \033[1;34m'%appimage_path.index(appimage)+appimage['short_name']+'\033[0m') for appimage in appimage_path]
	with open(data_json,'w')as f:
		f.write(json.dumps(appimage_path,ensure_ascii=False))

def remove_from_disk(appimage_path):
	print('\n当前库中应用: \033[1;32m%s\033[0m个\n'%len(read_from_json()))
	[print('\033[1;32m%s\033[0m. \033[1;34m'%appimage_path.index(appimage)+appimage['short_name']+'\033[0m') for appimage in appimage_path]
	remove_path=[]
	[remove_path.append(appimage_path[int(path_id)]) for path_id in input('\n请输入要移除的应用序号, 多个序号可用空格分开:').split(' ')]
	print('\n要从硬盘中删除的应用与要执行的指令如下, 共\033[1;32m%s\033[0m个\n'%len(remove_path))
	[print('\033[1;32m%s\033[0m. \033[1;34m'%remove_path.index(re)+re['short_name']+'\033[0m') for re in remove_path]
	[print('\033[1;31mrm %s\033[0m'%re['path']) for re in remove_path]
	if input('\n请输入y以确认执行:')=='y':
		[os.system('rm %s'%re['path']) for re in remove_path]

def main():
	check(input('检测到这是你第一次运行程序, 请输入扫描路径(或回车扫描全盘, 消耗时间较长):')) if not os.path.exists(data_json) else print('当前库中应用: \033[1;32m%s\033[0m个\n'%len(read_from_json()))
	menu=['扫描','启动','移除','删除']
	[print(str(menu.index(mode))+'. '+mode) for mode in menu]
	mode=input('\n请输入模式:')
	check(input('\n请输入路径(或回车扫描全盘, 消耗时间较长):')) if mode=='0' else (start_from_json(read_from_json()) if mode=='1' else ( remove_from_json(read_from_json()) if mode=='2' else (remove_from_disk(read_from_json()) if mode=='3' else print('\nOK')) ))

main()