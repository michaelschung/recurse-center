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
  int size;
};

BST* createBST() {
  BST* tree = malloc(sizeof(BST));
  tree->root = NULL;
  tree->size = 0;
  return tree;
}

// Not used, just for fun
int getSizeRecursive(Node* root) {
  if (root == NULL) return 0;
  return getSize(root->left) + getSize(root->right) + 1;
}

void printSize(BST* tree) {
  printf("SIZE: %d\n", tree->size);
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
  tree->size++;
  tree->root = insertHelper(tree->root, val);
}

int findSuccessor(Node* root) {
  root = root->right;
  while (root->left != NULL) {
    root = root->left;
  }
  return root->val;
}

Node* deleteHelper(int* pSize, Node* root, int val) {
  // If fell off the edge, return
  if (root == NULL) return NULL;
  // If found node to delete, three options
  if (val == root->val) {
    // First two ifs fulfill leaf case and one child case
    if (root->left == NULL) {
      Node* temp = root->right;
      free(root);
      *pSize = *pSize - 1;
      return temp;
    }
    if (root->right == NULL) {
      Node* temp = root->left;
      free(root);
      *pSize = *pSize - 1;
      return temp;
    }
    // Two child case
    // Find inorder successor
    int successor = findSuccessor(root);
    // Replace this val with sucessor val
    root->val = successor;
    root->right = deleteHelper(pSize, root->right, successor);
  } else if (val < root->val) {
    root->left = deleteHelper(pSize, root->left, val);
  } else {
    root->right = deleteHelper(pSize, root->right, val);
  }
  return root;
}

void delete(BST* tree, int val) {
  // Pass pointer to tree size to make it changeable
  tree->root = deleteHelper(&(tree->size), tree->root, val);
}