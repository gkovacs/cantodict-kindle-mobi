# CC-CEDICT Chinese-English Dictionary for Kindle with Mandarin and Cantonese (mobi format)

## About

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

