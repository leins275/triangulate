import argparse
import csv


def parse_input(input_file):
    points = []
    with open(input_file) as input:
        vertices = csv.reader(input)
        for point in vertices:
               points.append([ int(point[0]), int(point[1]) ])
    return points


def sort_graham(vertices):
    return []

def save_ans(output_file, triangles, error):
    if error != None:
        data = [error]
    else:
        data = triangles
    with open(output_file, 'w', newline='', encoding='utf-8') as output:
        writer = csv.writer(output)
        writer.writerows(data)


def earcut(vertices, index_sorted):
    return []

def register_launch_arguments():
    parser = argparse.ArgumentParser(description='Serve the app')
    parser.add_argument('-i', '--input', help='specify input file', default='./data/in.csv')
    parser.add_argument('-o', '--output', help='specify output file', default='./data/out.csv')

    return parser.parse_args()

if __name__ == '__main__':
    args = register_launch_arguments()
    error = None

    try:
        vertices = parse_input(args.input)
        index_sorted = sort_graham(vertices)
        triangles = earcut(vertices, index_sorted)
    except ValueError:
        error = 'ERROR: Incorrect input'

    save_ans(args.output, triangles, error)