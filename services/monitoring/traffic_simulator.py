import random
import uuid

from services.monitoring.error_logger import log_error
from services.monitoring.request_logger import log_request


PROVIDERS = ["Ollama", "Groq", "Gemini"]

MODELS = {
    "Ollama": ["llama3", "mistral"],
    "Groq": ["mixtral", "llama-3.1-70b"],
    "Gemini": ["gemini-1.5-flash", "gemini-1.5-pro"],
}

ERROR_TYPES = [
    "Timeout",
    "Rate Limit",
    "Validation Error",
    "Provider Failure",
    "Internal Server Error",
]

ERROR_MESSAGES = {
    "Timeout": "Provider response exceeded the configured timeout.",
    "Rate Limit": "Too many requests were sent to the provider.",
    "Validation Error": "The request payload failed validation.",
    "Provider Failure": "The AI provider returned an unexpected failure.",
    "Internal Server Error": "An unexpected internal processing error occurred.",
}


def generate_simulated_request():
    provider = random.choice(PROVIDERS)
    model = random.choice(MODELS[provider])

    status = random.choices(["Success", "Failed"], weights=[88, 12])[0]

    latency = random.randint(120, 2200)
    tokens = random.randint(400, 4500)
    cost = round(tokens * 0.00002, 4)

    request_id = f"REQ-{uuid.uuid4().hex[:8].upper()}"

    log_request(
        request_id=request_id,
        provider=provider,
        model=model,
        latency=latency,
        tokens=tokens,
        cost=cost,
        status=status,
    )

    if status == "Failed":
        error_type = random.choice(ERROR_TYPES)

        severity = random.choices(
            ["Low", "Medium", "High", "Critical"],
            weights=[20, 40, 30, 10],
        )[0]

        log_error(
            request_id=request_id,
            error_type=error_type,
            severity=severity,
            message=ERROR_MESSAGES[error_type],
        )

    return request_id


def generate_traffic(batch_size=10):
    generated = []

    for _ in range(batch_size):
        request_id = generate_simulated_request()
        generated.append(request_id)

    return generated