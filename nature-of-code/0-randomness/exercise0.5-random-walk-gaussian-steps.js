let walker;

function setup() {
  createCanvas(640, 640);
  walker = new Walker();
  background(255);
}

function draw() {
  walker.step();
  walker.show();
}

class Walker {
  constructor() {
    this.x = width / 2;
    this.y = height / 2;
  }

  show() {
    stroke(0);
    strokeWeight(2);
    point(this.x, this.y);
  }

  step() {
    const choice = floor(random(4));
    const stepSize = randomGaussian(5, 1);
    if (choice == 0) {
      this.x += stepSize;
    } else if (choice == 1) {
      this.x -= stepSize;
    } else if (choice == 2) {
      this.y += stepSize;
    } else {
      this.y -= stepSize;
    }
  }
}