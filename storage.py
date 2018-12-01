import os
import argparse
import tempfile
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key", type=str, help="key name")
parser.add_argument("--val", type=str, help="value")

args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
# print(storage_path)

if not os.path.exists(storage_path):
    with open(storage_path, "w", encoding='utf-8') as f:
        # print("File creates!")
        f.write("{}")

if args.key and args.val:
    # print("the key = {} and value equals {}".format(args.key, args.val))
    with open(storage_path, "r", encoding='utf-8') as fr:
        data = fr.read()
        dict = json.loads(data)
        # print(type(dict), dict)

        if args.key in dict:
            dict[args.key].append(args.val)
        else:
            # print(dict)
            dict.update({args.key: [args.val]})

        with open(storage_path, "w", encoding='utf-8') as fw:
            # print(dict)
            json.dump(dict, fw)

elif args.key:
    with open(storage_path, "r", encoding='utf-8') as fr:
        data = fr.read()
        dict = json.loads(data)

        if args.key in dict:
            print(*dict[args.key], sep=', ')
        else:
            print("None")
