#include <stdio.h>
#include "lib.c"

int main() {
  BST* tree = createBST();
  insert(tree, 5);
  insert(tree, 2);
  insert(tree, 8);
  insert(tree, 6);
  insert(tree, 10);
  insert(tree, 9);
  print(tree);
  printSize(tree);
  delete(tree, 10);
  print(tree);
  printSize(tree);
  return 0;
}