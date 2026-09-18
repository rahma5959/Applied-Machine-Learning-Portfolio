import os

from flask import Flask, render_template, request
from segmentation import segment_image


# Define the project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)


@app.route("/")
def home():
    # Define input and output paths
    input_path = os.path.join(
        BASE_DIR,
        "input_images",
        "pomme.jpg"
    )

    output_path = os.path.join(
        BASE_DIR,
        "static",
        "mask.png"
    )

    # Run image segmentation
    segment_image(input_path, output_path)

    # Display the web page
    return render_template("index.html")


@app.route("/segment", methods=["POST"])
def segment():
    # Check if an image was uploaded
    if "image" not in request.files:
        return "No image uploaded"

    image = request.files["image"]

    # Check if a file was selected
    if image.filename == "":
        return "No file selected"

    # Define the uploaded image path
    input_path = os.path.join(
        BASE_DIR,
        "input_images",
        "uploaded_image.jpg"
    )

    # Save the uploaded image
    image.save(input_path)

    # Define the static image path
    static_image_path = os.path.join(
        BASE_DIR,
        "static",
        "uploaded_image.jpg"
    )

    # Copy the uploaded image to the static folder
    with open(input_path, "rb") as source:
        with open(static_image_path, "wb") as destination:
            destination.write(source.read())

    # Define the output path
    output_path = os.path.join(
        BASE_DIR,
        "static",
        "mask.png"
    )

    # Run image segmentation
    segment_image(input_path, output_path)

    # Display the result page
    return render_template(
        "index.html",
        uploaded_image="uploaded_image.jpg",
        segmentation_result="segmentation_result.png"
    )


# Start the Flask server
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
