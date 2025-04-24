from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Docker Calculator</title>
<h2>Simple Calculator</h2>
<form method="POST">
  <input name="a" type="number" step="any" required> 
  <select name="op">
    <option value="+">+</option>
    <option value="-">-</option>
    <option value="*">*</option>
    <option value="/">/</option>
  </select>
  <input name="b" type="number" step="any" required>
  <input type="submit" value="Calculate">
</form>
{% if result is not none %}
<h3>Result: {{ result }}</h3>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def calculate():
    result = None
    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        op = request.form["op"]
        try:
            result = eval(f"{a}{op}{b}")
        except Exception as e:
            result = f"Error: {e}"
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
