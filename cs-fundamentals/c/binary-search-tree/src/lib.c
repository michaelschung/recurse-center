#include <stdio.h>
#include <stdlib.h>

typedef struct Node Node;

struct Node {
  int val;
  Node* next;
};

Node* createNode(int val) {
  Node* newNode = malloc(sizeof(Node));
  newNode->val = val;
  newNode->next = NULL;
  return newNode;
}

void append(Node** pHead, int val) {
  Node* newNode = createNode(val);
  if (*pHead == NULL) {
    *pHead = newNode;
    return;
  }
  Node* curr = *pHead;
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
  // Node* curr = head;
  while (head != NULL) {
    printf("%d -> ", head->val);
    head = head->next;
  }
  printf("NULL\n");
}