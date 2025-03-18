def move(no: int, x: int, y: int) ->None:
    if no > 1:
        move(no-1, x, 6-x-y)

        print(no,x,y)

        if no > 1 :
            move(no-1, 6-x-y,y)

n = int(input())
move(n,1,3)    