/*
NOTE: This breaks if the refractive index of a prism is significantly
lower than bgIndex. Not fully sure why, but I suspect it has to do
with trig values becoming negative – and I don't want to bother
fixing it right now.
*/

let beam;
let prisms;
let bgIndex = 1.2;

function setup() {
    createCanvas(600, 600);
    background(255);
    textSize(10);

    beam = new LightBeam(0, 0);
    prisms = [
        new Prism(50, 100, 2),
        new Prism(160, 200, 1)
    ];
}

function draw() {
    strokeWeight(0);
    fill(0);
    text("index: " + bgIndex, 5, height-5);
    text("(click anywhere to reset)", width/2-50, 550);

    beam.show();
    beam.update(prisms);

    for (let i = 0; i < prisms.length; i++) {
        prisms[i].show();
    }
}

// Some useful vector functions - may already exist but oh well
function getMagnitude(vector) {
    return Math.sqrt(vector.x**2 + vector.y**2);
}

function normalizeVector(vector) {
    let magnitude = getMagnitude(vector);
    let normalizedVector = createVector(vector.x, vector.y);
    normalizedVector.div(magnitude);
    return normalizedVector;
}

function setVectorMagnitude(vector, speed) {
    let newVector = normalizeVector(vector);
    newVector.mult(speed);
    return newVector;
}

class LightBeam {
    constructor(x, y) {
        this.pos = createVector(x, y);
        this.vel = createVector(1, 1);
        this.index = bgIndex;
    }

    show() {
        stroke(0);
        strokeWeight(1);
        point(this.pos.x, this.pos.y);
    }

    update(prisms) {
        let collider = this.getCollider(prisms);
        // No collider = default to background index
        let newIndex = !collider ? bgIndex : collider.index;
        this.calcNewAngle(newIndex);
        this.pos.add(this.vel);
    }

    // Returns colliding prism, or null
    getCollider(prisms) {
        for (let i = 0; i < prisms.length; i++) {
            let prism = prisms[i];
            if (prism.colliding(this.pos)) {
                return prism;
            }
        }
        return null;
    }

    calcNewAngle(newIndex) {
        let indexRatio = newIndex/this.index;
        // Calculate new directional vector
        let theta1 = Math.atan(this.vel.x/this.vel.y);
        let theta2 = Math.asin(Math.sin(theta1)/indexRatio);
        let newVelRaw = createVector(Math.tan(theta2), 1);
        // Adjust speed according to index ratio
        let oldSpeed = getMagnitude(this.vel);
        this.vel = setVectorMagnitude(newVelRaw, oldSpeed/indexRatio);
        this.index = newIndex;
    }
}

class Prism {
    constructor(x, y, index) {
        this.pos = createVector(x, y);
        this.size = createVector(100, 50);
        this.index = index;
    }

    show() {
        stroke(0);
        strokeWeight(1);
        noFill();
        rect(this.pos.x, this.pos.y, this.size.x, this.size.y);

        strokeWeight(0);
        fill(0);
        text("index: " + this.index, this.pos.x+5, this.pos.y+this.size.y-5);
    }

    // Check if given pos is inside prism
    colliding(pos) {
        if (this.pos.x <= pos.x && pos.x <= this.pos.x + this.size.x) {
            if (this.pos.y <= pos.y && pos.y <= this.pos.y + this.size.y) {
                return true;
            }
        }
        return false;
    }
}

function mousePressed() {
    setup();
}