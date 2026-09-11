# Segmentation DevOps Project

This project is a Flask image segmentation application with CI/CD integration via Jenkins.

## Project Structure

```
Segmentation_DevOps/
├── src/                    # Source code
│   ├── app.py             # Flask application
│   ├── main.py            # Main script
│   └── segmentation.py    # Segmentation functions
├── input_images/          # Input images
├── output_images/         # Processed images
├── tests/                 # Unit tests
├── static/                # Static files
├── templates/             # HTML templates
├── Dockerfile             # Docker configuration
├── Jenkinsfile            # Jenkins configuration
└── requirements.txt       # Python dependencies
```

## Prerequisites

- Docker installed
- Jenkins installed and configured
- Python 3.11+ (for local development)

## Local Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python src/app.py
```

The application will be accessible at http://localhost:5000

## Docker Usage

1. Build the Docker image:
```bash
docker build -t segmentation-app .
```

2. Run the container:
```bash
docker run -p 5000:5000 segmentation-app
```

## Jenkins Usage

### What is Jenkins?

Jenkins is an open-source automation server that automates software development tasks (CI/CD - Continuous Integration/Continuous Deployment).

### Jenkins Installation on Windows

1. **Download Jenkins**: https://www.jenkins.io/download/
2. **Install Jenkins**:
   - Run the Windows installer
   - Choose a port (default 8080)
   - Jenkins will be accessible at http://localhost:8080

3. **Initial configuration**:
   - Copy the admin password displayed
   - Install suggested plugins
   - Create an admin account

### Jenkins Pipeline Configuration

1. **Create a new project**:
   - Click "New Item"
   - Name it "segmentation-pipeline"
   - Choose "Pipeline"
   - Click OK

2. **Configure the pipeline**:
   - In the "Pipeline" section
   - Choose "Pipeline script from SCM"
   - Select "Git"
   - Repository URL: If you have a remote Git repo, enter the URL
   - Script path: `Jenkinsfile`
   - Click "Save"

3. **For local project (without Git)**:
   - Choose "Pipeline script"
   - Copy the Jenkinsfile content directly into the editor
   - Click "Save"

4. **Run the pipeline**:
   - Click "Build Now"
   - Jenkins will automatically execute all stages

### What the Jenkinsfile does

The Jenkinsfile I created automates:

1. **Checkout**: Retrieves source code from Git
2. **Build Docker Image**: Builds the Docker image with `docker build`
3. **Run Tests**: Executes unit tests with pytest in the container
4. **Deploy Application**: Launches the Flask application in a Docker container

### Test Results

✅ **Tests successful**: Unit tests pass successfully
✅ **Application functional**: Flask application starts correctly on port 5000

### Local Jenkinsfile Testing

To test the Jenkinsfile without Jenkins installed, use Docker commands manually:

```bash
# Build the image
docker build -t segmentation-app .

# Run tests
docker run --rm segmentation-app pytest tests/ -v

# Run the application
docker run -p 5000:5000 segmentation-app
```

## Tests

To run tests locally:
```bash
pytest tests/ -v
```

## Development

The project uses Flask for the web interface and OpenCV for image processing.
