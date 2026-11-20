def handle(responses):
    match responses:
        case 200:
            return "OK"
        case 404 | 410:
            return "Gone"
        case [x,y]:
            return f"pair is : {x},{y}"
        case {"user": name}:
            return f"user: {name}"
        case _:
            return "unknown"



print(handle(404))
print(handle([4,5]))
print(handle({"user":"danuj"}))