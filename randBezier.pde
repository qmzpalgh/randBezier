//#############################################################################
//# Sketch that draws a bezier curve to the screen and varies the position of #
//# each anchor point and control point based on a random acceleration value  #
//#                                                                           #
//# Author: James Gibbons                                                     #
//# Copyright: 2016                                                           #
//#############################################################################
ArrayList<PVector> vectors = new ArrayList<PVector>();

void setup() {
  fullScreen();
  background(0);
  stroke(255);
  noFill();
  vectors.add(new PVector(0, 0));//acceleration
  for (int i = 0; i < 4; i++) {
    vectors.add(new PVector(random(width), random(height)));
    vectors.add(new PVector(0, 0));//velocity
  }
}

void draw() {
    background(0, 0, 0, 10);
  for (int i = 1; i < 8; i += 2) {
    if (vectors.get(i).x > width || vectors.get(i).x < 0) {//if anchor point or handle reach the edge reverse their velocity
      vectors.get(i + 1).x = -vectors.get(i + 1).x;
    }
    if (vectors.get(i).y > height || vectors.get(i).y < 0) {
      vectors.get(i + 1).y = -vectors.get(i + 1).y;
    }
    vectors.get(0).x = random(-.1, .1);
    vectors.get(0).y = random(-.1, .1);
    vectors.get(i + 1).add(vectors.get(0));
    vectors.get(i).add(vectors.get(i + 1));
  }
  beginShape();
  vertex(vectors.get(1).x, vectors.get(1).y);
  bezierVertex(vectors.get(3).x, vectors.get(3).y, vectors.get(5).x, vectors.get(5).y, vectors.get(7).x, vectors.get(7).y);
  endShape();
}