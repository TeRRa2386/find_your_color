https://find-your-color.onrender.com/

# Find Your Color

This is a simple Flask web application that allows you to upload an image and see its top 10 most used colors.

The application extracts the most dominant colors in the image and displays them in HEX code format.

## Features

- Upload any image you like
- Automatically extract and display the top 10 colors in the image
- Colors are shown as colored boxes with their HEX codes
- Simple and clean user interface
- Responsive design for mobile and desktop

## Requirements

- Python 3.x
- Flask
- Pillow
- python-dotenv
- numpy (optional, but imported)

## How to Run

1. Clone this repository:
    ```
    git clone https://github.com/yourusername/find-your-color.git
    ```

2. Navigate to the project folder:
    ```
    cd find-your-color
    ```

3. (Optional but recommended) Create and activate a virtual environment:
    ```
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

4. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

5. Run the application:
    ```
    python main.py
    ```

6. Open your browser and go to:
    ```
    http://127.0.0.1:5000/
    ```

## Notes

- Uploaded images are stored in `static/uploads/`. This folder is excluded from Git.
- Color grouping uses a configurable factor to merge similar colors.
- The app is meant for educational and demonstration purposes.

## License

This project is licensed under the MIT License.
