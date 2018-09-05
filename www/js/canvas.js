import path from './path.js';

const canvas = document
  .getElementsByTagName('canvas')[0];
const ctx = canvas.getContext('2d');

ctx.fillStyle = 'rgb(200, 0, 0)';
ctx.fillRect(10, 10, 50, 50);

function handle(data) {
  for (let points of data) {
    path(ctx, points);
  }
}

fetch('data/data.json')
  .then(response => response.json())
  .then(handle);
