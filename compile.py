import os

references = [
	'dependencies\\lib\\sfmlnet-audio-2.dll',
	'dependencies\\lib\\sfmlnet-graphics-2.dll',
	'dependencies\\lib\\sfmlnet-system-2.dll',
	'dependencies\\lib\\sfmlnet-window-2.dll'
]

src = 'src\\*.cs'
lib = 'dependencies\\extlibs\\'
out = 'out\\BattleShipsClient.exe'
csc = 'C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\MSBuild\\15.0\\Bin\\Roslyn\\csc.exe'

compilerArgs = [
	'-out:' + out,
	'-lib:' + lib,
	'-reference:' + ','.join(references),
	'-langversion:7',
	'-platform:x64'
]

commands = [
	' '.join(['"' + csc + '"', src, ' '.join(compilerArgs)]),
	'xcopy res out\\res\\ /s /e',
	'xcopy dependencies\\extlibs out\\ /s /e',
	'xcopy dependencies\\lib out\\ /s /e'
]

for cmd in commands:
	os.system(cmd)
