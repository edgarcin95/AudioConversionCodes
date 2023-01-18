#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 16:21:20 2021

@author: edgarcin95
"""

import os

BD48KHz_path='/media/edgarcin95/HDDextra/Bases_de_datos_Tesis/BD_48_KHz/You_really_got_a_hold_on_me'
BD44100Hz_path = '/home/edgarcin95/Tesis/BD441000HzffmpegConvert/You_really_got_a_hold_on_me'

WAVs = os.listdir(BD48KHz_path)

#convert mp3 --> wav
for w in WAVs:
    orig = os.path.join(BD48KHz_path, w)
    new = os.path.join(BD44100Hz_path, w)
    
    if os.path.exists(new) is False:
        os.system('ffmpeg -i {} -acodec pcm_s24le -ar 44100 {}'\
                  .format(orig, new))