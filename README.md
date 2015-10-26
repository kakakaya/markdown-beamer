<!-- coding:utf-8, mode:gfm-mode -->
<!-- Author: kakakaya, Date: Sun Oct 25 23:55:02 2015 -->
# markdown-beamer
雑にbeamerのスライドをmarkdownから吐くやつ

# Install
入れる必要があるもの:
  * pandoc
  * texlive-luatex
  * eu2enc.def(texlive-xetex入れればなんとかなる)

上のものを入れてフォルダごと適当にパスが通る場所に置けばなんとかなる、はず


# Usage
空のディレクトリに移動して初期化する(色々なファイルがコピーされる)
```
$ cd mySlide
$ markdown-beamer.py --init
```
body.mdというファイルを編集する
```
$ emacs body.md
```
引数無しで叩いてPDFを生成する

```
$ markdown-beamer.py
$ ls output
```

# FAQ
Q. 空ではないディレクトリで初期化するときプロンプトなしで上書きしたい

A.
```
$ markdown-beamer.py --init --force
```

# TODO
  * TeXのソースを吐く所で止める機能(markdownから直接だけだと色々無理がある)
