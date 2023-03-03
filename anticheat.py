process_name = ""
signatures = ""
mode = 1
v = "1.0.0"
scan_delay = 5 

def crc(fileName):
	prev = 0
	for eachLine in open(fileName, "rb"):
		prev = zlib.crc32(eachLine, prev)
	return "%X"%(prev & 0xFFFFFFFF)

import os, subprocess, zlib, time
sigs_path = "./sigs/" +process_name + "_sigs.txt"
sigs_local_path = "./sig.txt"

if mode:
	sigs = subprocess.check_output('listdlls' + process_name).decode("utf-8")
	f = open(sigs_path, 'w')
	f.write(sigs)
	f.close()

	print("Сигнатура процесса" + process_name + " созданы!")


	f = open(sigs_local_path, 'w')
	f.write(sigs)
	f.close()

	while True:
		print("Scan to game...")

		sigs = subprocess.check_output('listdlls' + process_name).decode("utf-8")
		f = open(sigs_local_path, 'w')
		f.write(sigs)
		f.close()

		check = crc(sigs_path) == crc(sigs_local_path)

		if(check):
			print("Сигнатуры совпали, продолжить...")
			time.sleep(scan_delay);
			continue;
		else:
			print("Сигнатуры не совпали, бан!")
			os.system('taskkill /IM' + process_name + ' /F')
			break;
print("Античит завершил работу")


