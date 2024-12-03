#include <stdio.h>
#include <stdlib.h>

typedef struct Node Node;

struct Node {
  int val;
  Node* left;
  Node* right;
};

typedef struct BST BST;

struct BST {
  Node* root;
};

BST* createBST() {
  BST* tree = malloc(sizeof(BST));
  tree->root = NULL;
  return tree;
}

int getSize(Node* root) {
  if (root == NULL) return 0;
  return getSize(root->left) + getSize(root->right) + 1;
}

void printSize(BST* tree) {
  int size = getSize(tree->root);
  printf("SIZE: %d\n", size);
}

void printHelper(Node* root) {
  if (root == NULL) return;
  printHelper(root->left);
  printf("%d ", root->val);
  printHelper(root->right);
}

void print(BST* tree) {
  printHelper(tree->root);
  printf("\n");
}

Node* createNode(int val) {
  Node* newNode = malloc(sizeof(Node));
  newNode->val = val;
  newNode->left = NULL;
  newNode->right = NULL;
  return newNode;
}

Node* insertHelper(Node* root, int val) {
  if (root == NULL) {
    return createNode(val);
  }
  if (val < root->val) {
    root->left = insertHelper(root->left, val);
  } else {
    root->right = insertHelper(root->right, val);
  }
  return root;
}

void insert(BST* tree, int val) {
  tree->root = insertHelper(tree->root, val);
}

int findSuccessor(Node* root) {
  root = root->right;
  while (root->left != NULL) {
    root = root->left;
  }
  return root->val;
}

Node* deleteHelper(Node* root, int val) {
  // If fell off the edge, return
  if (root == NULL) return NULL;
  // If found node to delete, three options
  if (val == root->val) {
    // First two ifs fulfill leaf case and one child case
    if (root->left == NULL) {
      Node* temp = root->right;
      free(root);
      return temp;
    }
    if (root->right == NULL) {
      Node* temp = root->left;
      free(root);
      return temp;
    }
    // Two child case
    // Find inorder successor
    int successor = findSuccessor(root);
    // Replace this val with sucessor val
    root->val = successor;
    root->right = deleteHelper(root->right, successor);
  } else if (val < root->val) {
    root->left = deleteHelper(root->left, val);
  } else {
    root->right = deleteHelper(root->right, val);
  }
  return root;
}

void delete(BST* tree, int val) {
  tree->root = deleteHelper(tree->root, val);
}