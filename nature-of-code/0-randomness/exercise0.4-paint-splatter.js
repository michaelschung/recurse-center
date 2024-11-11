function setup() {
    createCanvas(640, 640);
    background(255);
    frameRate(1);
    noStroke();
}

function draw() {
//{!1} A normal distribution with mean 320 and standard deviation 60
    let x = random(640);
    let y = random(640);
    paintSplatter(x, y);
}

function paintSplatter(x, y) {
    const stdDev = 50;
    fill(255, 0, 0);
    for (let i = 0; i < 300; i++) {
        let paintX = randomGaussian(x, stdDev);
        let paintY = randomGaussian(y, stdDev);

        let dist = sqrt(pow(x-paintX, 2) + pow(y-paintY, 2));
        let diameter = min(10/(1.5*dist-20)+2, 100);

        circle(paintX, paintY, diameter);
    }
}