#include <stdio.h>
#include "lib.c"

int main() {
  // LinkedList* ll = (LinkedList*) malloc(sizeof(LinkedList));
  Node* head = NULL;
  append(&head, 1);
  append(&head, 2);
  append(&head, 3);
  print(head);
  delete(&head, 1);
  delete(&head, 2);
  print(head);
  return 0;
}