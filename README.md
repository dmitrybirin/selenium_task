# Test Python Selenium  Task

That's the simple task I've got. It was fun.
Task content:

Need to automate the test scenario with Selemium:

1. Open browser and maximize it
2. Go to the yandex.ru
3. Go to the "Электроника" -> "Мобильные телефоны."
4. Set two filter parameters: "Цена" to 20000 rub. and "Диагональ экрана" from 3 inches.
5. Randomly choose 5 Manufactors
6. Click Apply button
7. Check that the page contains 12 found elements
8. Remember the first element of found elements
9. Change sorting ("цена" or "новизна")
10. Find and click on the remembered object by name
11. Close the browser

## Install

```
git clone https://github.com/dmitrybirin/selenium_task.git
cd selenium_task
pip install -r requirements.txt
```
If there is no Chrome Driver in the system it should be installed in PATH
https://chromedriver.storage.googleapis.com/index.html?path=2.31

## Run

```
pytest test.py
```

## What hasn't been done

- [ ] Multiple browser support. Only chrome now
- [ ] Docs for every method and module
- [ ] Improved logging
- [ ] Docker container to handle all the setup