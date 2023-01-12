
import os
import argparse
import yaml

INDEX_TEMPLATE_HEADER = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>My Website</title>
    <link rel="stylesheet" href="./style.css">
    <link rel="icon" href="./favicon.ico" type="image/x-icon">
  </head>
  <body>
    <main>
        <h1>{0}</h1>  
    <p>
"""

INDEX_TEMPLATE_LINKLINE = "<h2><a href={1}>{0}</a></h2>{2}"

INDEX_TEMPLATE_FINAL = """
    </p>
    </main>
    <script src="index.js"></script>
  </body>
</html>
"""

EXCLUDED = ['index.html']

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("configyaml")
    args = parser.parse_args()
    
    with open(args.configyaml) as f:
      config_dict = yaml.load(f, Loader=yaml.SafeLoader)

    print(INDEX_TEMPLATE_HEADER.format(config_dict["title"]))
    for k, v in config_dict["pages"].items():
       print(INDEX_TEMPLATE_LINKLINE.format(k, v["notebook"].replace("ipynb", "html"), v["description"]))
    print(INDEX_TEMPLATE_FINAL)

if __name__ == '__main__':
    main()