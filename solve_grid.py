import logging
logging.basicConfig(level='INFO')

class solve_grid(object):
    def __init__(self, grid):
        self.grid=grid
        self.list_of_possible_val=[0,1,2,3,4,5,6,7,8,9]
        self.column_size=len(self.grid)
        self.row_size=len(self.grid[0])

    def get_empty_coordinates(self):
        xy=[]
        for i in range(self.column_size):
            for j in range(self.row_size):
                if self.grid[i][j] == 0:
                    xy.append((i,j))
        return xy

    def get_empty_location(self,l):
        for items in self.get_empty_coordinates():
            l[0]=items[0]
            l[1]=items[1]
            return True
        return False

    def possible_row_values(self, r):
        if r <= self.row_size:
            return (set(self.list_of_possible_val)-set(self.grid[r]))

    def possible_column_values(self, c):
        if c <= self.column_size:
            return (set(self.list_of_possible_val)- set([row[c] for row in self.grid]))

    def possible_cube_values(self, r, c):
        list_of_cube=[]
        r0 = (r//3)*3
        c0 = (c//3)*3
        for i in range(0,3):
            for j in range(0,3):
                list_of_cube.append(self.grid[r0+i][c0+j])
        return (set(self.list_of_possible_val)- set(list_of_cube))

    def check_if_number_is_valid_for_location(self,r,c, value):
        return value in self.possible_row_values(r) and value in self.possible_column_values(c) and value in self.possible_cube_values(r,c)


    def solve(self):
        l=[0,0]
        if(not self.get_empty_location(l)):
            return True

        row=l[0]
        col=l[1]

        for num in range(1,10):
            if(self.check_if_number_is_valid_for_location(row,col,num)):
                self.grid[row][col]=num
                if(self.solve()):
                    return True
                self.grid[row][col] = 0
        return False


if __name__ == '__main__':
    grid=[[3,0,6,5,0,8,4,0,0],
      [5,2,0,0,0,0,0,0,0],
      [0,8,7,0,0,0,0,3,1],
      [0,0,3,0,1,0,0,8,0],
      [9,0,0,8,6,3,0,0,5],
      [0,5,0,0,9,0,6,0,0],
      [1,3,0,0,0,0,2,5,0],
      [0,0,0,0,0,0,0,7,4],
      [0,0,5,2,0,6,3,0,0]]

    solve_me = solve_grid(grid)
    if(solve_me.solve()):
        print(grid)
    else:
        print("No solution exists")


