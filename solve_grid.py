import logging
import yaml
import argparse
import sys
from os import path

class solve_grid(object):
    def __init__(self, grid):
        self.grid=grid
        self.list_of_possible_val=[0,1,2,3,4,5,6,7,8,9]
        self.column_size=len(self.grid)
        self.row_size=len(self.grid[0])

    def get_empty_coordinates(self):
        return [(i,j) for i in range(self.column_size) for j in range(self.row_size) if self.grid[i][j] == 0]


    def get_empty_location(self,grid):
        return_val=False
        for items in self.get_empty_coordinates():
            grid[0]=items[0]
            grid[1]=items[1]
            return_val=True
        return return_val

    def possible_row_values(self, r):
        if r <= self.row_size:
            return (set(self.list_of_possible_val)-set(self.grid[r]))

    def possible_column_values(self, c):
        if c <= self.column_size:
            return (set(self.list_of_possible_val)- set([row[c] for row in self.grid]))

    def possible_cube_values(self, r, c):
        r0 = (r//3)*3
        c0 = (c//3)*3
        return (set(self.list_of_possible_val) - set([self.grid[r0+i][c0+j] for i in range(0,3) for j in range(0,3)]))


    def check_if_number_is_valid_for_location(self,r,c, value):
        return value in self.possible_row_values(r) and value in self.possible_column_values(c) and value in self.possible_cube_values(r,c)


    def solve(self):
        grid_num=[0,0]

        if(not self.get_empty_location(grid_num)):
            return True

        for num in range(1,10):
            if(self.check_if_number_is_valid_for_location(grid_num[0],grid_num[1],num)):
                self.grid[grid_num[0]][grid_num[1]]=num
                if(self.solve()):
                    return True
                self.grid[grid_num[0]][grid_num[1]] = 0
        return False

def main():
    parser = argparse.ArgumentParser(description=sys.modules[__name__].__doc__,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-L','--loglevel', type=str, default="INFO",  help="default logging enabled")
    parser.add_argument('-G','--grid', required=True, help="path to grid yaml file")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel, format='%(asctime)s %(levelname)s %(funcName)s:%(lineno)d %(message)s',
                        stream=sys.stdout)

    if not path.isfile(args.grid):
        logging.info(f"File not exist {args.grid}")

    with open(args.grid,'r') as file:
        documents = yaml.full_load(file)
    grid=[i for items, doc in documents.items() for i in doc]

    solve_me = solve_grid(grid)
    if(solve_me.solve()):
        logging.info(grid)
    else:
        logging.info(f"Solution cannot be reached {grid}")

if __name__ == '__main__':
    main()



