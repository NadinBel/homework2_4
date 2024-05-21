car = ["BMW", "MB", "LADA", "KIA", "HONDA"]
car_counts = 0
for i in car:
    print('Я езжу на автомабиле марки', i)
    for i in range(len(car)):
        car_counts += 10
        print(car_counts)


