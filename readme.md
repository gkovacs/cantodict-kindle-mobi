# CC-CEDICT Chinese-English Dictionary for Kindle with Mandarin and Cantonese (mobi format)

## About

These scripts generate a `.mobi` file from the CC-CEDICT Chinese-English dictionary and the CantoDict dictionary.

You can then load this `.mobi` file to your Kindle to use it as a dictionary.

The generated dictionary includes zhuyin (mandarin), jyutping (cantonese) and definitions for words.

# Running

First install python, python3 and kindlegen. Then run the following commands

```bash
python3 mkdict.py > dictionary.txt
python tab2opf.py -utf dictionary.txt
kindlegen dictionary.opf
```

# Author

[Geza Kovacs](https://github.com/gkovacs)

# License

MIT

# Related

For version with pinyin and no jyutping, see https://github.com/gkovacs/cc-cedict-kindle-mobi

