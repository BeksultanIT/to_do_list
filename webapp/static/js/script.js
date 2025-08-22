function calc(action) {
  var aVal = document.getElementById('a').value;
  var bVal = document.getElementById('b').value;

  var A = parseFloat(aVal);
  var B = parseFloat(bVal);

  var out = document.getElementById('res');

  if (isNaN(A) || isNaN(B)) {
    out.textContent = 'Error: enter numbers';
    out.className = 'err';
    return;
  }

  fetch('/api/' + action + '/', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ A: A, B: B })
  })
  .then(function(r) { return r.json().then(function(d){ return {status:r.status, data:d}; }); })
  .then(function(res) {
    if (res.status === 200) {
      out.textContent = 'Answer: ' + res.data.answer;
      out.className = 'ok';
    } else {
      out.textContent = 'Error: ' + res.data.error;
      out.className = 'err';
    }
  })
  .catch(function() {
    out.textContent = 'Error: request failed';
    out.className = 'err';
  });
}
