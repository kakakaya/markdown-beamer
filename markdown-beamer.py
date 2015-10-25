#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: kakakaya, Date: Sun Oct 25 17:07:49 2015
# from pprint import pprint as p
import sys
import os
# import shutil
import argparse


def initialize(path, force):
    if not os.path.isdir(path):
        raise Exception("[Error]指定のパスはディレクトリではないです: "+path)
    if not os.access(path, os.W_OK):
        raise Exception("[Error]指定のパスは書き込み不可です: "+path)
    if len(os.listdir(path)) > 0 and not force:
        print("[INFO]指定のパスは空ではないです: "+path)
        answer = ""
        while answer.lower() not in ["y", "yes", "n", "no"]:
            answer = input("上書きする可能性がありますが、初期化しますか？[y/n]")
        if answer.lower() in ["n", "no"]:
            print("終了します。")
            sys.exit(1)

    # 各ファイルをコピーしてくる
    for f in ["lib", "tmp", "output", "body.md"]:
        copy_from = os.path.split(os.path.abspath(sys.argv[0]))[0]+"/"+f
        print("cp -r "+copy_from+" "+path)


def make(path):
    # ファイル存在確認
    for f in ["lib", "tmp", "output", "body.md"]:
        if f not in os.listdir(path):
            raise Exception("[Error]File not found: {0}, working directory might bad?".format(f))

    headers = sorted(os.listdir(path+"/lib"))
    cmd = "pandoc --latex-engine=lualatex"
    for head in headers:
        cmd += " -H lib/{0}".format(head)
    cmd += " -t beamer -i body.md -o output/output.pdf"
    print(cmd)
    os.system(cmd)


def main():
    working_directory = os.getcwd()
    parser = argparse.ArgumentParser(description="")
    parser.add_argument(
        "-f", "--force",
        help="プロンプトを抑制します。",
        action='store_true',
        default=False,
    )
    parser.add_argument(
        "-i", "--init",
        action='store',
        nargs="?",
        metavar="NEWSLIDE_PATH",
        help="""新規スライドを作成する時に指定します。
        NEWSLIDE_PATHを指定するとその場所に、さもなくばカレントディレクトリに生成されます。
        注意:色々上書きされます。""",
        default=False
    )

    args = parser.parse_args()
    print(args)
    if args.init is not False:
        if args.init is None:
            # 作成先が未指定ならカレントディレクトリを対象にする
            initialize(working_directory)
        else:
            initialize(args.init, args.force)
    else:
        make(working_directory)


if __name__ == "__main__":
    main()