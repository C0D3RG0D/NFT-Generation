from handlers.slime_modification import create_image


def main():
    print("\nСколько изображений сгенерировать?")
    amount = int(input("-> "))
    for number in range(amount):
        dino_num = number + 1
        create_image(dino_num)
        print(f"[dino-{dino_num}][{amount}/{dino_num}] - успешно создан")


if __name__ == "__main__":
    main()
