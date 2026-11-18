from fastapi import FastAPI

app = FastAPI(title='企业安全生产管理平台', version='0.1.0')


@app.get('/api/v1/health')
def health() -> dict[str, str]:
  return {'status': 'ok'}
