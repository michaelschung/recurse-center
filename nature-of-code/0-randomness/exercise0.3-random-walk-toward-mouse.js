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
        const chaseMouseChance = 0.1;
        if (random(1) < chaseMouseChance) {
            this.x += (mouseX < this.x) ? -1 : 1;
            this.y += (mouseY < this.y) ? -1 : 1;
        } else {
            const choice = random(4)
            if (choice < 1) {
                this.x++;
            } else if (choice < 2) {
                this.x--;
            } else if (choice < 3) {
                this.y++;
            } else {
                this.y--;
            }
        }
    }
}