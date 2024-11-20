#include <stdio.h>
#include <stdlib.h>

struct Node {
  int val;
  struct Node* next;
};

typedef struct Node Node;

// typedef struct {
//   int val;
//   Node* next;
// } Node;

// typedef struct {
//   Node* head;
//   Node* tail;
//   int size;
// } LinkedList;

Node* createNode(int val) {
  Node* newNode = malloc(sizeof(Node));
  newNode->val = val;
  newNode->next = NULL;
  return newNode;
}

void append(Node** head, int val) {
  Node* newNode = createNode(val);
  if (*head == NULL) {
    *head = newNode;
    return;
  }
  Node* curr = *head;
  while (curr->next != NULL) {
    curr = curr->next;
  }
  curr->next = newNode;
}

// 0 = success, 1 = empty, 2 = val not found
int delete(Node** head, int val) {
  // If empty list
  if (*head == NULL) {
    return 1;
  }
  // If deleting head
  if ((*head)->val == val) {
    Node* temp = *head;
    *head = (*head)->next;
    free(temp);
    return 0;
  }
  // Otherwise
  Node* curr = *head;
  while (curr->next != NULL) {
    if (curr->next->val == val) {
      Node* temp = curr->next;
      curr->next = curr->next->next;
      free(temp);
      return 0;
    }
    curr = curr->next;
  }
  // If val not found
  return 2;
}

void print(Node* head) {
  Node* curr = head;
  while (curr != NULL) {
    printf("%d -> ", curr->val);
    curr = curr->next;
  }
  printf("NULL\n");
}