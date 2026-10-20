from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for
import csv
from datetime import datetime

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "books.csv"

@app.get("/")
def index():
    books = []

    with open(CSV_FILE, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            books.append(row)

    return render_template("index.html", books=books)

@app.get("/book/<int:book_id>")
def book_details(book_id):
    found_book = None

    with open(CSV_FILE, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for book in csv_reader:
            if int(book['id']) == book_id:
                found_book = book
                break
    
    if found_book:
        return render_template("details.html", book=found_book)
    else:
        return "Book not found!", 404

@app.get("/add")
def show_add_form():
    return render_template("add-book.html")

@app.post("/add")
def add_book():
    with open(CSV_FILE, mode="r", encoding="utf-8") as csv_file:
        reader = list(csv.reader(csv_file))
        last_id = 0

        if len(reader) > 1:
            last_row = reader[-1] 
            if last_row:  
                last_id = int(last_row[0])

        next_id = last_id + 1 

    date_raw = request.form.get("date")
    date_object = datetime.strptime(date_raw, "%Y-%m-%d")

    formatted_date = date_object.strftime("%m/%d/%Y")

    new_book_data = [
        next_id,
        request.form.get("title"),
        request.form.get("author"),
        request.form.get("genre"),
        request.form.get("image_url"),
        request.form.get("stars"),
        formatted_date,
        request.form.get("review"),
    ]

    with open(CSV_FILE, mode="a", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(new_book_data)

    return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(debug=True)
