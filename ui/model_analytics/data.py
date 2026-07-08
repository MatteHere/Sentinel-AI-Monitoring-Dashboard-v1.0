import pandas as pd


def get_model_data():
    return pd.DataFrame(
        {
            "model": [
                "Ollama",
                "Groq",
                "Gemini",
                "OpenAI",
                "Claude",
            ],
            "requests": [
                8420,
                12630,
                5340,
                3180,
                2260,
            ],
            "latency": [
                620,
                280,
                740,
                510,
                430,
            ],
            "success_rate": [
                97.8,
                99.5,
                98.2,
                99.1,
                98.9,
            ],
            "cost": [
                0,
                46,
                82,
                58,
                41,
            ],
        }
    )