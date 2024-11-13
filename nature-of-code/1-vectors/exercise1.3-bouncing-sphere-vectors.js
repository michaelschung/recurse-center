const boxSize = 400;
const rotationChange = 0.0005;

let ball;

function setup() {
  createCanvas(windowWidth, windowHeight, WEBGL);
  ball = new Ball();
  ambientLight(60, 60, 60);
  camera(0, 300, -750, 0, 0, 0, 0, 1, 0);
//   frameRate(5);
}

function draw() {
  background(255);
  
  rotateY(frameCount * rotationChange);
  rotateX(frameCount * rotationChange);

  ball.update();
  ball.display();

  stroke(0);
  fill(0, 0, 255, 25);
  box(boxSize, boxSize, boxSize);
}

class Ball {
  constructor() {
    this.location = createVector(50, 100, 0);
    this.velocity = createVector(2.5, 2.5, 3);
    this.size = 10;
    this.trailLocs = [];
  }
  
  bounce() {
    let atLeftBorder = (this.location.x - this.size/2 < -boxSize/2);
    let atRightBorder = (this.location.x + this.size/2 > boxSize/2);
    
    if(atLeftBorder || atRightBorder) {
      this.velocity.x = -this.velocity.x;
    }
    
    let atTopBorder = (this.location.y - this.size/2 < -boxSize/2);
    let atBottomBorder = (this.location.y + this.size/2 > boxSize/2);
    
    if(atTopBorder || atBottomBorder) {
      this.velocity.y = -this.velocity.y;
    }
    
    let atFrontBorder = (this.location.z - this.size/2 < -boxSize/2);
    let atBackBorder = (this.location.z + this.size/2 > boxSize/2);
    
    if(atFrontBorder || atBackBorder) {
      this.velocity.z = -this.velocity.z;
    }
  }
  
  update() {
    let newLocation = createVector(this.location.x, this.location.y, this.location.z);
    this.trailLocs.push(newLocation);
    if (this.trailLocs.length > 50) {
        this.trailLocs.splice(0, 1);
    }

    this.location.add(this.velocity);
    this.bounce();
  }
  
  display() {
    push();
    translate(this.location);
    normalMaterial();
    stroke(255, 0, 0);
    fill(255, 0, 0);
    sphere(this.size);
    pop();

    for (let i = 0; i < this.trailLocs.length; i++) {
      push();
      let trailLoc = this.trailLocs[i];
      translate(trailLoc);
      normalMaterial();
      stroke(255, 0, 0);
      fill(255, 0, 0);
      sphere(2);
      pop();
    }
  }
}