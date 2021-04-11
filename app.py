from sanic import Sanic, response
from sanic.exceptions import NotFound
from model1 import train_model, predict

app = Sanic(__name__)
train_model()

# When we navigate to /api/predict we have to pass in two values (age, income) which will then be packaged as
# json (strings) and later we can access this json in our predict_values function

@app.post('/api/predict')
async def predict_results(req):
  values = req.json  # values is a dictionary
  prediction = predict(values['Critic_Scores'])
  print('Predicated sales:', prediction)
  return response.json(prediction)

# When we navigate to '/' - serve the dist folder
app.static('/', './dist')

@app.exception(NotFound)
async def ignore_404s(req, err):
  return await response.file('./dist/index.html')

if __name__ == "__main__":
    app.run(port=8000)