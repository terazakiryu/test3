from flask import Flask, request, redirect, render_template
import math
from server import keep_alive

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/warikan')
def warikan():
  return render_template('warikan.html')


@app.route('/warikan2')
def warikan2():
  ninzu = int(request.args.get('ninzu'))
  gokei = int(request.args.get('gokei'))
  tani = int(request.args.get('tani'))
  style = request.args.get('style')
  base = ninzu * tani
  if style == "1":
    member = tani * (gokei // base)
    bucho = gokei - (member * ninzu) + member
    return render_template('warikan2.html',
                           gokei=gokei,
                           ninzu=ninzu,
                           member=member,
                           bucho=bucho,
                           value="部長の支払額")
  else:
    member = tani * (-1 * ((-1 * gokei) // base))
    bucho = (member * ninzu) - gokei
    return render_template('warikan2.html',
                           gokei=gokei,
                           ninzu=ninzu,
                           member=member,
                           bucho=bucho,
                           value="2次会予算")


@app.route('/zeikomi')
def zeikomi():
  return render_template('zeikomi.html')


@app.route('/zeikomi2')
def zeikomi2():
  num = int(request.args.get('num'))
  zeiritu = int(request.args.get('zeiritu'))
  x = int((num * (1 + (zeiritu * 0.01))) // 1)
  return render_template('zeikomi2.html', x=x, num=num, zeiritu=zeiritu)


@app.route('/youbi')
def youbi():
  return render_template('youbi.html')


app.run(host='0.0.0.0')

# ウェブサーバーを起動する
keep_alive()
