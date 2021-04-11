from sanic import Sanic, response
from sanic.exceptions import NotFound
from model1 import train_model, predict

app = Sanic(__name__)
train_model()

@app.post('/api/predict')
async def predict_results(req):
  values = req.json  # values is a dictionary
  prediction = predict(values['Critic_Scores'])
  print('Predicated sales:', prediction)
  return response.json(prediction)

app.static('/', './dist')

@app.exception(NotFound)
async def ignore_404s(req, err):
  return await response.file('./dist/index.html')

if __name__ == "__main__":
    app.run(port=8000)
