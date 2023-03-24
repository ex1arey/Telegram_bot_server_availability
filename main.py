import this
print(this)

films = ["Crazy, Stupid, Love.",
        "Seven",
        "Dead Poets Society",
        "Memento",
        "Harry Potter"]
for film in films:
    if film == "Memento":
        print("Фільм Memento знайденний! Цикл завершенно!")
        break

    print(film)
