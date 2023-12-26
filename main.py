from fastapi import FastAPI, Response

# http://127.0.0.1:8000/docs
# uvicorn main:app --reload

app = FastAPI()


@app.get("/story/")
def get_legacy_data():
    try:
      read_file = open("responce.json", "r")
      data = read_file.read()
      read_file.close ()

    except FileNotFoundError:
      read_file = open("app/responce.json", "r")
      data = read_file.read()
      read_file.close()

    return Response(content=data, media_type="application/json")
