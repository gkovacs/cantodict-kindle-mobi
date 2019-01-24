# CC-CEDICT Chinese-English Dictionary for Kindle with Mandarin and Cantonese (mobi format)

## Download

Amazon Kindle Store: [Pinyin and Jyutping](https://www.amazon.com/Chinese-English-Dictionary-Mandarin-Cantonese-Pronunciations-ebook/dp/B07MV9TJQB/) or [Zhuyin and Jyutping](https://www.amazon.com/Chinese-English-Dictionary-Mandarin-Cantonese-Pronunciations-ebook/dp/B07MVF4NGF)

Mobi ([sideload it](https://www.lifewire.com/load-non-amazon-books-kindle-1616647)): [Pinyin and Jyutping](https://github.com/gkovacs/cantodict-kindle-mobi/blob/master/dictionary.mobi) or [Zhuyin and Jyutping](https://github.com/gkovacs/cantodict-kindle-mobi/blob/master/dictionary_zhuyin.mobi)

Donations appreciated: [Paypal](https://www.paypal.me/gezak/5) [Venmo](https://venmo.com/?txn=pay&recipients=gezak&amount=5.00&note=for%20Chinese-English%20Dictionary&audience=public) [Bitcoin](https://www.gkovacs.com/bitcoin.html)

## About

Chinese-English Dictionary with Mandarin and Cantonese Pronunciations

Send to your Kindle, select it as the built-in dictionary, and you can look up words just by clicking on them!

Supports looking up both Simplified and Traditional characters. Over 200,000 entries.

Mandarin (Standard Chinese / Putonghua) pronunciations are in Pinyin (`nǐ hǎo`), Cantonese (Yue) pronunciations are in Jyutping (`nei5 hou2`). Example entry:

`发展` (Simplified) `發展` (Traditional) `fā zhǎn` (Mandarin Pinyin) `faat3 zin2` (Cantonese Jyutping) `development, growth, to develop, to grow, to expand`


Also includes Cantonese specific words such as 冇 and Cantonese specific words such as 唔該. Example entry:

`唔該` (Traditional) `唔该` (Simplified) `wú gāi` (Mandarin Pinyin) `m4 goi1` (Cantonese Jyutping) `please; thanks; excuse me`

## Supported Devices

### E-ink Kindles

With e-ink kindles, you can [add an external dictionary](https://www.epubor.com/how-to-change-or-add-dictionary-to-kindle.html) by buying it on the Kindle store ([or sideloading](https://www.lifewire.com/load-non-amazon-books-kindle-1616647)), highlighting a word, then selecting the dictionary.

### Kindle app on Android

If you want to use this on an Andoid device, you can do so by replacing an existing dictionary - ie, if you want to replace the built-in Chinese-English dictionary, replace `/sdcard/Android/data/com.amazon.kindle/files/B00AZOHEGE/B00AZOHEGE_EBOK.prc` with the dowloaded mobi file. More detailed instructions are as follows [(source)](https://www.mobileread.com/forums/showthread.php?t=245121).

```
Open any book (no matter which) and request a definition in a language that you won't use (Deutsche for example). The Kindle app will start to download that dictionary; wait the download is completed and exit from the app (use task manager to kill the app to make sure).

The downloaded dictionary will be in /sdcard/Android/data/com.amazon.kindle/files folder. In order to detect the downloaded dictionary, watch what is the last modified date. Remember the name of the .prc file (also you could find a .mbp file -you'll find them inside a folder named B00XXXXXXX-; of course, instead of XXX you'll have another thing) and rename it/them (change extensions).

Copy in this folder your french dictionary and give it the same name as the .prc file whose name you changed in the previous step (if your french dictionary has another extension than .prc, no matter, give it that extension, so that your dictionary is named something like B00XXXXXXX_EBOK.prc).

Now open Kindle app and use your dictionary (of course, you will be choosing the Deutsche dictionary but actually will be your french dict.)
```

## About (code)

These scripts generate a `.mobi` file from the CC-CEDICT Chinese-English dictionary and the CantoDict dictionary.

You can then load this `.mobi` file to your Kindle to use it as a dictionary.

The generated dictionary includes pinyin or zhuyin (mandarin), jyutping (cantonese) and definitions for words.

# Running

First install python, python3 and kindlegen. Then run the following commands

```bash
python3 mkdict.py > dictionary.txt
python tab2opf.py -utf dictionary.txt
kindlegen dictionary.opf
```

If you would like to have zhuyin pronunciations, run the following commands

```bash
python3 mkdict.py zhuyin > dictionary_zhuyin.txt
python tab2opf.py -utf dictionary_zhuyin.txt zhuyin
kindlegen dictionary_zhuyin.opf
```

If you would also like it in stardict format, install stardict-tools and then 

```bash
/usr/lib/stardict-tools/tabfile dictionary.txt
/usr/lib/stardict-tools/tabfile dictionary_zhuyin.txt
```

# Author

[Geza Kovacs](https://github.com/gkovacs)

# License

MIT

# Related

For version with pinyin and no jyutping, see https://github.com/gkovacs/cc-cedict-kindle-mobi

