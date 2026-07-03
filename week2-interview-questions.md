# Week 2 — FastAPI Interview Questions and Answers

This file includes coding questions, answers, and interview Q&A for Week 2: FastAPI and backend patterns.

## Coding Question 1: Simple FastAPI app with dependency injection

**Problem:** Create a FastAPI app with one endpoint using a dependency that returns a reusable config object.

**Answer:**
```python
from fastapi import FastAPI, Depends
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastAPI Demo"
    debug: bool = True


def get_settings():
    return Settings()


app = FastAPI()


@app.get("/info")
def info(settings: Settings = Depends(get_settings)):
    return {"app_name": settings.app_name, "debug": settings.debug}
```

## Coding Question 2: JWT auth middleware simulation

**Problem:** Build an authentication dependency that checks a fake bearer token.

**Answer:**
```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()
app = FastAPI()


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    if token != "secret-token":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return {"user_id": "user1"}


@app.get("/secure")
def secure_route(user=Depends(verify_token)):
    return {"message": "access granted", "user": user}
```

## Coding Question 3: Streaming response endpoint

**Problem:** Implement a `/stream` endpoint that returns text incrementally.

**Answer:**
```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()


def event_stream():
    for i in range(5):
        yield f"data: chunk {i}\n\n"
        time.sleep(0.2)


@app.get("/stream")
def stream():
    return StreamingResponse(event_stream(), media_type="text/event-stream")
```

## Coding Question 4: Background task for notification

**Problem:** Add a `/notify` endpoint that triggers a background task.

**Answer:**
```python
from fastapi import FastAPI, BackgroundTasks
import time

app = FastAPI()


def send_notification(email: str):
    time.sleep(1)
    print(f"Notification sent to {email}")


@app.post("/notify")
def notify(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_notification, email)
    return {"status": "queued"}
```

## Coding Question 5: File upload endpoint

**Problem:** Create an endpoint that accepts a file upload and returns file info.

**Answer:**
```python
from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    return {"filename": file.filename, "content_type": file.content_type, "size": len(content)}
```

## Interview Questions

### Question 1: Explain FastAPI dependency injection

**Answer:**
- FastAPI uses `Depends()` to declare dependencies that can be injected into path operations.
- Dependencies are callables that can return values or raise HTTP errors.
- FastAPI resolves dependencies recursively and caches them per request if needed.
- This pattern enables reusable auth, config, DB sessions, and testing hooks.

### Question 2: What is middleware in FastAPI?

**Answer:**
- Middleware wraps request processing and response generation.
- It can inspect or mutate requests/responses, implement logging, CORS, auth, or rate limiting.
- Middleware runs for every request, before and after endpoint execution.
- Use dependency injection for route-specific logic, and middleware for application-wide concerns.

### Question 3: How do you handle exceptions in FastAPI?

**Answer:**
- Use `HTTPException` for endpoint-level errors with custom status code and detail.
- Register exception handlers with `app.exception_handler()` for custom response payloads.
- Validate request bodies automatically using Pydantic, which raises 422 errors on invalid input.
- Centralized error handling improves consistency and security.

### Question 4: When should you use async endpoints?

**Answer:**
- Use async endpoints for I/O-bound operations like database calls, HTTP requests, and file reads.
- Async helps scale high-concurrency workloads by freeing the event loop during waits.
- Avoid async for CPU-heavy work; delegate that to thread pools or separate services.
- Ensure libraries used are async-compatible to avoid blocking the event loop.

### Question 5: How would you secure a FastAPI app?

**Answer:**
- Use HTTPS and strong auth methods such as OAuth2 or JWT.
- Validate and sanitize input via Pydantic models.
- Limit exposed endpoints and enforce role-based access.
- Add rate limiting, CORS controls, secret management, and logging.
- Protect against injection and avoid returning sensitive internals.
