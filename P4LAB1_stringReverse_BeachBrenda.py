while True:
    try: 
        backward = input()
        if backward == 'Done':
            continue
        elif backward == 'done':
            continue
        elif backward == 'd':
            continue
        print (backward[::-1])
    except :
        break
