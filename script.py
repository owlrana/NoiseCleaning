import sys
import os
os.environ["path"] = os.path.dirname(sys.executable) + ";" + os.environ["path"]
import glob
import operator
import re
import datetime
import dateutil.relativedelta
import win32gui
import win32ui
import win32con
import win32api
import numpy
import json
import csv
import urllib.request
import urllib.error
import scipy.ndimage
import scipy.stats
import multiprocessing
import subprocess
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from PIL import Image
from time import strftime
from time import sleep
from operator import itemgetter
from pydub import AudioSegment


###############################################################################
# GLOBAL CONSTANTS
###############################################################################

TEST_FILE = "test.wav" # be sure to change thees in case you want to test on your own system
SILENCE_FILE = "silence.wav"
SILENCE_PROFILE = "silence.prof"
SOX_PATH = '"C:\\Program Files (x86)\\sox-14-4-2\\sox.exe"' # can be changed to whatever the olace you've installed it to

PRINT_LEVEL=2


###############################################################################
# UTILITIES
###############################################################################

def myprint(str, level=0):
	if (level >= PRINT_LEVEL):
		print(str)


		
###############################################################################
# MAIN
###############################################################################
def find_silence(in_file):
	sound1 = AudioSegment.from_file(in_file, format="wav")
	ms = 0
	current_silence = 0
	longuest_time = 500
	longuest_val = None
	for i in sound1:
		if i.dBFS > -38.0:
			length = ms - current_silence
			if length > longuest_time:
				longuest_val = sound1[current_silence : ms]
				longuest_time = length
			current_silence = ms + 1
		ms += 1
	
	myprint("longuest segment " + str(longuest_time / 1000.0) + " seconds", 2)
	longuest_val[200:-200].export(SILENCE_FILE, format="wav")

	
def sox_denoise(in_file):
	
	#sox in.wav noiseprof out.prof
	#sox in.wav out.wav noisered out.prof 0.3
	sound1 = AudioSegment.from_file(SILENCE_FILE, format="wav")
	segment_length_sec = len(sound1) / 1000.0
	command = '{sox} "{wav_in}" -n trim 0 {silence_len} noiseprof {prof_out}'.format(sox=SOX_PATH, wav_in=SILENCE_FILE, silence_len=segment_length_sec, prof_out=SILENCE_PROFILE)
	myprint(command, 0)
	myprint(subprocess.call(command), 1)
	
	out_file = os.path.join(os.path.dirname(in_file), "cleaned", os.path.basename(in_file))
	if not os.path.exists(os.path.dirname(out_file)):
		os.makedirs(os.path.dirname(out_file))
	
	command = '{sox} "{wav_in}" "{wav_out}" noisered {prof_in} 0.3'.format(sox=SOX_PATH, wav_in=in_file, wav_out=out_file, prof_in=SILENCE_PROFILE)
	myprint(command, 0)
	myprint(subprocess.call(command), 1)
		
def cleanup():
	os.remove(SILENCE_FILE)
	os.remove(SILENCE_PROFILE)
	
		
###############################################################################
# MAIN
###############################################################################
		
def do_actions(actions, params):
	file_list = glob.glob(os.path.join(params["root"],"*.wav"))
	count = 1
	for f in file_list:
		myprint("[{}/{}] Processing : {}".format(count, len(file_list), f), 4)
		count += 1
		if "find_silence" in actions:
			find_silence(f)
		if "sox_denoise" in actions:
			sox_denoise(f)
	if "cleanup" in actions:
		cleanup()
		
		
if __name__ == '__main__':
	actions = [
		"find_silence",
		"sox_denoise",
		"cleanup",
		"nothing" # just so I don't need to play with the last ,
	]
	params = {
		"root" : sys.argv[1],
		#"root" : ".",
		"nothing" : None # don't have to deal with last ,
	}
	do_actions(actions, params)
	
	sys.exit(0)