#!/usr/bin/env python3
# coding: utf8

from memoize import memoize
from copy import copy
import dragonmapper
import dragonmapper.transcriptions

import sys

@memoize
def get_chars_to_remove():
  return [
    '…',
    '!',
    '?',
    '！',
    '？',
  ]

@memoize
def get_leave_unchanged_transcription():
  return set([
    'A C G',
    'P',
    'G',
    'C G',
    'S',
    'K',
    'Q',
    'T',
    'R',
    'c o s',
    'xx',
    'xx5',
    'B',
    '·',
    'M',
    'X',
    'L',
    'biū',
    'gīng',
    'm',
    'mˊ',
    'mˇ',
    'mˋ',
    'm˙',
    'V',
    'nˊ',
    'nˇ',
    'nˋ',
    'n˙',
    '…',
    '',
    'g',
    'w',
    't',
    'D',
    'f',
    'l',
    'k',
    'p',
    'w5',
    'Y5',
    'h5',
    'b',
    'n',
    'd',
    's',
    'QQ',
  ])

@memoize
def pinyin_to_zhuyin_fake(pinyin):
  leave_unchanged = get_leave_unchanged_transcription()
  if pinyin in leave_unchanged:
    return pinyin
  mappings = {
    'biu1': 'biū',
    'ging1': 'gīng',
    'm1': 'm',
    'm2': 'mˊ',
    'm3': 'mˇ',
    'm4': 'mˋ',
    'm5': 'm˙',
    'fiao1': 'fiāo',
    'fiao2': 'fiáo',
    'fiao3': 'fiǎo',
    'fiao4': 'fiào',
    'fiao5': 'fiao',
    'n1': 'n',
    'n2': 'nˊ',
    'n3': 'nˇ',
    'n4': 'nˋ',
    'n5': 'n˙',
    'g5?': 'g',
    'g5': 'g',
    'p5': 'p',
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
  if pinyin.startswith('A '):
    return 'A ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('B '):
    return 'B ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('C '):
    return 'C ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('G '):
    return 'G ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('P '):
    return 'P ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('D '):
    return 'D ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('N '):
    return 'N ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('H '):
    return 'H ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('K '):
    return 'K ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('k '):
    return 'k ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('M '):
    return 'M ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('S '):
    return 'S ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('Q '):
    return 'Q ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('T '):
    return 'T ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('U '):
    return 'U ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('V '):
    return 'V ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.endswith(' K'):
    return pinyin_to_zhuyin(pinyin[:len(pinyin) - 2]) + ' K'
  if pinyin.endswith(' O'):
    return pinyin_to_zhuyin(pinyin[:len(pinyin) - 2]) + ' O'
  if pinyin.endswith(' C'):
    return pinyin_to_zhuyin(pinyin[:len(pinyin) - 2]) + ' C'
  if pinyin.endswith(' P'):
    return pinyin_to_zhuyin(pinyin[:len(pinyin) - 2]) + ' P'
  if pinyin.endswith(' Q'):
    return pinyin_to_zhuyin(pinyin[:len(pinyin) - 2]) + ' Q'
  if ' ' in pinyin:
    return ' '.join([pinyin_to_zhuyin(x) for x in pinyin.split(' ')])
  for x in get_chars_to_remove():
    pinyin = pinyin.replace(x, '')
  return dragonmapper.transcriptions.to_pinyin(pinyin)

@memoize
def pinyin_to_zhuyin_real(pinyin):
  leave_unchanged = get_leave_unchanged_transcription()
  if pinyin in leave_unchanged:
    return pinyin
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
    'ging1': 'ㄍㄧㄥ',
    'biu1': 'ㄅㄧㄨ',
    'm1': 'ㄇ',
    'm2': 'ㄇˊ',
    'm3': 'ㄇˇ',
    'm4': 'ㄇˋ',
    'm5': 'ㄇ˙',
    'fiao1': 'ㄈㄧㄠ',
    'fiao2': 'ㄈㄧㄠˊ',
    'fiao3': 'ㄈㄧㄠˇ',
    'fiao4': 'ㄈㄧㄠˋ',
    'fiao5': 'ㄈㄧㄠ˙',
    'n1': 'ㄋ',
    'n2': 'ㄋˊ',
    'n3': 'ㄋˇ',
    'n4': 'ㄋˋ',
    'n5': 'ㄋ˙',
    'g5?': 'ㄍ˙',
    'g5': 'ㄍ˙',
    'p5': 'ㄆ˙',
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
  if pinyin.startswith('A '):
    return 'A ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('B '):
    return 'B ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('C '):
    return 'C ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('G '):
    return 'G ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('P '):
    return 'P ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('D '):
    return 'D ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('N '):
    return 'N ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('H '):
    return 'H ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('K '):
    return 'K ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('k '):
    return 'k ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('M '):
    return 'M ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('S '):
    return 'S ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('Q '):
    return 'Q ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('T '):
    return 'T ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('U '):
    return 'U ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.startswith('V '):
    return 'V ' + pinyin_to_zhuyin(pinyin[2:])
  if pinyin.endswith(' K'):
    return pinyin_to_zhuyin(pinyin[:len(pinyin) - 2]) + ' K'
  if pinyin.endswith(' O'):
    return pinyin_to_zhuyin(pinyin[:len(pinyin) - 2]) + ' O'
  if pinyin.endswith(' C'):
    return pinyin_to_zhuyin(pinyin[:len(pinyin) - 2]) + ' C'
  if pinyin.endswith(' P'):
    return pinyin_to_zhuyin(pinyin[:len(pinyin) - 2]) + ' P'
  if pinyin.endswith(' Q'):
    return pinyin_to_zhuyin(pinyin[:len(pinyin) - 2]) + ' Q'
  if ' ' in pinyin:
    return ' '.join([pinyin_to_zhuyin(x) for x in pinyin.split(' ')])
  for x in get_chars_to_remove():
    pinyin = pinyin.replace(x, '')
  return dragonmapper.transcriptions.pinyin_to_zhuyin(pinyin)

if len(sys.argv) > 1 and sys.argv[1] == 'zhuyin':
  pinyin_to_zhuyin = pinyin_to_zhuyin_real
else:
  pinyin_to_zhuyin = pinyin_to_zhuyin_fake

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

def merge_lists(list1, list2):
  list1_items = set(list1)
  output = []
  for item in list1:
    output.append(item)
  for item in list2:
    if item not in list1_items:
      output.append(item)
  return output

def prepend_text_to_each_item_of_second_list_and_merge(list1, list2, text):
  output = []
  for item in list1:
    output.append(item)
  for item in list2:
    item = text + ' ' + item
    output.append(item)
  return output

@memoize
def get_char_to_all_yue():
  output = {}
  for entry in get_merged_entries():
    trad = entry['trad']
    simp = entry['simp']
    if 'yue' not in entry:
      continue
    yue = entry['yue']
    if yue == None:
      continue
    if trad not in output:
      output[trad] = []
    if simp not in output:
      output[simp] = []
    if yue not in output[trad]:
      output[trad].append(yue)
    if yue not in output[simp]:
      output[simp].append(yue)
  return output

@memoize
def get_char_to_all_zhu():
  output = {}
  for entry in get_merged_entries():
    trad = entry['trad']
    simp = entry['simp']
    if 'zhu' not in entry:
      continue
    yue = entry['zhu']
    if yue == None:
      continue
    if trad not in output:
      output[trad] = []
    if simp not in output:
      output[simp] = []
    if yue not in output[trad]:
      output[trad].append(yue)
    if yue not in output[simp]:
      output[simp].append(yue)
  return output

def get_all_yue(simp):
  char_to_all_yue = get_char_to_all_yue()
  if simp in char_to_all_yue:
    return char_to_all_yue[simp]
  return []

def has_multiple_yue(simp):
  return len(get_all_yue(simp)) > 1

def get_all_zhu(simp):
  char_to_all_zhu = get_char_to_all_zhu()
  if simp in char_to_all_zhu:
    return char_to_all_zhu[simp]
  return []

def has_multiple_zhu(simp):
  return len(get_all_zhu(simp)) > 1

def merge_entries(entry1, entry2):
  output = copy(entry1)
  if entry1['pin'] == None and entry2['pin'] != None:
    output['pin'] = entry2['pin']
  if entry1['zhu'] == None and entry2['zhu'] != None:
    output['zhu'] = entry2['zhu']
  if entry1['yue'] == None and entry2['yue'] != None:
    output['yue'] = entry2['yue']
  if entry1['trad'] == None and entry2['trad'] != None:
    output['trad'] = entry2['trad']
  if entry1['simp'] == None and entry2['simp'] != None:
    output['simp'] = entry2['simp']
  definitions1 = entry1['def']
  definitions2 = entry2['def']
  zhu1 = entry1['zhu']
  zhu2 = entry2['zhu']
  yue1 = entry1['yue']
  yue2 = entry2['yue']
  defs = []
  if (zhu1 == zhu2) and (yue1 != yue2) and has_multiple_yue(output['simp']) and (yue2 != None):
    defs = prepend_text_to_each_item_of_second_list_and_merge(definitions1, definitions2, yue2)
  elif (zhu1 != zhu2) and (yue1 == yue2) and has_multiple_zhu(output['simp']) and (zhu2 != None):
    defs = prepend_text_to_each_item_of_second_list_and_merge(definitions1, definitions2, zhu2)
  elif (zhu1 != zhu2) and (yue1 != yue2) and (has_multiple_yue(output['simp']) or has_multiple_zhu(output['simp'])) and (zhu2 != None) and (yue2 != None):
    defs = prepend_text_to_each_item_of_second_list_and_merge(definitions1, definitions2, zhu2 + ' ' + yue2)
  else:
    defs = merge_lists(definitions1, definitions2)
  output['def'] = defs
  return output

@memoize
def get_stardict_items():
  output_dict = {}
  for entry in get_merged_entries():
    trad = entry['trad']
    simp = entry['simp']
    pin = entry['pin']
    yue = entry['yue']
    zhu = entry['zhu']
    definitions = entry['def']
    if trad == simp:
      if trad in output_dict:
        output_dict[trad] = {'key': trad, 'entry': merge_entries(output_dict[trad]['entry'], entry)}
      else:
        output_dict[trad] = {'key': trad, 'entry': entry}
    else:
      if trad in output_dict:
        output_dict[trad] = {'key': trad, 'entry': merge_entries(output_dict[trad]['entry'], entry)}
      else:
        output_dict[trad] = {'key': trad, 'entry': entry}
      if simp in output_dict:
        output_dict[simp] = {'key': simp, 'entry': merge_entries(output_dict[simp]['entry'], entry)}
      else:
        output_dict[simp] = {'key': simp, 'entry': entry}
  output = []
  for k in sorted(output_dict.keys()):
    output.append(output_dict[k])
  return output

def make_stardict_lines():
  output = []
  for item in get_stardict_items():
    key = item['key']
    entry = item['entry']
    trad = entry['trad']
    simp = entry['simp']
    pin = entry['pin']
    yue = entry['yue']
    zhu = entry['zhu']
    definitions = entry['def']
    if key == simp and key == trad:
      line = key + '\t' + zhu + '\\n' + ('\\n'.join(definitions))
      if yue != None:
        line = key + '\t' + zhu + ' ' + yue + '\\n' + ('\\n'.join(definitions))
    elif key == simp and key != trad:
      line = key + '\t' + trad + ' ' + zhu + '\\n' + ('\\n'.join(definitions))
      if yue != None:
        line = key + '\t' + trad + ' ' + zhu + ' ' + yue + '\\n' + ('\\n'.join(definitions))
    elif key == trad and key != simp:
      line = key + '\t' + simp + ' ' + zhu + '\\n' + ('\\n'.join(definitions))
      if yue != None:
        line = key + '\t' + simp + ' ' + zhu + ' ' + yue + '\\n' + ('\\n'.join(definitions))
    output.append(line)
  return output

'''
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
    if trad == simp:
      if trad in output_set:
        continue
      output_set.add(trad)
      line = trad + '\t' + zhu + '\\n' + ('\\n'.join(definitions))
      if yue != None:
        line = trad + '\t' + zhu + ' ' + yue + '\\n' + ('\\n'.join(definitions))
      output.append(line)
      continue
    line = trad + '\t' + simp + ' ' + zhu + '\\n' + ('\\n'.join(definitions))
    if yue != None:
      line = trad + '\t' + simp + ' ' + zhu + ' ' + yue + '\\n' + ('\\n'.join(definitions))
    if trad in output_set:
      continue
    output_set.add(trad)
    output.append(line)
    line = simp + '\t' + trad + ' ' + zhu + '\\n' + ('\\n'.join(definitions))
    if yue != None:
      line = simp + '\t' + trad + ' ' + zhu + ' ' + yue + '\\n' + ('\\n'.join(definitions))
    if simp in output_set:
      continue
    output_set.add(simp)
    output.append(line)
  return output
'''

def run_tests():
  test_line = 'U盤 U盘 [U pan2] /USB flash drive/see also 閃存盤|闪存盘[shan3 cun2 pan2]/'
  #print(get_entry_from_cedict_line(test_line))
  test_line2 = '臺中 台中 [Tai2 zhong1] /Taizhong or Taichung city in central Taiwan/'
  test_line2_entry = get_entry_from_cedict_line(test_line2)
  #print(get_yuepin(test_line2_entry))
  #print(make_stardict_lines()[1000])
  #print(get_all_yue('戏'))
  print(get_all_yue('觉'))

def main():
  for line in make_stardict_lines():
    print(line)

#run_tests()
main()
