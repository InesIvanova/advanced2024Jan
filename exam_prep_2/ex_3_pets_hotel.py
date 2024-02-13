def accommodate_new_pets(hotel_capacity, max_allowed_weight, *pets):
    accommodated_pets = {}
    are_all_accommodated = True

    for pet_name, pet_weight in pets:
        if not hotel_capacity:
            are_all_accommodated = False
            break
        if pet_weight <= max_allowed_weight:
            if pet_name not in accommodated_pets:
                accommodated_pets[pet_name] = 0
            accommodated_pets[pet_name] += 1
            hotel_capacity -= 1

    result = ""
    if are_all_accommodated:
        result += f"All pets are accommodated! Available capacity: {hotel_capacity}.\n"
    else:
        result += f"You did not manage to accommodate all pets!\n"

    result += "Accommodated pets:\n"

    if accommodated_pets:
        sorted_pets = sorted(accommodated_pets.items(), key=lambda kvp: kvp[0])
        for pet_name, pet_weight in sorted_pets:
            result += f"{pet_name}: {pet_weight}\n"
    return result[:-1]




from unittest import TestCase, main


class Test(TestCase):
    def test_accommodate_pets(self):
        result = accommodate_new_pets(
            1,
            5.0,
            ("dog", 17.0),
            ("cat", 15.8),
            ("dog", 22.7),
            ("dog", 15.01),

        )

        self.assertEqual(
            result.strip(),
            """All pets are accommodated! Available capacity: 1.
Accommodated pets:""")


if __name__ == '__main__':
    main()



