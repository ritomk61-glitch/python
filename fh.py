with open(r"C:\Users\ritom kumar hajra\Downloads\fire_robot_fixed.ino", "wb") as f:
    f.write(b"today we are trying to finish unit 4")

with open(r"C:\Users\ritom kumar hajra\Downloads\fire_robot_fixed.ino", "rb") as f:
    r=f.read()

    print(r)
    print(r.decode())

           