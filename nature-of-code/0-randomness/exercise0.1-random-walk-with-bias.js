let walker;

function setup() {
  createCanvas(640, 240);
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
    point(this.x, this.y);
  }

  step() {
    const choice = random(1);
    if (choice < 0.3) {
      this.x++;
    } else if (choice < 0.5) {
      this.x--;
    } else if (choice < 0.8) {
      this.y++;
    } else {
      this.y--;
    }
  }
}