# Quickbox

**Version:** 1.0.2

Simple web-based file manager built with Flask. Supports uploads, folder creation, multilingual interface, and theming.


## Features
- Upload multiple files via drag & drop
- Multilingual interface
- Theme support


## Screenshots
[<img src="/screenshots/dark_mode.png" alt="Dark mode" width="280"/>](https://github.com/PericlesSavio/Quickbox/blob/main/screenshots/dark_mode.png)
[<img src="/screenshots/light_mode.png" alt="Light mode" width="280"/>](https://github.com/PericlesSavio/Quickbox/blob/main/screenshots/light_mode.png)
[<img src="/screenshots/blue_mode.png" alt="Blue mode" width="280"/>](https://github.com/PericlesSavio/Quickbox/blob/main/screenshots/blue_mode.png)


## Installation
1. Clone the repository:
```bash
git clone https://github.com/PericlesSavio/Quickbox
cd quickbox
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
python app.py
```

4. Open your browser and navigate to:
```bash
http://localhost:5000
```


## How to run with Docker
1. Build the image:
```bash
docker build -t quickbox .
```

2. Build the image and start the container:
```bash
docker compose up --build
```

3. Access in your browser:
```bash
http://localhost:5000
```


## TODO List
- [ ] Add support for excluding files/folders
- [ ] Add support for adding folders with files using drag and drop
- [ ] Fix drag-and-drop fetch bug


## License
This project is licensed under the **GPL-3.0 License**. See the [LICENSE](https://github.com/PericlesSavio/Quickbox?tab=GPL-3.0-1-ov-file) file for details.