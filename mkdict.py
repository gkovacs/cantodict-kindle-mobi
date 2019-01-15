#!/usr/bin/env python3
# coding: utf8

from memoize import memoize
from copy import copy
import dragonmapper
import dragonmapper.transcriptions

@memoize
def pinyin_to_zhuyin(pinyin):
  mappings = {
    'yo1': 'ㄧㄛ',
    'yo2': 'ㄧㄛˊ',
    'yo3': 'ㄧㄛˇ',
    'yo4': 'ㄧㄛˋ',
    'yo5': 'ㄧㄛ˙',
    'o1': 'ㄛ',
    'o2': 'ㄛˊ',
    'o3': 'ㄛˇ',
    'o4': 'ㄛˋ',
    'o5': 'ㄛ˙',
    'O1': 'ㄛ',
    'O2': 'ㄛˊ',
    'O3': 'ㄛˇ',
    'O4': 'ㄛˋ',
    'O5': 'ㄛ˙',
    'dia1': 'ㄉㄧㄚ',
    'dia2': 'ㄉㄧㄚˊ',
    'dia3': 'ㄉㄧㄚˇ',
    'dia4': 'ㄉㄧㄚˋ',
    'dia5': 'ㄉㄧㄚ˙',
    'tei1': 'ㄊㄟ',
    'tei2': 'ㄊㄟˊ',
    'tei3': 'ㄊㄟˇ',
    'tei4': 'ㄊㄟˋ',
    'tei5': 'ㄊㄟ˙',
    'eng1': 'ㄥ',
    'eng2': 'ㄥˊ',
    'eng3': 'ㄥˇ',
    'eng4': 'ㄥˋ',
    'eng5': 'ㄥ˙',
  }
  if pinyin in mappings:
    return mappings[pinyin]
  for k,v in mappings.items():
    if (' ' + k) in pinyin:
      return pinyin_to_zhuyin(pinyin.replace(' ' + k, ' ' + v))
  for k,v in mappings.items():
    if pinyin.startswith(k + ' '):
      return pinyin_to_zhuyin(pinyin.replace(k + ' ', v + ' ', 1))
  if 'u:' in pinyin:
    return pinyin_to_zhuyin(pinyin.replace('u:', 'ü'))
  if pinyin.startswith('o '):
    return 'o ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('c '):
    return 'c ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('X '):
    return 'X ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('O '):
    return 'O ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('O '):
    return 'O ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.endswith(' K'):
    return pinyin_to_zhuyin(pinyin[:len(pinyin) - 2]) + ' K'
  if pinyin.endswith(' O'):
    return pinyin_to_zhuyin(pinyin[:len(pinyin) - 2]) + ' O'
  return dragonmapper.transcriptions.pinyin_to_zhuyin(pinyin)

@memoize
def get_cedict_lines():
  return open('cedict_1_0_ts_utf-8_mdbg.txt').readlines()

@memoize
def get_cantodict_lines():
  return open('cccanto-webdist.txt').readlines()

@memoize
def get_cedict_readings_lines():
  return open('cccedict-canto-readings.txt').readlines()

@memoize
def get_trad_to_pinyin_to_yuepin():
  output = {}
  for entry in get_cantodict_entries():
    trad = entry['trad']
    pin = entry['pin']
    yue = entry['yue']
    if trad not in output:
      output[trad] = {}
    if pin not in output[trad]:
      output[trad][pin] = yue
  for entry in get_cedict_readings_entries():
    trad = entry['trad']
    pin = entry['pin']
    yue = entry['yue']
    if trad not in output:
      output[trad] = {}
    if pin not in output[trad]:
      output[trad][pin] = yue
  return output

@memoize
def get_trad_to_yuepin():
  output = {}
  for entry in get_cantodict_entries():
    trad = entry['trad']
    yue = entry['yue']
    if trad not in output:
      output[trad] = yue
  for entry in get_cedict_readings_entries():
    trad = entry['trad']
    yue = entry['yue']
    if trad not in output:
      output[trad] = yue
  return output

def get_entry_from_cantodict_line(line):
  simp_start = line.index(' ')
  trad = line[:simp_start]
  simp_end = line.index(' ', simp_start + 1)
  simp = line[simp_start + 1 : simp_end]
  pinyin_start = line.index('[', simp_end + 1)
  pinyin_end = line.index(']', pinyin_start + 1)
  pinyin = line[pinyin_start + 1 : pinyin_end]
  yuepin_start = line.index('{', pinyin_end + 1)
  yuepin_end = line.index('}', yuepin_start + 1)
  yuepin = line[yuepin_start + 1 : yuepin_end]
  definitions = []
  if '/' in line:
    def_start = line.index('/', yuepin_end + 1)
    definition_text = line[def_start + 1 :]
    definitions = definition_text.split('/')
    definitions = [x.strip() for x in definitions]
    definitions = [x for x in definitions if x != '']
  entry = {
    'simp': simp,
    'trad': trad,
    'pin': pinyin,
    'yue': yuepin,
    'def': definitions,
  }
  return entry

def get_entry_from_cedict_line(line):
  simp_start = line.index(' ')
  trad = line[:simp_start]
  simp_end = line.index(' ', simp_start + 1)
  simp = line[simp_start + 1 : simp_end]
  pinyin_start = line.index('[', simp_end + 1)
  pinyin_end = line.index(']', pinyin_start + 1)
  pinyin = line[pinyin_start + 1 : pinyin_end]
  def_start = line.index('/', pinyin_end + 1)
  definition_text = line[def_start + 1 :]
  definitions = definition_text.split('/')
  definitions = [x.strip() for x in definitions]
  definitions = [x for x in definitions if x != '']
  entry = {
    'simp': simp,
    'trad': trad,
    'pin': pinyin,
    'def': definitions,
  }
  return entry

def get_yuepin(entry):
  trad = entry['trad']
  pin = entry['pin']
  trad_to_pinyin_to_yuepin = get_trad_to_pinyin_to_yuepin()
  if trad in trad_to_pinyin_to_yuepin and pin in trad_to_pinyin_to_yuepin[trad]:
    return trad_to_pinyin_to_yuepin[trad][pin]
  trad_to_yuepin = get_trad_to_yuepin()
  if trad in trad_to_yuepin:
    return trad_to_yuepin[trad]
  return None

@memoize
def get_cedict_entries():
  output = []
  cedict_lines = get_cedict_lines()
  for line in cedict_lines:
    line = line.strip()
    if line.startswith('#'):
      continue
    if '[' not in line:
      continue
    entry = get_entry_from_cedict_line(line)
    output.append(entry)
  return output

@memoize
def get_cantodict_entries():
  output = []
  cantodict_lines = get_cantodict_lines()
  for line in cantodict_lines:
    line = line.strip()
    if line.startswith('#'):
      continue
    if '[' not in line:
      continue
    entry = get_entry_from_cantodict_line(line)
    output.append(entry)
  return output

@memoize
def get_cedict_readings_entries():
  output = []
  cedict_readings_lines = get_cedict_readings_lines()
  for line in cedict_readings_lines:
    line = line.strip()
    if line.startswith('#'):
      continue
    if '[' not in line:
      continue
    entry = get_entry_from_cantodict_line(line)
    output.append(entry)
  return output

@memoize
def get_merged_entries():
  output = []
  for entry in get_cedict_entries():
    entry = copy(entry)
    entry['yue'] = get_yuepin(entry)
    entry['zhu'] = pinyin_to_zhuyin(entry['pin'])
    output.append(entry)
  for entry in get_cantodict_entries():
    entry = copy(entry)
    entry['zhu'] = pinyin_to_zhuyin(entry['pin'])
    output.append(entry)
  return output

def make_stardict_lines():
  output = []
  output_set = set()
  for entry in get_merged_entries():
    trad = entry['trad']
    simp = entry['simp']
    pin = entry['pin']
    yue = entry['yue']
    zhu = entry['zhu']
    definitions = entry['def']
    line = trad + '\t' + simp + ' ' + zhu + '\\n' + ('\\n'.join(definitions))
    if yue != None:
      line = trad + '\t' + simp + ' ' + zhu + ' ' + yue + '\\n' + ('\\n'.join(definitions))
    if trad in output_set:
      continue
    output_set.add(trad)
    output.append(line)
    if trad == simp:
      continue
    line = simp + '\t' + trad + ' ' + zhu + '\\n' + ('\\n'.join(definitions))
    if yue != None:
      line = simp + '\t' + trad + ' ' + zhu + ' ' + yue + '\\n' + ('\\n'.join(definitions))
    if simp in output_set:
      continue
    output_set.add(simp)
    output.append(line)
  return output

test_line = 'U盤 U盘 [U pan2] /USB flash drive/see also 閃存盤|闪存盘[shan3 cun2 pan2]/'
#print(get_entry_from_cedict_line(test_line))
test_line2 = '臺中 台中 [Tai2 zhong1] /Taizhong or Taichung city in central Taiwan/'
test_line2_entry = get_entry_from_cedict_line(test_line2)
#print(get_yuepin(test_line2_entry))
#print(make_stardict_lines()[1000])
for line in make_stardict_lines():
  print(line)
