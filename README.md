# Flask App with CI/CD using GitHub Actions, Docker Hub, and Render

This project demonstrates a simple Flask web application with a full CI/CD pipeline:

- Automatically builds and pushes a Docker image to Docker Hub on every push to the `main` branch.
- Triggers deployment on [Render](https://render.com) using a deploy hook URL.

## 🧰 Prerequisites

1. **Docker Hub account**
2. **GitHub repository**
3. **Render account**
4. **Docker installed locally (for testing purposes)**

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

### 2. Flask App Structure

```text
├── src
    └── templates
        └── home.html
    └── tests
        └── test_flask_app.py
    └── main.py
├── .python-version
├── pyproject.toml
├── Dockerfile
├── .github
│   └── workflows
│       └── ci-cd_pipeline.yml
└── README.md
```

---

### 3. Create `Dockerfile`

### 4. Create GitHub Actions Workflow

### 5. Set Up Render

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Create a **Web Service**
3. Choose **Docker** as deployment method
4. Enter your Docker image: `your-dockerhub-username/flask-ci-cd`
5. Copy the deploy hook from the service settings

---

### 6. Add GitHub Secrets

In your GitHub repository, go to **Settings > Secrets and variables > Actions**, then add:

- `DOCKER_USERNAME` – your Docker Hub username
- `DOCKER_PASSWORD` – your Docker Hub password or access token
- `RENDER_DEPLOY_HOOK_URL` – your Render deploy hook URL which you have copied

---



## ✅ How It Works

1. You push code to the `main` branch.
2. GitHub Actions builds and pushes a Docker image to Docker Hub.
3. The deploy hook triggers Render to pull the latest image and deploy it.

---

## 🚀 Example Usage

```bash
git add .
git commit -m "Updated feature"
git push origin main
```

That's it — your app will build, push, and deploy automatically.

---
