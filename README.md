# studyos
Creating a place to study in a fun, useful and gamified way

---

## Internal Design

`src/core`: manages internal things, like session or image utilities.

`src/UI`: uses the files in `core/` to implement and connect the user interface with logic.

`tests`: image tests.

`src/main.py`: initializer and main runner. Coordinates other tasks using the files in the `ui/` folder.