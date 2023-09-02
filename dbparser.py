import argparse

parser = argparse.ArgumentParser(description="Parse databases for easier access to information.")
parser.add_argument("-i", metavar="Input", help="The input file name.")
parser.add_argument("-s", metavar="Search", help="Search term parameter.")
parser.add_argument("-o", metavar="Output", default="dbparse.txt", help="[OPTIONAL] The output file name.")
parser.add_argument("-e", metavar="Exclude", help="[Optional] Exclude lines that include a certain word.")
args = parser.parse_args()

with open(args.i, "r", encoding="utf-8") as input_file:
    with open(args.o, "w", encoding="utf-8") as output_file:
        for line in input_file:
            if not args.e or args.e not in line:
                if args.s in line:
                    lines = line.split("\n")
                    for split_line in lines:
                        output_file.write(split_line.strip() + "\n")





