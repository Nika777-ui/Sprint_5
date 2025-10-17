# Sprint_5
Sprint 5 - Avtotesty dlya Stellar Burgers
Opisanie proekta
Proekt soderzhit avtomatizirovannye testy dlya veb-servisa Stellar Burgers s ispolzovaniem Selenium WebDriver.


Registraciya - uspeshnaya registraciya i oshibka pri nekorrektnom parole
Vhod v sistemu - 4 sposoba vhoda v akkaunt
Navigaciya - perekhody po lichnomu kabinetu i konstruktoru
Konstruktor burgerov - perekhody mezhdu razdelami

bash
pytest tests/test_registration.py -v           # Testy registracii
pytest tests/test_vhod.py -v                   # Testy vhoda
pytest tests/test_navigation.py -v             # Testy navigacii
pytest tests/test_constructor.py -v            # Testy konstruktora