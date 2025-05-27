from myapp import create_app
print("Starting the Flask application...")
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)