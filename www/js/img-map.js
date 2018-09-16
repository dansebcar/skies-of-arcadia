function createElement(name, attrs) {
  const elem = document.createElement(name);

  for (const attr in attrs) {
    elem.setAttribute(attr, attrs[attr]);
  }

  return elem;
}

function appendChildren(parent, ...children) {
  for (const child of children) {
    parent.appendChild(child);
  }

  return parent;
}

function enumerate(iterable) {
  return function*() {
    let i = 0;

    for (const item of iterable) {
      yield [i, item];
      i++;
    }
  };
}

const style = createElement('style');

const css = `
  div {
    background-color: green;
    width: 300px;
    height: 300px;
  }
`;

style.textContent = css;

customElements.define('img-map', class extends HTMLElement {
  constructor() {
    super();

    const src = this.getAttribute('src');

    const img = createElement('img', {src});

    const {canvas, ctx} = this.createCanvas();

    this.pointContainer = createElement('div');

    fetch('data/data.json')
      .then(response => response.json())
      .then(data => this.handle(data));

    const shadow = this.attachShadow({mode: 'open'});

    appendChildren(shadow, style, img, canvas, this.pointContainer);
  }
  createCanvas({width=300, height=300} = {}) {
    const canvas = createElement('canvas', {width, height});

    const ctx = canvas.getContext('2d');

    ctx.fillStyle = 'rgb(0, 200, 200)';
    ctx.fillRect(10, 10, 50, 50);

    return {canvas, ctx};
  }
  handle(data) {
   for (const [i, item] of enumerate(data)) {

     if (Array.isArray(item)) {

     }
   }
  }
  drawLine(a, b) {
    
  }
});
