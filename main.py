from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

API_URL = "https://v6.exchangerate-api.com/v6/ed074681246bddcedae2d6de/latest/USD"

async def get_conversion_rates():
    """
    Получает курсы валют из внешнего API.
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(API_URL)
            response.raise_for_status()
            data = response.json()
            return data.get("conversion_rates", {})
        except httpx.HTTPStatusError as exc:
            raise HTTPException(status_code=exc.response.status_code, detail="Ошибка при запросе к внешнему API.")
        except httpx.RequestError:
            raise HTTPException(status_code=500, detail="Не удалось выполнить запрос к внешнему API.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Неожиданная ошибка: {e}")

@app.get("/convert")
async def convert(from_currency: str, to_currency: str, value: float):
    """
    Конвертирует валюты.

    Args:
        from_currency: Начальная валюта.
        to_currency: Целевая валюта.
        value: Сумма для конвертации.

    Returns:
        Конвертированная сумма.
    """
    if value <= 0:
        raise HTTPException(status_code=400, detail="Сумма для конвертации должна быть больше нуля.")

    conversion_rates = await get_conversion_rates()

    if from_currency not in conversion_rates or to_currency not in conversion_rates:
        raise HTTPException(status_code=400, detail="Некорректные валюты.")

    converted_value = (conversion_rates[to_currency] / conversion_rates[from_currency]) * value
    return {
        "converted_value": converted_value
    }