# Quickbox

**Version:** 1.0.0

Simple web-based file manager built with Flask. Supports uploads, folder creation, multilingual interface, and theming.


## Features
- Upload multiple files via drag & drop
- Multilingual interface
- Theme support


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

2. Run the container:
```bash
docker run -p 5000:5000 quickbox
```

3. Using docker-compose:
```bash
docker-compose up --build
```

4. Access in your browser:
```bash
http://localhost:5000
```

## TODO List
- [ ] Add support for excluding files/folders

## License
This project is licensed under the **GPL-3.0 License**. See the [LICENSE](https://github.com/PericlesSavio/Quickbox?tab=GPL-3.0-1-ov-file) file for details.