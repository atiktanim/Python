while True:
    try:
        number=int(input("What's your favourite number?\n"))
        print(18/number)
        break
    except ValueError:
        print("Make sur eand enter a number")
    except ZeroDivisionError:
        print("Don't pick 0")
    except:
        break
    finally:
        print("loop complete")
