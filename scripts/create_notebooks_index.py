
import os
import argparse

INDEX_TEMPLATE_HEADER = """
<html>
<body>
<h2>{0}</h2>
<p>
"""

INDEX_TEMPLATE_LINKLINE = "<li><a href={1}>{0}</a></li>"

INDEX_TEMPLATE_FINAL = """
</p>
</body>
</html>
"""

EXCLUDED = ['index.html']

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    parser.add_argument("--header")
    args = parser.parse_args()
    fnames = [fname for fname in sorted(os.listdir(args.directory))
              if fname not in EXCLUDED and os.path.splitext(fname)[1] == ".html"]
    header = (args.header if args.header else os.path.basename(args.directory))
    print(INDEX_TEMPLATE_HEADER.format(header))
    for fname in fnames:
       print(INDEX_TEMPLATE_LINKLINE.format(fname, os.path.join(args.directory, fname)))
    print(INDEX_TEMPLATE_FINAL)

if __name__ == '__main__':
    main()
