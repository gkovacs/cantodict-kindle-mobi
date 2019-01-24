# CC-CEDICT Chinese-English Dictionary for Kindle with Mandarin and Cantonese (mobi format)

## Download (Amazon Kindle Store)

[Pinyin and Jyutping version](https://www.amazon.com/Chinese-English-Dictionary-Mandarin-Cantonese-Pronunciations-ebook/dp/B07MV9TJQB/)

[Zhuyin and Jyutping version](https://www.amazon.com/Chinese-English-Dictionary-Mandarin-Cantonese-Pronunciations-ebook/dp/B07MVF4NGF)

## Download (mobi)

[Pinyin and Jyutping version](https://github.com/gkovacs/cantodict-kindle-mobi/blob/master/dictionary.mobi)

[Zhuyin and Jyutping version](https://github.com/gkovacs/cantodict-kindle-mobi/blob/master/dictionary_zhuyin.mobi)

## Donate

[Paypal](https://www.paypal.me/gezak/5)

[Venmo](https://venmo.com/?txn=pay&recipients=gezak&amount=5.00&note=for%20Chinese-English%20Dictionary&audience=public)

[Bitcoin](https://www.gkovacs.com/bitcoin.html)

## About

Chinese-English Dictionary with Mandarin and Cantonese Pronunciations

Send to your Kindle, select it as the built-in dictionary, and you can look up words just by clicking on them!

Supports looking up both Simplified and Traditional characters. Over 200,000 entries.

Mandarin (Standard Chinese / Putonghua) pronunciations are in Pinyin (example: nǐ hǎo), Cantonese (Yue) pronunciations are in Jyutping (example: nei5 hou2).

Example entry: 发展 (Simplified) 發展 (Traditional) fā zhǎn (Mandarin Pinyin) faat3 zin2 (Cantonese Jyutping) development, growth, to develop, to grow, to expand

Also includes Cantonese specific words such as 冇 and Cantonese specific words such as 唔該

Example entry: 唔該 (Traditional) 唔该 (Simplified) wú gāi (Mandarin Pinyin) m4 goi1 (Cantonese Jyutping) please; thanks; excuse me

## About (technical)

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

