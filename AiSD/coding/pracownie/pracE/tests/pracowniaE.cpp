#include <stdio.h>
#include <iostream>
#include <limits.h>
// #include <fstream>

using namespace std;

class Node
{
    public:
    long long key;
    Node *left;
    Node *right;
    int height;
};

int max(int a, int b){
    if (a > b) {
        return a;
    }else {
        return b;
    }
}

int min(int a, int b){
    if (a < b){
        return a;
    }else {
        return b;
    }
}

int height(Node* node){
    if (node == NULL){
        return 0;
    }
    return node->height;
}

Node *leftRotate(Node *root){
    // przepinamy wskaźniki
    Node *B = root->right;
    Node *Y = B->left;

    B->left = root;
    root->right = Y;

    // zmieniamy wysokości dynamicznie
    root->height = 1 + max(height(root->left), height(root->right));
    B->height = 1 + max(height(B->left), height(B->right));

    // zwracamy korzeń nowo utworzonego drzewa
    return B;

}

Node *rightRotate(Node *root){
    // przepinamy wskaźniki
    Node *B = root->left;
    Node *Y = B->right;

    B->right = root;
    root->left = Y;

    // zmieniamy wysokości dynamicznie
    root->height = 1 + max(height(root->left), height(root->right));
    B->height = 1 + max(height(B->left), height(B->right));

    return B;
}

int getBalanceFactor(Node *node){
    return height(node->left) - height(node->right);
}

Node *balanceTree(Node *root){

    // obliczamy balance factor, zeby zobaczyć czy drzewo jest
    // left heavy (bF > 0), czy right heavy (bf < 0)
    int bF = getBalanceFactor(root);

    // teraz balansujemy drzewo
    // LEFT-HEAVY
    if (bF > 1) {
        // LEFT-RIGHT
        if (getBalanceFactor(root->left) < 0) {
            root->left = leftRotate(root->left);
        }
        // LEFT-LEFT
        return rightRotate(root);
        
        
    }else if (bF < -1){
        // RIGHT-LEFT
        if (getBalanceFactor(root->right) > 0){
            root->right = rightRotate(root->right);
        }
        // RIGHT-RIGHT
        return leftRotate(root);
    }

    return root;
}


Node *getMinInOrder(Node *node){
    if (node->left == NULL) {
        return node;
    }else {
        return getMinInOrder(node->left);
    }
}


Node *Insert(Node *root, long long key){
    // na początku standardowy insert w BST
    if (root == NULL){
        Node *node = new Node();
        node->key = key;
        node->left = NULL;
        node->right = NULL;
        node->height = 1;
        return node;
    }
    if (key < root->key){
        // do lewej gałęzi dokładamy drzewo, ktore utworzymy
        root->left = Insert(root->left, key);
    }else if (key > root->key) {
        root->right = Insert(root->right, key);
    }else {
        // jak taki wierzchołek juz istnieje
        return root;
    }

    // obliczamy wysokość po dodaniu wierzchołka
    root->height = 1 + max(height(root->left), height(root->right));

    return balanceTree(root);
}

Node *Delete(Node *root, long long key){
    // na początku standardowy delete w BST
    if (root == NULL){
        // printf("BRAK\n");
        return root;
    }
    if (key < root->key){
        root->left = Delete(root->left, key);
    }else if (key > root->key){
        root->right = Delete(root->right, key);
    }else {
        // jak doszliśmy az tutaj to root->key == key i mozna usunąć
        // printf("OK\n");
        if (root->left == NULL){
            // usuwamy root i zwracamy zamiast niego całą prawą gałąź
            Node *temp = root->right;
            delete root;
            return temp;
        }else if (root->right == NULL){
            Node *temp = root->left;
            delete root;
            return temp;
        }else {
            // mamy oba poddrzewa, szukamy upper w prawym
            Node *temp = getMinInOrder(root->right);
            // zamiast usuwać, po prostu podmieniamy wartość
            root->key = temp->key;
            // nie chemy dwoch takich samych wartości w drzewie, to wyrzucamy podmienianą wartość
            // z prawego poddrzewa
            root->right = Delete(root->right, root->key); 
        }
    }

    if (root == NULL){
        return NULL;
    }

    // obliczamy wysokość po dodaniu wierzchołka
    root->height = 1 + max(height(root->left), height(root->right));

    return balanceTree(root);
}

bool findKey(Node *root, long long key){
    if (root == NULL){
        return false;
    }else if (key > root->key){
        return findKey(root->right, key);
    }else if (key < root->key){
        return findKey(root->left, key);
    }
    return true;
}


long long Upper(Node *root, long long x){
    Node *current = root;
    long long result = LLONG_MAX;
    while (current){
        if (current->key >= x){
            result = current->key;
            // zacieśniamy przedział
            current = current->left;
        }else {
            current = current->right;
        }
    }

    return result;
}


long long Lower(Node *root, long long x){
    Node *current = root;
    long long result = LLONG_MIN;
    while (current) {
        if (current->key <= x){
            result = current->key;
            // chcemy znaleźć większą liczbę potencjalnie, idziemy w prawo
            current = current->right;
        }else {
            current = current->left;
        }
    }
    return result;
}

void preOrder(Node *root) 
{ 
    if(root != NULL) 
    { 
        cout << root->key << " "; 
        preOrder(root->left); 
        preOrder(root->right); 
    }
} 

int main() {

    // ifstream infile;
    // infile.open("/Users/szymon/Documents/Studia-UWr/AiSD/coding/pracownie/pracE/tests/test.txt");

    int N;
    // infile >> N;
    scanf("%d", &N);

    Node *root = NULL;

    for (int i = 0; i < N; i++){
        char op;
        long long x;
        // infile >> op >> x;
        scanf(" %c %lld", &op, &x);
        if (op == 'I'){
            root = Insert(root, x);
        }else if (op == 'D'){
            if (findKey(root, x)){
                root = Delete(root, x);
                printf("OK\n");
            }else {
                printf("BRAK\n");
            }
            // root = Delete(root, x);
        }else if (op == 'U'){
            long long upper = Upper(root, x);
            if (upper == LLONG_MAX){
                printf("BRAK\n");
            }else {
                printf("%lld\n", upper);
            }
        }else if (op == 'L') {
            long long lower = Lower(root, x);
            if (lower == LLONG_MIN){
                printf("BRAK\n");
            }else {
                printf("%lld\n", lower);
            }
        }
    }

     

    // preOrder(root); 
    // cout << "\n" << endl;
 
    // root = Delete(root, 1); 
    // preOrder(root);

    return 0;
}