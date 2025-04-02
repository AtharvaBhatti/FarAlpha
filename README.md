# FastAPI Hello User API with GitHub Actions Deployment

A simple FastAPI application with a CI/CD pipeline using GitHub Actions to deploy to a virtual machine (VM).

## Features
- **`GET /`**: Returns `{"status": "Online"}`.
- **`GET /sayHello`**: Returns `{"message": "Hello User"}`.
- Automated deployment to a VM on `git push` to the `main` branch.
- Runs on **port 80** with Systemd service management.

## Prerequisites
- Python 3.9+
- FastAPI and Uvicorn (see `requirements.txt`).
- GitHub repository with secrets configured:
  - `SSH_HOST`: IP address of the VM (e.g., `172.206.225.34`).
  - `SSH_USER`: VM username (e.g., `azureuser`).
  - `SSH_KEY`: Full content of the SSH private key (`.pem` file).

## Installation
1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd <repository-directory>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run locally:
   ```bash
   uvicorn main:app --reload
   ```

4. Test locally: [http://localhost:8000/sayHello](http://localhost:8000/sayHello)

## Deployment with GitHub Actions
### Workflow Configuration
The workflow (`.github/workflows/deploy.yml`) automates:
- Copying code to the VM via SCP.
- Installing dependencies.
- Setting up a Systemd service to run the API on port 80.

### Steps to Deploy
1. Set up GitHub Secrets:
   - Go to your repo → **Settings** → **Secrets and variables** → **Actions**.
   - Add `SSH_HOST`, `SSH_USER`, and `SSH_KEY` (see Secrets Setup).

2. Push to GitHub:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

3. Verify Deployment:
   - Check the **Actions** tab for workflow success.
   - Test the API:
     ```bash
     curl http://<VM-IP>/sayHello
     # Example: curl http://172.206.225.34/sayHello
     ```

## Testing the API
### Post-Deployment
```bash
# Check root endpoint
curl http://<VM-IP>/
# Output: {"status":"Online"}

# Check /sayHello endpoint
curl http://<VM-IP>/sayHello
# Output: {"message":"Hello User"}
```

## Project Structure
```
.
├── .github/
│   └── workflows/
│       └── deploy.yml       # GitHub Actions workflow
├── main.py                  # FastAPI application code
├── requirements.txt         # Dependencies (FastAPI, Uvicorn)
└── README.md                # Project documentation
```

## Challenges & Solutions
### Port 80 Permissions
- Used Systemd to run the service under a non-root user (azureuser).

### Service Activation Failures
- Fixed by specifying absolute paths to python3 and uvicorn in the Systemd service.

### Secrets Management
- Stored SSH keys and VM credentials in GitHub Secrets (no hardcoding).

