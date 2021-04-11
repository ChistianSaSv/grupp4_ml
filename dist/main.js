
$('#my-cta-button').click(async function() {
  let criticScores = $('#score-input').val()

  let testValues = {
    score = criticScores
  }

  let res = await fetch('/api/predict', {
    method: 'POST',
    body: JSON.stringify(testValues)
  })

  let prediction = await res.json()

  $('#prediction').html(`
   <em>${prediction['predict']}</em>`)
})